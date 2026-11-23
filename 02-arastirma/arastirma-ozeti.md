# Kullanıcı Araştırması Özeti

Hazırlayan: Ebrar Topal · Hafta 2 çıktısı

Mobil kredi şikayetleri başvuru formunda değil, kararda ve sonrasında yoğunlaşıyor. 41 şikayetin 20'si onaylanan kredinin kullandırılamaması (11) ya da gerekçesiz red (9) ile ilgili.

## Yöntem

- **Kaynak:** Şikayetvar'da mobil uygulamadan yapılan bireysel ihtiyaç kredisi başvurularıyla ilgili 41 şikayet. 11 banka: Akbank, Enpara, Garanti BBVA, Halkbank, ING, İş Bankası, Kuveyt Türk, QNB, TEB, VakıfBank, Yapı Kredi.
- **Ek kaynak:** Google Play yorumları (Halkbank'ın 2 yorumu, QNB için Kimola'nın yayımlanmış yorum analizi). Toplam 44 kayıt.
- **Kapsam dışı:** Kredi kartı, konut kredisi ve TOKİ şikayetleri.
- **Analiz:** Her kayıt etiket, süreç adımı ve darboğaz kodu ile tek tek sınıflandırıldı (`etiketleme.csv`).
- Yalnızca herkese açık, kamuya yayımlanmış içerik kullanıldı; gerçek kişilerden veri toplanmadı.

## Bulgular: darboğazlara göre

| Darboğaz | Şikayet sayısı | Bankalar |
| --- | --- | --- |
| D5 Onay sonrası kullandırım | 11 | Halkbank (7), TEB (3), ING (1) |
| Diğer yeni sorunlar | 11 | VakıfBank (5, başvuru ekranı açılmıyor), Garanti BBVA ve Akbank (gösterilen limit geçersiz, kanal yönlendirmesi, rızasız başvuru), Enpara (kimlik doğrulama), TEB (teknik hata) |
| D6 Gerekçesiz red | 9 | Akbank (4), Garanti BBVA, Enpara, İş Bankası, Kuveyt Türk, QNB |
| D3 Bekleme | 4 | Garanti BBVA (2), Enpara (2) |
| Darboğaz dışı (faiz, koşul, rıza) | 4 | Enpara (2), Yapı Kredi (2) |
| D1 Elle form | 1 | Garanti BBVA |
| D2 Gelir belgesi | 1 | İş Bankası |
| D4 Eksik belge | 0 | – |

## Üç ana bulgu

1. **Onay ekranı sürecin sonu değil.** 11 şikayette kredi onaylanmış ama para hesaba geçmemiş ya da kredi iptal edilmiş. Müşteriye kalan tek seçenek çoğu zaman "iptal" düğmesi.
2. **Red gerekçesi açıklanmıyor.** 9 şikayette müşteri neden reddedildiğini öğrenemiyor ve şubeye yönlendiriliyor. Müşteri tekrar başvuruyor ve her başvurunun kredi notunu etkilemesinden endişe ediyor.
3. **Gösterilen teklif ile gerçek karar uyuşmuyor.** Uygulama kişiye özel limit ya da faizsiz kampanya gösteriyor, başvuru yine de reddediliyor (Garanti BBVA, Akbank, QNB). Bu, To-Be'deki "ön onaylı limit" önerisi için bir risk; bu yüzden FR-13 eklendi.

## Yorum ve sınırlılıklar

- Şikayet sitelerine ağırlıkla para ya da zaman kaybeden müşteriler yazıyor. Formdan sıkılıp vazgeçen müşteri genelde şikayet yazmaz; D1 ve D2'nin az görünmesi bu sorunların olmadığını göstermez.
- 41 şikayet istatistiksel olarak temsil edici değil, ama tekrar eden temaları gösteriyor.
- Banka bazında sıralama yapılmamalı.
- Kayıtlar şikayet sayfalarındaki özetlerden alındı.

## Persona'lar (kurgusal)

Persona'lar araştırma bulgularından türetilmiştir, gerçek kişiler değildir.

**Elif, 27, özel sektör çalışanı (D5):** Acil bir masraf için aynı gün 40 bin TL kredi kullanmak istiyor. Başvurusu dakikalar içinde onaylanıyor ama para hesaba geçmiyor. İhtiyacı: onaydan sonra ne olduğunu görmek; sorun çıkarsa net bir sonraki adım.

**Murat, 41, kamu çalışanı, kredi notu iyi (D6):** Uygulamada gördüğü kampanyalı krediden yararlanmak istiyor. Başvurusu anında reddediliyor ve nedeni açıklanmıyor. İhtiyacı: genel red nedeni ve ne zaman tekrar başvurabileceği.

**Ayşe, kredi tahsis uzmanı (banka içi):** Dosyaları belirlenen süre içinde sonuçlandırmak istiyor. Müşteriler bekleyen dosyalar için şubeyi ve çağrı merkezini arıyor. İhtiyacı: bekleyen ve hatalı dosyaları tek bir iş kuyruğunda görmek. (Varsayım; iş ilanlarından doğrulanacak.)

## Kaynaklar

- Şikayetvar, ilgili banka sayfaları (kayıt bazında linkler `etiketleme.csv` içinde)
- [Kimola: QNB Mobil Google Play yorum analizi](https://kimola.com/reports/explore-insights-from-qnb-mobil-customer-feedback-analysis-google-play-tr-146594)
