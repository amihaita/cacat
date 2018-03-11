# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nrunu = ['un','o','unu']
nrdoi = ['doi','două']
convertor = {1:'unu', 2:'doi',3:'trei', 4:'patru', 5:'cinci', 6:'șase', 7:'șapte', 8:'opt', 9:'nouă', 0:''}
numar = input('Introduceți numărul: ')
ordin = {12:'sute',11:'zeci', 10:'miliarde', 9:'sute', 8:'zeci', 7:'milioane', 6:'sute', 5:'zeci', 4:'mii', 3:'sute', 2:'zeci', 1:''}
lungime_numar = len(numar)
print('Ați introdus un număr din %d cifre' %lungime_numar)
'''
sute = numar[-3:]
print (sute)
mii = numar[-6:(lungime_numar-3)]
print (mii)
milioane = numar[-9:(lungime_numar-6)]
print (milioane)
miliarde = numar[-12:(lungime_numar-9)]
print (miliarde)
'''
for cifra in enumerate(numar):
    print (convertor[int(cifra[1])])
    #print ((cifra[0]))
    #print ((lungime_numar))
    print(ordin[lungime_numar-cifra[0]])
