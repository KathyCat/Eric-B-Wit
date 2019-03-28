def first_entity_value(entities, entity):
    if entity not in entities:
        return ''
    val = entities[entity][0]['value']
    if not val:
        return ''
    return val

def get_intent(response):
    intent = response['intent']
    if not intent:
        return ''
    return intent