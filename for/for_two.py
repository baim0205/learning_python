import json

def get_file_json(filename):
    """Membaca file JSON dan mengambil options dari kategori 'science' jika ada."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        # Pastikan kategori 'science' ada dalam quiz
        if "science" not in data["quiz"]:
            print("Error: Kategori 'science' tidak ditemukan dalam file JSON.")
            return []
        
        option_list = []
        for question in data["quiz"]["science"].values():
            option_list.append(question["options"])

        return option_list

    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return []
    except json.JSONDecodeError:
        print("Error: File JSON tidak valid.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Menjalankan fungsi
filename = "data.json"
options = get_file_json(filename)

# Menampilkan hasil jika tidak kosong
if options:
    for idx, option in enumerate(options, start=1):
        print("=-=-=-=-=")
        print(f"Question {idx} Options: {option}")
        print("=-=-=-=-=")
else:
    print("Tidak ada data yang bisa ditampilkan.")

'''
Next Tulis Here!!
'''