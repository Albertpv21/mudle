import random 
def kasutajaandmed():
    log = input('Kirjutage kasutajanimi ')
    password = input('Kirjutage parool ')
    return log, password

def login(kasutajanimed,log,password,passwords):
    n = len(kasutajanimed)
    signal = 0
    for i in range(n):
        reg = input("Kas soovite registreeruda? y/n ")
        if reg == 'n':
            print("Te ei saa süsteemi kasutada")
        elif reg == 'y':
            print("Alustame registreerimisprotsessi")
            registreerimine(log,password,kasutajanimed,passwords)
        else:
            print("Sisestusviga")
        if kasutajanimed[i] == log and passwords[i] == password:
            print("Autoriseerimine õnnestus. Olete sisse logitud")
            signal = 1
        elif kasutajanimed[i] == log and passwords[i] != password:
            print("Vale parool")
            signal = -1
    if signal == 0:      
        print("Olete uus kasutaja")
        
    
def registreerimine(log,password,kasutajanimed,passwords):
    kasutajanimed.append(log)
    print("Olete uus kasutaja")
    print("Nüüd loome uue parooli")
    valik = input("Loo parool: a - automaatselt, m - käsitsi: ")
    if valik == 'a':
        new_password = passauto()
        passwords.append(new_password)
        print(kasutajanimed)
        print(passwords)
    elif valik == 'm':
        new_password = input("Sisestage parool (vähemalt 12 tähemärki) ")
        n = len(new_password)
        while n < 12:
            new_password = input('Liiga lühike parool. Palun sisestage uuesti ')
            n = len(new_password)
        passwords.append(new_password)
    else:
        print("Sisestusviga")

def passauto()->str:
    str0= ".,_"
    str1 = '0123456789'
    str2 =  'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    print(psword)
    return psword
def paskontroll(passwords: str)->bool:
    ls=list(passwords)
    for e in ls:
        if e.isdigit(): d=True
        if e.isalpha(): a=True
        if e.isupper(): u=True
        if e.islower(): l=True
        if e in list(".,:!_*/+-¤%#&"): s=True
    if d==True and a==True and u==True and l==True and s==True:
        t=True
    else:
        t=False
    return t
