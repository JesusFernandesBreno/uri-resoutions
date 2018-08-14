def interc(a,b):
    print(len(conjs[a]&conjs[b]))
        

def uniao(a,b):
    print(len(conjs[a]|conjs[b]))

def op(op, conj_a, conj_b):
    if op == 1:
        interc(conj_a-1,conj_b-1)
    else:
        uniao(conj_a-1,conj_b-1)

conjs = []

for i in range( int(input()) ):
    conjs = [set(str(input()).split()[1:]) for i in range(int(input()))]
    for j in range( int(input()) ):
        ops = str(input()).split()
        op(int(ops[0]), int(ops[1]) , int(ops[2]))
