def bissextile(year):
    isbissextile = False
    if int(year):
        if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or \
                (year % 4 == 0 and year % 100 != 0):
            return True
        elif (year % 4 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
            return False
