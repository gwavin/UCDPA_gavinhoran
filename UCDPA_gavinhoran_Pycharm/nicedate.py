import datetime
# import nicedate import nicedate

def nicedate(year_week):
    return datetime.datetime.strptime('{0}-1'.format(year_week), "%Y-W%W-%w")
