import datetime
from datetime import date
import sys
#try:
#date_str = input("enter the date in dd-mm-yyyy format: ")
#except ValueError :
# print(" date is out of range")
while True:
 try:
  date_str = input("enter the date in dd-mm-yyyy format: ")
  date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y')
  f_date = date_obj.date()
  l_date = date.today()
  if (f_date > l_date):
   delta = f_date - l_date
   print("from now :",delta.days,"days")
  else:
   delta = l_date - f_date
   print("past from now :",delta.days,"days")
   break
 except ValueError as er:
  print(er)
#  exit()
#print("great entered successfully")
