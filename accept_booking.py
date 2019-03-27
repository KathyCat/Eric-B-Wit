# for 6:00 am - 7:30 am / 7:31 am - 11:00 am

'''
Training user input for wit.ai during 6:00 am - 7:30 am
Hi, i would like to book a teacher for {time} on {date} for {class type}
- Reply from these steps:
  - Please enter (missing parts)

 '''

from wit import Wit
import constant
import common




'''
 parse datetime, could use parsedatetime 2.4 or embedded Wit.ai duckling
 '''
def handle_message (response, info):
    entities = response[constant.ENTITIES]
    if info[constant.DATE] is '':
        info[constant.DATE] = first_entity_value(entities, constant.DATE)  
    if info[constant.TIME] is '':
        info[constant.TIME] = first_entity_value(entities, constant.TIME)
    if info[constant.DURATION] is '':
        info[constant.DURATION] = first_entity_value(entities, constant.DURATION)
    if info[constant.CLASS_TYPE] is '':
        info[constant.CLASS_TYPE] = first_entity_value(entities, constant.CLASS_TYPE)    


def add_booking (first_input):  
    
    '''
     Setup Wit and information to be stored
     '''
    client = Wit(constant.WIT_TOKEN) 
    info = {}
    info[constant.DATE] = ''
    info[constant.TIME] = ''
    info[constant.DURATION] = ''
    info[constant.CLASS_TYPE] = ''
    handle_message(client.message(first_input), info)

    # 2.1 Requst more information if there are missing parts in user input
    while info[constant.DATE] is '' or info[constant.TIME] is '' or info[constant.DURATION] is '' or info[constant.CLASS_TYPE] is '':
        if info[constant.DATE] is '':
            print ('Which date?')
        elif info[constant.TIME] is '':
            print ('What time does the class start?')
        elif info[constant.DURATION] is '':
            print ('How long will it last?')
        else:
            print ('What is the class level?')
        
        user_input = input()
        handle_message(client.message(user_input) , info)      
 
    
    # 3.1 Fetch college name and location from db

        
    
    # 3.2 Elly ask for confirmation (include additional info like teacher name)
    print ('Would you like to book a teacher for ' + info[constant.CLASS_TYPE] +' class at ' + info[constant.TIME] + ' ' + info[constant.DATE] + '?')
    
    print ('Thanks! Your booking is on its way to your email inbox.')