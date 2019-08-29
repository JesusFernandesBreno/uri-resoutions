def t():
    return '-'*39
    
def l(s):
    if s == '':
        return '|'+' '*37+'|'+'\n'
    return '|'+' '*8+s+' '*(37-(len(s)+8))+'|'+'\n'
s = ''
s += t()+'\n'
for i in range(5):
    if i == 0:
        s += l('Roberto')
    elif i== 2:
        s += l('5786')
    elif i == 4:
        s += l('UNIFEI')
    else:
        s += l('')
    
s += t()
print(s)
