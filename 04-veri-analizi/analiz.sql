-- Dijital Kredi Başvuru Süreci – Veri Analizi (Hafta 4)
-- Veritabanı: kredi_basvuru.db (SQLite, SENTETİK veri)
-- Çalıştırma: DB Browser for SQLite > Execute SQL, ya da: sqlite3 kredi_basvuru.db < analiz.sql

-- S1. Başvuru hunisi: her adımda kaç başvuru kaldı?
-- (Sadece Mobil kanal; huni sırası son_adim'e göre)
WITH adimlar AS (
  SELECT son_adim, COUNT(*) AS n FROM basvurular WHERE kanal = 'Mobil' GROUP BY son_adim
), toplam AS (SELECT SUM(n) AS t FROM adimlar)
SELECT son_adim AS "Bırakılan / son adım",
       n AS "Başvuru",
       ROUND(100.0 * n / (SELECT t FROM toplam), 1) AS "Yüzde"
FROM adimlar
ORDER BY CASE son_adim WHEN 'Ekran açılmadı' THEN 1 WHEN 'Tutar ve vade' THEN 2
         WHEN 'Bilgi girişi' THEN 3 WHEN 'Gelir belgesi' THEN 4 ELSE 5 END;

-- S2. Kanala göre tamamlama (gönderme) oranı
SELECT kanal AS "Kanal",
       COUNT(*) AS "Başlayan",
       SUM(gonderim_zamani IS NOT NULL) AS "Gönderilen",
       ROUND(100.0 * SUM(gonderim_zamani IS NOT NULL) / COUNT(*), 1) AS "Tamamlama %"
FROM basvurular GROUP BY kanal;

-- S3. Gelir belgesi istenince bırakma oranı yaş grubuna göre (D2)
SELECT m.yas_grubu AS "Yaş grubu",
       COUNT(*) AS "Belge istenen",
       SUM(b.son_adim = 'Gelir belgesi') AS "Belge adımında bırakan",
       ROUND(100.0 * SUM(b.son_adim = 'Gelir belgesi') / COUNT(*), 1) AS "Bırakma %"
FROM basvurular b JOIN musteriler m ON m.musteri_id = b.musteri_id
WHERE b.gelir_belgesi_istendi = 1
GROUP BY m.yas_grubu ORDER BY m.yas_grubu;

-- S4. Karar türüne göre dağılım ve ortalama karar süresi (saat)
SELECT karar_turu AS "Karar türü",
       COUNT(*) AS "Başvuru",
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM basvurular WHERE karar_turu IS NOT NULL), 1) AS "Pay %",
       ROUND(AVG((julianday(karar_zamani) - julianday(gonderim_zamani)) * 24), 2) AS "Ort. karar süresi (saat)"
FROM basvurular WHERE karar_turu IS NOT NULL GROUP BY karar_turu;

-- S5. Eksik belge, manuel incelemeyi ne kadar uzatıyor? (D3, D4)
SELECT CASE eksik_belge WHEN 1 THEN 'Eksik belge var' ELSE 'Eksik belge yok' END AS "Durum",
       COUNT(*) AS "Dosya",
       ROUND(AVG((julianday(tamamlanma_zamani) - julianday(atanma_zamani)) * 24), 1) AS "Ort. inceleme (saat)",
       ROUND(100.0 * SUM(sonuc = 'Onay') / COUNT(*), 1) AS "Onay %"
FROM manuel_inceleme GROUP BY eksik_belge;

-- S6. Onaydan sonra ne oluyor? (D5)
SELECT aktarim_durumu AS "Onay sonrası durum",
       COUNT(*) AS "Başvuru",
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM basvurular WHERE sonuc = 'Onay'), 1) AS "Onaylananların %'si"
FROM basvurular WHERE sonuc = 'Onay' GROUP BY aktarim_durumu ORDER BY 2 DESC;

-- S7. Kaybedilen kredi hacmi: onaylanıp kullandırılamayan tutar (D5)
SELECT COUNT(*) AS "İptal edilen onaylı kredi",
       SUM(tutar) AS "Toplam tutar (TL)",
       ROUND(AVG(tutar)) AS "Ortalama tutar (TL)"
FROM basvurular WHERE aktarim_durumu = 'İptal edildi';

-- S8. Gerekçesiz red sonrası 7 gün içinde tekrar başvuru (D6)
SELECT COUNT(*) AS "Tekrar başvuru",
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM basvurular WHERE sonuc = 'Red'), 1) AS "Redlere oranı %",
       SUM(sonuc IS NOT NULL) AS "Karara ulaşan tekrar",
       ROUND(100.0 * SUM(sonuc = 'Red') / SUM(sonuc IS NOT NULL), 1) AS "Karara ulaşanlarda red %"
FROM basvurular WHERE tekrar_basvuru = 1;

-- S9. Ön onaylı limit gösterildiği hâlde reddedilenler
SELECT CASE on_onayli_limit_gosterildi WHEN 1 THEN 'Limit gösterildi' ELSE 'Limit gösterilmedi' END AS "Durum",
       COUNT(*) AS "Karar verilen",
       ROUND(100.0 * SUM(sonuc = 'Red') / COUNT(*), 1) AS "Red %"
FROM basvurular WHERE kanal = 'Mobil' AND sonuc IS NOT NULL
GROUP BY on_onayli_limit_gosterildi;

-- S10. Uçtan uca: 100 başlayan mobil başvurudan kaçı krediyi gerçekten kullanıyor?
SELECT COUNT(*) AS "Başlayan",
       SUM(gonderim_zamani IS NOT NULL) AS "Gönderilen",
       SUM(sonuc = 'Onay') AS "Onaylanan",
       SUM(aktarim_durumu IN ('Aktarıldı', 'Gecikmeli aktarıldı')) AS "Kullandırılan",
       ROUND(100.0 * SUM(aktarim_durumu IN ('Aktarıldı', 'Gecikmeli aktarıldı')) / COUNT(*), 1) AS "Başlayanların %'si"
FROM basvurular WHERE kanal = 'Mobil';
