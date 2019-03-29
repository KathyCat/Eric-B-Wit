from datetime import datetime
import booking 
import constant

def fetch_session():
   '''
    6:00am - 7:30am / 7:31am - 11:00am / 11:01am -2:30pm / 2:31pm - 8:30pm / 8:31pm - 12:00am/
    '''
   datemask = '%I:%M%p'
   time_point = []  
   time_point.append(datetime.strptime('6:00am', datemask)) 
   time_point.append(datetime.strptime('7:30am', datemask))
   time_point.append(datetime.strptime('11:00am', datemask))
   time_point.append(datetime.strptime('2:30pm', datemask))
   time_point.append(datetime.strptime('8:30pm', datemask))
   time_point.append(datetime.strptime('11:59pm', datemask))
   
   #now = datetime.strftime(datetime.today(), datemask)  
   now = datetime.strptime('7:00am', datemask)
   
   for i in range(0, len(time_point)):
      if now >= time_point[i] and now <= time_point[i+1]:
         return 's' + str(i) # s0, s1, s2, ...
   return 's5'
   
def greeting_start(session, username, info):
   if session == 's0' or session == 's1':
      print ('Good morning ' + username + ', this is Elly, your duty coordinator')
   if session == 's1':
      print ('Bookings for morning sessions close at 7.30am.')
      print ('Would you like to book a teacher for ' + info[constant.TIME] + ' for ' + info[constant.CAMPUS] + ' or for tomorrow?') 
   if session == 's2':
      print ('Hello ' + username + ', this Elly, your duty coordinator.')
      print ("Bookings for this morning's sessions are now closed.")
      print ('Would you like to book a teacher for ' + info[constant.TIME] + ' for ' + info[constant.CAMPUS] + ' or for tomorrow?') 
   if session == 's3':
      print ('Hello ' + username + ', welcome to the RT booking desk, this is Elly. ')
      print ('Are you booking a teacher for tomorrow ' + info[constant.TIME] + ' at ' + info[constant.CAMPUS] + ' or for another time?') 
   if session == 's4':      
      print ('Good evening ' + username + ', welcome to the RT booking desk, this is Elly')
      print ('Are you booking a teacher for tomorrow ' + info[constant.TIME] + ' at ' + info[constant.CAMPUS] + '?') 
   if session == 's5':
      print ('Good evening [name], welcome to the RT booking desk, this is Elly')
      print ('Are you booking a teacher for ' + info[constant.TIME] + ' at ' + info[constant.CAMPUS] + '?')

      
def greeting_end(session):
   if session == 's0' or session == 's1' or session == 's2':
      print ('Thanks! Your booking is on its way to your email inbox.')
   elif session == 's3':
      print ('Thanks! You will receive a booking confirmation by email shortly. Goodnight.')
   else:
      print ('Thanks - your booking has been received. Our booking desk is currently closed and your booking will be sent by email when we re-open at 6.00am. ')

'''
 Main process starts here
 '''
print ('Enter first interation:')
user_input = input() 
username = 'Sarah' # Fetch username from db
session = fetch_session()

info = {}
info[constant.CLASS_TYPE] = '' 
info[constant.CAMPUS] = 'Lonsdale' # Fetch campus from db
info[constant.DATE] = '' # Fetch time from db
info[constant.TIME] = ''  # Fetch time from db 
info[constant.DURATION] = '' # Fetch time from db
info[constant.TEACHER] = ''

greeting_start(session, username, info) # Greet users

'''
 Decide route
'''
# consider intent  
booking.add_booking(user_input, info)

greeting_end(session)