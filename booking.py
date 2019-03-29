from wit import Wit
import constant
import re

'''
 parse datetime, could use parsedatetime 2.4 or embedded Wit.ai duckling
 '''
def update_info (response, info): 
    entities = response['entities']
    for item in entities.items(): # entities in response
        entity = item[0]
        val_list = item[1]
        if entity in constant.ENTITIES:
            result = ''       
            for v in val_list:
                result = result + str(v['value']) + ' ' # handle multiple values            
            info[entity] = result.strip()

def send_confirm (info):
    comfirm_msg = 'So, you would like to book a teacher for ' + info[constant.CLASS_TYPE] +' class at ' + info[constant.TIME] + ' ' + info[constant.DATE]
    if info[constant.TEACHER] is not '': # add additional information to confirmation message
        comfirm_msg = comfirm_msg + ' with teacher ' + info[constant.TEACHER]
    comfirm_msg += ', right?'
    print (comfirm_msg)    

def add_booking (first_input, info):    
    '''
     Setup Wit and information to be stored
     '''
    client = Wit(constant.WIT_TOKEN) 
    update_info(client.message(first_input), info) 

    # 2.1 Requst more information if there are missing parts in user input
    while info[constant.DATE] is '' or info[constant.TIME] is '' or info[constant.DURATION] is '' or info[constant.CLASS_TYPE] is '':         
        for entity, val in info.items():
            if val is '':
                print(constant.QUESTIONS[entity]) # Require missing information from users
                info[entity] = input() # Accept user input
                break
        
    # 3 Elly ask for confirmation (include additional info like teacher name)
    confirm = True
    while confirm:
        send_confirm(info)
        comfirm_input = input()
        '''
        Update information
        '''
        if not re.search(r'yes|right|sure', comfirm_input, re.I): # User need to revise the information          
            print ('What do you want to change?')
            user_input = input()
            update_info(client.message(user_input), info)
            revise = True
            while revise:
                print ('Anything else?')
                user_input = input()
                if re.search(r'no', user_input, re.I):
                    revise = False # No further revise
                else:
                    update_info(client.message(user_input), info)
        else:
            confirm = False # User confirm the information