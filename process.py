from datetime import datetime

import booking 

'''
 fetch user input
 '''
print ('Enter first interation:')
user_input = input()


'''
 get current time 
 6:00am - 7:30am / 7:31am - 11:00am / 11:01am -2:30pm / 2:31pm - 8:30pm / 8:31pm - 12:00am/
 '''
datemask = '%I:%M%p'
time_point = []
time_point.append(datetime.strptime('12:01am', datemask))
time_point.append(datetime.strptime('6:00am', datemask)) 
time_point.append(datetime.strptime('7:31am', datemask))
time_point.append(datetime.strptime('11:01am', datemask))
time_point.append(datetime.strptime('2:31pm', datemask))
time_point.append(datetime.strptime('8:31pm', datemask))

now = datetime.strftime(datetime.today(), datemask)


'''
 Greet user
 fetch username from db
 '''
username = 'Sarah'
greet = "Good morning " + username + ", this is Elly, your duty coordinator" 
print(greet)

'''
 Decide route
'''
# if now >= time_point[1] and now < time_point[2]:
booking.add_booking(user_input)

'''
username = 'Sarah'
greets = []
greets.append("Good morning " + username + ", this is Elly, your duty coordinator")
greets.append("Hello " + username + ", this Elly, your duty coordinator.")
greets.append("Good evening " + username + ", welcome to the RT booking desk, this is Elly")

'''