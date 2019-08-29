d ={'suco':120,'morango':85,'mamao':85,'goiaba':70,'manga':56,'laranja':50,'brocolis':34}
while True:
    k = int(input())
    if k == 0:
        break
    tot = 0
    n = [str(input()).split() for i in range(k)]
    for i in n:
        tot += int(i[0])*d[i[1]]
    if tot < 110:
        print('Mais {} mg'.format(110-tot))
    elif tot > 130:
        print('Menos {} mg'.format(tot-130))
    else:
        print(tot,'mg')
