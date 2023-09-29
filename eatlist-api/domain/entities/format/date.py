from datetime import datetime


def convert_datetime_to_iso_8601_with_timezone(date: datetime) -> str:
    return date.strftime('%Y-%m-%dT%H:%M:%SZ')
