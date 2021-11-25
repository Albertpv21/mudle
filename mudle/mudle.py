from Funktsioonid import * 
users=loe_failist_listisse("users.txt")
passwords=loe_failist_listisse("passwords.txt")
print(users)
print(passwords)

while True:
    print("Reg-1,Avt-2,Välja-3")
    valik = input("Millist tahate teha->")
    if valik == '1':
        log, password = kasutajaandmed()
        registreerimine(log,password,users,passwords)
    elif valik == '2':
        log, passwords = kasutajaandmed()
        login(users,log,password,passwords)
    elif valik == '3':
        print("Head aega")
        break
    else:
        print("Vajad kirjutada 1,2,3")
        while 1:
            pas=intput("Sisesta oma parool")
            tulemus=paskontroll(pas)
            if tulemus==True:
                users.append(log)
                passwords.append(pas)
                break
    else:
        print("Viga")
        faili_sisu_umberkirjutamine("users.txt",users)
        faili_sisu_umberkirjutaminet("passwords.txt",passwords)
        quit

