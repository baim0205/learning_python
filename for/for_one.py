# import json

# with open ("test.json", "r") as file:
#     data = json.load(file)

#     # melakukan for pada data, pilih quizlalu ambil option nya

# # Mengambil semua opsi 
# option_list = []

# for category in data["quiz"].values():
#     for question in category.values():
#         option_list.append(question["options"])

# # Agar lebih rapih
# for idx, option in enumerate(option_list, start=1):
#     print(f"Question {idx} Options: {option}")

# # print(data)
# print("=====")
# print(option_list)

# Using Fungsi 

import json

def get_quiz_options(filename):
    """Membaca file JSON dan mengambil semua options dari setiap pertanyaan dalam quiz."""
    with open(filename, "r") as file:
        data = json.load(file)

    # Mengambil semua opsi
    option_list = []
    for category in data["quiz"].values():
        print("Loop 1 Ini isi dari data values yang dimasukan ke category:", category)
        for question in category.values():
            print("Loop 2 Ini isi dari category values yang dimasukan ke question:", question)
            option_list.append(question["options"])
            # append() menambahkan elemen di akhir list.
    
    return option_list

# Contoh pemanggilan fungsi
filename = "test.json"
options = get_quiz_options(filename)

# Menampilkan hasil
for idx, option in enumerate(options, start=1):
    print("=-=-=-=-=")
    print(f"Question {idx} Options: {option}")
    print("=-=-=-=-=")

print("=====")
print(options)


'''
Soal : 
1. Ambilah atau reading data test.json di dalam script python
2. Setelah data json berhasil di buka selanjutnya tolong ambil nilai options saja 
yang ada pada data.json 

Pemecahan masalah : 
siapkan list kosong untuk menampung sebuah nilai option_list = []
setelah itu lakukan looping untuk mengambil data lalu ambil values quiz 
setelah itu lakukan looping kembali untuk nilai yang sudah berhasil di filter
setelah sudah sesuai maukan ke dalam option_list dan gunakan fungsi append untuk 
mengambil nilai "option" saja

Nulis category yang mana nanti akan di isi oleh data yang akan di filter atau di loop 
disini di filter dengan quiz lalu isinya kuis ada apa saja -> ke category
setelah di simpan di category, buat lagi tulis question buat di masukan nilai category 
'''