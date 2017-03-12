cnp = input("Introduceți CNP: ")
comparednum = "279146358279"
comparedcnp = cnp[0:13]
zicnp = int(cnp[5:7])
lunacnp = int(cnp[3:5])
ancnp = int(cnp[1:3])
sexnum = int(cnp[0])
reprsec = cnp[0]
maxziluna = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def checklcnp(param):
    if len(param) != 13:
        exit("Lungime CNP incorectă, CNP trebuie să aibă 13 caractere!")
checklcnp(cnp)


def checkluna(param):
    if lunacnp not in range(1, 13):
        exit("Caracterele 4 și 5 incorecte! Luna nu este corectă, anul are 12 luni!")
checkluna(cnp)


def checkzi(param):
    if zicnp not in range(1, 32):
        exit("Caracterele 6 și 7 incorecte! Lunile anului pot avea maxim 31 de zile.")
    if zicnp not in range(1, maxziluna[lunacnp]+1):
        print("Ziua nu este corectă!")
checkzi(cnp)


def checksex(param):
    if sexnum == 0:
        print("CNP nu poate să începă cu 0")
    elif sexnum in [1, 3, 5, 7]:
        print("sex masculin")
    elif sexnum in [2, 4, 6, 8]:
        print("sex feminin")
    else:
        print("cetățean străin nerezident - nu se poate preciza sexul")
checksex(cnp)


def checkan(param):
    global secol
    try:
        if int(reprsec) in range(1, 3):
            secol = 19
        elif int(reprsec) in range(3, 5):
            secol = 18
        elif int(reprsec) in range(5, 7):
            secol = 20
        print("Persoana născută în %02d.%02d.%s%s" % (zicnp, lunacnp, secol, ancnp))
        return secol
    except NameError:
        print("Secvența ce conține data nașterii este incorectă!")
checkan(cnp)


def control(cnp):
    total = 0
    rez = [x * y for x, y in zip(comparednum, comparedcnp)]
    for i in range(len(rez)):
        total = total + rez[i]
    sc = total%11
    if sc == 10:
        sc -= 9
print(sc)

print("Persoana s-a născut în secolul %s" % (int(secol + 1)))
