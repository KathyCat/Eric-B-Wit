from datetime import datetime, time 
import booking 
import constant
import greeting

def fetch_session():
   '''
    6:00am - 7:30am / 7:31am - 11:00am / 11:01am -2:30pm / 2:31pm - 8:30pm / 8:31pm - 12:00am/
    '''
   datemask = '%I:%M%p'
   time_point = []  
   time_point.append(time(6, 0, 0)) 
   time_point.append(time(7, 30, 0))
   time_point.append(time(11, 0, 0))
   time_point.append(time(14, 30, 0))
   time_point.append(time(20, 30, 0))
   time_point.append(time(23, 59, 0))
   
   now = datetime.now().time()
   
   for i in range(0, len(time_point)):
      if now >= time_point[i] and now <= time_point[i+1]:
         return 's' + str(i) # s0, s1, s2, ...
   return 's5'
   
'''
 Main process starts here
 '''
print ('Enter first interation:')
user_input = input() 
username = 'Sarah' # Fetch username from db
session = fetch_session()

info = {}
info[constant.CLASS_TYPE] = '' 
info[constant.CAMPUS] = '' # Fetch campus from db
info[constant.DATE] = '' # Fetch time from db
info[constant.TIME] = ''  # Fetch time from db 
info[constant.DURATION] = '' # Fetch time from db
info[constant.TEACHER] = ''

greeting.greeting_start(session, username) # Greet users

'''
 Decide route
'''
# consider intent  
booking.add_booking(user_input, info, session)

greeting.greeting_end(session)