cnp = input("Introduceți CNP: ")
comparednum = "279146358279"
try:
    listcnp = list(map(int, cnp))
    listcn = list(map(int, comparednum))
    comparedcnp = cnp[0:13]
    zicnp = int(cnp[5:7])
    lunacnp = int(cnp[3:5])
    ancnp = int(cnp[1:3])
    sexnum = int(cnp[0])
    reprsec = cnp[0]
except ValueError:
    exit("Format CNP incorect! CNP trebuie să conțină 13 cifre!")
maxziluna = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
regiunea = {"01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor", "06": "Bistrița Năsăud",
            "07": "Botoșani", "08": "Brașov", "09": "Brăila", "10": "Buzău", "11": "Caraș Severin", "12": "Cluj",
            "13": "Constanța", "14": "Covasna", "15": "Dambovița", "16": "Dolj", "17": "Galați", "18": "Gorj",
            "19": "Harghita", "20": "Hunedoara", "21": "Ialomița", "22": "Iași", "23": "Ilfov", "24": "Maramureș",
            "25": "Mehedinți", "26": "Mureș", "27": "Neamț", "28": "Olt", "29": "Prahova", "30": "Satu Mare",
            "31": "Sălaj", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timiș", "36": "Tulcea",
            "37": "Vaslui", "38": "Vâlcea", "39": "Vrancea", "40": "București", "41": "București Sectorul 1",
            "42": "București Sectorul 2", "43": "București Sectorul 3", "44": "București Sectorul 4",
            "45": "București Sectorul 5", "46": "București Sectorul 6", "51": "Călărași", "52": "Giurgiu"}


def checklcnp(cnp):
    if len(cnp) != 13:
        exit("Lungime CNP incorectă, CNP trebuie să aibă 13 caractere!")
    return len(cnp)


def checksex(cnp):
    if sexnum == 0:
        sex = "Cifra corespunzătoare pentru sex incorectă"
    elif sexnum in [1, 3, 5, 7]:
        sex = "sex masculin"
    elif sexnum in [2, 4, 6, 8]:
        sex = "sex feminin"
    else:
        sex = "cetățean străin nerezident - nu se poate preciza sexul"
    return sex


def checkan(cnp):
    global secol
    global an
    try:
        if int(reprsec) in range(1, 3):
            secol = 19
        elif int(reprsec) in range(3, 5):
            secol = 18
        elif int(reprsec) in range(5, 7):
            secol = 20
        an = int(str(secol) + cnp[1:3])
        return secol+1
    except NameError:
        exit("Cifra corespunzătoare pentru secolul nașterii este incorectă!")



def checkluna(cnp):
    if lunacnp not in range(1, 13):
        exit("Luna nu este corectă, anul are 12 luni! Ați introdus %s pentru lună!" % lunacnp)
    return lunacnp

def checkzi(cnp):
    try:
        if zicnp not in range(1, maxziluna[lunacnp]+1):
            print("Ziua nu este corectă! Luna %s are %s zile" %(lunacnp, maxziluna[lunacnp]))
    except KeyError:
        print("Zi naștere incorectă")
    return zicnp


def checkregiune(cnp):
    print("Verificare regiune: ...")
    try:
        return regiunea[cnp[7:9]]
    except KeyError:
        print("Cod regiune greșit")


def control(cnp):
    print("Verificare sumă control: ...")
    total = 0
    rez = [x * y for x, y in zip(listcn, listcnp)]
    for i in range(len(rez)):
        total = total + rez[i]
    sc = total % 11
    if sc == 10:
        sc -= 9
    if sc != int(cnp[12]):
        mesaj = "CNP INCORECT!!! Suma de control nu corespunde!"
        exit("CNP INCORECT!!! Suma de control nu corespunde!")
    else:
        mesaj = "CNP CORECT!!! Suma de control corespunde!"
    return mesaj

print("Verificare lungime CNP: ...")
print(checklcnp(cnp))
print("Verificare secvență sex: ...")
print(checksex(cnp))
print("Verificare secol dată naștere: ...")
print(checkan(cnp))
print("Verificare lună naștere: ...")
print(checkluna(cnp))
print("Verificare zi naștere: ...")
print(checkzi(cnp))
print(checkregiune(cnp))
print(control(cnp))
print("Persoana născută în %02d.%02d.%d" % (zicnp, lunacnp, an))