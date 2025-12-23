import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Sınav Karakter Testi", page_icon="🎓")

# Başlık
st.title("🧠 Hangi Sınav Öğrenci Tipisin?")
st.write("Aşağıdaki 10 soruyu dürüstçe cevapla, analizini yapalım!")
st.markdown("---")

# Puanları tutacağımız sözlük (Başlangıçta hepsi 0)
scores = {
    "Panik Pilotu": 0,       # Çok heyecanlı, eli ayağına dolaşan
    "Erteleyici Filozof": 0, # Zeki ama çalışmayı sevmeyen
    "Garantici Kaplumbağa": 0, # Mükemmeliyetçi, yavaş çözen
    "Stratejik Ninja": 0     # İdeal öğrenci profili
}

# --- SORULAR BAŞLIYOR ---

# SORU 1
st.subheader("1. Sınavda çok zor bir soruyla karşılaştın. İlk tepkin?")
s1 = st.radio(
    "Seçim 1:",
    [
        "Eyvah! Yapamıyorum, kesin diğerlerini de yapamayacağım. (Panik)", 
        "Aman canım, sonra bakarım. (Erteleyici)", 
        "Bu soruyla inatlaşırım, çözmeden bırakmam! (Garantici)", 
        "Yanına işaret koyar, turlama taktiğiyle sonra dönerim. (Stratejik)"
    ],
    key="s1", label_visibility="collapsed"
)
if "Eyvah" in s1: scores["Panik Pilotu"] += 1
elif "Aman" in s1: scores["Erteleyici Filozof"] += 1
elif "inatlaşırım" in s1: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 2
st.subheader("2. Çalışma masanın durumu genelde nasıldır?")
s2 = st.radio(
    "Seçim 2:",
    [
        "Çok dağınık, aradığımı bulamıyorum ve bu beni geriyor.", 
        "Kitaplar, bilgisayar, abur cubur... Karışık ama keyfim yerinde.", 
        "Sadece o an çalışacağım kitap ve kalemim var. Her şey milimetrik.", 
        "Düzenlidir ama aşırıya kaçmam, ihtiyacım olan yanımda."
    ],
    key="s2", label_visibility="collapsed"
)
if "geriyor" in s2: scores["Panik Pilotu"] += 1
elif "keyfim" in s2: scores["Erteleyici Filozof"] += 1
elif "milimetrik" in s2: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 3
st.subheader("3. Deneme sınavındasın, son 15 dakika kaldı. Ne yaparsın?")
s3 = st.radio(
    "Seçim 3:",
    [
        "Elim ayağım titrer, bildiğimi de unuturum.", 
        "Sıkıldım zaten, kalanları sallar çıkarım.", 
        "Hala çözemediğim o zor soruyla uğraşmaya devam ederim.", 
        "Boş bıraktığım kolay soruları tararım, yapabildiğimi yaparım."
    ],
    key="s3", label_visibility="collapsed"
)
if "titrer" in s3: scores["Panik Pilotu"] += 1
elif "sallar" in s3: scores["Erteleyici Filozof"] += 1
elif "devam ederim" in s3: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 4
st.subheader("4. Sabah alarm çaldı ama canın hiç ders çalışmak istemiyor...")
s4 = st.radio(
    "Seçim 4:",
    [
        "Vicdan azabı çekerim ama yataktan da çıkamam, günüm zehir olur.", 
        "Beş dakika daha... diyerek öğleni ederim.", 
        "Programa uymalıyım! Zorla da olsa kalkar masaya otururum.", 
        "Kendime 15 dk 'ayılma süresi' veririm, sonra kahvemi alıp başlarım."
    ],
    key="s4", label_visibility="collapsed"
)
if "Vicdan" in s4: scores["Panik Pilotu"] += 1
elif "öğleni" in s4: scores["Erteleyici Filozof"] += 1
elif "Zorla" in s4: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 5
st.subheader("5. Deneme sonucun kötü geldi. İlk düşüncen?")
s5 = st.radio(
    "Seçim 5:",
    [
        "Ben bu sınavı kazanamayacağım, bittim ben.", 
        "Aman ya, sorular çok saçmaydı zaten.", 
        "Nerede hata yaptım? Her şıkkı tek tek incelemeliyim.", 
        "Hata analizimi yapıp eksik konularımı listeme eklerim."
    ],
    key="s5", label_visibility="collapsed"
)
if "kazanamayacağım" in s5: scores["Panik Pilotu"] += 1
elif "saçmaydı" in s5: scores["Erteleyici Filozof"] += 1
elif "incelemeliyim" in s5: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 6
st.subheader("6. Telefonunla aran nasıl?")
s6 = st.radio(
    "Seçim 6:",
    [
        "Sürekli bildirimlere bakmaktan odaklanamıyorum.", 
        "Ders çalışırken bile elimde, onsuz yapamam.", 
        "Odamda durur ama sessizdedir, molalarda bakarım.", 
        "Ders çalışırken telefon başka odada durur."
    ],
    key="s6", label_visibility="collapsed"
)
if "odaklanamıyorum" in s6: scores["Panik Pilotu"] += 1
elif "onsuz" in s6: scores["Erteleyici Filozof"] += 1
elif "molalarda" in s6: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 7
st.subheader("7. Konu çalışırken nasıl ilerlersin?")
s7 = st.radio(
    "Seçim 7:",
    [
        "Çok hızlı geçerim, hemen soru çözmek isterim ama yapamayınca üzülürüm.", 
        "Bugün çalışmasam mı? Yarın iki katı çalışırım.", 
        "Her detayı ezberlemeye çalışırım, özetin özetini çıkarırım.", 
        "Ana mantığı kavrar, çıkmış sorulara bakarım."
    ],
    key="s7", label_visibility="collapsed"
)
if "üzülürüm" in s7: scores["Panik Pilotu"] += 1
elif "Yarın" in s7: scores["Erteleyici Filozof"] += 1
elif "ezberlemeye" in s7: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 8
st.subheader("8. Arkadaşın senden yüksek not aldı. Ne hissedersin?")
s8 = st.radio(
    "Seçim 8:",
    [
        "Kendimi yetersiz hissederim, moralim çöker.", 
        "Şansı yaver gitmiştir, önemli değil.", 
        "Nasıl benden yüksek alır? Daha fazla çalışmalıyım!", 
        "Tebrik ederim. Onun çalışma yönteminde farklı ne var diye sorarım."
    ],
    key="s8", label_visibility="collapsed"
)
if "yetersiz" in s8: scores["Panik Pilotu"] += 1
elif "Şansı" in s8: scores["Erteleyici Filozof"] += 1
elif "Daha fazla" in s8: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 9
st.subheader("9. Sınavdan önceki gece ne yaparsın?")
s9 = st.radio(
    "Seçim 9:",
    [
        "Uyku tutmaz, sabaha kadar notlara bakarım.", 
        "Dizi izlerim veya oyun oynarım, kafa dağıtırım.", 
        "Son tekrarlarımı yapar, erkenden yatarım.", 
        "Hafif bir yürüyüş yapar, zihnimi boşaltır, vaktinde uyurum."
    ],
    key="s9", label_visibility="collapsed"
)
if "Uyku tutmaz" in s9: scores["Panik Pilotu"] += 1
elif "Dizi" in s9: scores["Erteleyici Filozof"] += 1
elif "Son tekrarlarımı" in s9: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1
st.markdown("---")

# SORU 10
st.subheader("10. Senin için başarının sırrı nedir?")
s10 = st.radio(
    "Seçim 10:",
    [
        "Hata yapmamak. Hata yapmak felakettir.", 
        "Zeki olmak. Zekiysen zaten yaparsın.", 
        "Çok çalışmak. Günde 15 saat çalışmak.", 
        "Süreklilik ve doğru strateji."
    ],
    key="s10", label_visibility="collapsed"
)
if "felakettir" in s10: scores["Panik Pilotu"] += 1
elif "Zeki olmak" in s10: scores["Erteleyici Filozof"] += 1
elif "Çok çalışmak" in s10: scores["Garantici Kaplumbağa"] += 1
else: scores["Stratejik Ninja"] += 1

st.markdown("---")

# --- SONUÇ HESAPLAMA ---

if st.button("Analizimi Göster! 🚀", type="primary"):
    
    # En yüksek puanı alanı bul
    winner = max(scores, key=scores.get)
    
    st.balloons()
    st.success(f"TEST SONUCUN: {winner}")
    
    # Detaylı Açıklamalar
    if winner == "Panik Pilotu":
        st.write("### 🚨 Durum Analizi")
        st.write("Bilgi eksiğin yok ama **özgüven ve sakinlik** eksiğin var. Sınavı bir 'bilgi ölçümü' değil, 'hayat memat meselesi' olarak görüyorsun. Bu kaygı performansını düşürüyor.")
        st.info("**Tavsiyem:** Her sabah 5 dk nefes egzersizi yap. Denemelerde turlama tekniğini mutlaka kullan.")

    elif winner == "Erteleyici Filozof":
        st.write("### 🐢 Durum Analizi")
        st.write("Potansiyelin çok yüksek, zekisin ama **disiplin** sorunun var. 'Sonra yaparım', 'Hallederim' diyerek kendini kandırıyorsun. Konfor alanın senin en büyük düşmanın.")
        st.info("**Tavsiyem:** Pomodoro tekniği (25 dk ders + 5 dk mola) tam sana göre. Telefonu odadan çıkar.")

    elif winner == "Garantici Kaplumbağa":
        st.write("### 🐢 Durum Analizi")
        st.write("Mükemmeliyetçisin. Her şeyi en ince ayrıntısına kadar bilmek istiyorsun. Ancak sınav bir **hız testidir**. Bir soruyla 5 dakika inatlaşmak sana kaybettirir.")
        st.info("**Tavsiyem:** 'Boş bırakma sanatı'nı öğrenmelisin. Yapamadığın soruya işaret koy ve geç. Geri dönünce çözeceksin.")

    else:
        st.write("### 🥷 Durum Analizi")
        st.write("Tebrikler! Sen tam bir **Sınav Ninjasısın**. Duygularını değil mantığını kullanıyorsun. Zamanı yönetiyor, hatalarından ders çıkarıyorsun.")
        st.info("**Tavsiyem:** Bu disiplini bozma. Artık hızlanmaya ve derece yapmaya odaklanabilirsin.")