cnp = input("Introduceti CNP: ")
comparednum = "279146358279"
listcn = list(map(int,comparednum))
try:
    listcnp = list(map(int,cnp))
except ValueError:
    print("Nu ati introdus cifre!")
partcnp = cnp[0:12]
an = cnp[1:3]
luna = cnp[3:5]
zi = cnp[5:7]
reprsec = cnp[0]
try:
    if int(reprsec) in range(1,3):
        secol = 19
    elif int(reprsec) in range(3,5):
        secol = 18
    elif int(reprsec) in range(5,7):
        secol = 20
    print(type(an))
    print("Persoana nascuta in %s.%s.%s%s" %(zi, luna, secol, an))
except NameError:
    print("Prima cifra din CNP incorecta!")
def control(cnp):
    total = 0
    if len(cnp) != 13:
        print ("Formatul cnp-ului este necorespunzator.")
    else:
        rez = [x * y for x, y in zip(listcn, listcnp)]
        for i in range(len(rez)):
            total = total + rez[i]
    sc = total%11
    if sc == 10:
        sc = sc -9
            
    print(sc)
    print(partcnp)
    print(total)
control(cnp)

