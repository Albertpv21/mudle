def loe_failist(file:str)->str:
    """Loeme tekst failist
    
    """
    f=open(file,"r")
    stroka=f.read() #Просто читает текст
    stroka=f.readlines() #Читает полностью текст(пробелы и тд)
    return stroka
stroka=loe_failist("TextFile.txt")
print(stroka)
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file,"r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_
spisok=loe_failist_listisse("TextFile.txt")
print(spisok)

def salvesta_failisse(file:str):
    f=open(file,"a")
    text=input("Sisesta tekst:")
    f.write(text+"\n")

for i in range(10):
    salvesta_failisse("Loetelu2.txt")

def faili_sisu_imberkirjutamine(file:str):
    text=input("Sisesta uus tekst:")
    wtih open(file,"w") as f:
        f.write(text+"\n")

faili_sisu_umberkirjutamine(input("Faili nimetus")+".txt")







