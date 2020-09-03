def table_driven_agent(percept):
    percepts=[]
    table=[['dirt','suck the dust'],['clean','move']]
    percepts.append(percept)
    action = lookup(percept,table)
    if action == 'move':
       action = move(percept[1])
    return(action)
def lookup(percept,table):
    for i in table:
        if i[0] == percept[0]:
            return(i[1])
def move(percept):
    if percept == 'left':
        return('Go to right')
    elif percept == 'right':
        return('Go to left')
percept = list(map(str,input("Enter the status and postion: ").split(',')))
action = table_driven_agent(percept)
print(action)
