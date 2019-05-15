from datetime import date
f_date = date(2017,3,30)
l_date = date.today()
if (f_date > l_date):
 delta = f_date - l_date
 print( "from now:",delta.days)
else:
 delta = l_date - f_date
 print( "passed from now:",delta.days)
