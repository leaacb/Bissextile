from datetime import datetime, timedelta


def get_utc_timestamp():
    local = datetime.now()
    new_local = local + timedelta(hours=1)
    return new_local.strftime("%Y/%m/%d, %H:%M:%S")


