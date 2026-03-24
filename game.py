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

def stat_bar(puan, genislik=20):
    dolu = int(puan / 100 * genislik)
    bos = genislik - dolu
    return f"[{'█' * dolu}{'░' * bos}] {puan}/100"

def stats_goster(state):
    k = state["kariyer"]
    p = state["patron"]
    a = state["arkadaslar"]
    gun = state["gun"]
    isim = state["isim"]
    poz = state["pozisyon"]
    print(f"\n  👤 {isim} ({poz})  |  📅 Gün {gun}")
    print(f"  💼 Kariyer   : {stat_bar(k)}")
    print(f"  😤 Patron    : {stat_bar(p)}")
    print(f"  🤝 Arkadaşlar: {stat_bar(a)}\n")

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

def sonuc_goster(deltas, aciklama):
    k = deltas.get("kariyer", 0)
    p = deltas.get("patron", 0)
    a = deltas.get("arkadaslar", 0)
    satirlar = []
    if k != 0:
        satirlar.append(f"{'✅' if k > 0 else '❌'} {'+'if k>0 else ''}{k} Kariyer Puanı")
    if p != 0:
        satirlar.append(f"{'😊' if p > 0 else '😠'} {'+'if p>0 else ''}{p} Patron İlişkisi")
    if a != 0:
        satirlar.append(f"{'🤗' if a > 0 else '😒'} {'+'if a>0 else ''}{a} Arkadaşlık")
    if not satirlar:
        satirlar.append("😐 Hiçbir stat değişmedi")
    for s in satirlar:
        print(f"  {s}")
    print(f"  💬 {aciklama}")
    durakla(1.8)


# ─────────────────────────────────────────────
#  GENEL SENARYOLAR
# ─────────────────────────────────────────────

def senaryo_sprint(state):
    ayrac()
    yaz("📋  SENARYO: SPRINT PLANNING TOPLANTISI")
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
        {"metin": "'Tabii ki!' de ve mucize bekle.",
         "kariyer": -15, "patron": +5, "arkadaslar": -5,
         "aciklama": "Sprint'in ortasında çöktün. Tarık Bey mutlu başladı ama sonra 'neden söylemedi?' dedi."},
        {"metin": "Story point hesapla, gerçekçi bir tahmin sun.",
         "kariyer": +20, "patron": +10, "arkadaslar": +5,
         "aciklama": "Veri odaklı yaklaşımın takdir gördü. Ekip de 'sonunda biri söyledi' diye rahladı."},
        {"metin": "'Önce önceliklendirme yapalım' de.",
         "kariyer": +10, "patron": 0, "arkadaslar": +5,
         "aciklama": "Sağduyulu buldular ama Tarık Bey biraz sıkıldı."},
        {"metin": "Telefona bak, 'özür dilerim acil bir şey var' de ve kaç.",
         "kariyer": -5, "patron": -15, "arkadaslar": -5,
         "aciklama": "Kaçtın ama Slack'te 47 kez mention'landın. Tarık Bey seni bir hafta sormadı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_slack(state):
    ayrac()
    yaz("💬  SENARYO: YANLIŞ SLACK MESAJI")
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
         "kariyer": -10, "patron": -20, "arkadaslar": 0,
         "aciklama": "Herkes gördü. Slack bildirim geçmişi silinemez. Tarık Bey susmayı tercih etti — bu daha kötü."},
        {"metin": "Hemen 'Yanlış kanala göndermiş, özür dilerim!' yaz.",
         "kariyer": -5, "patron": -10, "arkadaslar": +5,
         "aciklama": "Dürüst davrandın ama utanç hâlâ devam ediyor. Arkadaşlar sempati gösterdi."},
        {"metin": "Tarık Bey'e özür DM'i at, yüz yüze konuş.",
         "kariyer": +15, "patron": +10, "arkadaslar": 0,
         "aciklama": "Olgun bir yaklaşım. Tarık Bey takdir etti, gerginlik dağıldı."},
        {"metin": "Sahiplen: 'Evet, bu benim gerçek düşüncem, konuşalım.'",
         "kariyer": +5, "patron": -5, "arkadaslar": +15,
         "aciklama": "Cesur ama riskli. Arkadaşlar 'bizim sesi' dedi. Tarık Bey ikili görüşme istedi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_prod_hata(state):
    ayrac()
    yaz("🚨  SENARYO: CUMA 17:58 — PROD'DA HATA")
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
         "kariyer": +25, "patron": +20, "arkadaslar": +10,
         "aciklama": "Sorumluluk aldın, 45 dakikada fix'ledin. Tarık Bey 'işte bu' dedi. Efsane oldun."},
        {"metin": "Deploy'u revert et, sonra incele.",
         "kariyer": +20, "patron": +15, "arkadaslar": +5,
         "aciklama": "Hızlı düşündün. Servis kurtarıldı, herkes eve gidebildi. Akıllı hamle."},
        {"metin": "Telefonu cebine koy, 'görmedim' de.",
         "kariyer": -30, "patron": -30, "arkadaslar": -20,
         "aciklama": "Pazartesi toplantısı çok gergin geçti. Çok. Tarık Bey ekip önünde ismi telaffuz etti."},
        {"metin": "On-call arkadaşını ara, durumu devret.",
         "kariyer": -5, "patron": -5, "arkadaslar": -10,
         "aciklama": "Teknik olarak doğru ama 'senin deploy'unda' baskısı hissedildi. Arkadaş da sinirli."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_code_review(state):
    ayrac()
    yaz("🔍  SENARYO: CODE REVIEW CEHENNEMİ")
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
    for y in yorumlar[:3]:
        yaz(f"  💬 '{y}'")
    durakla(0.5)
    yaz("\nSon yorum: 'Genel mantık iyi ama ciddi refactor lazım.'")
    print()
    secim = secim_al([
        {"metin": "Tüm yorumları dikkate al, PR'ı güncelle.",
         "kariyer": +20, "patron": +5, "arkadaslar": +10,
         "aciklama": "Büyüdün. Kod kalitesi arttı, Mert approve etti ve seni 'öğreniyor' diye övdü."},
        {"metin": "'LGTM dersen merge ederim' de.",
         "kariyer": -20, "patron": -5, "arkadaslar": -15,
         "aciklama": "Mert çıldırdı. Teknik borç birikti. Arkadaşlık gerildi, ortam gergin."},
        {"metin": "Sadece kolay değişiklikleri yap, geri kalanı 'TODO' bırak.",
         "kariyer": -5, "patron": 0, "arkadaslar": -5,
         "aciklama": "TODO'lar asla çözülmedi. Altı ay sonra hâlâ orada. Mert hatırladı."},
        {"metin": "Mert'le sync kur, nelerin gerçekten kritik olduğunu tartış.",
         "kariyer": +15, "patron": +5, "arkadaslar": +15,
         "aciklama": "Pragmatik yaklaşım. İkisi de tatmin oldu. Mert artık sana lunch'ta yer ayırıyor."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_toplanti(state):
    ayrac()
    yaz("📅  SENARYO: BU TOPLANTI BİR E-POSTA OLABİLİRDİ")
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
         "kariyer": -5, "patron": +5, "arkadaslar": 0,
         "aciklama": "2 saat gitti. Feature gecikmesi başladı. Ama Tarık Bey 'kararlıydı' dedi."},
        {"metin": "'Bu kararı 3 kişi alabilir, ben çıkayım mı?' de.",
         "kariyer": +10, "patron": -5, "arkadaslar": +5,
         "aciklama": "Biraz garip baktılar ama haklıydın. Çıktın, feature'ı bitirdin."},
        {"metin": "Toplantıda gizlice feature'ı kodla.",
         "kariyer": +5, "patron": -10, "arkadaslar": +10,
         "aciklama": "Riskli ama pull off ettin. Arkadaşlar 'kahraman' dedi. Tarık Bey 'dikkatli ol' dedi."},
        {"metin": "Herkese 'Bu asenkron çözülebilir' mini-eğitimi ver.",
         "kariyer": +15, "patron": +5, "arkadaslar": +15,
         "aciklama": "Toplantı kültürü değişmeye başladı. Ekip seni sevdi. Tarık Bey not aldı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_mentor(state):
    ayrac()
    yaz("🎓  SENARYO: YENİ ELEMAN")
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
         "kariyer": -5, "patron": +5, "arkadaslar": +20,
         "aciklama": "Zeynep mutlu, ekip seni sevdi. Ama senin deadline'ın patladı."},
        {"metin": "README'yi güncelle, kurulum scriptı yaz, ikisi de kazansın.",
         "kariyer": +25, "patron": +15, "arkadaslar": +20,
         "aciklama": "Zeynep işe başladı, ekip README'den kurtuldu. Tarık Bey seni 'inisiyatif' kelimesiyle andı."},
        {"metin": "'Dokümantasyon yok, trial & error yap' de.",
         "kariyer": -15, "patron": -5, "arkadaslar": -20,
         "aciklama": "Zeynep ilk haftasını zor geçirdi. Senden soğudu. Ekip fark etti."},
        {"metin": "Başka bir ekip arkadaşına yönlendir.",
         "kariyer": 0, "patron": 0, "arkadaslar": -5,
         "aciklama": "Zeynep yardım aldı ama sen fırsatı kaçırdın. Küçük bir güven kaybı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_zam_gorusmesi(state):
    ayrac()
    yaz("💰  SENARYO: ZAM GÖRÜŞMESİ")
    ayrac()
    durakla()
    yaz("Yıl sonu geldi. Tarık Bey seni 1-on-1'a çağırdı.")
    yaz("Masaya oturuyorsun. Tarık Bey klasörü açıyor.")
    durakla(0.8)
    yaz("\nTarık Bey: 'Bu yıl iyiydi. Sana %8 zam düşündük.'")
    durakla(0.5)
    yaz("Enflasyon: %65. Seninle aynı pozisyonda biri dışarıda 2x maaş alıyor.")
    yaz("Tarık Bey gülümsüyor. Sen...")
    print()
    secim = secim_al([
        {"metin": "'Teşekkürler!' de, sessizce içten ağla.",
         "kariyer": -10, "patron": +5, "arkadaslar": 0,
         "aciklama": "Tarık Bey memnun. Sen değil. Altı ay sonra mülakat vermeye başladın."},
        {"metin": "Piyasa araştırmasını göster, müzakere et.",
         "kariyer": +20, "patron": -5, "arkadaslar": 0,
         "aciklama": "Gergin bir sessizlik oldu. Sonunda %18 anlaştınız. Haklıydın."},
        {"metin": "'Düşüneceğim' de, offer letter ile geri dön.",
         "kariyer": +25, "patron": -15, "arkadaslar": +5,
         "aciklama": "Rakip şirket %40 teklif etti. Tarık Bey counter yaptı. Power move."},
        {"metin": "Reddet, kapıyı çarp çık.",
         "kariyer": -5, "patron": -25, "arkadaslar": +10,
         "aciklama": "Dramatik ama etkili. Arkadaşlar alkışladı. Tarık Bey özür diledi. Şans eseri."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_deadline_uzatma(state):
    ayrac()
    yaz("⏰  SENARYO: DEADLINE İMKÂNSIZ")
    ayrac()
    durakla()
    yaz("Tarık Bey yeni bir özellik istedi. Teslimat: bu Cuma.")
    yaz("Sen içinden hesaplıyorsun: minimum 3 haftalık iş.")
    yaz("Tarık Bey 'müşteri bekleniyor' diyor. Gözlerin doldu mu az önce?")
    durakla(0.8)
    yaz("\nEkipten kimse itiraz etmedi. Sıra sende.")
    print()
    secim = secim_al([
        {"metin": "'Tamam' de, 4 gün uyu madan çalış.",
         "kariyer": -20, "patron": +5, "arkadaslar": -5,
         "aciklama": "Cuma akşamı yarım biten bir şey teslim ettin. Ekip de bitik. Kimse iyi baktı."},
        {"metin": "Tahmini ayrıştır, 3 alternatif sun: MVP / tam / fazla mesai.",
         "kariyer": +20, "patron": +10, "arkadaslar": +5,
         "aciklama": "Tarık Bey seçenekler karşısında yumuşadı. MVP'yi seçti. İlişki güçlendi."},
        {"metin": "Sessiz kal, iş arkadaşınla 'imkânsız' diye fısılda.",
         "kariyer": -10, "patron": 0, "arkadaslar": -10,
         "aciklama": "Fısıltı duyuldu. Hem işi yetiştiremedin hem de profesyonellik sorgulandı."},
        {"metin": "'Bu sürede olmaz, en erken 3 hafta' de, nedenini belgele.",
         "kariyer": +15, "patron": -10, "arkadaslar": +10,
         "aciklama": "Tarık Bey sinirli baktı ama değerlendirdi. Ekip 'cesur' dedi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_cay_ocagi(state):
    ayrac()
    yaz("☕  SENARYO: ÇAY OCAĞI DEDİKODUSU")
    ayrac()
    durakla()
    yaz("Çay ocağında Mert ve Zeynep bir şeyler konuşuyor.")
    yaz("Yaklaşınca duyuyorsun: Tarık Bey'in favori çalışanı Kemal hakkında.")
    yaz("Mert: 'Kemal'in o PR'ı ben yazdım, adını bile koymadı.'")
    durakla(0.8)
    yaz("\nSeni görünce ikisi de susuyor. Bekleyerek bakıyorlar.")
    print()
    secim = secim_al([
        {"metin": "Kulak tıka, çayını al, dön.",
         "kariyer": 0, "patron": 0, "arkadaslar": -5,
         "aciklama": "Güvenilir görünmek istedin ama 'soğuk' olarak etiketlendim dedi Zeynep."},
        {"metin": "Dinle, sempati göster ama fikir verme.",
         "kariyer": 0, "patron": 0, "arkadaslar": +10,
         "aciklama": "Dinlemeyi biliyorsun. Mert sana güvenmeye başladı."},
        {"metin": "'Tarık Bey'e söyleyelim mi?' de.",
         "kariyer": -5, "patron": +5, "arkadaslar": -20,
         "aciklama": "İyi niyetliydin ama Mert sana bir daha sır vermeyeceğine yemin etti."},
        {"metin": "'Bunu yazılı belgele, PR history var zaten' de.",
         "kariyer": +5, "patron": 0, "arkadaslar": +15,
         "aciklama": "Pratik ve işe yarar bir öneri. Mert PR commit geçmişini buldu. Mutlu son."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_uzaktan_kamera(state):
    ayrac()
    yaz("🎥  SENARYO: ZOOM'DA KAMERA AÇILDI")
    ayrac()
    durakla()
    yaz("Uzaktan çalışma günü. Zoom toplantısı var: 'Q3 Roadmap Review'")
    yaz("Sen toplantıya bağlanıyorsun, kamerayı kapalı tutuyorsun...")
    durakla(0.5)
    yaz("...çünkü üzerinde pijama var. Ve mutfaktasın. Ve elinde peynir.")
    durakla(0.5)
    yaz("Tarık Bey: 'Herkesi görmek istiyorum, kameraları açalım!'")
    durakla(1)
    yaz(f"\n{state['isim']}, bekleniyor. Peynir hâlâ elinde.")
    print()
    secim = secim_al([
        {"metin": "Kamerayı aç, peynirle selamla.",
         "kariyer": -5, "patron": -5, "arkadaslar": +20,
         "aciklama": "Tarık Bey kaş kaldırdı. Ama ekip chat'te 💀😂 doldu. Legend oldun."},
        {"metin": "Hızla gömlek giy, 30 saniyede hazırlan.",
         "kariyer": +5, "patron": +10, "arkadaslar": +5,
         "aciklama": "Az farkla atlattın. Tarık Bey memnun. Çorabının rengi fark edilmedi."},
        {"metin": "'Kamerada teknik sorun var' de.",
         "kariyer": -10, "patron": -10, "arkadaslar": 0,
         "aciklama": "Kimse inanmadı. Arka planda buzdolabı sesi duyuldu."},
        {"metin": "Kamerayı aç ama ekrana kitap tut, yüzü kapat.",
         "kariyer": -15, "patron": -15, "arkadaslar": +10,
         "aciklama": "Mert ekran görüntüsünü 3 farklı gruba attı. Şirket efsanesi oldun. Kötü anlamda."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_reply_all(state):
    ayrac()
    yaz("📧  SENARYO: REPLY ALL FELAKETİ")
    ayrac()
    durakla()
    yaz("Şirket genelinde bir e-posta geldi: 'Yılsonu değerlendirme anketi'")
    yaz("İnsan Kaynakları'na 'Bu anket saçmalık, kimse doldurmaz' diye yanıt yazdın.")
    durakla(0.8)
    yaz("...")
    durakla(0.5)
    yaz("Gönder.")
    durakla(0.5)
    yaz("'Reply All' ile.")
    durakla(0.5)
    yaz("Alıcılar: 247 kişi.")
    durakla(1)
    yaz("\nGenel Müdür de o listede. 👁️")
    print()
    secim = secim_al([
        {"metin": "Bir özür e-postası gönder... 'Reply All' ile.",
         "kariyer": -25, "patron": -20, "arkadaslar": +15,
         "aciklama": "İkinci e-posta birincisinden daha ünlü oldu. Şirket tarihine geçtin."},
        {"metin": "IK'yı ara, durumu açıkla, özür dile.",
         "kariyer": +5, "patron": -10, "arkadaslar": 0,
         "aciklama": "IK direktörü 'ne güzel dürüstlük' dedi. Ama Genel Müdür hâlâ seni biliyor."},
        {"metin": "Hiçbir şey yapma, fırtınanın geçmesini bekle.",
         "kariyer": -10, "patron": -15, "arkadaslar": 0,
         "aciklama": "Konu üç gün boyunca şirket koridorlarında dolaştı. Sessizlik onu büyüttü."},
        {"metin": "Anketi doldur, 'İşte bu yüzden doldurmak istedim' de.",
         "kariyer": +10, "patron": -5, "arkadaslar": +20,
         "aciklama": "Absürt ama işe yaradı. Ekip saygı gösterdi. IK bunu vakasına yazdı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_kopek_gunu(state):
    ayrac()
    yaz("🐶  SENARYO: OFİSE KÖPEK GETİR GÜNÜ")
    ayrac()
    durakla()
    yaz("Şirket yeni bir 'çalışan mutluluğu' girişimi başlattı.")
    yaz("Her Cuma: 'Bring Your Pet to Work' günü.")
    yaz("Mert golden retriever getirdi. Zeynep papağan. Patronun sekreteri üç kedi.")
    durakla(0.8)
    yaz(f"\n{state['isim']}, sen ne getirdin?")
    print()
    secim = secim_al([
        {"metin": "Hiçbir şey getirme, çalışmaya devam et.",
         "kariyer": 0, "patron": 0, "arkadaslar": -10,
         "aciklama": "Herkes sosyalleşirken sen ekranın başındasın. 'O hep böyle' dediler."},
        {"metin": "Köpeğini getir. Mert'in köpeğiyle kavga çıkar.",
         "kariyer": -10, "patron": -15, "arkadaslar": -5,
         "aciklama": "IT odasına kadar kovaladılar. Tarık Bey 'evcil hayvan politikası' maili attı. Nedeni sensin."},
        {"metin": "Balık getir. Kavanozla. 'Bu da pet sayılır' de.",
         "kariyer": +5, "patron": +5, "arkadaslar": +20,
         "aciklama": "'Patron Balık' ismi verildi. Ofis maskotu oldu. Herkes sever. Kariyer mi? Biraz."},
        {"metin": "Oyuncak robot getir, 'En az bakım gerektiren pet' de.",
         "kariyer": +10, "patron": +10, "arkadaslar": +15,
         "aciklama": "Tarık Bey 'bu yaratıcılık' dedi. Zeynep bunu LinkedIn'e koydu. Viral oldu."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_kahve_makinesi(state):
    ayrac()
    yaz("☕  SENARYO: KAHVE MAKİNESİ KRİZİ")
    ayrac()
    durakla()
    yaz("Sabah 08:55. Toplantı 09:00'da.")
    yaz("Kahve makinesinin önünde sıra var. Dördüncü sıradasın.")
    durakla(0.5)
    yaz("Tam sıran geldi.")
    durakla(0.3)
    yaz("Makine: BEEEP. 'Su deposu boş.'")
    durakla(0.5)
    yaz("Herkes sana bakıyor. Makineyi en son sen kullanmıştın dün.")
    yaz("Tarık Bey de sırada. Elinde kupası. Gözleri sende.")
    print()
    secim = secim_al([
        {"metin": "Depoyu doldur, toplantıya geç kal.",
         "kariyer": -5, "patron": +15, "arkadaslar": +10,
         "aciklama": "Toplantıya geç kaldın ama ekip 'en azından doldurdu' dedi. Tarık Bey kafanı okşadı."},
        {"metin": "'Ben doldurmadım ki' de ve çık.",
         "kariyer": 0, "patron": -20, "arkadaslar": -15,
         "aciklama": "Herkes duydu. Kimse inanmadı. Makinenin yanında 'son kullanan: {isim}' logu var."},
        {"metin": "Depoyu doldur VE toplantıya zamanında yetiş.",
         "kariyer": +10, "patron": +20, "arkadaslar": +15,
         "aciklama": "30 saniyede koşarak depoyu doldurdum diyerek toplantıya girdin. Efsanevi giriş."},
        {"metin": "Markete çık, hazır kahve getir herkese.",
         "kariyer": +5, "patron": +15, "arkadaslar": +25,
         "aciklama": "18 kişilik ofise Starbucks getirdin. Masraf yaptın. Ama herkes seni sevdi."},
    ]).copy()
    secim["aciklama"] = secim["aciklama"].replace("{isim}", state["isim"])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_wifi_yok(state):
    ayrac()
    yaz("📡  SENARYO: OFİS İNTERNETİ ÇÖKTÜ")
    ayrac()
    durakla()
    yaz("Sabah 10:00. Şirketin internet bağlantısı kesildi.")
    yaz("Büyük bir sunum 14:00'da. Online.")
    yaz("IT ekibi: 'ISP'nin sorunu, saat yok.'")
    durakla(0.8)
    yaz("\nHerkes panikliyor. Tarık Bey koridorda volta atıyor.")
    yaz("Arkadaşlarından biri: 'Telefon hotspot'u olur mu?'")
    print()
    secim = secim_al([
        {"metin": "Hotspot aç, 6 kişiyi bağla ve sunum yap.",
         "kariyer": +15, "patron": +20, "arkadaslar": +20,
         "aciklama": "Telefonun eridi ama sunum oldu. Tarık Bey seni 'kriz çözücü' diye tanımladı."},
        {"metin": "Kafeden çalış, sunumu oradan yap.",
         "kariyer": +10, "patron": +5, "arkadaslar": +5,
         "aciklama": "Pratik çözüm. Kahve de içtin. Pek de fena değil."},
        {"metin": "Sunumu ertele, 'elimden geleni yaptım' de.",
         "kariyer": -10, "patron": -15, "arkadaslar": 0,
         "aciklama": "Müşteri sinirle ayrıldı. Tarık Bey seni 'çözüm bulamadın' diye yazdı."},
        {"metin": "IT ekibine 4 saatte 47 Slack mesajı at.",
         "kariyer": -5, "patron": 0, "arkadaslar": -10,
         "aciklama": "IT ekibi seni blokla dı. Sorun hâlâ çözülmedi. İlişkiler gerildi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_yetki_hatasi(state):
    ayrac()
    yaz("🔐  SENARYO: YANLIŞ ORTAMDA KOMUT")
    ayrac()
    durakla()
    yaz("Perşembe sabahı. Bir script çalıştıracaksın.")
    yaz("Terminal penceresi açık. Komutu yazıyorsun.")
    yaz("Enter.")
    durakla(1)
    yaz("\n...")
    durakla(0.5)
    yaz("Script çalışıyor.")
    durakla(0.5)
    yaz("Hızlı çalışıyor.")
    durakla(0.5)
    yaz("Çok hızlı.")
    durakla(0.5)
    yaz("Production database'indesin. Staging değil. PROD.")
    durakla(1)
    yaz(f"\n{state['isim']}... 40.000 satır veri değişti.")
    print()
    secim = secim_al([
        {"metin": "Hemen durdur, DBA'yi ara, rollback planla.",
         "kariyer": +10, "patron": -5, "arkadaslar": +5,
         "aciklama": "Hızlı aksiyon. 2 saatte rollback tamamlandı. 'Nasıl olduysa' sorusu geldi ama kriz yönettin."},
        {"metin": "Kimseye söyleme, sanki hiçbir şey olmamış gibi devam et.",
         "kariyer": -30, "patron": -30, "arkadaslar": -20,
         "aciklama": "Müşteri şikâyetleri başladı. Audit log her şeyi gösterdi. Tarık Bey toplantıya çağırdı."},
        {"metin": "Post-mortem belgesi hazırla, şeffaf ol.",
         "kariyer": +20, "patron": +10, "arkadaslar": +10,
         "aciklama": "Olgunluk gösterdin. Süreç iyileşti. Artık prod/staging renk kodlu."},
        {"metin": "İşi bırak, çantanı al, kapıdan çık.",
         "kariyer": -20, "patron": -20, "arkadaslar": +5,
         "aciklama": "Dramatik çıkış. Ama sorunu çözmeden gittin. Arkadaşlar anlayış gösterdi. Tarık Bey göstermedi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_ofis_muzigi(state):
    ayrac()
    yaz("🎵  SENARYO: OFİSTE MÜZİK KAVGASI")
    ayrac()
    durakla()
    yaz("Açık ofis. 23 kişi. Herkesin müzik zevki farklı.")
    yaz("Bugün Mert kulaklığını takıp tam ses açtı.")
    yaz("Ama kulaklık tak sesini kesmedi, hoparlörden çalıyor.")
    durakla(0.8)
    yaz("\nTüm ofis Mert'in 'lo-fi hip hop beats to code to' playlistini dinliyor.")
    yaz("Zeynep şikayet etti. Mert 'bu konsantrasyon müziği' dedi.")
    yaz(f"\n{state['isim']}, sen ne yaparsın?")
    print()
    secim = secim_al([
        {"metin": "Kulaklığını tak, umursamazlık moduna geç.",
         "kariyer": 0, "patron": 0, "arkadaslar": -5,
         "aciklama": "Sorun çözülmedi ama sen etkilenmedin. Zeynep 'hiç umursamadı' dedi."},
        {"metin": "Mert'e kibarca 'hoparlör yerine kulaklık' de.",
         "kariyer": +5, "patron": +5, "arkadaslar": +10,
         "aciklama": "Mert utandı, kablosuz kulaklık taktı. Zeynep sana teşekkür etti."},
        {"metin": "Ofis Spotify'ı aç, death metal çal.",
         "kariyer": -10, "patron": -10, "arkadaslar": -5,
         "aciklama": "Savaş tırmandı. Tarık Bey 'müzik yasak' kararı aldı. Sen nedenisin."},
        {"metin": "Toplantı odası rezerve et, 'sessiz çalışma alanı' oluştur.",
         "kariyer": +10, "patron": +10, "arkadaslar": +15,
         "aciklama": "Kahraman oldun. Toplantı odası artık 'deep work zone'. Tarık Bey onayladı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_linkedin(state):
    ayrac()
    yaz("💼  SENARYO: LİNKEDİN POSTU")
    ayrac()
    durakla()
    yaz("Büyük bir bug fix yaptın. Haftalarca uğraştın.")
    yaz("Gururla LinkedIn'e yazıyorsun:")
    yaz("\n  'Büyük bir sorunu çözdük! Ekibimizle gurur duyuyorum 🚀'")
    durakla(0.8)
    yaz("\nPost viral oldu: 847 beğeni, 43 yorum.")
    yaz("Ama Tarık Bey DM attı: 'Bu iç proje bilgisi paylaşılır mıydı?'")
    yaz("Mert de comment'e yazdı: 'Ekip mi? Ben de vardım orada 🙂'")
    print()
    secim = secim_al([
        {"metin": "Postu sil, özür dile.",
         "kariyer": -5, "patron": +10, "arkadaslar": -5,
         "aciklama": "847 kişi gördü. Silmek geç kaldı. Mert hâlâ gülümsüyor."},
        {"metin": "Tarık Bey'e 'Gizli bilgi yok' diye açıkla.",
         "kariyer": +10, "patron": +5, "arkadaslar": 0,
         "aciklama": "Haklıydın ve ikna ettin. Tarık Bey 'sosyal medya politikası' belgesi hazırladı."},
        {"metin": "Mert'i de tag'le, 'Birlikte çözdük' diye güncelle.",
         "kariyer": +15, "patron": 0, "arkadaslar": +20,
         "aciklama": "Mert 'bu adam tam oldu' dedi. Birlikte daha fazla recruiter mesajı aldınız."},
        {"metin": "Tarık Bey'i de tag'le, 'Harika liderlik teşekkürler' ekle.",
         "kariyer": +5, "patron": +20, "arkadaslar": -5,
         "aciklama": "Tarık Bey eridi. Mert 'patrona yağ çekiyor' dedi. Her stratejinin maliyeti var."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_ceo_ziyaret(state):
    ayrac()
    yaz("👔  SENARYO: CEO BEKLENMEDİK OFİS ZİYARETİ")
    ayrac()
    durakla()
    yaz("Çarşamba sabahı. Herkes işinin başında.")
    yaz("Asansör açıldı. CEO Serdar Bey ofise girdi.")
    yaz("Kimse beklemiyor. Tarık Bey titreyerek ayağa kalktı.")
    durakla(0.8)
    yaz("\nSerdar Bey tur atıyor. Masalara uğruyor.")
    yaz(f"Ve senin masana geldi: '{state['isim']} değil misin? Ne üzerinde çalışıyorsun?'")
    yaz("Tarık Bey uzaktan izliyor.")
    print()
    secim = secim_al([
        {"metin": "Panikle, ekranı kapat, 'önemli bir şey' de.",
         "kariyer": -10, "patron": -5, "arkadaslar": 0,
         "aciklama": "Serdar Bey 'neden kapattı acaba' diye Tarık Bey'e sordu. Açıklama toplantısı oldu."},
        {"metin": "Net ve özlü anlat: proje, etki, zorluk.",
         "kariyer": +25, "patron": +15, "arkadaslar": +5,
         "aciklama": "Serdar Bey 'bu adam hazırmış' dedi. Tarık Bey'e döndü: 'Bunu takip et.'"},
        {"metin": "Tarık Bey'e bak, onay bekle, sonra konuş.",
         "kariyer": 0, "patron": +10, "arkadaslar": 0,
         "aciklama": "Sadık göründün. Ama fırsatı kaçırdın. Serdar Bey devam etti."},
        {"metin": "'Aslında bir sorunumuz var, şirkette X eksik' de.",
         "kariyer": -5, "patron": -20, "arkadaslar": +10,
         "aciklama": "Serdar Bey not aldı. Tarık Bey gece senin 1-on-1'ını ekledi takvime. Ertesi gün."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_agile_kriz(state):
    ayrac()
    yaz("🔄  SENARYO: 'AGILE DEĞİLİZ, AMA AGILE YAPIYORUZ'")
    ayrac()
    durakla()
    yaz("Yeni bir scrum master işe başladı: Deniz.")
    yaz("İlk gün: 'Agile süreçleri iyileştireceğiz!'")
    yaz("Daily standup artık 45 dakika. Sprint retrospective 3 saat.")
    durakla(0.8)
    yaz("Velocity düştü. Moral düştü. Kimse memnun değil.")
    yaz(f"\nDeniz senden next sprint'te 'agile champion' olmanı istiyor.")
    print()
    secim = secim_al([
        {"metin": "Kabul et, agile evangelist ol.",
         "kariyer": -10, "patron": +5, "arkadaslar": -15,
         "aciklama": "Ekip seni 'süreç polisi' diye andı. Standup'ta seni görmek istemediler."},
        {"metin": "Nazikçe reddet, verimlilik metriklerini göster.",
         "kariyer": +15, "patron": -5, "arkadaslar": +15,
         "aciklama": "Ekip seni sevdi. Deniz'le gerildi ama Tarık Bey metriklere baktı."},
        {"metin": "Deniz'le otur, 'lightweight agile' versiyonu tasarla.",
         "kariyer": +20, "patron": +10, "arkadaslar": +10,
         "aciklama": "İş birliği kazandı. Standuplar 15 dakikaya indi. Herkes mutlu."},
        {"metin": "'Biz zaten waterfall yapıyoruz, kabul edelim' de.",
         "kariyer": -5, "patron": -10, "arkadaslar": +5,
         "aciklama": "Gerçekçiydin ama kimse duymak istemedi. Deniz şikâyetçi oldu."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_gece_yarisi_deploy(state):
    ayrac()
    yaz("🌙  SENARYO: GECE YARISI DEPLOY TEKLIFI")
    ayrac()
    durakla()
    yaz("Saat 23:15. Yatmak üzeresin.")
    yaz("Tarık Bey Whatsapp'tan yazdı:")
    yaz("\n  'Hocam şu deployment acil lazım, 30 dakikan var mı?'")
    durakla(0.8)
    yaz("\nBu ayki 6. gece yarısı talebi.")
    yaz("Eşin/arkadaşın 'ne zaman biter bu?' diye bakıyor.")
    yaz("Ama sabah kritik bir demo var.")
    print()
    secim = secim_al([
        {"metin": "Kalk, deploy et, kahvaltıda uyu.",
         "kariyer": +5, "patron": +20, "arkadaslar": 0,
         "aciklama": "Tarık Bey çok memnun. Ama bu 7. sefer oldu. Pattern başladı."},
        {"metin": "Reddet: 'Mesai saatleri dışı, sabah halledelim.'",
         "kariyer": +15, "patron": -15, "arkadaslar": +5,
         "aciklama": "Tarık Bey sinirli. Ama sınır koydun. Demo sabah sorunsuz geçti."},
        {"metin": "Reddet ve on-call politikası taslağı gönder.",
         "kariyer": +20, "patron": -10, "arkadaslar": +10,
         "aciklama": "Tarık Bey önce sinirli, sonra 'haklısın' dedi. Şirkete resmi on-call eklendi."},
        {"metin": "Yap ama sabah toplantıda geç saate kadar çalıştığını belirt.",
         "kariyer": 0, "patron": +10, "arkadaslar": 0,
         "aciklama": "Toplantıda bahsettin. Herkes 'vay be' dedi. Tarık Bey 'kahvaltonun bedeli bizden' dedi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_teknik_borc(state):
    ayrac()
    yaz("🏚️  SENARYO: TEKNİK BORÇ TOPLANTISI")
    ayrac()
    durakla()
    yaz("Şirketin ana servisi 8 yıllık spaghetti kod.")
    yaz("Her yeni özellik 3 kat daha uzun sürüyor.")
    yaz("Ekip refactor istiyor. Tarık Bey: 'Bizi geride bırakır, hayır.'")
    durakla(0.8)
    yaz("\nSen sunum hazırladın: teknik borç maliyeti hesabı.")
    yaz("Tarık Bey sunum odasına oturdu. Hazırsın.")
    print()
    secim = secim_al([
        {"metin": "Tüm teknik detayı anlat: stack trace'ler, metrikler.",
         "kariyer": +5, "patron": -5, "arkadaslar": +5,
         "aciklama": "Tarık Bey 10. slaytta uyukladı. Ekip güldü. Mesaj iletilmedi."},
        {"metin": "Sadece iş etkisini göster: maliyet, gecikme, risk.",
         "kariyer": +20, "patron": +15, "arkadaslar": +10,
         "aciklama": "Tarık Bey 'rakamlarla anlat' sever. İkna oldu. Refactor roadmap başladı."},
        {"metin": "Refactor'ı gizlice feature içine göm.",
         "kariyer": +10, "patron": 0, "arkadaslar": +15,
         "aciklama": "Ekip seni alkışladı. Tarık Bey hiç fark etmedi. Sistematik ama riskli."},
        {"metin": "'Refactor etmezsek 6 ayda yeni geliştirici bulamazsınız' de.",
         "kariyer": +15, "patron": -15, "arkadaslar": +5,
         "aciklama": "Doğruydu. Ama tehdite benzedi. Tarık Bey gerindi ama dinledi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def senaryo_cursor_ai(state):
    ayrac()
    yaz("🤖  SENARYO: AI ARACIYLA KOD YAZDIRDIN")
    ayrac()
    durakla()
    yaz("Bu sprint'te görevin: ödeme modülü refactor.")
    yaz("AI aracıyla 2 saatte bitirdin. Normalde 5 gün sürerdi.")
    yaz("Kod çalışıyor. Testler geçiyor.")
    durakla(0.8)
    yaz("\nAma Tarık Bey sprint review'da soruyor:")
    yaz("'Bu kadar hızlı nasıl bitirdin? AI mi kullandın?'")
    yaz("Ekip meraklı gözlerle bakıyor.")
    print()
    secim = secim_al([
        {"metin": "Hayır de, 'kendim yazdım' de.",
         "kariyer": -20, "patron": -10, "arkadaslar": -10,
         "aciklama": "Mert kodu inceledi. AI pattern'leri belli. 'Neden yalan söyledin?' toplantısı oldu."},
        {"metin": "Evet de, araç ve süreci şeffafça anlat.",
         "kariyer": +20, "patron": +10, "arkadaslar": +15,
         "aciklama": "Tarık Bey 'ekibe anlat' dedi. Ekip AI araç eğitimi aldı. Kahraman oldun."},
        {"metin": "'Biraz yardım aldım' de, detay verme.",
         "kariyer": -5, "patron": -5, "arkadaslar": 0,
         "aciklama": "Belirsiz cevap şüphe yarattı. Mert 'kim yardım etti?' diye sordu."},
        {"metin": "Konuyu değiştir, 'iyi değil mi?' de.",
         "kariyer": 0, "patron": -10, "arkadaslar": -5,
         "aciklama": "Deflection fark edildi. 'Şeffaf değil' notu düşüldü performans değerlendirmesine."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim


# ─────────────────────────────────────────────
#  TEST MÜHENDİSİ SENARYOLARI
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
         "kariyer": -10, "patron": 0, "arkadaslar": +5,
         "aciklama": "Bir ay sonra prod'da o bug çıktı. 'Flaky testti' diyemedin. Mert seni anmadı."},
        {"metin": "Root cause analiz et, intermittent failing'in kaynağını bul.",
         "kariyer": +20, "patron": +15, "arkadaslar": +5,
         "aciklama": "Race condition buldun. Hem test hem kod düzeldi. Tarık Bey ismine not düştü."},
        {"metin": "Birkaç kez çalıştır, geçince merge et.",
         "kariyer": -5, "patron": -5, "arkadaslar": 0,
         "aciklama": "Geçici çözüm oldu. Sorun iki hafta sonra yine patladı. Mert 'biliyordum' dedi."},
        {"metin": "Test altyapısı ekibine ticket aç, belgeleri.",
         "kariyer": +10, "patron": +5, "arkadaslar": +5,
         "aciklama": "Doğru kanalı kullandın. Yavaş ama kalıcı çözüm geldi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
         "kariyer": -25, "patron": -20, "arkadaslar": -5,
         "aciklama": "Müşteriler keşfetti. Sabahın 3'ünde acil toplantı. Adın her yerde."},
        {"metin": "PM'e bildir, release'i ertele, bug fix önceliği ver.",
         "kariyer": +20, "patron": +15, "arkadaslar": +5,
         "aciklama": "Tarık Bey sinirli oldu ama haklı olduğunu kabul etti. Krizi önledin."},
        {"metin": "Sadece developer'a ilet, o karar versin.",
         "kariyer": +5, "patron": 0, "arkadaslar": 0,
         "aciklama": "Sorumluluk geçti ama sen fırsatı kaçırdın. 'Söyledi mi söylemedi mi' tartışması başladı."},
        {"metin": "Riski belgele, 'release edelim ama hemen hot-fix planlayalım' de.",
         "kariyer": +15, "patron": +10, "arkadaslar": +5,
         "aciklama": "Pragmatik yaklaşım. Herkes risk farkındaydı, hot-fix sabah yayına girdi."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
         "kariyer": -15, "patron": +5, "arkadaslar": -5,
         "aciklama": "İlk sprintte 3 gün sürdü. Hata oranı arttı. Motivasyonun sıfırlandı."},
        {"metin": "Otomasyonun ROI'sini hesapla, Tarık Bey'e sun.",
         "kariyer": +20, "patron": +15, "arkadaslar": +5,
         "aciklama": "Maliyet analizi ikna etti. Araçlar geri geldi, sana teşekkür etti."},
        {"metin": "En kritik 40 testi manuel yap, gerisini risk olarak belgele.",
         "kariyer": +10, "patron": +5, "arkadaslar": +5,
         "aciklama": "Makul bir orta yol. Herkes kabul etti, risk bilinçli alındı."},
        {"metin": "Karşı çıkmadan işi başka takım arkadaşına devret.",
         "kariyer": -5, "patron": 0, "arkadaslar": -10,
         "aciklama": "Problem çözülmedi, sadece yer değiştirdi. Liderlik fırsatı kaçtı. Arkadaş sinirli."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
         "kariyer": -20, "patron": 0, "arkadaslar": +5,
         "aciklama": "İki hafta sonra 'basit' kod prod'da patlattı. 'Test yoktu neden?' sorusu geldi sana."},
        {"metin": "Neden test gerektiğini örnekle açıkla, itiraz et.",
         "kariyer": +15, "patron": +10, "arkadaslar": -5,
         "aciklama": "Mert önce sinirli oldu, sonra haklı olduğunu kabul etti. Süreç güçlendi."},
        {"metin": "Kendin test yaz, PR'a comment olarak ekle.",
         "kariyer": +20, "patron": +10, "arkadaslar": +10,
         "aciklama": "Eylemle örnek gösterdin. Mert 'bak bu işe yarıyor' dedi. Kültür değişti."},
        {"metin": "Manager'a escalate et.",
         "kariyer": -5, "patron": 0, "arkadaslar": -15,
         "aciklama": "Mesele büyüdü, gereksiz gerilim oldu. Mert seninle küstü."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
        {"metin": "DevOps'u tekrar ara, escalate et.",
         "kariyer": +15, "patron": +10, "arkadaslar": +5,
         "aciklama": "Israr ettin, saat 17:00'de ortam ayağa kalktı. Testleri bitirdin."},
        {"metin": "Prod ortamında test et, 'sadece bir kez' diyerek.",
         "kariyer": -30, "patron": -25, "arkadaslar": -10,
         "aciklama": "Prod'daki veriyi bozdun. Gece yarısı acil rollback. Tarihe geçtin."},
        {"metin": "Release'i ertele, 'test edilmeden gidemez' de.",
         "kariyer": +10, "patron": -5, "arkadaslar": +5,
         "aciklama": "Tarık Bey sinirli oldu ama haklı kararı kabul etti. Sonra teşekkür etti."},
        {"metin": "Eksik test raporuyla release'e geç, sonra kapatırız.",
         "kariyer": -15, "patron": -10, "arkadaslar": -5,
         "aciklama": "3 bug prod'a gitti. 'Sonra kapatalım' dediğin testler kapanmadı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
         "kariyer": -25, "patron": -20, "arkadaslar": -10,
         "aciklama": "Ay sonunda gerçek metrikler ortaya çıktı. Güven tamamen sarsıldı."},
        {"metin": "Hangi alanların riskli kaldığını, neden bu duruma gelindiğini belgele.",
         "kariyer": +20, "patron": +10, "arkadaslar": +5,
         "aciklama": "Şeffaflık takdir gördü. Süreç sorunu gün yüzüne çıktı, ekip düzeltildi."},
        {"metin": "İçi boş testler yaz, coverage'ı anlık artır.",
         "kariyer": -10, "patron": -5, "arkadaslar": -5,
         "aciklama": "Coverage %80 oldu ama testler hiçbir şeyi doğrulamıyordu. Sonra belli oldu."},
        {"metin": "Sonraki sprint için risk-öncelikli test planı sun.",
         "kariyer": +10, "patron": +5, "arkadaslar": +5,
         "aciklama": "Proaktif yaklaşım beğenildi. Kısa vadede ağrı, uzun vadede güven."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
         "kariyer": -20, "patron": +5, "arkadaslar": 0,
         "aciklama": "Config değişikliği 2 servisi bozdu. Hafta sonu acil müdahale. Adın anıldı."},
        {"metin": "Riski Tarık Bey'e belgele, yazılı onaylatarak atla.",
         "kariyer": +10, "patron": +5, "arkadaslar": +5,
         "aciklama": "Kararı ona bıraktın, riski görünür kıldın. Bir sorun çıkınca arkana bakıyorsun."},
        {"metin": "Kısa hedefli smoke test yap, 30 dakikada bitir.",
         "kariyer": +15, "patron": +10, "arkadaslar": +5,
         "aciklama": "Akıllı denge. Kritik yollar test edildi, zaman korundu. Herkes mutlu."},
        {"metin": "Full regression için ısrar et, gecikmeyı kabul et.",
         "kariyer": +5, "patron": -10, "arkadaslar": +5,
         "aciklama": "Doğru karardı ama Tarık Bey gerildi. Haklıydın, ama ilişki zorlandı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def tm_yuk_testi(state):
    ayrac()
    yaz("📈  SENARYO: YÜK TESTİ BAŞARISIZ")
    ayrac()
    durakla()
    yaz(f"Büyük kampanya lansmanı yarın. Beklenen: 5000 eş zamanlı kullanıcı.")
    yaz("Yük testini çalıştırdın:")
    durakla(0.8)
    yaz("\n  500 kullanıcı  → ✅ OK")
    yaz("  1000 kullanıcı → ✅ OK")
    yaz("  2000 kullanıcı → ❌ Sistem yanıt vermiyor")
    durakla(1)
    yaz("\nRelease yarın sabah. Tarık Bey 'lansman iptal edilemez' diyor.")
    print()
    secim = secim_al([
        {"metin": "Test parametrelerini 500'e düşür, 'geçti' de.",
         "kariyer": -25, "patron": -15, "arkadaslar": -5,
         "aciklama": "Lansman başladı, sistem 800 kullanıcıda çöktü. Canlı yayın felaketi."},
        {"metin": "Sonuçları paylaş, ekiple emergency toplantı çağır.",
         "kariyer": +20, "patron": +10, "arkadaslar": +10,
         "aciklama": "Zor karar ama doğru karar. Lansman 1 gün ertelendi, felaket önlendi."},
        {"metin": "Sadece developer'a ilet, 'senin sorunun' de.",
         "kariyer": +5, "patron": 0, "arkadaslar": -5,
         "aciklama": "Developer düzeltti ama sen loop dışında kaldın. Katkın görünmedi."},
        {"metin": "Raporu 'test ortamı sorunu olabilir' notu ile sun.",
         "kariyer": -10, "patron": -5, "arkadaslar": 0,
         "aciklama": "Belirsizlik kötü karar almaya yol açtı. Prod'da doğrulandı: sorun gerçekti."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

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
         "kariyer": -20, "patron": -15, "arkadaslar": -10,
         "aciklama": "Savunma modu krizi büyüttü. 'Peki neden senaryoda yoktu?' sorusu geldi."},
        {"metin": "Durumu kabul et, kaçan senaryoyu belgele, süreç iyileştirmesi öner.",
         "kariyer": +20, "patron": +15, "arkadaslar": +5,
         "aciklama": "Olgunluk gösterdin. Bunu fırsata çevirdin, test planı güçlendi."},
        {"metin": "Sessiz kal, developer fix yaparken bekle.",
         "kariyer": -10, "patron": -10, "arkadaslar": -5,
         "aciklama": "Pasif kaldın. 'Test mühendisi ne iş yapıyor?' sorusu başladı."},
        {"metin": "Hemen hot-fix için test senaryolarını hazırla ve sürece katıl.",
         "kariyer": +15, "patron": +10, "arkadaslar": +10,
         "aciklama": "Hızlı aksiyon aldın. Fix'in doğru çalıştığını da sen onayladın."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim

def tm_kopyala_yapistir(state):
    ayrac()
    yaz("📋  SENARYO: STACKOVERFLOW'DAN KOPYALA-YAPIŞTIR")
    ayrac()
    durakla()
    yaz("Developer Zeynep PR açtı. Test yoktu ama kod çalışıyordu.")
    yaz("Sen inceleyince fark ettin: kritik bir güvenlik fonksiyonu")
    yaz("birebir Stack Overflow'dan kopyalanmış.")
    durakla(0.8)
    yaz("\nYorum bile aynen kopyalanmış: '// fix from John, 2019'")
    yaz("Lisans: 'Creative Commons, attribution required'")
    print()
    secim = secim_al([
        {"metin": "Görmezden gel, en azından çalışıyor.",
         "kariyer": -15, "patron": -5, "arkadaslar": +5,
         "aciklama": "6 ay sonra lisans auditi başladı. 'Kim merge etti?' diye soruldu."},
        {"metin": "Zeynep'e PR'da yorum bırak, yeniden yaz de.",
         "kariyer": +15, "patron": +5, "arkadaslar": +5,
         "aciklama": "Zeynep öğrendi. Kod düzeldi. PR kalite rehberi güncellendi."},
        {"metin": "Hukuk birimine ilet.",
         "kariyer": 0, "patron": +5, "arkadaslar": -15,
         "aciklama": "Yasal olarak doğru. Ama Zeynep senden ürktü. Ekip 'abartmadı mı?' dedi."},
        {"metin": "Kodu kendin yeniden yaz, Zeynep'e sonra anlat.",
         "kariyer": +10, "patron": +5, "arkadaslar": +10,
         "aciklama": "Sorunu çözdün ve öğrettin. Zeynep minnettardı."},
    ])
    sonuc_goster(secim, secim["aciklama"])
    return secim


# ─────────────────────────────────────────────
#  SONUÇ EKRANI
# ─────────────────────────────────────────────

def oyun_sonu(state):
    ayrac()
    yaz("🏁  OYUN SONU — FİNAL DURUM")
    ayrac()

    k = state["kariyer"]
    p = state["patron"]
    a = state["arkadaslar"]
    isim = state["isim"]
    poz = state["pozisyon"]

    yaz(f"Son durum: {isim} ({poz})")
    print()
    print(f"  💼 Kariyer   : {stat_bar(k)}")
    print(f"  😤 Patron    : {stat_bar(p)}")
    print(f"  🤝 Arkadaşlar: {stat_bar(a)}")
    print()
    durakla(1)

    # Kariyer sonucu
    if k >= 80:
        yaz("⭐  KARİYER: Şirketin Efsanesi — LinkedIn profilin recruiter istilasında.")
    elif k >= 60:
        yaz("👍  KARİYER: Güvenilir Yazılımcı — Zam görüşmesi yakında. Belki.")
    elif k >= 40:
        yaz("😐  KARİYER: Fark Edilmeyen Çalışan — Tarık Bey bazen adını karıştırıyor.")
    elif k >= 20:
        yaz("😬  KARİYER: Kriz Uzmanı (Ama Nedeni Genelde Sen) — HR 'gelişim planı' dedi.")
    else:
        yaz(f"💀  KARİYER: '{isim.lower()}lamak' şirkette bir fiil oldu.")

    durakla(0.5)

    # Patron sonucu
    if p >= 80:
        yaz("🤝  PATRON: Tarık Bey seni 'geleceğin lideri' olarak gösteriyor.")
    elif p >= 60:
        yaz("👔  PATRON: Tarık Bey senden memnun, ama bunu yüzüne söylemez.")
    elif p >= 40:
        yaz("😶  PATRON: Tarık Bey seni 'var da yok da aynı' kategorisine koydu.")
    elif p >= 20:
        yaz("😤  PATRON: Tarık Bey seninle toplantı öncesi derin nefes alıyor.")
    else:
        yaz("🔥  PATRON: Tarık Bey seni her hafta IK'ya 'sorunlu çalışan' diye işliyor.")

    durakla(0.5)

    # Arkadaş sonucu
    if a >= 80:
        yaz("🎉  ARKADAŞLAR: Mert ve Zeynep seni 'öğle yemeği first pick' ilan etti.")
    elif a >= 60:
        yaz("😊  ARKADAŞLAR: Ekip seni seviyor. Doğum günündeki pastada adın var.")
    elif a >= 40:
        yaz("🙂  ARKADAŞLAR: Kimseden şikâyet yok ama özel Whatsapp grubuna da alınmadın.")
    elif a >= 20:
        yaz("😒  ARKADAŞLAR: Mutfakta girerken konuşmalar kesiliyor.")
    else:
        yaz("👻  ARKADAŞLAR: 'Kim bu?' sorusu hâlâ soruluyor. 6. ayındasın.")

    # Genel değerlendirme
    print()
    ortalama = (k + p + a) // 3
    if ortalama >= 75:
        print("  ╔══════════════════════════════════════╗")
        print("  ║  MÜKEMMEL GENEL SKOR — HAYALİ ÇALIŞAN ║")
        print("  ╚══════════════════════════════════════╝")
        yaz(f"\n{isim}, şirkette her şeyi dengelemeyi başardın.")
        yaz("Bu gerçek hayatta çok nadir görülür. Tebrikler.")
    elif ortalama >= 55:
        print("  ┌──────────────────────────────────────┐")
        print("  │      İYİ SKOR — SAĞLAM ÇALIŞAN       │")
        print("  └──────────────────────────────────────┘")
        yaz(f"\n{isim}, bazı dengeler kuruldU, bazıları kurulmadı.")
        yaz("Gerçek hayat da böyle aslında. İyi gidiyorsun.")
    elif ortalama >= 35:
        print("  ┌──────────────────────────────────────┐")
        print("  │    ORTA SKOR — GELİŞİM GEREKLİ       │")
        print("  └──────────────────────────────────────┘")
        yaz(f"\n{isim}, bazı ilişkileri ihmal ettin.")
        yaz("Kariyer sadece kod yazmaktan ibaret değil...")
    else:
        print("  ╔══════════════════════════════════════╗")
        print("  ║     DÜŞÜK SKOR — YENİ BAŞLANGIÇ?      ║")
        print("  ╚══════════════════════════════════════╝")
        yaz(f"\n{isim}... belki başka bir şirket, belki başka bir karakter?")
        yaz("Neyse ki bu sadece bir oyun. Gerçek hayatta tekrar şans var.")

    print()
    yaz("Oynamak için teşekkürler. Gerçek yazılım hayatı bundan çok farklı değil.")
    ayrac()


# ─────────────────────────────────────────────
#  KARAKTER OLUŞTURMA
# ─────────────────────────────────────────────

def karakter_olustur():
    baslik_goster()
    yaz("Bir yazılım firmasında çalışıyorsun.")
    yaz("Her karar kariyerini, patronunla ilişkini ve arkadaşlıklarını etkiliyor.\n")

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
    yaz("Kariyer: 50 | Patron İlişkisi: 50 | Arkadaşlık: 50")
    yaz("Her şey senin elinde.\n")
    durakla(1)

    return {
        "isim": isim,
        "pozisyon": pozisyon,
        "kariyer": 50,
        "patron": 50,
        "arkadaslar": 50,
        "gun": 1,
    }


# ─────────────────────────────────────────────
#  ANA OYUN DÖNGÜSÜ
# ─────────────────────────────────────────────

def main():
    state = karakter_olustur()

    genel_havuz = [
        senaryo_sprint,
        senaryo_slack,
        senaryo_prod_hata,
        senaryo_code_review,
        senaryo_toplanti,
        senaryo_mentor,
        senaryo_zam_gorusmesi,
        senaryo_deadline_uzatma,
        senaryo_cay_ocagi,
        senaryo_uzaktan_kamera,
        senaryo_reply_all,
        senaryo_kopek_gunu,
        senaryo_kahve_makinesi,
        senaryo_wifi_yok,
        senaryo_yetki_hatasi,
        senaryo_ofis_muzigi,
        senaryo_linkedin,
        senaryo_ceo_ziyaret,
        senaryo_agile_kriz,
        senaryo_gece_yarisi_deploy,
        senaryo_teknik_borc,
        senaryo_cursor_ai,
    ]

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
        tm_kopyala_yapistir,
    ]

    if state["pozisyon"] == "Test Mühendisi":
        random.shuffle(tm_havuz)
        senaryolar = tm_havuz[:7]
    else:
        random.shuffle(genel_havuz)
        senaryolar = genel_havuz[:7]

    for i, senaryo in enumerate(senaryolar, 1):
        state["gun"] = i
        stats_goster(state)
        deltas = senaryo(state)
        state["kariyer"]    = max(0, min(100, state["kariyer"]    + deltas.get("kariyer", 0)))
        state["patron"]     = max(0, min(100, state["patron"]     + deltas.get("patron", 0)))
        state["arkadaslar"] = max(0, min(100, state["arkadaslar"] + deltas.get("arkadaslar", 0)))
        durakla(1)

    oyun_sonu(state)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Oyundan çıkıldı. Gerçek hayatta bu kadar kolay değil!")
