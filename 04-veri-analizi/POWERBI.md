# Power BI Dashboard (Hafta 5)

Sayfa başlığı: "Dijital Kredi Başvurusu – As-Is Performansı (sentetik veri)"

## Model

- `musteriler[musteri_id]` → `basvurular[musteri_id]` (bire çok)
- `basvurular[basvuru_id]` → `manuel_inceleme[basvuru_id]` (bire bir)
- `basvurular` tablosuna Power Query'de `Ay` sütunu: `Date.StartOfMonth(DateTime.Date([baslangic_zamani]))`

## DAX ölçüleri

```
Başvuru Sayısı = COUNTROWS(basvurular)

Gönderilen = CALCULATE([Başvuru Sayısı], NOT ISBLANK(basvurular[gonderim_zamani]))

Tamamlama Oranı = DIVIDE([Gönderilen], [Başvuru Sayısı])

Otomatik Karar Oranı =
DIVIDE(
    CALCULATE([Başvuru Sayısı], basvurular[karar_turu] IN {"otomatik_onay", "otomatik_red"}),
    CALCULATE([Başvuru Sayısı], basvurular[karar_turu] <> "")
)

Kullandırılan = CALCULATE([Başvuru Sayısı], basvurular[aktarim_durumu] IN {"Aktarıldı", "Gecikmeli aktarıldı"})

Uçtan Uca Dönüşüm = DIVIDE([Kullandırılan], [Başvuru Sayısı])

Kaybedilen Hacim (TL) = CALCULATE(SUM(basvurular[tutar]), basvurular[aktarim_durumu] = "İptal edildi")

Belge Bırakma Oranı =
DIVIDE(
    CALCULATE([Başvuru Sayısı], basvurular[son_adim] = "Gelir belgesi"),
    CALCULATE([Başvuru Sayısı], basvurular[gelir_belgesi_istendi] = 1)
)

Tekrar Başvuru Oranı =
DIVIDE(
    CALCULATE([Başvuru Sayısı], basvurular[tekrar_basvuru] = 1),
    CALCULATE([Başvuru Sayısı], basvurular[sonuc] = "Red")
)
```

Huni için `DATATABLE` ile 7 adımlı yardımcı tablo ve `SWITCH(SELECTEDVALUE(Huni[Sıra]), …)` ölçüsü kullanıldı.

## Görseller

| Yer | Görsel |
| --- | --- |
| Üst sıra | 4 kart: Başvuru Sayısı, Tamamlama Oranı, Otomatik Karar Oranı, Uçtan Uca Dönüşüm |
| Sol orta | Huni |
| Sağ orta | Kümelenmiş sütun: yaş grubu × Belge Bırakma Oranı |
| Sol alt | Çizgi: Ay × Tamamlama Oranı |
| Sağ alt | Çubuk: aktarım durumu + Kaybedilen Hacim kartı |
| Sol kenar | Dilimleyiciler: kanal, yaş grubu, şehir |

## Kontrol değerleri

| Ölçü | Beklenen |
| --- | --- |
| Başvuru Sayısı | 8.000 |
| Tamamlama Oranı | %64,1 |
| Otomatik Karar Oranı | %75,4 |
| Uçtan Uca Dönüşüm | %42,3 |
| Kaybedilen Hacim (TL) | 5.445.000 |
| Tekrar Başvuru Oranı | %28,4 |

> Dashboard ekran görüntüsünü `dashboard.png` adıyla bu klasöre ekleyin.
