import time
import sys
import random

# Windows terminali icin UTF-8 zorla
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# ─────────────────────────────────────────────
#  YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────────

def yaz(text, hiz=0.025):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(hiz)
    print()

def ayrac():
    print("\n" + "-" * 60 + "\n")

def durakla(sn=1.2):
    time.sleep(sn)

def stats_goster(kariyer, gun, isim, pozisyon):
    bar = kariyer_bar(kariyer)
    print(f"\n  👤 {isim} ({pozisyon})  |  📅 Gün {gun}")
    print(f"  💼 Kariyer: {bar}\n")

def secim_al(secenekler):
    while True:
        for i, s in enumerate(secenekler, 1):
            print(f"  [{i}] {s['metin']}")
        try:
            secim = int(input("\n  > Seçiminiz: ")) - 1
            if 0 <= secim < len(secenekler):
                print()
                return secenekler[secim]
        except (ValueError, KeyboardInterrupt):
            pass
        print("  Geçersiz seçim, tekrar deneyin.")

def kariyer_bar(puan, genislik=24):
    dolu = int(puan / 100 * genislik)
    bos = genislik - dolu
    renk = "█" * dolu + "░" * bos
    return f"[{renk}] {puan}/100"

def baslik_goster():
    print()
    print("  ┌─────────────────────────────────────────────────────┐")
    print("  │                                                     │")
    print("  │   💻   Y A Z I L I M C I   H A Y A T I   💻       │")
    print("  │                                                     │")
    print("  │             B i r   K a r i y e r                  │")
    print("  │              S i m ü l a s y o n u                 │")
    print("  │                                                     │")
    print("  └─────────────────────────────────────────────────────┘")
    print()

def sonuc_goster(delta, aciklama):
    if delta > 0:
        print(f"  ✅ +{delta} Kariyer Puanı — {aciklama}")
    elif delta < 0:
        print(f"  ❌ {delta} Kariyer Puanı — {aciklama}")
    else:
        print(f"  😐 Kariyer puanın değişmedi. {aciklama}")
    durakla(1.5)

# ─────────────────────────────────────────────
#  SENARYO 1: SPRINT PLANNING
# ─────────────────────────────────────────────

def senaryo_sprint(state):
    ayrac()
    yaz("📋  SENARYO 1: SPRINT PLANNING TOPLANTISI")
    ayrac()
    durakla()

    yaz(f"Pazartesi sabahı 09:00. Henüz kahveni bile içmemişken PM Tarık Bey")
    yaz("'Bugün sprint planning var, 5 dakikaya gel' mesajını atmış.")
    yaz("Toplantı odasına girdiğinde ekran dolup taşıyor: 47 backlog item.")
    durakla()
    yaz(f"\nTarık Bey coşkuyla konuşuyor: 'Bu sprint {state['isim']}, hepsini bitiririz değil mi?'")
    yaz("Ekip sana bakıyor. Tarık Bey sana bakıyor. Ofisteki kaktüs bile sana bakıyor.")

    print()
    secim = secim_al([
        {"metin": "'Tabii ki!' de ve mucize bekle.",                "delta": -15, "aciklama": "Sprint'in ortasında çöktün. Tarık Bey 'neden söylemedi ki?' dedi."},
        {"metin": "Story point hesapla, gerçekçi bir tahmin sun.",   "delta": +20, "aciklama": "Veri odaklı yaklaşımın takdir gördü. Kıdemli mühendis vibes'ı."},
        {"metin": "'Önce önceliklendirme yapalım' de.",             "delta": +10, "aciklama": "Sağduyulu buldular ama Tarık Bey biraz sıkıldı."},
        {"metin": "Telefona bak, 'özür dilerim acil bir şey var' de ve kaç.", "delta": -5,  "aciklama": "Kaçtın ama Slack'te 47 kez mention'landın."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  SENARYO 2: YANLIŞ SLACK MESAJI
# ─────────────────────────────────────────────

def senaryo_slack(state):
    ayrac()
    yaz("💬  SENARYO 2: YANLIŞ SLACK MESAJI")
    ayrac()
    durakla()

    yaz("Öğle arası. Arkadaşına şikâyet mesajı yazacaksın:")
    yaz(f"\n  'Tarık Bey bugün de saçmaladı, toplantı tam bir felaketti 🤦'")
    durakla(0.5)
    yaz("\n...ve Enter'a bastın.")
    durakla(0.8)
    yaz("...")
    durakla(0.5)
    yaz("Gönderildi.")
    durakla(0.5)
    yaz("Kanal: #genel 👁️  (127 üye)")
    durakla(1)
    yaz("\nTarık Bey mesajı okudu. 👀")

    print()
    secim = secim_al([
        {"metin": "Mesajı sil ve hiçbir şey olmamış gibi davran.",
         "delta": -10, "aciklama": "Herkes gördü. Herkes. Slack bildirim geçmişi silinemez."},
        {"metin": "Hemen 'Yanlış kanala göndermiş, üzgünüm!' yaz.",
         "delta": -5,  "aciklama": "Dürüst davrandın ama utanç hâlâ devam ediyor."},
        {"metin": "Tarık Bey'e özür DM'i at, yüz yüze konuş.",
         "delta": +15, "aciklama": "Olgun bir yaklaşım. Tarık Bey takdir etti, gerginlik dağıldı."},
        {"metin": "Sahiplen: 'Evet, bu benim gerçek düşüncem, konuşalım.'",
         "delta": +5,  "aciklama": "Cesur ama riskli. Bazıları saygı duydu, bazıları hayrete düştü."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  SENARYO 3: CUMA AKŞAMI PROD HATASI
# ─────────────────────────────────────────────

def senaryo_prod_hata(state):
    ayrac()
    yaz("🚨  SENARYO 3: CUMA 17:58 — PROD'DA HATA")
    ayrac()
    durakla()

    yaz("Çantanı alıyorsun, kapıya yürüyorsun...")
    yaz("Telefon titriyor.")
    yaz("'CRITICAL: Ödeme servisi çöktü. 500 hata. Müşteriler etkileniyor.'")
    durakla(0.8)
    yaz(f"\nSon deploy senindi. 17:45'te merge etmiştin.")
    yaz("Ekip henüz ofiste. Tarık Bey de.")

    print()
    secim = secim_al([
        {"metin": "Geri dön, sorunu analiz et ve düzelt.",
         "delta": +25, "aciklama": "Sorumluluk aldın, 45 dakikada fix'ledin. Efsane oldun."},
        {"metin": "Deploy'u revert et, sonra incele.",
         "delta": +20, "aciklama": "Hızlı düşündün. Servis kurtarıldı, herkes eve gidebildi."},
        {"metin": "Telefonu cebine koy, 'görmedim' de.",
         "delta": -30, "aciklama": "Pazartesi toplantısı çok gergin geçti. Çok."},
        {"metin": "On-call arkadaşını ara, durumu devret.",
         "delta": -5,  "aciklama": "Teknik olarak doğru ama 'senin deploy'unda' baskısı hissedildi."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  SENARYO 4: CODE REVIEW CEHENNEMİ
# ─────────────────────────────────────────────

def senaryo_code_review(state):
    ayrac()
    yaz("🔍  SENARYO 4: CODE REVIEW")
    ayrac()
    durakla()

    yaz("PR'ını açtın. Güzel bir özellik, üç günlük emek.")
    yaz("Kıdemli geliştirici Mert, PR'ını incelemeye başlıyor...")
    durakla(1)

    yorumlar = [
        "Bu değişken ismi ne anlama geliyor?",
        "Magic number kullanmışsın, constant yap.",
        "Neden bu kadar nested if var?",
        "Test yazmamışsın.",
        "Bu import kullanılmıyor.",
        "Yorum satırı Türkçe ama proje İngilizce.",
    ]
    random.shuffle(yorumlar)
    secilen = yorumlar[:3]

    yaz(f"\nMert'in yorumları geldi:")
    for y in secilen:
        yaz(f"  💬 '{y}'")

    durakla(0.5)
    yaz("\nSon yorum: 'Genel mantık iyi ama ciddi refactor lazım.'")

    print()
    secim = secim_al([
        {"metin": "Tüm yorumları dikkate al, PR'ı güncelle.",
         "delta": +20, "aciklama": "Büyüdün. Kod kalitesi arttı, Mert approve etti."},
        {"metin": "'LGTM dersen merge ederim' de.",
         "delta": -20, "aciklama": "Mert çıldırdı. Teknik borç birikti. İlişkin gerildi."},
        {"metin": "Sadece kolay değişiklikleri yap, geri kalanı 'TODO' bırak.",
         "delta": -5,  "aciklama": "TODO'lar asla çözülmedi. Altı ay sonra hâlâ orada."},
        {"metin": "Mert'le sync kur, nelerin gerçekten kritik olduğunu tartış.",
         "delta": +15, "aciklama": "Pragmatik yaklaşım. İkisi de tatmin oldu."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  SENARYO 5: GEREKSİZ TOPLANTI
# ─────────────────────────────────────────────

def senaryo_toplanti(state):
    ayrac()
    yaz("📅  SENARYO 5: BU TOPLANTI BİR E-POSTA OLABİLİRDİ")
    ayrac()
    durakla()

    yaz("Takviminde 2 saatlik bir toplantı var: 'Yeni dashboard renk paleti kararı'")
    yaz("Davet listesinde 14 kişi var. Sen de dahilsin.")
    yaz("Elinde bitmesi gereken bir feature var. Deadline yarın.")
    durakla(0.5)
    yaz("\nToplantı başlıyor. İlk 20 dakika renk teorisi tartışması.")
    yaz("Tasarımcı ile PM aynı rengi farklı isimlerle tartışıyor.")
    yaz("'Bu turkuaz değil, zümrüt yeşili!' — 38. dakika.")

    print()
    secim = secim_al([
        {"metin": "Sabırla otur, not al, katılımcı görün.",
         "delta": -5,  "aciklama": "2 saat gitti. Feature gecikmesi başladı."},
        {"metin": "'Bu kararı 3 kişi alabilir, ben çıkayım mı?' de.",
         "delta": +10, "aciklama": "Biraz garip baktılar ama haklıydın. Çıktın, feature'ı bitirdin."},
        {"metin": "Toplantıda gizlice feature'ı kodla.",
         "delta": +5,  "aciklama": "Riskli ama pull off ettin. Birileri fark etmiş olabilir."},
        {"metin": "Herkese 'Bu asenkron çözülebilir' mini-eğitimi ver.",
         "delta": +15, "aciklama": "Toplantı kültürü değişmeye başladı. Ekip seni sevdi."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  SENARYO 6: YENİ ELEMAN MENTORLUĞU
# ─────────────────────────────────────────────

def senaryo_mentor(state):
    ayrac()
    yaz("🎓  SENARYO 6: YENİ ELEMAN")
    ayrac()
    durakla()

    yaz("Bugün ekibe yeni bir junior developer katıldı: Zeynep.")
    yaz("Tarık Bey: 'Zeynep'i sen karşıla, onboard et, yardımcı ol.'")
    yaz(f"Sen: '...' (deadline yarın, 0 zaman, 100 soru geliyor)")
    durakla(0.5)
    yaz("\nZeynep ilk sorusunu soruyor:")
    yaz("'Repo'yu clone'ladım ama çalıştıramadım, README'de yazan komutu denedim.'")
    yaz("(README son güncellenme tarihi: 3 yıl önce)")

    print()
    secim = secim_al([
        {"metin": "Her şeyi bırak, Zeynep'e saat harca.",
         "delta": -5,  "aciklama": "Zeynep mutlu, ama senin deadline'ın patladı."},
        {"metin": "README'yi güncelle, kurulum scriptı yaz, ikisi de kazansın.",
         "delta": +25, "aciklama": "Zeynep işe başladı, ekip de README'den kurtuldu. Kahraman oldun."},
        {"metin": "'Dokümantasyon yok, trial & error yap' de.",
         "delta": -15, "aciklama": "Zeynep ilk haftasını zor geçirdi. Senden soğudu."},
        {"metin": "Başka bir ekip arkadaşına yönlendir.",
         "delta": 0,   "aciklama": "Zeynep yardım aldı ama sen fırsatı kaçırdın."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  TEST MÜHENDİSİ SENARYOLARI (havuz: 9 adet, her oyunda 6 tanesi rastgele seçilir)
# ─────────────────────────────────────────────

def tm_flaky_test(state):
    ayrac()
    yaz("🔴  SENARYO: FLAKY TEST")
    ayrac()
    durakla()

    yaz("CI pipeline'da bir test var: bazen geçiyor, bazen geçmiyor.")
    yaz("Bugün de kırmızı yandı. Kimse neden olduğunu bilmiyor.")
    yaz("Developer Mert: 'Bu test zaten hep böyle, ignore et.'")
    durakla(0.8)
    yaz("\nSen son 10 çalışmaya baktın: 6 başarılı, 4 başarısız. Pattern yok.")

    print()
    secim = secim_al([
        {"metin": "Testi skip et, zaten hep böyle.",
         "delta": -10, "aciklama": "Bir ay sonra prod'da o bug çıktı. 'Flaky testti' diyemedin."},
        {"metin": "Root cause analiz et, intermittent failing'in kaynağını bul.",
         "delta": +20, "aciklama": "Race condition buldun. Hem test hem kod düzeldi. Efsanesin."},
        {"metin": "Birkaç kez çalıştır, geçince merge et.",
         "delta": -5,  "aciklama": "Geçici çözüm oldu. Sorun iki hafta sonra yine patladı."},
        {"metin": "Test altyapısı ekibine ticket aç, belgeleri.",
         "delta": +10, "aciklama": "Doğru kanalı kullandın. Yavaş ama kalıcı çözüm geldi."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_kritik_bug(state):
    ayrac()
    yaz("🚨  SENARYO: RELEASE ÖNCESI KRİTİK BUG")
    ayrac()
    durakla()

    yaz("Release'e 2 saat kaldı. Tarık Bey heyecanlı: 'Bu akşam deploy!'")
    yaz("Test sürecinin son aşamasında ödeme akışında bir edge case buldun.")
    durakla(0.8)
    yaz("\nBug: Kupon kodu + yabancı para birimi birlikte kullanılınca sipariş tutarı 0 TL oluyor.")
    yaz("Nadir bir senaryo ama müşteri isterse sıfır TL'ye ürün alabilir.")

    print()
    secim = secim_al([
        {"metin": "Sessiz kal, zaten nadir bir senaryo.",
         "delta": -25, "aciklama": "Müşteriler keşfetti. Sabahın 3'ünde acil toplantı. Adın her yerde."},
        {"metin": "PM'e bildir, release'i ertele, bug fix önceliği ver.",
         "delta": +20, "aciklama": "Tarık Bey sinirli oldu ama haklı olduğunu kabul etti. Krizi önledin."},
        {"metin": "Sadece developer'a ilet, o karar versin.",
         "delta": +5,  "aciklama": "Sorumluluk geçti ama sen fırsatı kaçırdın. 'Bildirdi mi söyledin mi?' tartışması başladı."},
        {"metin": "Riski belgele, 'release edelim ama hemen hot-fix planlayalım' de.",
         "delta": +15, "aciklama": "Pragmatik yaklaşım. Herkes risk farkındaydı, hot-fix sabah yayına girdi."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_manuel_otomasyon(state):
    ayrac()
    yaz("🤖  SENARYO: MANUEL Mİ OTOMASYON MU?")
    ayrac()
    durakla()

    yaz("3 aydır yazdığın 200 otomasyonlu test var. Pipeline 12 dakikada çalışıyor.")
    yaz("Tarık Bey'in yeni kararı: 'Maliyeti kısmak için CI araçlarını kapıyoruz.'")
    durakla(0.5)
    yaz("\n'Her release öncesi sen manuel test yaparsın, idare eder.'")
    yaz("200 test case. Manuel. Her sprint.")

    print()
    secim = secim_al([
        {"metin": "'Tamam' de, 200 test case'i manuel çalıştır.",
         "delta": -15, "aciklama": "İlk sprintte 3 gün sürdü. Hata oranı arttı. Motivasyonun sıfırlandı."},
        {"metin": "Otomasyonun ROI'sini hesapla, Tarık Bey'e sun.",
         "delta": +20, "aciklama": "Maliyet analizi ikna etti. Araçlar geri geldi, sana teşekkür etti."},
        {"metin": "En kritik 40 testi manuel yap, gerisini risk olarak belgele.",
         "delta": +10, "aciklama": "Makul bir orta yol. Herkes kabul etti, risk bilinçli alındı."},
        {"metin": "Karşı çıkmadan işi başka takım arkadaşına devret.",
         "delta": -5,  "aciklama": "Problem çözülmedi, sadece yer değiştirdi. Liderlik fırsatı kaçtı."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_test_gerekmiyor(state):
    ayrac()
    yaz("🙄  SENARYO: 'TEST YAZMAYA GEREK YOK'")
    ayrac()
    durakla()

    yaz("Developer Mert yeni bir ödeme entegrasyonu yazdı.")
    yaz("PR açıldı. Test yok. Mert: 'Bu kadar basit şeye test yazılmaz,")
    yaz("zaten çalışıyor, görüyorum.'")
    durakla(0.8)
    yaz(f"\n{state['isim']}, senin onayın da isteniyor PR için.")

    print()
    secim = secim_al([
        {"metin": "Mert kıdemli, anlaşmak kolay — approve et.",
         "delta": -20, "aciklama": "İki hafta sonra 'basit' kod prod'da patlattı. 'Test yoktu neden?' sorusu geldi sana."},
        {"metin": "Neden test gerektiğini örnekle açıkla, itiraz et.",
         "delta": +15, "aciklama": "Mert önce sinirli oldu, sonra haklı olduğunu kabul etti. Süreç güçlendi."},
        {"metin": "Kendin test yaz, PR'a comment olarak ekle.",
         "delta": +20, "aciklama": "Eylemle örnek gösterdin. Mert 'bak bu işe yarıyor' dedi. Kültür değişti."},
        {"metin": "Manager'a escalate et.",
         "delta": -5,  "aciklama": "Mesele büyüdü, gereksiz gerilim oldu. Mert seninle küstü."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_ortam_coktu(state):
    ayrac()
    yaz("💻  SENARYO: TEST ORTAMI DOWN")
    ayrac()
    durakla()

    yaz("Release yarın sabah 10:00. Test ortamı bu sabahtan beri down.")
    yaz("DevOps ekibi 'bakıyoruz' dedi, saat 15:00, hâlâ down.")
    yaz(f"\n{state['isim']}, 45 test case var ve 0 ortam.")

    print()
    secim = secim_al([
        {"metin": "DevOps'u tekrar ara, escalate et, düzeltilmesini iste.",
         "delta": +15, "aciklama": "Israr etttin, saat 17:00'de ortam ayağa kalktı. Testleri bitirdin."},
        {"metin": "Prod ortamında test et, 'sadece bir kez' diyerek.",
         "delta": -30, "aciklama": "Prod'daki veriyi bozdun. Gece yarısı acil rollback. Tarihe geçtin."},
        {"metin": "Release'i ertele, 'test edilmeden gidemez' de.",
         "delta": +10, "aciklama": "Tarık Bey sinirli oldu ama haklı kararı kabul etti. Sonra teşekkür etti."},
        {"metin": "Eksik test raporuyla release'e geç, sonra kapatırız.",
         "delta": -15, "aciklama": "3 bug prod'a gitti. 'Sonra kapatalım' dediğin testler kapanmadı."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_coverage(state):
    ayrac()
    yaz("📊  SENARYO: COVERAGE BASKISI")
    ayrac()
    durakla()

    yaz("Sprint review'da metrikler ekranda: Test coverage %73.")
    yaz("Hedef %80'di. Tarık Bey sert bakıyor.")
    yaz(f"'{state['isim']}, neden hedefin altındasın? Bu ay zam görüşmesi var.'")
    durakla(0.8)
    yaz("\nGerçek sebep: ekip yeni modülü coverage olmadan merge etti, sen itiraz ettin ama dinlenmedin.")

    print()
    secim = secim_al([
        {"metin": "Coverage raporunu 'düzenle', %80 göster.",
         "delta": -25, "aciklama": "Ay sonunda gerçek metrikler ortaya çıktı. Güven tamamen sarsıldı."},
        {"metin": "Hangi alanların riskli kaldığını, neden bu duruma gelindiğini belgele.",
         "delta": +20, "aciklama": "Şeffaflık takdir gördü. Süreç sorunu gün yüzüne çıktı, ekip düzeltildi."},
        {"metin": "İçi boş testler yaz, coverage'ı anlık artır.",
         "delta": -10, "aciklama": "Coverage %80 oldu ama testler hiçbir şeyi doğrulamıyordu. Sonra belli oldu."},
        {"metin": "Sonraki sprint için risk-öncelikli test planı sun.",
         "delta": +10, "aciklama": "Proaktif yaklaşım beğenildi. Kısa vadede ağrı, uzun vadede güven."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_regression(state):
    ayrac()
    yaz("⏩  SENARYO: REGRESSION ATLAYALIM MI?")
    ayrac()
    durakla()

    yaz("'Küçük bir değişiklik' — sadece bir config güncellemesi.")
    yaz(f"Tarık Bey: '{state['isim']}, full regression için vaktimiz yok, geç git.'")
    durakla(0.5)
    yaz("\nSen bu 'küçük değişiklik'in geçen ay ödeme modülünü etkilediğini biliyorsun.")
    yaz("Config değerleri 4 farklı servise yayılıyor.")

    print()
    secim = secim_al([
        {"metin": "Tamam de, regresyon atla.",
         "delta": -20, "aciklama": "Config değişikliği 2 servisi bozdu. Hafta sonu acil müdahale. Adın anıldı."},
        {"metin": "Riski Tarık Bey'e belgele, yazılı onaylatarak atla.",
         "delta": +10, "aciklama": "Kararı ona bıraktın, ama riski görünür kıldın. Bir sorun çıkınca arkana bakıyorsun."},
        {"metin": "Kısa hedefli smoke test yap, 30 dakikada bitir.",
         "delta": +15, "aciklama": "Akıllı denge. Kritik yollar test edildi, zaman korundu. Herkes mutlu."},
        {"metin": "Full regression için ısrar et, gecikmeyı kabul et.",
         "delta": +5,  "aciklama": "Doğru karardı ama Tarık Bey gerildi. Haklıydın, ama ilişki zorlandı."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_yuk_testi(state):
    ayrac()
    yaz("📈  SENARYO: YÜK TESTİ BAŞARISIZ")
    ayrac()
    durakla()

    yaz(f"Büyük kampanya lansmanı yarın, {state['isim']}. Beklenen: 5000 eş zamanlı kullanıcı.")
    yaz("Yük testini çalıştırdın:")
    durakla(0.8)
    yaz("\n  500 kullanıcı → ✅ OK")
    yaz("  1000 kullanıcı → ✅ OK")
    yaz("  2000 kullanıcı → ❌ Sistem yanıt vermiyor")
    durakla(1)
    yaz("\nRelease yarın sabah. Tarık Bey 'lansman iptal edilemez' diyor.")

    print()
    secim = secim_al([
        {"metin": "Test parametrelerini 500'e düşür, 'geçti' de.",
         "delta": -25, "aciklama": "Lansman başladı, sistem 800 kullanıcıda çöktü. Canlı yayın felaketi."},
        {"metin": "Sonuçları paylaş, ekiple emergency toplantı çağır.",
         "delta": +20, "aciklama": "Zor karar ama doğru karar. Lansman 1 gün ertelendi, felaket önlendi."},
        {"metin": "Sadece developer'a ilet, 'senin sorunun' de.",
         "delta": +5,  "aciklama": "Developer düzeltti ama sen loop dışında kaldın. Katkın görünmedi."},
        {"metin": "Raporu 'test ortamı sorunu olabilir' notu ile sun.",
         "delta": -10, "aciklama": "Belirsizlik kötü karar almaya yol açtı. Prod'da doğrulandı: sorun gerçekti."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


def tm_prod_bug(state):
    ayrac()
    yaz("😰  SENARYO: PROD'DA KAÇIRILAN BUG")
    ayrac()
    durakla()

    yaz(f"Dün deploy oldu. Bugün müşteri desteği {state['isim']}'e yazdı:")
    yaz("'Fatura PDF'leri boş geliyor, 500+ şikâyet var.'")
    durakla(0.8)
    yaz("\nTest sürecine baktın: fatura modülünü test etmiştin ama")
    yaz("PDF render edge case'i senaryolarında yoktu.")
    yaz("\nTarık Bey toplantı odası kapısını çaldı.")

    print()
    secim = secim_al([
        {"metin": "'Ben test ettim, sorun bende değil' de.",
         "delta": -20, "aciklama": "Savunma modu krizi büyüttü. 'Peki neden senaryoda yoktu?' sorusu geldi."},
        {"metin": "Durumu kabul et, kaçan senaryoyu belgele, süreç iyileştirmesi öner.",
         "delta": +20, "aciklama": "Olgunluk gösterdin. Bunu fırsata çevirdin, test planı güçlendi."},
        {"metin": "Sessiz kal, developer fix yaparken bekle.",
         "delta": -10, "aciklama": "Pasif kaldın. 'Test mühendisi ne iş yapıyor?' sorusu başladı."},
        {"metin": "Hemen hot-fix için test senaryolarını hazırla ve sürece katıl.",
         "delta": +15, "aciklama": "Hızlı aksiyon aldın. Fix'in doğru çalıştığını da sen onayladın."},
    ])

    sonuc_goster(secim["delta"], secim["aciklama"])
    return secim["delta"]


# ─────────────────────────────────────────────
#  SONUÇ EKRANI
# ─────────────────────────────────────────────

def oyun_sonu(state):
    ayrac()
    yaz("🏁  OYUN SONU")
    ayrac()

    k = state["kariyer"]
    isim = state["isim"]
    pozisyon = state["pozisyon"]

    yaz(f"Son durum: {isim} ({pozisyon}) — Kariyer Puanı: {k}/100")
    print()
    durakla()

    print(f"  💼 Final Kariyer Skoru: {kariyer_bar(k)}")
    print()
    durakla(0.8)

    if k >= 80:
        print("         trophy")
        print("         ___")
        print("        (   )")
        print("     *   ) (   *")
        print("    ***  (___)  ***")
        print("   *****  | |  *****")
        print("  ███████─┴─┴─███████")
        print()
        yaz("⭐  MÜKEMMEL SONUÇ: Şirketin Efsanesi")
        yaz(f"Tarık Bey seni toplantıda 'role model' olarak tanıttı.")
        yaz("LinkedIn profilin haftada 3 recruiter mesajı alıyor.")
        yaz("Mert artık PR'larına 'iyi iş' yazıyor. Bu çok nadir.")
    elif k >= 60:
        print("          \\o/")
        print("           |")
        print("          / \\")
        print("        güvenilir")
        print()
        yaz("👍  İYİ SONUÇ: Güvenilir Yazılımcı")
        yaz("Ekipte sağlam bir yeriniz var. Kimse sizi görmezden gelmiyor.")
        yaz("Zam görüşmesi yakında. Belki.")
    elif k >= 40:
        print("          ._.  ")
        print("          |_|  zzzz")
        print("          | |")
        print("         /   \\")
        print()
        yaz("😐  ORTA SONUÇ: Fark Edilmeyen Çalışan")
        yaz("Günler geçiyor, sen varken de yokken de ekip devam ediyor.")
        yaz("Tarık Bey senin adını bazen karıştırıyor.")
    elif k >= 20:
        print("         /!\\")
        print("        / ! \\")
        print("       /______\\")
        print("        dikkat")
        print()
        yaz("😬  KÖTÜ SONUÇ: Kriz Uzmanı (Ama Nedeni Sen Oluyorsun)")
        yaz("Her hafta bir şey oluyor. Tesadüf değil artık.")
        yaz("HR seni 'gelişim planı' için davet etti.")
    else:
        print("        _____")
        print("       / x x \\")
        print("      |   ^   |")
        print("      |  ___  |  BOOM")
        print("       \\_____/")
        print("    ~~~kaos~~~")
        print()
        yaz("💀  FELAKETLİ SONUÇ: Efsanevi Kaos")
        yaz(f"'{isim}' ismi şirkette bir fiil oldu: 'Bunu {isim.lower()}lama!'")
        yaz("Mülakat pratiği yapmana gerek yok, çünkü zaten gitmek zorundasın.")
        yaz("Yeni şirkette fresh start. Belki bu sefer farklı gider.")

    print()
    yaz("Oynamak için teşekkürler. Gerçek yazılım hayatı bundan çok farklı değil.")
    ayrac()


# ─────────────────────────────────────────────
#  KARAKTER OLUŞTURMA
# ─────────────────────────────────────────────

def karakter_olustur():
    baslik_goster()
    yaz("Bir yazılım firmasında çalışıyorsun.")
    yaz("Her karar kariyerini etkiliyor. Bazıları düşündüğün gibi değil.\n")

    isim = input("  Karakterinin adı: ").strip() or "Ali"
    print()

    yaz("  Pozisyonunu seç:")
    pozisyonlar = ["Junior Developer", "Mid-level Developer", "Senior Developer", "DevOps Mühendisi", "Test Mühendisi"]
    for i, p in enumerate(pozisyonlar, 1):
        print(f"    [{i}] {p}")

    while True:
        try:
            secim = int(input("\n  > Seçiminiz: ")) - 1
            if 0 <= secim < len(pozisyonlar):
                pozisyon = pozisyonlar[secim]
                break
        except ValueError:
            pass
        print("  Geçersiz seçim.")

    print()
    yaz(f"Merhaba {isim}! {pozisyon} olarak işe başlıyorsun.")
    yaz("Kariyer puanın: 50/100. Her şey senin elinde.\n")
    durakla(1)

    return {"isim": isim, "pozisyon": pozisyon, "kariyer": 50, "gun": 1}


# ─────────────────────────────────────────────
#  ANA OYUN DÖNGÜSÜ
# ─────────────────────────────────────────────

def main():
    state = karakter_olustur()

    if state["pozisyon"] == "Test Mühendisi":
        tm_havuz = [
            tm_flaky_test,
            tm_kritik_bug,
            tm_manuel_otomasyon,
            tm_test_gerekmiyor,
            tm_ortam_coktu,
            tm_coverage,
            tm_regression,
            tm_yuk_testi,
            tm_prod_bug,
        ]
        random.shuffle(tm_havuz)
        senaryolar = tm_havuz[:6]
    else:
        senaryolar = [
            senaryo_sprint,
            senaryo_slack,
            senaryo_prod_hata,
            senaryo_code_review,
            senaryo_toplanti,
            senaryo_mentor,
        ]

    for i, senaryo in enumerate(senaryolar, 1):
        state["gun"] = i
        stats_goster(state["kariyer"], state["gun"], state["isim"], state["pozisyon"])
        delta = senaryo(state)
        state["kariyer"] = max(0, min(100, state["kariyer"] + delta))
        durakla(1)

    oyun_sonu(state)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Oyundan çıkıldı. Gerçek hayatta bu kadar kolay değil!")
