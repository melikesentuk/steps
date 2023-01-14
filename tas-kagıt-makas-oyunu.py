#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
action_list = ["makas", "kagit", "tas"]
oyuncu_1_skor = 0
oyuncu_2_skor = 0

tur_sayıcı = 0
toplam_tur = int(input("Kaç tur oynamak istersiniz ? :  "))

while True:

  tur_sayıcı +=1
  print("Tur sayısı :", tur_sayıcı)

  oyuncu_1_secim = random.choice(action_list)  #aksiyon seçimi
  oyuncu_2_secim = action_list[random.randint(0,2)]
  print("oyuncu_1   : ", oyuncu_1_secim)    # seçimlerin yazdırılması
  print("oyuncu_2   : ", oyuncu_2_secim)  

  if oyuncu_1_secim == oyuncu_2_secim:
    print("İKİ OYUNUNCUNUN DA SEÇİMİ AYNI")

  elif oyuncu_1_secim == "kagit":
    if oyuncu_2_secim  == "kaya":
      print("Kazanan : Oyuncu 1")
      oyuncu_1_skor +=1
    else:
      print("Kazanan : Oyuncu 2") 
      oyuncu_1_skor += 1


  elif oyuncu_1_secim == "kagit":
    if oyuncu_2_secim =="makas":
      print(" Kazanan: Oyuncu 2")
      oyuncu_2_skor +=1
    else:
      print("Kazanan : Oyuncu 1")
      oyuncu_1_skor +=1

  elif oyuncu_1_secim == "makas":
    if oyuncu_2_secim == "kaya":
      print("Kazanan : Oyuncu 2")
      oyuncu_2_skor +=1
    else:
      print("Kazanan  : Oyuncu 1")
      oyuncu_1_skor +=1


  elif oyuncu_1_secim == "makas":
    if oyuncu_2_secim == "kagit":
      print("Kazanan : Oyuncu 1")
      oyuncu_1_skor+=1
    else:
      print("Kazanan : Oyuncu 2")
      oyuncu_2_skor +=1

  elif oyuncu_1_secim == "kaya":  
    if oyuncu_2_secim == "makas":
      print("Kazanan : Oyuncu 1")
      oyuncu_1_skor +=1
  else:
    print("Kazanan : Oyuncu 2")
    oyuncu_2_skor +=1

  print("SKOR : "  "Oyuncu_1 :",oyuncu_1_skor, "   Oyuncu_2 :", oyuncu_2_skor )

  if tur_sayıcı == (toplam_tur):
    break
if oyuncu_1_skor == oyuncu_2_skor:
  print("BERABERE , Kazanan yok")
elif oyuncu_1_skor >oyuncu_2_skor:
  print( "KAZANAN :  **OYUNCU_1 **  ", oyuncu_1_skor, "-" , oyuncu_2_skor)
else:
  print("KAZANAN : **OYUNCU_2**", oyuncu_1_skor, "-",  oyuncu_1_skor)


# In[ ]:





# In[ ]:




