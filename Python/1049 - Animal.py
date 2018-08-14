n1 = input()
n2 = input()
n3 = input()
vertebrado = {'ave': {'carnivoro' : 'aguia', 'onivoro': 'pomba'}, 'mamifero' : {'onivoro':'homem','herbivoro':'vaca'}}
invertebrado = {'inseto': {'hematofago' : 'pulga', 'herbivoro': 'lagarta'}, 'anelideo' : {'hematofago':'sanguessuga','onivoro':'minhoca'}}
animais = {'vertebrado': vertebrado,'invertebrado':invertebrado}
print('{}'.format(animais[n1][n2][n3]))
