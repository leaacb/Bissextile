from datetime import datetime


def get_utc_timestamp():
    local = datetime.now()
    return local.strftime("%Y/%m/%d, %H:%M:%S")


