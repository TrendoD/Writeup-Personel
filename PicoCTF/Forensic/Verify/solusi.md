# Writeup Lengkap: Challenge Verify (picoCTF 2024)

## Informasi Challenge
- **Nama**: Verify
- **Kategori**: Forensik
- **Tingkat Kesulitan**: Mudah
- **Tag**: Forensik, picoCTF 2024, grep, browser_webshell_solvable, checksum
- **Penulis**: JEFFERY JOHN

## Deskripsi Challenge
Banyak orang mencoba menipu pemain saya dengan flag imitasi. Saya ingin memastikan mereka mendapatkan yang asli! Saya akan memberikan hash SHA-256 dan script dekripsi untuk membantu Anda mengetahui bahwa flag saya adalah sah.

## Analisis Awal

Berdasarkan file dan informasi yang diberikan, kita perlu:
1. Menemukan file dengan hash SHA-256 yang cocok di antara ratusan file dalam direktori "files"
2. Mendekripsi file tersebut untuk mendapatkan flag yang sah

Checksum yang diberikan adalah:
```
467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02
```

## Langkah-langkah Penyelesaian

### Langkah 1: Login ke Instance Challenge

Hubungkan ke instance menggunakan perintah SSH yang disediakan:
```bash
ssh -p 52840 ctf-player@rhea.picoctf.net
```

Saat diminta, terima fingerprint dengan mengetik `yes` dan gunakan password `83dcefb7`.

### Langkah 2: Menjelajahi Lingkungan Server

Setelah terhubung, saya memeriksa file yang tersedia:
```bash
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
```

Kemudian saya memeriksa isi file checksum.txt:
```bash
ctf-player@pico-chall$ cat checksum.txt
467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02
```

Ini mengkonfirmasi hash SHA-256 yang perlu kita cocokkan.

### Langkah 3: Mengidentifikasi Proses Dekripsi

Melihat cara kerja script decrypt:
```bash
ctf-player@pico-chall$ decrypt.sh
Expected usage: decrypt.sh <filename>
```

Saya juga mencoba menjalankannya pada file checksum:
```bash
ctf-player@pico-chall$ decrypt.sh checksum.txt
bad magic number
Error: Failed to decrypt 'checksum.txt'. This flag is fake! Keep looking!
```

Ini mengkonfirmasi bahwa kita perlu menemukan file yang benar untuk didekripsi.

### Langkah 4: Memeriksa Direktori Files

Saya menemukan bahwa direktori "files" berisi banyak file dengan nama acak:
```bash
ctf-player@pico-chall$ cd files
ctf-player@pico-chall$ ls | wc -l
203
```

Dengan 203 file untuk diperiksa, kita perlu mengotomatisasi proses pencarian file dengan hash yang cocok.

### Langkah 5: Menemukan File dengan Hash SHA-256 yang Cocok

Saya membuat skrip shell untuk mengulang semua file dan memeriksa hash SHA-256 mereka:

```bash
for file in *; do
    hash=$(sha256sum "$file" | awk '{print $1}')
    if [ "$hash" = "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02" ]; then
        echo "File yang cocok ditemukan: $file"
        echo "Hash: $hash"
    fi
done
```

Setelah menjalankan skrip ini, saya menemukan file dengan hash SHA-256 yang cocok. Mari kita sebut `FILE_COCOK` untuk writeup ini (nama file sebenarnya bervariasi).

### Langkah 6: Mendekripsi File yang Cocok

Saya kembali ke direktori induk dan menjalankan skrip decrypt.sh pada file yang cocok:

```bash
cd ..
./decrypt.sh files/FILE_COCOK
```

Ini menjalankan proses dekripsi dan mengungkapkan flag.

## Flag

Format flag adalah `picoCTF{...}`. Flag yang tepat akan ditampilkan setelah menjalankan skrip decrypt.sh pada file yang benar.

```
picoCTF{trust_but_verify_451fd69b}
```

Karena disini file yang cocok pada saya adalah 45lfd69b kemungkinan flagnya akan memakai file yang cocok pada bagian akhir untuk flagnya
