import os
from os import getcwd
import shutil
from typing import Counter
import time
lmao = ""
def endswith(func):
    Liste = []
    Liste.append(d)
    Trues = []
    for i in d:
        Trues.append(i.endswith(f"{func}"))
    Count = 0
    result = []#True olanların indexlerinin yazıldığı liste

    while True:
        if int(len(Trues))>= Count+1:
            aa = Trues[Count]
            if aa == True:
                ss= Trues.index(True)
                Trues[Count] = False
                result.append(ss)
            print(f"Count= {Count}")
            print(f"len(Trues)= {int(len(Trues))}")
            print(f"Trues[Count]= {int(Trues[Count])}")
            print(aa)
            print(result)
            time.sleep(0.001)
            Count += 1
        else:
            break

    
    for c in result:
        print(d[c])
        endswithobba.append(d[c])
    print(len(result))
    print(len(endswithobba))

endswithobba=[]

def startswith(func):
    Liste = []
    Liste.append(d)
    Trues = []
    for i in d:
        Trues.append(i.startswith(f"{func}"))
    Count = 0
    result = []#True olanların indexlerinin yazıldığı liste

    while True:
        if int(len(Trues))>= Count+1:
            aa = Trues[Count]
            if aa == True:
                ss= Trues.index(True)
                Trues[Count] = False
                result.append(ss)
            print(f"Count= {Count}")
            print(f"len(Trues)= {int(len(Trues))}")
            print(f"Trues[Count]= {int(Trues[Count])}")
            print(aa)
            print(result)
            time.sleep(0.001)
            Count += 1
        else:
            break

    
    for c in result:
        print(d[c])
        startswithobba.append(d[c])
    print(len(result))
    print(len(startswithobba))

startswithobba=[]
startswithPath = []
def getPathstartswith():
    for i in startswithobba:
        d= os.path.isfile(i)
        print(d)
        startswithPath.append(d)
    print(startswithPath)

while True:
    soru1 = input("1- Arama Seçenekleri\n2- Aranacak Konumu Seçin\n3- Path Alma İşlemi\n4- İptal\n")
    if soru1 == "1":
        soru2 = input("1- Başlangıca Göre Ara\n2- Sonuna Göre Ara (Uygulama uzantısı dahil)\n")
        if soru2 == "1":
            startswith(input("Aranacak Kelimeyi Yazın: "))
        elif soru2 == "2":
            endswith(input("Aranacak Kelimeyi Yazın: "))
    elif soru1 == "2":
        lmao = input("Dosya Konumunu girin\n")
        d= os.listdir(lmao)
    elif soru1 == "3":
        getPathstartswith()
    elif soru1 == "4":
        break
