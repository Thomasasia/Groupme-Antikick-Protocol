from groupy import Bot, Group, Member, FilterList
from time import sleep
from groupy.api.endpoint import Messages


global start_message_id

global start_id_init

def get_messages(gp, sid):
    sleep(1)
    print(str(gp.id))
    print(str(sid))
    try:
        raw = Messages.index(gp.id, since_id = sid)
        print('New Data!!')
    except:
        print('NO NEW DATA')
        return[]
    new_messages = []
    for m in raw['messages']:
        new_messages.append(m['text'])
    
    removal_messages = []
    for m in new_messages:
        pure = True
        if 'removed' in m:
            removal_messages.append(m)
    return removal_messages


def init_start_id(g):
    if start_id_init == False:
        print('oye')
        start_message_id = g.messages().newest.id
        print(start_message_id)
        sleep(1)
    
#Mr.Thomas removed Akshay Harish from the group.


start_message_id = 0

start_id_init = False


while True:
    group_id = 28604898
#    group_id = 34475325
    try:
        groups = Group.list()
    except:
        print('too many requests?')
        continue
#    print(groups)
    group = None
#    print(group)
    try:
        members = Member.list()
    except:
        continue
#    print(str(type(group.members()))) 
    for grp in groups:
        if int(grp.id) == group_id:
            group = grp
    print(str(group))
    if start_id_init == False:
        print('oye, ', group.messages().newest.text)
        start_message_id = group.messages().newest.id
        print(start_message_id)
        start_id_init = True
        sleep(1)
 
    messages = get_messages(group, start_message_id)
    print('Newest message: ',group.messages().newest)

    to_add = []
    
    for message in messages:
        print(message)
        start_index = message.find('removed')+8
        end_index = message.rfind(' from')
        name = message[start_index:end_index]
        print(name)
        for mem in members:
            if mem.nickname == name:
                to_add.append(mem)
                continue
    new_list = FilterList.filter(to_add)
#    for add_id in to_add:
    
    try:
        group.add(*new_list)
        print('A Danke Boi was re-added')
    except:
        pass
    start_message_id = group.messages().newest.id
    sleep(1)
    


