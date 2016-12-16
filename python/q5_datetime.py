# Hint:  use Google to find python function
from datetime import date
####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

def find_days_dashes(date_start, date_stop):
    start_array = map(int, date_start.split('-'))
    stop_array = map(int, date_stop.split('-'))
    d0 = date(start_array[2], start_array[0], start_array[1])
    d1 = date(stop_array[2], stop_array[0], stop_array[1])
    delta = d1-d0
    return delta.days
print find_days_dashes(date_start, date_stop)

####b)
date_start = '12312013'
date_stop = '05282015'
def find_days_nodashes(date_start, date_stop):
    d0 = date(int(date_start[4:]), int(date_start[0:2]), int(date_start[2:4]))
    d1 = date(int(date_stop[4:]), int(date_stop[0:2]), int(date_stop[2:4]))
    delta = d1-d0
    return delta.days
print find_days_nodashes(date_start, date_stop)
####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

def find_days_words(date_start, date_stop):
    start_array =  date_start.split('-')
    stop_array = date_stop.split('-')
    d = {'Jan' : 1, 'Jul': 7}
    d0 = date(int(start_array[2]), d[start_array[1]], int(start_array[0]))
    d1 = date(int(stop_array[2]), d[stop_array[1]], int(stop_array[0]))
    delta = d1-d0
    return delta.days
print find_days_words(date_start, date_stop)
