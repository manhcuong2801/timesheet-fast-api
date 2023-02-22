
from datetime import time, date, datetime, timedelta
import calendar

from const import export_day, NO_CHECKOUT


def time2str(value):
    if isinstance(value, str):
        return value
    if isinstance(value, (time, datetime)):
        return value.strftime("%d")
    return ""


def datetime2str(value):
    if isinstance(value, str):
        return value
    if isinstance(value, (time, datetime)):
        return value.strftime("%Y-%m-%d")
    return ""


def str2date(value):
    if isinstance(value, (date, datetime)):
        return value
    return datetime.strptime(value, "%Y-%m-%d")


def str2datetime(value):
    if isinstance(value, (date, datetime)):
        return value
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


first_day = time2str(f"{export_day}")
start = datetime.strptime(first_day, "%Y-%m-%d")

days_in_month = calendar.monthrange(start.year, start.month)[1]
plus_day = timedelta(days=days_in_month - 1)
end = start + plus_day
step = timedelta(days=1)
