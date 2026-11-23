"""
Sentetik kredi başvuru verisi üretici
Proje: Dijital Bireysel Kredi Başvuru Süreci (portföy projesi)

UYARI: Bu veri gerçek değildir. Oranlar, 2. haftadaki Şikayetvar araştırmasından
ve genel varsayımlardan türetilmiştir. Analiz sonuçları bu varsayımları yansıtır;
amaç SQL ile süreç analizi yapabilmeyi göstermektir.

Çalıştırma: python veri_uret.py  ->  kredi_basvuru.db ve csv/ klasörü
"""
import random, sqlite3, os, csv
from datetime import datetime, timedelta

random.seed(42)
N_MUSTERI = 6000
N_BASVURU = 8000
BASLANGIC = datetime(2026, 5, 1)
GUN = 184  # Mayıs - Ekim 2026

# --- Varsayımlar (README'de de listelenir) ---
P_EKRAN_ACILMADI = 0.02          # başvuru ekranı açılmıyor (araştırma: 7 kayıt)
P_BIRAK_TUTAR = 0.14             # tutar/vade ekranında bırakma
P_BIRAK_BILGI = 0.10             # bilgi girişinde bırakma (D1)
P_BELGE_ISTENIR = 0.55           # gelir belgesi istenen başvuru oranı
P_BIRAK_BELGE = {"18-29": 0.20, "30-44": 0.28, "45+": 0.38}  # belge adımında bırakma (D2)
P_KARAR = {"otomatik_onay": 0.50, "otomatik_red": 0.25, "manuel": 0.25}
P_EKSIK_BELGE = 0.30             # manuel incelemede eksik belge (D4)
P_MANUEL_ONAY = 0.70
P_ONONAY_GOSTER = 0.40           # mobilde ön onaylı limit gösterilen müşteri
P_ONONAY_RED = 0.15              # limit gösterildiği halde red (araştırma: 3 kayıt)
P_TEKRAR_BASVURU = 0.30          # gerekçesiz red sonrası 7 gün içinde tekrar başvuru (D6)
P_SOZLESME_BIRAK = 0.04          # onay sonrası sözleşmeyi onaylamama
P_AKTARIM_HATA = 0.04            # aktarım hatası (D5)
P_HATA_COZULUR = 0.45            # hatalı aktarımın sonradan çözülmesi

SEHIRLER = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Konya", "Diğer"]
SEHIR_W = [30, 12, 9, 6, 5, 4, 34]
GELIR = ["0-25 bin", "25-50 bin", "50-100 bin", "100 bin+"]
GELIR_W = [25, 40, 25, 10]


def yas_grubu(y):
    return "18-29" if y < 30 else ("30-44" if y < 45 else "45+")


def ts(d):
    return d.strftime("%Y-%m-%d %H:%M:%S") if d else None


musteriler = []
for i in range(1, N_MUSTERI + 1):
    yas = max(18, min(70, int(random.gauss(37, 11))))
    musteriler.append({
        "musteri_id": i,
        "yas": yas,
        "yas_grubu": yas_grubu(yas),
        "sehir": random.choices(SEHIRLER, SEHIR_W)[0],
        "gelir_araligi": random.choices(GELIR, GELIR_W)[0],
        "musteri_suresi_yil": random.randint(0, 15),
        "on_onayli_limit_var": int(random.random() < P_ONONAY_GOSTER),
    })

basvurular, manuel = [], []
bid = 0


def basvuru_olustur(m, baslangic, tekrar_mi):
    global bid
    bid += 1
    kanal = random.choices(["Mobil", "İnternet şube"], [80, 20])[0]
    tutar = random.choice([10000, 20000, 30000, 50000, 75000, 100000, 150000, 200000])
    vade = random.choice([6, 12, 18, 24, 36])
    b = {"basvuru_id": bid, "musteri_id": m["musteri_id"], "kanal": kanal, "tutar": tutar, "vade_ay": vade,
         "tekrar_basvuru": int(tekrar_mi), "on_onayli_limit_gosterildi": int(kanal == "Mobil" and m["on_onayli_limit_var"]),
         "baslangic_zamani": ts(baslangic), "son_adim": None, "gelir_belgesi_istendi": 0,
         "gonderim_zamani": None, "karar_turu": None, "karar_zamani": None, "sonuc": None,
         "red_gerekcesi_gosterildi": None, "sozlesme_onay_zamani": None,
         "aktarim_durumu": None, "aktarim_zamani": None}
    t = baslangic
    if kanal == "Mobil" and random.random() < P_EKRAN_ACILMADI:
        b["son_adim"] = "Ekran açılmadı"; return b
    t += timedelta(minutes=random.uniform(0.5, 3))
    if random.random() < P_BIRAK_TUTAR:
        b["son_adim"] = "Tutar ve vade"; return b
    t += timedelta(minutes=random.uniform(2, 8))
    if random.random() < P_BIRAK_BILGI:
        b["son_adim"] = "Bilgi girişi"; return b
    if random.random() < P_BELGE_ISTENIR:
        b["gelir_belgesi_istendi"] = 1
        t += timedelta(minutes=random.uniform(5, 40))
        if random.random() < P_BIRAK_BELGE[m["yas_grubu"]]:
            b["son_adim"] = "Gelir belgesi"; return b
    b["son_adim"] = "Gönderildi"
    b["gonderim_zamani"] = ts(t)
    # Karar
    p = dict(P_KARAR)
    karar = random.choices(list(p), list(p.values()))[0]
    if b["on_onayli_limit_gosterildi"] and karar == "otomatik_red" and random.random() > P_ONONAY_RED / P_KARAR["otomatik_red"]:
        karar = "otomatik_onay"  # limit gösterilenlerde red daha seyrek ama sıfır değil
    b["karar_turu"] = karar
    if karar == "manuel":
        atanma = t + timedelta(minutes=random.uniform(1, 10))
        eksik = random.random() < P_EKSIK_BELGE
        sure = random.uniform(24, 96) if eksik else random.uniform(3, 30)
        bitis = atanma + timedelta(hours=sure)
        mon = random.random() < (P_MANUEL_ONAY - (0.1 if eksik else 0))
        manuel.append({"basvuru_id": bid, "atanma_zamani": ts(atanma), "tamamlanma_zamani": ts(bitis),
                       "eksik_belge": int(eksik), "sonuc": "Onay" if mon else "Red"})
        t = bitis
        b["sonuc"] = "Onay" if mon else "Red"
    else:
        t += timedelta(seconds=random.uniform(20, 90))
        b["sonuc"] = "Onay" if karar == "otomatik_onay" else "Red"
    b["karar_zamani"] = ts(t)
    if b["sonuc"] == "Red":
        b["red_gerekcesi_gosterildi"] = 0  # As-Is: gerekçe gösterilmiyor (D6)
        return b
    # Onay sonrası (D5)
    if random.random() < P_SOZLESME_BIRAK:
        b["aktarim_durumu"] = "Sözleşme onaylanmadı"; return b
    t += timedelta(minutes=random.uniform(1, 15))
    b["sozlesme_onay_zamani"] = ts(t)
    if random.random() < P_AKTARIM_HATA:
        if random.random() < P_HATA_COZULUR:
            b["aktarim_durumu"] = "Gecikmeli aktarıldı"
            b["aktarim_zamani"] = ts(t + timedelta(days=random.uniform(1, 6)))
        else:
            b["aktarim_durumu"] = "İptal edildi"
    else:
        b["aktarim_durumu"] = "Aktarıldı"
        b["aktarim_zamani"] = ts(t + timedelta(seconds=random.uniform(5, 60)))
    return b


while bid < N_BASVURU:
    m = random.choice(musteriler)
    bas = BASLANGIC + timedelta(days=random.uniform(0, GUN - 8), hours=random.gauss(0, 3))
    b = basvuru_olustur(m, bas, False)
    basvurular.append(b)
    if b["sonuc"] == "Red" and random.random() < P_TEKRAR_BASVURU and bid < N_BASVURU:
        t2 = datetime.strptime(b["karar_zamani"], "%Y-%m-%d %H:%M:%S") + timedelta(days=random.uniform(0.1, 7))
        basvurular.append(basvuru_olustur(m, t2, True))

# --- Yazma ---
if os.path.exists("kredi_basvuru.db"):
    os.remove("kredi_basvuru.db")
con = sqlite3.connect("kredi_basvuru.db")
os.makedirs("csv", exist_ok=True)
for ad, satirlar in [("musteriler", musteriler), ("basvurular", basvurular), ("manuel_inceleme", manuel)]:
    kolonlar = list(satirlar[0].keys())
    con.execute(f"CREATE TABLE {ad} ({', '.join(kolonlar)})")
    con.executemany(f"INSERT INTO {ad} VALUES ({','.join('?' * len(kolonlar))})", [tuple(r[k] for k in kolonlar) for r in satirlar])
    with open(f"csv/{ad}.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=kolonlar); w.writeheader(); w.writerows(satirlar)
con.commit(); con.close()
print(len(musteriler), "müşteri,", len(basvurular), "başvuru,", len(manuel), "manuel inceleme")
