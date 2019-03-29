import constant 
'''
def get_entity_value(entities, entity): # get values
    if entity not in entities:
        return ''
    values = entities[entity]
    result = ''

    for v in values:
        result = result + v['value'] + ' '    
    if not result:
        return ''
    return result.strip()

def get_intent(response):
    intent = response['intent']
    if not intent:
        return ''
    return intent
    
def update_info (response, info):
    entities = response[constant.ENTITIES]
    for entity, val in info.items():
        if val is '':
            info[entity] = get_entity_value(entities, entity)
'''


            