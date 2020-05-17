from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
from pandas import ExcelFile
import random
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

DNA_SIZE = 15            # DNA length
POP_SIZE = 50            # population size

def penduduk():
    return np.random.randint(2, size=(POP_SIZE, DNA_SIZE))

# Proses / Fungsi untuk membaca file yang diberikan untuk di tunjukkan di Program
def bacafile():
    file = open("D:\Other\Tupro2\contoh_data\data_latih_opsi_1.txt", "r")
    return file.readlines()

# Proses / Fungsi unutuk mengonversi file yang telah diberikan menjadi angka biner dengan panjang 15 bit
def konversi2():
    col_names = ['SUHU', 'WAKTU', 'KONDISI',  'KELEMBAPAN', 'IYA/TIDAK']
    file = pd.read_csv("D:\Other\Tupro2\contoh_data\data_latih_opsi_1.csv", header=None, names=col_names)
    file.head()
    file2 = file.iloc[:,:4]
    fly = file.iloc[:,4]
    onehot_encoder = OneHotEncoder(sparse=False)
    onehot_encoded = onehot_encoder.fit_transform(file2).astype(int)
    arrraydata = []
    tambaharr = []
    data = []
    hasilKonversi = []
    arrraydata.append(onehot_encoded)
    for i in range(len(fly)):
        if(fly[i] == "tidak"):
            tambaharr.append(0)
            hasilKonversi = np.append(arrraydata[0][i], [tambaharr])
            data.append(hasilKonversi)
        elif(fly[i] == "ya"):
            tambaharr.append(1)
            hasilKonversi = np.append(arrraydata[0][i], [tambaharr])
            data.append(hasilKonversi)
        tambaharr = []
    return data

# Proses / Fungsi untuk menghitung nilai fitness kemungkinan 1
def fitness():
    pop = penduduk()
    conv = konversi2()
    arrfit = []
    arrterima = []
    arrtolak = []
    terima = 0
    tolak = 0
    terima1 = 0
    tolak1 = 0

    for i in range (len(pop)):
        for j in range(len(pop[i])):
            if pop[i][j] == conv[i][j]:
                isi = 1
            else:
                isi = 0
            arrfit.append(isi)
    for h in range(len(arrfit)):
        if arrfit[h] == 1:
            terima = 1
        else:
            tolak = 1
        terima1 = terima1 + terima
        tolak1 = tolak1 + tolak
        
        arrterima.append(terima)
        arrtolak.append(tolak)
    return arrfit, terima1, tolak1

# Proses / Fungsi untuk menghitung nilai fitness kemungkinan 2
def fitness2():
    pop = penduduk()
    conv = konversi2()
    isi = 0
    issi = 0

    for i in range(np.any(len(pop))):
        if pop[i] == conv[i]:
            isi = 1
        else:
            isi = 0
        issi = issi + isi
    return issi

# Proses / Fungsi untuk mencari orang tua dari fitness yang terbaik
def ortu(pops, pops2):
    popor = []
    for i in range(10):
        rand = random.randint(0,len(pops)-1)
        print("ortu ke - ", rand+1)
        popor.append(pops[rand])
    return(popor)

def main():
    pop = penduduk()
    conv = konversi2()
    print("Populasi dari Random Number")
    print('')
    for i in range(len(pop)):
        print(pop[i])
    print('')
    print('')
    data = bacafile()
    print(" Suhu ", " Waktu ", " Kondisi ",  " Kelembapan ", " Terbang/Tidak ")
    print(*data,sep="\n")
    for i in range(len(data)):
        print(data[i])
    covert = konversi2()
    print('')
    print("Hasil Konversi")
    print(*covert,sep="\n")
    print('')
    
    for i in range(len(pop)):
        acc = 0
        dcc = 0
        hasil = np.bitwise_and(pop[i], conv)
        print("Populasi ", i)
        for j in range(len(pop)):
            if hasil[j][14] == 1:
                print(j+1,'',hasil[j], " = Terima")
                acc = acc + 1
            else:
                print(j+1,'',hasil[j], " = Tolak")
                dcc = dcc + 1
        print("Yang Diterima : ", acc)
        print("Yang Ditolak  : ", dcc)
        print("Nilai Fitness : ", (acc/(acc+dcc)))
        print('')

if __name__ == "__main__":
    main()