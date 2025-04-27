mahasiswa = [
    {"nama": "Eichal Elphindo Ginting", "nim": "122140165", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 78},
    {"nama": "Rizky Abdillah", "nim": "122140127", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 68},
    {"nama": "Bezalel Samuel Manik", "nim": "122140140", "nilai_uts": 90, "nilai_uas": 88, "nilai_tugas": 92},
    {"nama": "Havidz Ridho Pratama", "nim": "122140160", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
    {"nama": "Muhammad Hakiki", "nim": "122140044", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 40}
]

for mhs in mahasiswa:
    nilai_akhir = (0.3 * mhs["nilai_uts"]) + (0.4 * mhs["nilai_uas"]) + (0.3 * mhs["nilai_tugas"])
    mhs["nilai_akhir"] = round(nilai_akhir, 2)
    
    # Menentukan grade
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif nilai_akhir >= 70:
        mhs["grade"] = "B"
    elif nilai_akhir >= 60:
        mhs["grade"] = "C"
    elif nilai_akhir >= 50:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<12} {:<6}".format(
    "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Grade"
))
print("-" * 70)

for mhs in mahasiswa:
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<12} {:<6}".format(
        mhs["nama"], mhs["nim"], mhs["nilai_uts"], mhs["nilai_uas"],
        mhs["nilai_tugas"], mhs["nilai_akhir"], mhs["grade"]
    ))

tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"Nama: {tertinggi['nama']}, NIM: {tertinggi['nim']}, Nilai Akhir: {tertinggi['nilai_akhir']}, Grade: {tertinggi['grade']}")

print("\nMahasiswa dengan nilai terendah:")
print(f"Nama: {terendah['nama']}, NIM: {terendah['nim']}, Nilai Akhir: {terendah['nilai_akhir']}, Grade: {terendah['grade']}")
