dias = int(input('Quantos dias você quer saber?'))
anos = dias//365
meses = (dias%365)//30
dia = (dias%365)%30

print('{} ano(s), {} mes(es), {} dia(s)'.format(anos,meses,dia))








