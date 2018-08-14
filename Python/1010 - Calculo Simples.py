ns1 = str(input()).split()
ns2 = str(input()).split()

ns1_1 = int(ns1[1])
ns1_2 = float(ns1[2])

ns2_1 = int(ns2[1])
ns2_2 = float(ns2[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(ns1_1*ns1_2+ns2_1*ns2_2))
