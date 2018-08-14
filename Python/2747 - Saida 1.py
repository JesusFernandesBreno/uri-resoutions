def t():
    return '-'*39
    
def l():
    return '|'+' '*37+'|'+'\n'
s = ''
s += t()+'\n'
for i in range(5):
    s += l()
s += t()
print(s)
