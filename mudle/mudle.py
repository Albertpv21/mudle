from Funktsioonid import * 
users=["Albert"]
passwords=["12345"]

while True:
    print("Reg-1,Avt-2,Välja-3")
    valik = input("Millist tahate teha->")
    if valik == '1':
        log, password = kasutajaandmed()
        registreerimine(log,password,users,passwords)
    elif valik == '2':
        log, password = kasutajaandmed()
        login(users,log,password,passwords)
    elif valik == '3':
        print("Head aega")
        break
    else:
        print("Vajad kirjutada 1,2,3")
