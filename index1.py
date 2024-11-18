nilai_murid = {
    'murid1' : {
        'nama' : 'Hilmi',
        'usia' : 20,
        'nilai' : {
            'matematika' : 90,
            'sains' : 90,
            'bahasa_english' : 80   
        }
    },
    'murid2' : {
        'nama' : 'Farah',
        'usia' : 20,
        'nilai': {
            'matematika' : 90,
            'sains' : 90,
            'bahasa_english' : 80   
        }
    },
    'murid3' : {
        'nama' : 'Qoni',
        'usia' : 20,
        'nilai':{
            'matematika' : 90,
            'sains' : 90,
            'bahasa_english' : 80   
        }
    }
}

# print semua murid 
print("semua data murid")
for murid, info in nilai_murid.items():
    print  (f"{murid} : {info}")
    print()
# print hanya nilai matematika dari murid2
print("nilai matematika dari murid ke2")
print(nilai_murid['murid2']['nilai']['matematika'])
print()
# print nama murid 3
print("nama murid ke3 adalah")
print(nilai_murid['murid3']['nama'])


