# Veri Analizi Bulguları (Hafta 4)

> **Önemli:** Veri **sentetiktir**. 8.000 başvuru, araştırma bulgularından ve genel varsayımlardan türetilen oranlarla `veri_uret.py` ile üretildi (seed 42). Sonuçlar bu varsayımları yansıtır; amaç, gerçek veriyle aynı soruların nasıl yanıtlanacağını göstermektir.

## Veri seti

| Tablo | Satır | İçerik |
| --- | --- | --- |
| musteriler | 6.000 | yaş, şehir, gelir aralığı, müşteri süresi, ön onaylı limit |
| basvurular | 8.000 | kanal, tutar, vade, son adım, karar türü, sonuç, aktarım durumu, tekrar başvuru, zaman damgaları |
| manuel_inceleme | 1.259 | atanma ve tamamlanma zamanı, eksik belge, sonuç |

Dönem: Mayıs–Ekim 2026. Araçlar: Python, SQLite, SQL (`analiz.sql`, sorgular S1–S10), Power BI.

## Bulgular

**1. Huni: başlayan mobil başvuruların %36'sı gönderilmeden kayıp (S1)**

| Son adım | Başvuru | Pay |
| --- | --- | --- |
| Ekran açılmadı | 125 | %2,0 |
| Tutar ve vade | 896 | %14,0 |
| Bilgi girişi (D1) | 544 | %8,5 |
| Gelir belgesi (D2) | 740 | %11,5 |
| Gönderildi | 4.102 | %64,0 |

**2. Belge adımı yaşlı müşteriyi daha çok kaybediyor (S3, D2).** Belge istendiğinde bırakma: 18-29 yaş %21,0 · 30-44 yaş %26,9 · 45+ yaş %37,6.

**3. Manuel inceleme kararların %25'i ama sürenin neredeyse tamamı (S4, S5, D3, D4)**

| Karar türü | Pay | Ortalama karar süresi |
| --- | --- | --- |
| Otomatik onay | %53,1 | ~1 dakika |
| Otomatik red | %22,4 | ~1 dakika |
| Manuel inceleme | %24,6 | 29,1 saat |

Eksik belge çıkan dosyalar ortalama 60,3 saat, eksiksiz dosyalar 16,7 saat sürüyor (3,6 kat).

**4. Onaydan sonra kayıp (S6, S7, D5)**

| Onay sonrası durum | Başvuru | Pay |
| --- | --- | --- |
| Hemen aktarıldı | 3.320 | %92,5 |
| Sözleşme onaylanmadı | 139 | %3,9 |
| Gecikmeli aktarıldı (1-6 gün) | 66 | %1,8 |
| İptal edildi | 64 | %1,8 |

İptal edilen 64 onaylı kredinin toplam tutarı **5.445.000 TL**.

**5. Gerekçesiz red tekrar başvuru yaratıyor (S8, D6).** Reddedilenlerin %28,4'ü (437 başvuru) 7 gün içinde yeniden başvurdu ve bunların %28,4'ü yine reddedildi.

**6. Ön onaylı limit gösterilse de red kalkmıyor (S9).** Limit gösterilenlerde red oranı %22,4, gösterilmeyenlerde %33,4.

## KPI başlangıç değerleri (As-Is)

| KPI | Değer |
| --- | --- |
| Başvuru tamamlama oranı (mobil) | %64,0 |
| Otomatik karar oranı | %75,4 |
| Manuel incelemede ortalama süre | 29,1 saat |
| Onaylanıp kullandırılamayan ya da geciken kredi | %3,6 |
| Başlayan başvurudan kullandırılan krediye dönüşüm | %42,7 |

## Dosyaları çalıştırma

```bash
python veri_uret.py            # kredi_basvuru.db ve csv/ klasörünü yeniden üretir
sqlite3 kredi_basvuru.db < analiz.sql
```

`csv/` klasöründeki üç dosya Power BI'a yüklenir. DAX ölçüleri ve kontrol değerleri `POWERBI.md` dosyasındadır.
