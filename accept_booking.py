# for 6:00 am - 7:30 am / 7:31 am - 11:00 am

'''
Training user input for wit.ai during 6:00 am - 7:30 am
Hi, i would like to book a teacher for {time} on {date} for {class type}
- Reply from these steps:
  - Please enter (missing parts)

 '''

from wit import Wit
import constant

def first_entity_value(entities, entity):
    if entity not in entities:
        return ''
    val = entities[entity][0]['value']
    if not val:
        return ''
    return val


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


def start_conversation (first_input):  
    # 1 Elly greet user
    '''
     fetch username from db
     '''
    username = 'Sarah'
    greet = "Good morning " + username + ", this is Elly, your duty coordinator"  
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
 
    
    # 3 Elly ask for confirmation
    print ('Thank you for booking ' + info[constant.CLASS_TYPE] +' class at ' + info[constant.TIME] + ' ' + info[constant.DATE])