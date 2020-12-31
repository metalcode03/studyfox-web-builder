from datetime import datetime, timedelta
from calendar import *
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_date__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li class="calender_list">{event.get_html_url}</li>\n'
        if day != 0:
            if day == datetime.today().day:
              return f"<td class='day today'>{day}<ul>{d}</ul></td>\n"
            return f"<td class='day' >{day}<ul>{d}</ul></td>\n"
        return '<td></td>\n'

    def formattitle(self):
        title = ''
        title += '<tr>\n'
        title += '  <th colspan="7" class="datepicker-title" style="display: none;"></th>\n'
        title += '</th>\n'
        return title

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        dow = 'dow'
        return '<th class="%s">%s</th>\n' % (dow, day_abbr[day])

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr>\n {week}</tr>\n'

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = '%s %s' % (month_name[themonth], theyear)
        else:
            s = '%s' % month_name[themonth]
        return '<tr>\n<th class="prev">«</th>\n<th colspan="5" class="%s">%s</th>\n<th class="next">»</th>\n</tr>\n' % (
            "datepicker-switch", s)

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(
            start_date__year=self.year, start_date__month=self.month)
        cal = f'<table class="table-condensed">\n'
        cal += f'<thead>\n'
        cal += f'{self.formattitle()}'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        cal += f'</thead>\n'
        cal += f'<tbody>\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        cal += f'</tbody>\n'
        cal += f'</table>\n'

        return cal
