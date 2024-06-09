import random

sepatu = ["Nike", "Jordan", "Adidas", "Newbalance"]

while True:
    acak1 = random.choice(sepatu)
    print ( "Ini Sepatu Anda" , acak1)
    pilihan = input("Ingin mencoba lagi? (y/n): ")
    
    if pilihan != "y":
        break