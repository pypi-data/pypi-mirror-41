# ------------------------------------------------------------------------------
# Recurrence
# ------------------------------------------------------------------------------
# Somewhat based upon RFC5545 RRules, implemented using dateutil.rrule
# Does not support timezones ... and probably never will
# Does not support a frequency of by hour, by minute or by second
#
# See also:
#   https://github.com/django-recurrence/django-recurrence
#   https://github.com/dakrauth/django-swingtime

import sys
from operator import attrgetter
import calendar
import datetime as dt
from dateutil.rrule import rrule, rrulestr, rrulebase
from dateutil.rrule import DAILY, WEEKLY, MONTHLY, YEARLY
from dateutil.rrule import weekday as rrweekday
from .telltime import dateFormatDMY
from .manythings import toOrdinal, hrJoin

# ------------------------------------------------------------------------------
class Weekday(rrweekday):
    def __repr__(self):
        s = ("MO", "TU", "WE", "TH", "FR", "SA", "SU")[self.weekday]
        if not self.n:
            return s
        else:
            return "{:+d}{}".format(self.n, s)

    def __str__(self):
        return self._getWhen(0)

    def _getWhen(self, offset):
        when = calendar.day_name[self.weekday]
        if offset == 0:
            if not self.n:
                return when
            else:
                return "{} {}".format(toOrdinal(self.n), when)
        localWhen = calendar.day_name[(self.weekday + offset) % 7]
        if not self.n:
            return localWhen
        else:
            ordinal = toOrdinal(self.n)
            if offset < 0:
                return "{} before the {} {}".format(localWhen, ordinal, when)
            else:
                return "{} after the {} {}".format(localWhen, ordinal, when)

MO, TU, WE, TH, FR, SA, SU = map(Weekday, range(7))
WEEKDAYS = [MO, TU, WE, TH, FR]
WEEKEND = [SA, SU]
EVERYDAY = WEEKDAYS + WEEKEND

JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = range(1, 13)

# ------------------------------------------------------------------------------
class Recurrence(rrulebase):
    def __init__(self, *args, **kwargs):
        super().__init__()
        arg0 = args[0] if len(args) else None
        if isinstance(arg0, str):
            self.rule = rrulestr(arg0, **kwargs)
            if not isinstance(self.rule, rrule):
                raise ValueError("Only support simple RRules for now")
        elif isinstance(arg0, Recurrence):
            self.rule = arg0.rule
        elif isinstance(arg0, rrule):
            self.rule = arg0
        else:
            self.rule = rrule(*args, **kwargs)

    # expose all
    freq        = property(attrgetter("rule._freq"))
    interval    = property(attrgetter("rule._interval"))
    count       = property(attrgetter("rule._count"))
    byweekno    = property(attrgetter("rule._byweekno"))
    byyearday   = property(attrgetter("rule._byyearday"))
    byeaster    = property(attrgetter("rule._byeaster"))
    bysetpos    = property(attrgetter("rule._bysetpos"))

    @property
    def dtstart(self):
        """
        The recurrence start date.
        """
        return self.rule._dtstart.date()

    @property
    def frequency(self):
        """
        How often the recurrence repeats.
        ("YEARLY", "MONTHLY", "WEEKLY", "DAILY")
        """
        freqOptions = ("YEARLY", "MONTHLY", "WEEKLY", "DAILY")
        if self.freq < len(freqOptions):
            return freqOptions[self.freq]
        else:
            return "unsupported_frequency_{}".format(self.freq)

    @property
    def until(self):
        """
        The last occurence in the rule is the greatest date that is
        less than or equal to the value specified in the until parameter.
        """
        if self.rule._until is not None:
            return self.rule._until.date()

    @property
    def wkst(self):
        """
        The week start day.  The default week start is got from
        calendar.firstweekday() which Joyous sets based on the Django
        FIRST_DAY_OF_WEEK setting.
        """
        return Weekday(self.rule._wkst)

    @property
    def byweekday(self):
        """
        The weekdays where the recurrence will be applied.  In RFC5545 this is
        called BYDAY, but is renamed by dateutil to avoid ambiguity.
        """
        retval = []
        if self.rule._byweekday:
            retval += [Weekday(day) for day in self.rule._byweekday]
        if self.rule._bynweekday:
            retval += [Weekday(day, n) for day, n in self.rule._bynweekday]
        return retval

    @property
    def bymonthday(self):
        """
        The month days where the recurrence will be applied.
        """
        retval = []
        if self.rule._bymonthday:
            retval += self.rule._bymonthday
        if self.rule._bynmonthday:
            retval += self.rule._bynmonthday
        return retval

    @property
    def bymonth(self):
        """
        The months where the recurrence will be applied.
        """
        if self.rule._bymonth:
            return list(self.rule._bymonth)
        else:
            return []

    def _iter(self):
        for occurence in self.rule._iter():
            yield occurence.date()

    def getCount(self):
        """
        How many occurrences will be generated.
        The use of the until keyword together with the count keyword is deprecated.
        """
        return self.rule.count()

    def __repr__(self):
        dtstart = ""
        if self.dtstart:
            dtstart = "DTSTART:{:%Y%m%d}\n".format(self.dtstart)
        rrule = "RRULE:{}".format(self._getRrule())
        retval = dtstart + rrule
        return retval

    def _getRrule(self):
        parts = ["FREQ={}".format(self.frequency)]
        if self.interval and self.interval != 1:
            parts.append("INTERVAL={}".format(self.interval))
        if self.wkst:
            parts.append("WKST={!r}".format(self.wkst))
        if self.count:
            parts.append("COUNT={}".format(self.count))
        if self.until:
            parts.append("UNTIL={:%Y%m%d}".format(self.until))
        for name, value in [('BYSETPOS',   self.bysetpos),
                            ('BYDAY',      self.byweekday),
                            ('BYMONTH',    self.bymonth),
                            ('BYMONTHDAY', self.bymonthday),
                            ('BYYEARDAY',  self.byyearday),
                            ('BYWEEKNO',   self.byweekno)]:
            if value:
                parts.append("{}={}".format(name,
                                            ",".join(repr(v) for v in value)))
        return ";".join(parts)

    def __str__(self):
        return self._getWhen(0)

    def _getWhen(self, offset, numDays=1):
        retval = ""
        if self.freq == DAILY:
            if self.interval > 1:
                retval = "Every {} days".format(self.interval)
            else:
                retval = "Daily"
        elif self.freq == WEEKLY:
            days = ["{}s".format(d._getWhen(offset)) for d in self.byweekday]
            retval = hrJoin(days)
            if self.interval == 2:
                retval = "Fortnightly on {}".format(retval)
            elif self.interval > 2:
                retval = "Every {} weeks on {}".format(self.interval, retval)

        elif self.freq in (MONTHLY, YEARLY):
            if self.freq == MONTHLY:
                of = " of the month"
            else:
                months = [calendar.month_name[m] for m in self.bymonth]
                of = " of {}".format(hrJoin(months))
            days = []
            if self.byweekday:
                if len(self.byweekday) == 7 and all(not day.n for day in self.byweekday):
                    retval = "Everyday"
                    of = ""
                else:
                    days = ["{}".format(d._getWhen(offset)) for d in self.byweekday]
                    retval = hrJoin(days)
                    if not self.byweekday[0].n:
                        retval = "Every "+retval
                        of = ""
                    else:
                        retval = "The {}".format(retval)

            elif len(self.bymonthday) > 1:
                days = ["the {}".format(toOrdinal(d)) for d in self.bymonthday]
                if offset == -2:
                    retval = "Two days before {} day".format(hrJoin(days))
                elif offset == -1:
                    retval = "The day before {} day".format(hrJoin(days))
                elif offset == 1:
                    retval = "The day after {} day".format(hrJoin(days))
                elif offset == 2:
                    retval = "Two days after {} day".format(hrJoin(days))
                elif offset != 0:
                    retval = hrJoin(["{}{:+d}".format(day, offset) for day in days])

            elif len(self.bymonthday) == 1:
                wrappedMonthNames = calendar.month_name[:]
                wrappedMonthNames[0] = calendar.month_name[-1]
                wrappedMonthNames.append(calendar.month_name[1])

                d = self.bymonthday[0]
                if d == 1 and offset < 0:
                    d = offset
                    if self.freq != MONTHLY:
                        months = [wrappedMonthNames[m-1] for m in self.bymonth]
                        of = " of {}".format(hrJoin(months))
                elif d == -1 and offset > 0:
                    d = offset
                    if self.freq != MONTHLY:
                        months = [wrappedMonthNames[m+1] for m in self.bymonth]
                        of = " of {}".format(hrJoin(months))
                else:
                    d += offset
                retval = "The {} day".format(toOrdinal(d))
            retval += of
            if self.interval >= 2:
                if self.freq == MONTHLY:
                    retval = "{}, every {} months".format(retval, self.interval)
                else:
                    retval = "{}, every {} years".format(retval, self.interval)
        if numDays >= 2:
            retval += " for {} days".format(numDays)
        if self.until:
            until = self.until + dt.timedelta(days=offset)
            # TODO make format configurable
            retval += " (until {})".format(dateFormatDMY(until))
        return retval

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
