# Proje Tanımı: Dijital Bireysel Kredi Başvuru Sürecinin İyileştirilmesi

Hazırlayan: Ebrar Topal · Hafta 1 çıktısı

Bu proje, bir bankanın mobil uygulamasındaki ihtiyaç kredisi başvuru sürecini inceler. Amacı, müşterinin başvuruyu yarıda bırakmasına yol açan adımları bulmak ve bunları azaltan yeni bir süreç önermektir. Proje kurgusal bir "Örnek Banka" üzerinden, herkese açık kaynaklar ve sentetik veriyle yürütülür.

## Arka plan

Bireysel bankacılık işlemlerinin giderek büyüyen bir kısmı mobil uygulamalardan yapılıyor. Kredi, bankalar için hem önemli bir gelir kaynağı hem de müşteriyi bankaya bağlayan bir ürün. Başvuru süreci zahmetliyse müşteri birkaç dakika içinde başka bir bankanın uygulamasına geçebiliyor.

## Problem

Örnek Banka'da mobil uygulamadan başlayan ihtiyaç kredisi başvurularının önemli bir kısmı tamamlanmadan bırakılıyor. Tamamlanan başvuruların bir kısmı da manuel incelemeye düşüp 1-3 gün bekliyor.

**Problem cümlesi:** Mobil kredi başvurusu yapan müşteri, süreç elle veri girişi ve belge yüklemesi gerektirdiği ve sonucu belirsiz bir süre beklettiği için başvurusunu yarıda bırakıyor. Bu durum bankanın kredi gelirini ve müşteri memnuniyetini düşürüyor, kredi tahsis ekibine de tekrar eden manuel iş yüklüyor.

## Hedef

Müşterinin kredi başvurusunu birkaç dakikada tamamlayıp çoğu durumda anında karar aldığı, banka içinde de manuel iş yükünün azaldığı bir süreç tasarlamak.

## Kapsam

| Kapsam içi | Kapsam dışı |
| --- | --- |
| Mobil uygulamadan bireysel ihtiyaç kredisi başvurusu | Konut ve taşıt kredisi, şube ve internet şubesi kanalları |
| Kimlik, bilgi ve gelir doğrulama adımları | Kredi skorlama modelinin iç mantığı |
| Karar süreci ve manuel inceleme adımı | Kredinin kullanımından sonraki tahsilat ve gecikme süreçleri |
| Başvuru durumu bildirimleri ve dijital sözleşme onayı | Yazılım geliştirme ve test |

## Varsayımlar ve kısıtlar

- Başvuru sahibi bankanın mevcut müşterisidir.
- Kimlik doğrulama ve KKB sorgusu için entegrasyon mevcuttur.
- Proje yeni bir kredi skor modeli kurmaz, mevcut karar motorunu kullanır.
- **Kısıt:** Gerçek banka verisine ve çalışanlarına erişim yoktur; herkese açık kaynaklar ve sentetik veri kullanılır.
- **Kısıt:** Proje tek kişi tarafından 8 haftada tamamlanır.

## Yöntem ve takvim

| Hafta | Çıktı |
| --- | --- |
| 1 | Proje tanımı |
| 2 | Kullanıcı araştırması özeti, persona'lar, paydaş analizi |
| 3 | As-Is süreç haritası (BPMN) |
| 4 | Veri analizi (Python, SQL) |
| 5 | Power BI dashboard'u ve To-Be süreç haritası |
| 6 | BRD ve Jira backlog'u |
| 7 | Wireframe'ler |
| 8 | Sunum ve portföy sayfası |
