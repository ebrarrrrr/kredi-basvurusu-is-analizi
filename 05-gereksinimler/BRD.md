# İş Gereksinimleri Dokümanı (BRD): Dijital Bireysel Kredi Başvurusu

Hazırlayan: Ebrar Topal · Sürüm 1.0 · 23 Kasım 2026

Bu doküman, Örnek Banka'nın mobil ihtiyaç kredisi başvuru sürecinin yeniden tasarımı için iş gereksinimlerini tanımlar. Gereksinimler kullanıcı araştırmasına (44 kayıt), As-Is süreç modeline ve veri analizine dayanır. Banka kurgusal, veri sentetiktir.

## 1. İş hedefleri

Amacımız, başlayan mobil başvuruların daha fazlasının gerçekten kullandırılan krediye dönüşmesi ve banka içindeki manuel iş yükünün azalmasıdır. Hedef değerler varsayımsaldır ve pilot sonrasında güncellenmelidir.

| KPI | As-Is | Hedef |
| --- | --- | --- |
| Başvuru tamamlama oranı (mobil) | %64,0 | %75 |
| Otomatik karar oranı | %75,4 | %85 |
| Manuel incelemede ortalama süre | 29,1 saat | 4 iş saati (SLA) |
| Onaylanıp kullandırılamayan ya da geciken kredi | %3,6 | %1'in altında |
| Başlayan başvurudan kullandırılan krediye dönüşüm | %42,7 | %52 |
| Red sonrası 7 gün içinde tekrar başvuru | %28,4 | %15 |

## 2. Kapsam

| Kapsam içi | Kapsam dışı |
| --- | --- |
| Mevcut müşterinin mobil uygulamadan ihtiyaç kredisi başvurusu | Yeni müşteri edinimi, konut ve taşıt kredisi |
| Teklif, bilgi, gelir, karar, manuel inceleme adımları | Kredi skor modelinin iç mantığı |
| Dijital sözleşme onayı ve kredinin hesaba aktarımı | Tahsilat ve gecikme süreçleri |
| Müşteri bildirimleri ve tahsis ekibinin iş kuyruğu | Şube ve çağrı merkezi ekranları |

## 3. Paydaşlar

| Paydaş | Rolü | Ana beklentisi |
| --- | --- | --- |
| Dijital kanal ürün sahibi | Sponsor, önceliklendirme | Dönüşüm oranının artması |
| Bireysel müşteri | Son kullanıcı | Hızlı, şeffaf başvuru |
| Kredi tahsis ekibi | Manuel inceleme | Eksiksiz dosya, daha az takip işi |
| Risk yönetimi | Onay | Takipteki kredi oranının artmaması |
| Uyum ve hukuk | Onay | KVKK ve tüketici mevzuatına uyum |
| BT ve entegrasyon | Geliştirme | Net ve uygulanabilir gereksinim |

## 4. Mevcut durum ve sorunlar

As-Is sürecinde altı darboğaz tespit edildi. Araştırmada en sık görülenler karardan sonraki adımlardı; veri analizinde ise en büyük kayıp başvuru gönderilmeden önce gerçekleşiyor.

| Kod | Darboğaz | Araştırma (kayıt) | Veri analizi bulgusu |
| --- | --- | --- | --- |
| D1 | Form elle dolduruluyor | 1 | Başvuruların %8,5'i bilgi girişinde bırakılıyor |
| D2 | Gelir belgesi isteniyor | 1 | Belge istendiğinde bırakma 45+ yaşta %37,6 |
| D3 | Manuel incelemede bekleme, durum bilgisi yok | 4 | Manuel inceleme ortalama 29,1 saat |
| D4 | Eksik belge döngüsü | 0 | Eksik belge incelemeyi 3,6 kat uzatıyor |
| D5 | Onaylanan kredi hesaba geçmiyor | 12 | Onaylananların %3,6'sı iptal ya da gecikme; 5,4 milyon TL kayıp hacim |
| D6 | Red gerekçesi açıklanmıyor | 9 | Reddedilenlerin %28,4'ü 7 gün içinde tekrar başvuruyor |

## 5. Önerilen çözüm

To-Be sürecinde müşteri bilgileri önceden doldurulmuş olarak görür, gelir bilgisi açık rızayla dijital alınır ve çoğu başvuru anında sonuçlanır. Manuel incelemeye düşen dosyalar SLA'lı bir iş kuyruğunda ilerler. Kredi onaylandıktan sonra aktarım hatası otomatik olarak yeniden denenir. Reddedilen müşteriye genel red nedeni gösterilir. Ayrıntılı akış drawio dosyasının "4 - To-Be" sayfasındadır.

## 6. Fonksiyonel gereksinimler

Öncelikler MoSCoW yöntemiyle belirlendi: Must (olmazsa olmaz), Should (önemli), Could (olsa iyi olur).

| Kod | Gereksinim | Öncelik | Kaynak |
| --- | --- | --- | --- |
| FR-01 | Sistem, mevcut müşteriye başvuru ekranında ön onaylı kredi limitini göstermelidir. | Must | Araştırma |
| FR-02 | Sistem, tutar ve vade seçildiğinde aylık taksiti, faizi ve toplam geri ödeme tutarını anında hesaplamalıdır. | Must | Tüketici mevzuatı |
| FR-03 | Sistem, başvuru formunu bankadaki müşteri kayıtlarıyla önceden doldurmalıdır. | Must | D1 |
| FR-04 | Sistem, gelir bilgisini almadan önce müşteriden açık rıza almalı ve rızayı tarih ve saatiyle kaydetmelidir. | Must | D2, KVKK |
| FR-05 | Sistem, gelir bilgisi dijital alınamazsa belge yükleme seçeneği sunmalıdır. | Should | D2 |
| FR-06 | Sistem, başvuruyu karar motoruna göndermeli ve sonucu otomatik onay, otomatik red veya manuel inceleme olarak sınıflandırmalıdır. | Must | D3 |
| FR-07 | Sistem, manuel incelemeye düşen dosyaları SLA süresiyle birlikte tahsis ekibinin iş kuyruğuna atamalı ve SLA aşımını uyarmalıdır. | Must | D3 |
| FR-08 | Sistem, müşteriye başvuru durumunu uygulamada göstermeli ve her durum değişikliğinde bildirim göndermelidir. | Must | D3 |
| FR-09 | Sistem, eksik belge istendiğinde müşterinin belgeyi uygulama içinden yüklemesine izin vermelidir. | Should | D4 |
| FR-10 | Sistem, yarım kalan başvuruyu 7 gün saklamalı ve müşteriye hatırlatma göndermelidir. | Could | Veri analizi |
| FR-11 | Sistem, onaylanan kredinin aktarımı başarısız olursa işlemi otomatik yeniden denemeli, müşteriye durumu ve sonraki adımı göstermeli ve aktarım tamamlanana kadar operasyon ekibine bildirim göndermelidir. | Must | D5 |
| FR-12 | Sistem, reddedilen başvuruda müşteriye genel red nedeni kategorisini ve yeniden başvuru için önerilen süreyi göstermelidir. | Should | D6 |
| FR-13 | Sistem, uygulamada gösterilen ön onaylı limiti karar motorunun güncel sonucuyla eşleştirmeli; limit geçerli değilse göstermemelidir. | Must | Araştırma |
| FR-14 | Sistem, müşteriye başvuru öncesinde sözleşme öncesi bilgi formunu göstermeli ve sözleşmenin dijital olarak onaylanmasını sağlamalıdır. | Must | Tüketici mevzuatı |

## 7. Fonksiyonel olmayan gereksinimler

| Kod | Gereksinim |
| --- | --- |
| NFR-01 | Otomatik karar, başvuru gönderiminden sonra 60 saniye içinde müşteriye gösterilmelidir. |
| NFR-02 | Başvuru akışı 7/24 kullanılabilir olmalı; aylık erişilebilirlik hedefi %99,5'tir. |
| NFR-03 | Başvuru ekranı açılamıyorsa müşteriye nedeni ve alternatif kanal anlaşılır bir mesajla gösterilmelidir. (Araştırma: 7 kayıt) |
| NFR-04 | Kişisel ve finansal veriler aktarımda ve depolamada şifrelenmelidir. |
| NFR-05 | Başvuruya ait tüm adımlar denetim kaydı (audit log) olarak tutulmalıdır. |
| NFR-06 | Başvuru akışı en fazla 5 ekrandan oluşmalı ve ekran okuyucularla kullanılabilir olmalıdır. |

## 8. Regülasyon gereksinimleri

Güncel mevzuat uygulama öncesinde uyum ekibiyle doğrulanmalıdır.

- **KVKK (6698 sayılı Kanun):** Aydınlatma metni, gelir verisi için açık rıza, verinin yalnızca amaçla sınırlı kullanılması (FR-04).
- **Tüketici mevzuatı (6502 sayılı Kanun):** Sözleşme öncesi bilgi formu, toplam maliyetin açıkça gösterilmesi ve cayma hakkı bilgilendirmesi (FR-02, FR-14).
- **BDDK düzenlemeleri:** Uzaktan kimlik doğrulama ve elektronik ortamda sözleşme kurulması kuralları; ihtiyaç kredisinde vade ve limit sınırları.
- **MASAK:** Müşteriyi tanı (KYC) yükümlülükleri.

## 9. Varsayımlar, bağımlılıklar ve riskler

**Varsayımlar:** Başvuru sahibi mevcut müşteridir. Mevcut karar motoru kullanılır; yeni skor modeli kurulmaz.

**Bağımlılıklar:** KKB sorgusu entegrasyonu; gelir bilgisinin dijital alınması için kamu veri kaynaklarıyla entegrasyon; mobil bildirim altyapısı; tahsis ekibinin iş kuyruğu aracı.

| Risk | Etki | Önlem |
| --- | --- | --- |
| Otomatik karar oranı artarken takipteki kredi oranı yükselir | Yüksek | Risk ekibiyle pilot; karar eşikleri kademeli değiştirilir |
| Red nedeni gösterilmesi skor modelinin tersine mühendisliğine yol açar | Orta | Yalnızca genel kategoriler gösterilir, ayrıntı verilmez |
| Gelir verisi entegrasyonu gecikir | Orta | FR-05 ile belge yükleme yedek yol olarak kalır |
| SLA hedefi tahsis ekibi kapasitesini aşar | Orta | Kapasite analizi; SLA pilotta 8 saatle başlar |

## 10. Açık sorular

1. Red nedeni kategorileri hangileri olacak ve uyum ekibi bunları onaylıyor mu?
2. Aktarım hatasında kaç kez otomatik yeniden deneme yapılacak?
3. Ön onaylı limit hangi sıklıkta yeniden hesaplanacak?
4. SLA hesabında hafta sonu ve resmi tatiller nasıl sayılacak?

## 11. İzlenebilirlik

| Darboğaz | Gereksinim | User story (Jira) |
| --- | --- | --- |
| D1 | FR-03 | US-03 |
| D2 | FR-04, FR-05 | US-04, US-05 |
| D3 | FR-06, FR-07, FR-08 | US-06, US-07, US-08, US-09, US-10 |
| D4 | FR-09 | US-11 |
| D5 | FR-11 | US-14, US-15, US-16 |
| D6 | FR-12 | US-17, US-18 |
| Gösterilen limit uyuşmuyor | FR-01, FR-13 | US-01, US-19 |
| Mevzuat | FR-02, FR-14 | US-02, US-13 |
| Yarım kalan başvuru | FR-10 | US-12 |
| KPI takibi | – | US-20 |
