# Dijital Bireysel Kredi Başvurusu – İş Analizi Vaka Çalışması

Bir bankanın mobil uygulamasındaki ihtiyaç kredisi başvuru sürecini uçtan uca analiz edip yeniden tasarladığım 8 haftalık bireysel iş analizi projesi.

> Banka kurgusaldır ("Örnek Banka"). Kullanıcı araştırması herkese açık şikayet ve uygulama yorumlarıyla yapıldı; sayısal analizdeki veri **sentetiktir**. Gerçek bir bankanın verisi kullanılmadı.

## Kısaca

| | |
| --- | --- |
| **Problem** | Başlayan mobil başvuruların yalnızca %42,7'si kullandırılan krediye dönüşüyor. |
| **Beklenmeyen bulgu** | Şikayetlerin yarısı formla değil, **karardan sonrasıyla** ilgili: onaylanan kredinin hesaba geçmemesi ve gerekçesiz red. |
| **Çözüm** | Önceden doldurulmuş form, açık rızayla dijital gelir bilgisi, SLA'lı manuel inceleme kuyruğu, aktarım hatasında otomatik yeniden deneme, genel red nedeni. |
| **Hedef** | Uçtan uca dönüşüm %42,7 → %52, manuel inceleme 29 saat → 4 iş saati. |

## Süreç ve yöntem

| Hafta | Ne yaptım | Çıktı |
| --- | --- | --- |
| 1 | Problem, kapsam, KPI'lar | [Proje tanımı](01-proje-tanimi/proje-tanimi.md) |
| 2 | 11 bankadan 44 şikayet ve yorumu etiketledim, persona'lar çıkardım | [Araştırma özeti](02-arastirma/arastirma-ozeti.md), [etiketleme verisi](02-arastirma/etiketleme.csv) |
| 3 | As-Is süreci BPMN ile modelledim, 6 darboğaz buldum | [drawio dosyası](03-surec-bpmn/kredi-basvurusu-bpmn.drawio) |
| 4 | 8.000 kayıtlık sentetik veri ürettim, SQL ile analiz ettim | [Bulgular](04-veri-analizi/BULGULAR.md), [SQL](04-veri-analizi/analiz.sql), [Python](04-veri-analizi/veri_uret.py) |
| 5 | Power BI dashboard'u (DAX) ve To-Be süreç | [Power BI rehberi](04-veri-analizi/POWERBI.md) |
| 6 | 14 FR + 6 NFR'lik BRD, izlenebilirlik, Jira'da 20 user story ve Sprint 1 | [BRD](05-gereksinimler/BRD.md), [user story'ler](05-gereksinimler/jira_user_stories.csv) |
| 7-8 | 7 ekran wireframe, 10 slaytlık sunum, portföy sayfası | [Tasarım ve sunum](06-tasarim-ve-sunum/) |

## Darboğazlar ve çözümler

| Kod | Darboğaz | Kanıt | Gereksinim |
| --- | --- | --- | --- |
| D1 | Form elle dolduruluyor | Başvuruların %8,5'i bilgi girişinde bırakılıyor | FR-03 |
| D2 | Gelir belgesi isteniyor | 45+ yaşta bırakma %37,6 | FR-04, FR-05 |
| D3 | Manuel incelemede bekleme | Ortalama 29,1 saat | FR-06, FR-07, FR-08 |
| D4 | Eksik belge döngüsü | İncelemeyi 3,6 kat uzatıyor | FR-09 |
| D5 | Onaylanan kredi hesaba geçmiyor | 12 şikayet; 5,4 milyon TL kayıp hacim | FR-11 |
| D6 | Red gerekçesi açıklanmıyor | 9 şikayet; %28,4 tekrar başvuru | FR-12 |

## Araçlar

BPMN (draw.io) · SQL (SQLite) · Python · Power BI (DAX) · Jira (Scrum) · BRD, user story, kabul kriterleri, MoSCoW, izlenebilirlik matrisi

## Klasörler

```
01-proje-tanimi/     problem, kapsam, KPI
02-arastirma/        araştırma özeti, persona'lar, 44 kayıtlık etiketleme tablosu
03-surec-bpmn/       As-Is ve To-Be süreç (draw.io ile açılır)
04-veri-analizi/     veri üretimi, SQLite veritabanı, SQL sorguları, CSV, Power BI
05-gereksinimler/    BRD ve Jira'ya aktarılan user story'ler
06-tasarim-ve-sunum/ wireframe ve sunum
docs/                portföy sayfası (GitHub Pages)
```

## Öğrendiklerim

- Hipotezim formun uzun olmasıydı; araştırma, asıl acının karardan sonra yaşandığını gösterdi. Süreci "onay" ekranında bitirmek yerine paraya erişime kadar uzattım.
- Uygulamada gösterilen ön onaylı limitin gerçek kararla uyuşmaması, kendi önerimin de bir risk taşıdığını gösterdi; bunun için FR-13'ü ekledim.
- Şikayet verisi temsil edici değildir: formdan sıkılıp vazgeçen müşteri genelde şikayet yazmaz. Bu yüzden araştırmayı sayısal analizle birlikte okudum.

## İletişim

Ebrar Topal · [LinkedIn](https://www.linkedin.com/in/KULLANICI-ADINIZ)
