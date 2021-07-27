print("Selamat Datang, Nama kamu siapa ya?")
nama = input("Tolong tulis nama kamu disini: ")
nama_asli = "Mahdy"
if nama==nama_asli:
    print("Halo", nama, "perkenalkan Saya adalah sebuah program")
else:
    print("kamu gk usah bohong, aku tau nama kamu Mahdy")

print(" ")
print(" ")
umur = int(input("Umur Kamu berapa? "))
umur_asli = 19
if umur == umur_asli:
    print("cuma buat nambah info aja, heheheheh :) :)")
else:
    print("ga usah bohong lagi umur kamu udah 19, aku tau kok!!")

print(" ")
print(" ")
ultah = input("BTW kamu ultah ya hari ini(ya/tidak)?  ")

while ultah != "tidak":
    print(input("jangan pura pura lupa, kamu ultah kan? "))

banyak = int(input("Mau diucapin berapa kali? "))
while banyak <= 0:
    print("serius, mau diucapin berapa kali? ")

for a in range(banyak):
    print("HAPPY BIRTHDAY MAHDY!!! <3 <3")

while True:
    pass
