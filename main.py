import getpass
import json
import os
import datetime
statusAkun = ""

# Proses untuk Data Menu
y = open('menu.json')
data = json.load(y)
menuList = len(data['menu'])
order = [["Nama Menu", "Harga", "Jumlah Pembelian", "Total"]]
orderList = len(order)

menuList = len(data['menu'])
for i in range(0, menuList):
    order.append(["", 0, 0, 0])

def tambah_json(new_data, filename='menu.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["menu"].append(new_data)
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        # Sets file's current position at offset.


def tambahHOrder_json(new_data, filename='menu.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["history"].append(new_data)
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        # Sets file's current position at offset.


def edit_json(id, nama, harga, stok, filename='menu.json'):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["menu"][id]["Nama Menu"] = str(nama)
        file_data["menu"][id]["Harga"] = int(harga)
        file_data["menu"][id]["Stok"] = int(stok)
        file.seek(0)
        # convert back to json.
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)

def delete_json(delete_data, filename='menu.json'):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["menu"].pop(delete_data)

        file.seek(0)
        # convert back to json.
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)


def deleteSomeOrder_json(delete_data, filename='menu.json'):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["history"].pop(delete_data)

        file.seek(0)
        # convert back to json.
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)


def menull():
    os.system('cls')
    y = open('menu.json')
    data = json.load(y)
    menuList = len(data['menu'])
    for i in range(0, menuList):
        print(str(i) + " | " + str(data['menu'][i]["Nama Menu"]) +
              " | " + str(data['menu'][i]["Harga"]) +   " | " + str(data['menu'][i]["Stok"]))
    print("\n")


def menuRoti(state):
    os.system("cls")
    y = open('menu.json')
    data = json.load(y)
    menuList = len(data['menu'])

    print("Data Menu\n")
    menull()
    while True:
        crud = input("Pilih[tambah/edit/hapus/kembali] : ")
        if crud == "tambah":
            nama = str(input("Masukan Nama menu baru : "))
            while True:
                try:
                    harga = int(input("Masukan harga : "))
                    stok = int(input("Masukan jumlah stok : "))
                    break
                except ValueError:
                    print("Gunakan angka!")
                    continue
            y = {"Nama Menu": str(nama), "Harga": int(harga), "Stok": int(stok)}
            tambah_json(y)
            menull()
        elif crud == "edit":
            while True:
                try:
                    menuDel = int(
                        input("Pilih nomor menu yang akan di edit : "))
                    break
                except:
                    print("Gunakan Angka")
                    continue
            while True:
                if menuDel >= menuList or menuDel == 0:
                    print("||--------------Menu tidak ada--------------||")
                    try:
                        menuDel = int(
                            input("Pilih nomor menu yang akan di edit : "))
                    except:
                        print("Gunakan Angka")
                        continue
                else:
                    break
            nama = str(input("Masukan nama menu baru : "))
            harga = int(input("Masukan harga : "))
            stok = int(input("Masukan jumlah stok : "))
            edit_json(menuDel, nama, harga, stok)
            menull()
        elif crud == "hapus":
            print(menuList)
            while True:
                try:
                    menuDel = int(
                        input("Pilih nomor menu yang akan di hapus : "))
                    break
                except ValueError:
                    print("Gunakan angka!")
                    continue

            while True:
                if menuDel > menuList or menuDel == 0:
                    print("||--------------Menu tidak ada--------------||")
                    try:
                        menuDel = int(
                            input("Pilih nomor menu yang akan di hapus : "))
                    except ValueError:
                        print("Gunakan angka!")
                        continue
                else:
                    break
            validate = str(input("apakah anda yakin? [y/n] : "))
            if validate == "y":
                delete_json(menuDel)
            menull()
        elif crud == "kembali":
            os.system('cls')
            mainProcess(state)
            break
        else:
            print("tidak ada!")

# Proses untuk Data Orderan jika ada yang mau beli


def orders():
    orderList = len(order)
    for i in range(0, orderList):
        if order[i][3] == 0:
            continue
        print(str(i) + " | " + str(order[i][0]) + " | Rp." + str(
            order[i][1]) + " | " + str(order[i][2]) + " | Rp." + str(order[i][3]) + " | ")


def tambah():
    while True:
        try:
            menus = int(input("Masukan nomor menu : "))
            break
        except ValueError:
            print("Gunakan Angka")
            continue
    while True:
        if menus > menuList or menus == 0:
            print("||--------------Menu tidak ada--------------||")
            try:
                menus = int(input("Masukan nomor menu : "))
            except ValueError:
                print("Gunakan Angka")
                continue
        elif data['menu'][menus]["Stok"] == 0:
            print("||--------------Stok tidak tersedia--------------||")
            try:
                menus = int(input("Masukan nomor menu : "))
            except ValueError:
                print("Gunakan Angka")
                continue
        else:
            break
    while True:
        try:
            jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
            break
        except ValueError:
            print("Gunakan Angka")
            continue
    while True:
        if jumlah_pembelian > data['menu'][menus]['Stok']:
            print("|| Stok tidak mencukupi ||")
            try:
                jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
            except ValueError:
                print("Gunakan Angka")
                continue
        else:
            break
    lol = menus
    order[lol][0] = str(data["menu"][lol]["Nama Menu"])
    order[lol][1] = int(data["menu"][lol]["Harga"])
    order[lol][2] = int(order[lol][2]) + int(jumlah_pembelian)
    order[lol][3] = int(order[lol][2]) * int(order[lol][1])
    print("\n")
    orderList = len(order)
    orders()


def kurang():
    while True:
        try:
            menus = int(input("Masukan nomor menu : "))
            break
        except ValueError:
            print("Gunakan Angka")
            continue
    while True:
        if order[menus][3] == 0:
            print("||--------------Menu tidak ada--------------||")
            try:
                menus = int(input("Masukan nomor menu : "))
            except ValueError:
                print("Gunakan Angka")
                continue
        else:
            break
    while True:
        try:
            jumlah_pembelian = int(input("Masukkan jumlah pengurangan: "))
            break
        except ValueError:
            print("Gunakan Angka")
            continue
    lol = menus
    order[lol][0] = str(data["menu"][lol]["Nama Menu"])
    order[lol][1] = int(data["menu"][lol]["Harga"])
    order[lol][2] = int(order[lol][2]) - int(jumlah_pembelian)
    order[lol][3] = int(order[lol][2]) * int(order[lol][1])
    if order[lol][2] < 0:
        order[lol][2] = 0
        order[lol][3] = int(order[lol][2]) * int(order[lol][1])
    print("\n")
    orders()

def kurangedit_json(nana, filename='menu.json'):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        orderList = len(order)
        for i in range(0, orderList):
            if order[i][3] == 0 or file_data['menu'][i]['Stok'] == 'Stok':
                continue
            file_data['menu'][i]['Stok'] = int(file_data['menu'][i]['Stok']) - int(order[i][2]) 
        file.seek(0)
        # convert back to json.
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)

def hasil():
    orderl = len(order)
    
    y = open('menu.json')
    data = json.load(y)
    kurangedit_json(0)
    # table menu dipesan pelanggan
    print("")
    orders()
    print("")

    total_bayar = 0
    loop = 1
    while loop < orderl:
        total_bayar = total_bayar + int(order[loop][3])
        loop += 1
    diskon = 0
    # jika membeli diatas harga 50000 akan mendapatkan potongan diskon 10%
    if total_bayar > 50000:
        diskon = total_bayar * (10/100)
    # jika membeli diatas harga 100000 akan mendapatkan potongan diskon 25%
    elif total_bayar > 100000:
        diskon = total_bayar * (25/100)
    else:
        print("tidak ada diskon")

    bayar = total_bayar - diskon

    x = datetime.datetime.now()
    y = {"tanggal": str(x.strftime("%d - %b - %Y")), "penghasilan": int(bayar)}
    tambahHOrder_json(y)
    print("")
    print("Harga sebelum diskon : Rp.{}".format(int(total_bayar)))
    print("Potongan harga yang didapatkan : Rp.{}".format(int(diskon)))
    print("Harga setelah diskon : Rp.{}".format(int(bayar)))
    print("=====")
    print("Total Pembayaran Anda: Rp.{}".format(int(bayar)))


def orderBatal():
    for i in range(1, menuList):
        order[i][0] = ""
        order[i][1] = 0
        order[i][2] = 0
        order[i][3] = 0


def DataOrderan(state):
    menull()
    os.system("cls")
    y = open('menu.json')
    data = json.load(y)
    menuList = len(data['menu'])
    menull()
    pr = str(input("Input Data [y/n] : "))
    if pr != "y":
        os.system("cls")
        mainProcess(state)

    tambah()

    while True:
        jawab = input(
            "Apakah ada yang menu yang ingin ditambah atau dikurangi [tambah/kurang/tidak/reset/keluar]: ")
        if jawab == "tambah":
            menull()
            tambah()
        elif jawab == "kurang":
            orders()
            kurang()
        elif jawab == "tidak":
            hasil()
        elif jawab == "reset":
            orderBatal()
            orders()
        elif jawab == "keluar":
            orderBatal()
            os.system("cls")
            mainProcess(state)
            break
        else:
            print("tidak ada !")
            jawab = input(
                "Apakah ada yang menu yang ingin ditambah atau dikurangi? [tambah/kurang/tidak/reset/keluar]: ")


def historyD():
    y = open('menu.json')
    data = json.load(y)
    dataH = len(data['history'])

    for i in range(0, dataH):
        print(str(i) + " | " + str(data['history'][i]["tanggal"]) +
              " | Rp." + str(data['history'][i]["penghasilan"]))
    print("\n")
    total = 0
    ki = 1
    while(ki < dataH):
        total = total + int(data['history'][ki]["penghasilan"])
        ki += 1
    guinevere = dataH - 1
    average = total / guinevere
    print("Penghasilan saat ini : Rp." + str(total))
    print("Rata Rata Penghasilan saat ini : Rp." + str(average) + "\n")


def historyDataOrderan(state):
    os.system("cls")
    y = open('menu.json')
    data = json.load(y)
    dataH = len(data['history'])
    historyD()
    while True:
        aksi = input("pilih aksi [deleteAll/deleteSome/keluar] : ")
        if aksi == "deleteSome":
            while True:
                try:
                    a = int(input("Pilih nomor history yang akan dihapus : "))
                    break
                except ValueError:
                    print("Gunakan Angka")
                    continue
            while True:
                if a > dataH or dataH == 1:
                    print("Data tidak ada")
                    try:
                        a = int(input("Pilih nomor history yang akan dihapus : "))
                    except ValueError:
                        print("Gunakan Angka")
                        continue
                elif a == 0:
                    break
                else:
                    os.system("cls")
                    deleteSomeOrder_json(a)
                    historyD()
                    break
        elif aksi == "deleteAll":
            sure = input("apakah anda yakin akan menghapus semuanya [y/n]: ")
            if sure == "y":
                if dataH != 0 or dataH != 1:
                    os.system("cls")
                    i = 1
                    while i < dataH:
                        deleteSomeOrder_json(i)
                        i += 1
                    historyD
                else:
                    print("Data sudah kosong")
        elif aksi == "keluar":
            os.system("cls")
            mainProcess(state)
            break
        else:
            print("tidak ada!")


def mainProcess(state):
    print("-------------------Welcome to Bakery-------------------\n")
    if state == "Admin":
        list = ["Proses Pemesanan", "Data Menu", "Pemasukan Bulan ini"]
    else:
        list = ["Proses Pemesanan"]
    num = len(list)
    for i in range(0, num):
        print(str(i + 1) + ". " + str(list[i]))
    print("0. Logout")
    while True:
        try:
            inputData = int(input("Pilih nomor aktivitas : "))
        except ValueError:
            print("Input Number Please!")
            continue
        if inputData == 1:
            DataOrderan(state)
            break
        if inputData == 2:
            menuRoti(state)
            break
        if inputData == 3 and state == "Admin":
            historyDataOrderan(state)
            break
        elif inputData == 0:
            os.system('cls')
            state = ""
            login()
            break
        else:
            print("Tidak Ada")
            try:
                inputData = int(input("Pilih nomor aktivitas : "))
            except ValueError:
                print("Input Number Please!")
                continue


def login():
    print("-------------------Welcome to Bakery-------------------")
    while True:
        pilihan = str(input("[login / keluar] : "))
        if pilihan == "login":
            break
        elif pilihan == "keluar":
            quit()
        else:
            print("Tidak Ada")
    username = str(input("Username : "))
    password = str(getpass.getpass("Password : "))
    while True:
        if username == "grace" and password == "210":
            os.system('cls')
            statusAkun = ""
            print("\nLogin Berhasil\n")
            mainProcess(statusAkun)
            break
        elif username == "grace" and password == "107":
            os.system('cls')
            statusAkun = "Admin"
            print("\nLogin Berhasil\n")
            mainProcess(statusAkun)
            break
        else:
            print(
                "[-------------------Antara Username atau Password anda yang salah-------------------]")
            username = str(input("Username : "))
            password = str(getpass.getpass("Password : "))

login()
