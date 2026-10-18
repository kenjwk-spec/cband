# APK cband by keno - SC by KENO
import requests

print("=== CEK BAND WA ===")
print("cband by keno")
print("by KENO\n")

nomor = input("Masukin nomor WA: ").strip()
nomor = nomor.replace("+","").replace(" ","").replace("-","")

try:
    url = f"https://wa.me/{nomor}"
    r = requests.get(url, timeout=10)
    txt = r.text.lower()

    if "not found" in txt or "invalid" in txt or r.status_code == 404:
        print("\nband by keno")
    else:
        print("\nbelum keband nih, gas terus kink")
        print(url)

except:
    print("\nGagal cek, cek manual")
    print(f"https://wa.me/{nomor}")

print("\nby KENO")
