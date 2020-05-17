import csv

def fuzifikasi(fol, eng):
    fr = 0
    fs = 0
    ft = 0
    er = 0
    es = 0
    et = 0

    if(fol <=20000):
        fr = 1
        fs = 0
        pengikut = 'rendah'
    elif(fol > 20000) and (fol < 50000):
        fr = (50000-fol)/(50000-20000)
        fs = (fol-20000)/(50000-20000)
        pengikut = 'rendah'
    elif (fol > 50000) and (fol < 95117):
        fs = (95117 - fol)/(95117 - 50000)
        ft = (fol - 50000)/(95117 - 50000)
        pengikut = 'sedang'
    elif (fol >= 95117):
        ft = 1
        fs = 0
        pengikut = 'tinggi'
    
    if (eng <= 3):
        er = 1
        es = 0
        engage = 'rendah'
    elif (eng > 3) and (eng < 7):
        er = (7 - eng)/(7 - 3)
        es = (eng - 3)/(7 - 3)
        engage = 'rendah'
    elif (eng > 7) and (eng < 9.4):
        es = (9.4 - eng)/(9.4 - 7)
        et = (eng - 7)/(9.4 - 7)
        engage = 'sedang'
    elif (eng >= 9.4):
        et = 1
        es = 0
        engage = 'tinggi'
    
    return fr, fs, ft, er, es, et, pengikut, engage

# def inferensi2(fr, fs, ft, er, es, et, pengikut, engage):
#     if (pengikut == 'rendah') and (engage == 'rendah'):
#         return 'tolak'
#     elif (pengikut == 'rendah') and (engage == 'sedang'):
#         return 'tolak'
#     elif (pengikut == 'rendah') and (engage == 'tinggi'):
#         return 'tolak'    
#     elif (pengikut == 'sedang') and (engage == 'rendah'):
#         return 'tolak'   
#     elif (pengikut == 'sedang') and (engage == 'sedang'):
#         return 'terima'   
#     elif (pengikut == 'sedang') and (engage == 'tinggi'):
#         return 'terima'   
#     elif (pengikut == 'tinggi') and (engage == 'rendah'):
#         return 'tolak'   
#     elif (pengikut == 'tinggi') and (engage == 'sedang'):
#         return 'terima'   
#     elif (pengikut == 'tinggi') and (engage == 'tinggi'):
#         return 'terima'   

def inferensi(fr, fs, ft, er, es, et, pengikut, engage):
    iya = [0, 0, 0]
    tidak = [0, 0, 0, 0, 0, 0]
    if (fr > 0) and (er > 0):
        tidak[0] = min(fr, er)
    if (fr > 0) and (es > 0):
        iya[0] = min(fr, es)
    if (fr > 0) and (et > 0):
        iya[1] = min(fr, et)
    if (fs > 0) and (er > 0):
        tidak[1] = min(fs, er)
    if (fs > 0) and (es > 0):
        tidak[2] = min(fs, es)
    if (fs > 0) and (et > 0):
        iya[2] = min(fs, et)
    if (ft > 0) and (er > 0):
        tidak[3] = min(ft, er)
    if (ft > 0) and (es > 0):
        tidak[4] = min(ft, es)
    if (ft > 0) and (et > 0):
        tidak[5] = min (ft, et)

    return max(iya), max(tidak)

def defuzifikasi(iya, tidak):
    return (iya*60 + tidak*40)/(iya+tidak)

def main():
    with open('D:\\OneDrive - Telkom University\\Telkom Univ\\Semester 5\\Kecerdasan Buatan\\Tupro 3\\influencers.csv') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        with open('D:\\OneDrive - Telkom University\\Telkom Univ\\Semester 5\\Kecerdasan Buatan\\Tupro 3\\chosen.csv','w',newline='')as f:
            fieldnames=['id']
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                fr, fs, ft, er, es, et, pengikut, engage = fuzifikasi(float(row[1]), float(row[2]))
                iya, tidak = inferensi(fr, fs, ft, er, es, et, pengikut, engage)
                hasil = defuzifikasi(iya, tidak)
                if(hasil > 40):
                    print('ID yang teripilih, ID ke-',row[0])
                    print('Nilai Y* : ',round(hasil,2))
                    writer.writerow({'id':row[0]})
if __name__ == "__main__":
    main()