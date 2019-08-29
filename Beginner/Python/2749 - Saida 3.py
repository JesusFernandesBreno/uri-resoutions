def t():
    return '-'*39
    
def l(s,c):
    if s == '':
        return '|'+' '*37+'|'+'\n'
    return '|'+' '*c+s+' '*(37-(len(s)+c))+'|'+'\n'
s = ''
s += t()+'\n'
for i in range(5):
    if i == 0:
        s += l('x = 35',0)
    elif i== 2:
        s += l('x = 35',15)
    elif i == 4:
        s += l('x = 35',31)
    else:
        s += l('',0)
    
s += t()
print(s)
