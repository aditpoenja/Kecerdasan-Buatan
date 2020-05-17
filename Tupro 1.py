import random
# Proses Pencarian Kromosom Untuk ke Setiap Individu
def sendiri(chrome):
    krom = []
    for i in range(chrome):
        krom.append(random.randint(0,1))
    return krom

# Proses Pencarian Nilai Minimum
def rumusnilainmin(x1, x2):
    min = round(((4-((2.1)*(x1**2))+((x1**4)/3))*(x1**2)+(x1*x2)+(-4+(4*(x2**2)*x2**2))), 4)
    return(min)

# Proses Pencarian Fenotip untuk setiap individu
def rumusfenotip(rpopulasi, ra1, rb2, ra2, chrome):
    pembagia = 0
    pembagib = 0
    pembagia2 = 0
    gtot1 = 0
    gtot2 = 0
    g = 0
    h = 0
    tengah = len(chrome)//2
    for i in range(len(chrome)):
        pembagia = 2**-i+1
        pembagib = pembagib+pembagia

    for i in range(tengah):
        pembagia = 2**-i+1
        g = chrome[i]*pembagia
        gtot1 = gtot1 + g

    for tengah in range(len(chrome)):
        pembagia2 = 2**-tengah+1
        h = chrome[tengah]*pembagia2
        gtot2 = gtot2 + h

    return (round((rpopulasi)+((ra1-rpopulasi)/pembagib)*(gtot1), 4)) , round(((rb2)+((ra2-rb2)/pembagib)*(gtot2)), 4)

# Proses Pencarian Nilai Fitness
def fitt(chrome):
    return(round(1/(chrome+0.00001), 4))

# Proses Pengumpulan individu menjadi Populasi
def pop(ind):
    pops = []
    for i in range(ind):
        pops.append(sendiri(10))
    return pops

# Proses Pencarian Individu yang dicari Untuk Menjadi Orang Tua
def ortu(pops, angka):
    popor = []
    for i in range(10):
        rand = random.randint(0,len(pops)-1)
        print("ortu ke - ", rand+1)
        popor.append(pops[rand])
    return(popor)

# Proses Pengawinan atau Cross Over di antara orang tua terpilih tadi, disini ada 4 fungsi untuk trial and error
def merit(popor):
    j = 0
    i = 0
    kawin1 = []
    kawin2 = []
    kawin3 = []
    a = popor[0]
    b = popor[1]
    #kawin4 = []
    #nikahaja = []
    nikahaja = len(popor)
    acak = random.randint(0,nikahaja)
    print("BATAS : ", acak)
    for i in range(len(popor)):
        for b in range(nikahaja):
            kawin1.append(a)
            kawin2.append(b)
        for j in range(acak):
            kawin1.append(popor[i-1][b])
        for acak in range(len(popor)):
            kawin2.append(popor[i-1][b])
        #i = 0
        for k in range(acak):
            kawin2.append(popor[i][b])
        for acak in range(len(popor)):
            kawin1.append(popor[i][b])
    
    # for k in range(len(popor)):
    #     kawin3.append(kawin1)
    # kawin3.append(kawin1)
    kawin3.append(kawin2)
    # kawin4.append(kawin2)
    # kawin4.append(kawin1)
    #kawin3.append(kawin2)
    return(kawin3)

def married(popor):
    # nikah = []
    # mid = len(popor)//2
    # for i in range(mid):
    #     nikah = popor[i]
    nikah1 = []
    nikah2 = []
    nikah3 = []
    nikahaja = len(popor)
    #range = len(pops)
    batas = random.randint(0,nikahaja-1)
    print("BATAS ",batas)
    for b in range(nikahaja):
        #nikah2.append(popor[b])
        for i in range(batas):
            if i < batas:
                nikah2.append(popor[b][i])
            else:
                nikah3.append(popor[i])
        for batas in range(nikahaja):
            if j < batas:
                nikah3.append(popor[j])
            else:
                nikah2.append(popor[j])
    #nikah1.append(nikah2)
    #nikah1.append(nikah3)
    for k in range(len(popor)):
        nikah3.append(nikah2[k])
    return(nikah3)

def wedding(popor):
    kawin1 = []
    kawin2 = []
    kawin3 = []
    nikahaja = len(popor)
    tengah = len(popor)//2
    for i in range(tengah):
        kawin1.append(popor[i])
    for tengah in range(nikahaja):
        kawin2.append(popor[tengah])
    kawin3.append(kawin1)
    kawin3.append(kawin2)
    return(kawin3)

# Fungsi Pengawinan atau Cross Over yang terpilih, menjadi sebuah anak
def nikah(popor):
    nikah1 = []
    nikah2 = []
    b = 1
    # print(popor)
    nikahaja = len(popor)
    # print(nikahaja)
    batas = random.randint(1,8)
    print("BATAS ", batas)
    for b in range(batas):
        for i in range(batas):
            nikah1.append(popor[b-1][i])
            nikah2.append(popor[b][i])
        for batas in range(nikahaja):
            nikah1.append(popor[b][batas])
            nikah2.append(popor[b-1][batas])
    return(nikah1, nikah2)


# Proses Mutasi dari Anak terpilih
def mutasi (nikah1, nikah2):
    for i in range(len(nikah1)):
        if nikah1[i] == 1:
            nikah1[i] = 0
        else:
            nikah1[i] = 1
    for j in range(len(nikah2)):
        if nikah2[j] == 1:
            nikah2[j] = 0
        else:
            nikah2[j] = 1
    return(nikah1, nikah2)

def main():
    ax = 0
    angka = 10
    az = []
    d = []
    e = []
    for i in range(1):
        print("Populasi Ke: ", i+1)
        print(" ")
        populasi = pop(angka)
        probability = []
        
        for j in range(angka):
            print(*populasi,sep="\n")
            a,b = rumusfenotip(-3, 3, -2, 2, populasi[j])
            minimum = rumusnilainmin(a,b)
            az.append(fitt(minimum))
            ax = ax + az[j]
            print("Fenotip X1    : ", a, "  ", "| Fenotip X2    : ", b, "| Nilai Minimum : ", minimum, "| Nilai Fitness : ", az[j], " | Individu Bagian ke - ", j + 1)
            j = j + 1

        print("Total Nilai Fitness dari Populasi", i + 1, " : ", ax)
        print(" ")
        for j in range(angka):
            probability.append(az[j]/ax)
            print("Nilai Probabilitas Individu Ke - ", j + 1," : ", round(probability[j], 1))
            print("Konversi Probabilitas ke Integer : ",int(round(probability[j], 1)*10))
            j = j + 1
        print(" ")

        c = ortu(populasi, angka)
        print("Ortu Terpilih : ", *c,sep="\n")
        print("Kawin : ")
        d, e = nikah(c)
        for l in range(angka):
            print("anak ke -",l+1," ", d, e)
            print(" ")
        print(" ")

        print("Invert : ")
        mutasi(d, e)
        print(d)
        print(e)
        print(" ")
        print(" ")
if __name__ == "__main__":
    main()