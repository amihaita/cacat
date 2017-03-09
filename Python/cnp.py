cnp = input("Introduceti CNP: ")
comparednum = "279146358279"
def checksex(cnp):
    sexnum = int(cnp[0])
    if sexnum in [1,3,5,7]:
        print("sex masculin")
    elif sexnum in [2,4,6,8]:
        print("sex feminin")
    else:
        print("cetățean străin - nu se poate preciza sexul")
checksex(cnp)

def checkzi(cnp):
    reprsec = cnp[0]
    zi = int(cnp[5:7])
    if zi not in range(1,32):
        print("Ziua nu este corectă!")
checkzi(cnp)
def checkan(cnp):
    reprsec = cnp[0]
    an = int(cnp[1:3])
    luna = int(cnp[3:5])
    zi = int(cnp[5:7])
    try:
        if int(reprsec) in range(1, 3):
            secol = 19
        elif int(reprsec) in range(3, 5):
            secol = 18
        elif int(reprsec) in range(5, 7):
            secol = 20
        print("Persoana născută în %02d.%02d.%s%s" %(zi, luna, secol, an))
    except NameError:
        print("Secvența ce conține data nașterii este incorectă!")
checkan(cnp)