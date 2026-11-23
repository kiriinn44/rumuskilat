# SPUSH - VERSI PY
import subprocess

def jalanin(perintah):
    hasil = subprocess.run(perintah, shell=True, capture_output=True, text=True)
    print(hasil.stdout)
    if hasil.stderr:
        print(hasil.stderr)
    return hasil.stdout.strip()

jalanin("git add .")
pesan = input("Pesan commit: ").strip()
if not pesan:
    pesan = "update"
jalanin(f'git commit -m "{pesan}"')
jalanin("git pull origin main")
jalanin("git push origin main")
print("PUSH SELESAI...")
# END - PUSH PY