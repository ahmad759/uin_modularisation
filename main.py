nama = 'ahmad'
program = 'gerak lurus'
print (f'program {program} oleh {nama}')

def hitung_kecepatan (jarak,waktu):
    kecepatan = jarak/ waktu
    print (f'jarak = {jarak/1000}km ditempuh dalam waktu = {waktu/ 60}menit')
    print (f'sehingga kecepatan + {kecepatan} m/s')
    return kecepatan

kecepatan = hitung_kecepatan(1000,5*60)
kecepatan = hitung_kecepatan(3000,70*60)

def hitung_luas (panjang,lebar):
    luas = panjang*lebar
    print (f'luas persegi panjang adalah {luas}m persegi')
    return luas


luas = hitung_luas(100,65)


#buat fungsi baru