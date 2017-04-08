# Hint:  use Google to find python function

from datetime import datetimegi

####a) 
date_start = '01-02-2013'
t0 = datetime.strptime(date_start, '%m-%d-%Y')

date_stop = '07-28-2015'   
t1 = datetime.strptime(date_stop, '%m-%d-%Y')

time_diff_a = t1 - t0
time_diff_a.days
# 937

####b)  
date_start = '12312013'
t0 = datetime.strptime(date_start, '%m%d%Y')

date_stop = '05282015'  
t1 = datetime.strptime(date_stop,'%m%d%Y')

time_diff_b = t1 - t0
time_diff_b.days
# 513

####c)  
date_start = '15-Jan-1994'  
t0 = datetime.strptime(date_start, '%d-%b-%Y')

date_stop = '14-Jul-2015'  
t1 = datetime.strptime(date_stop,'%d-%b-%Y')

time_diff_c = t1 - t0
time_diff_c.days
# 7850