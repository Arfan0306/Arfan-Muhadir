lampu=input("masukan lampu merah : ")

if lampu == "merah":
    print("berhenti")
elif lampu == "kuning":
    print("hati-hati")
elif lampu == "hijau":
    print("lanjut jalan")
else:
    print ("tidak ada dalam daftar")

nilai = int(input("masukan nilai :"))
if nilai >= 80:
    print("A")
elif nilai >= 60:
    print("B")
elif nilai >= 40:
    print("C")
else:
    print("E")

nilai1 = int(input("masukan nilai1 :"))
nilai2 = int(input("masukan nilai2 :"))

if nilai1:
    a = nilai1 * nilai2
    print (a)
            
