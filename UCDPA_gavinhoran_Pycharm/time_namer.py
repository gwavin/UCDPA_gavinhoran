from datetime import datetime

filename = 'lmplotTestsV'

def time_namer(filename):
    t = '{0:%H%M%S%d%m%y}'.format(datetime.now())
    return(filename + t)


print(time_namer(filename))
