import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Öğrenci Performans Analizi", page_icon="📊", layout="wide")

# --- YAN MENÜ (KİMLİK BİLGİLERİ) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3407/3407024.png", width=100)
    st.header("Öğrenci Bilgileri")
    ad_soyad = st.text_input("Adın Soyadın:", placeholder="Örn: Ali Yılmaz")
    sinif = st.selectbox("Sınıfın:", ["12. Sınıf (YKS)", "11. Sınıf", "Mezun", "Diğer"])
    st.info("💡 Bu test, rehberlik servisi tarafından çalışma alışkanlıklarını analiz etmek için hazırlanmıştır.")

# --- ANA BAŞLIK ---
st.title("🎓 Akademik Performans ve Alışkanlık Envanteri")
st.markdown(f"""
Merhaba **{ad_soyad if ad_soyad else 'Öğrenci'}**! 
Bu analiz senin **Odaklanma**, **Strateji** ve **Psikolojik Sağlamlık** düzeyini ölçmek için tasarlandı.
Lütfen aşağıdaki 17 soruyu en dürüst halinle cevapla.
""")
st.divider()

# PUAN DEĞİŞKENLERİ (Başlangıç 0)
score_focus = 0      # Odak & Teknoloji
score_strategy = 0   # Teknik & Planlama
score_resilience = 0 # Psikoloji & Kaygı

# --- BÖLÜM 1: ODAKLANMA VE DİJİTAL ALIŞKANLIKLAR ---
st.header("📱 Bölüm 1: Odaklanma ve Ekran Yönetimi")

q1 = st.radio("1. Ders çalışırken telefonun nerede durur?", 
     ["Elimin altında, masada.", "Odamda ama sessizde.", "Başka bir odada / kapalı."], key="q1")
if q1 == "Başka bir odada / kapalı.": score_focus += 3
elif q1 == "Odamda ama sessizde.": score_focus += 2
else: score_focus += 0

q2 = st.radio("2. Günlük ortalama ekran süren (Instagram, TikTok, Oyun vb.) ne kadar?", 
     ["4 saatten fazla.", "2-4 saat arası.", "2 saatten az."], key="q2")
if q2 == "2 saatten az.": score_focus += 3
elif q2 == "2-4 saat arası.": score_focus += 1
else: score_focus += 0

q3 = st.radio("3. Masaya oturduğunda 'derin odaklanmaya' geçmen ne kadar sürer?", 
     ["Sürekli kalkarım, bir türlü odaklanamam.", "15-20 dk oyalanırım sonra başlarım.", "Hemen başlarım ve en az 40 dk kalkmam."], key="q3")
if q3 == "Hemen başlarım ve en az 40 dk kalkmam.": score_focus += 3
elif q3 == "15-20 dk oyalanırım sonra başlarım.": score_focus += 1
else: score_focus += 0

q4 = st.radio("4. Müzikle ders çalışma alışkanlığın nasıldır?", 
     ["Sözlü, hareketli müzikler dinlerim.", "Sadece enstrümantal/sözsüz müzik dinlerim.", "Tam sessizlikte çalışırım."], key="q4")
if q4 == "Tam sessizlikte çalışırım.": score_focus += 3
elif q4 == "Sadece enstrümantal/sözsüz müzik dinlerim.": score_focus += 2
else: score_focus += 0

q5 = st.radio("5. Bir paragraf sorusu veya uzun metin okurken dikkatin dağılır mı?", 
     ["Evet, başa dönüp tekrar okurum.", "Bazen dalıp giderim.", "Genelde tek seferde anlarım."], key="q5")
if q5 == "Genelde tek seferde anlarım.": score_focus += 3
elif q5 == "Bazen dalıp giderim.": score_focus += 1
else: score_focus += 0

st.divider()

# --- BÖLÜM 2: AKADEMİK STRATEJİ VE TEKNİK ---
st.header("📝 Bölüm 2: Çalışma Stratejileri ve Teknik")

q6 = st.radio("6. Haftalık veya günlük çalışma planı yapar mısın?", 
     ["Hayır, kafama göre çalışırım.", "Yaparım ama genelde uymam.", "Yazılı planım vardır ve %80 uyarım."], key="q6")
if q6 == "Yazılı planım vardır ve %80 uyarım.": score_strategy += 3
elif q6 == "Yaparım ama genelde uymam.": score_strategy += 1
else: score_strategy += 0

q7 = st.radio("7. Deneme sınavından sonra yanlışlarına ne zaman bakarsın?", 
     ["Bakmam, sadece netimi hesaplar geçerim.", "Birkaç gün sonra bakarım.", "Aynı gün mutlaka analiz ederim."], key="q7")
if q7 == "Aynı gün mutlaka analiz ederim.": score_strategy += 3
elif q7 == "Birkaç gün sonra bakarım.": score_strategy += 1
else: score_strategy += 0

q8 = st.radio("8. Zorlandığın bir dersi (Örn: Matematik) çalışma sıklığın nedir?", 
     ["O dersten kaçarım, en sona bırakırım.", "Haftada 1-2 kez bakarım.", "Her gün az da olsa o derse vakit ayırırım."], key="q8")
if q8 == "Her gün az da olsa o derse vakit ayırırım.": score_strategy += 3
elif q8 == "Haftada 1-2 kez bakarım.": score_strategy += 1
else: score_strategy += 0

q9 = st.radio("9. Sınavda 'Turlama Tekniği'ni (yapamadığını geçip sonra dönme) uygular mısın?", 
     ["Hayır, sırayla giderim inatlaşırım.", "Bazen denerim.", "Evet, asla bir soruyla 2 dakikadan fazla uğraşmam."], key="q9")
if q9 == "Evet, asla bir soruyla 2 dakikadan fazla uğraşmam.": score_strategy += 3
elif q9 == "Bazen denerim.": score_strategy += 1
else: score_strategy += 0

q10 = st.radio("10. Konu çalışırken nasıl not tutarsın?", 
     ["Kitabın altını çizerim sadece.", "Hocanın her dediğini yazarım.", "Kendi cümlelerimle özet çıkarır/zihin haritası yaparım."], key="q10")
if q10 == "Kendi cümlelerimle özet çıkarır/zihin haritası yaparım.": score_strategy += 3
elif q10 == "Hocanın her dediğini yazarım.": score_strategy += 2
else: score_strategy += 1

q11 = st.radio("11. Tekrar yapma düzenin nasıldır?", 
     ["Sadece sınavdan önce çalışırım.", "Sıkılınca eski konulara bakarım.", "Günlük/Haftalık/Aylık periyodik tekrarlarım vardır."], key="q11")
if q11 == "Günlük/Haftalık/Aylık periyodik tekrarlarım vardır.": score_strategy += 3
elif q11 == "Sıkılınca eski konulara bakarım.": score_strategy += 1
else: score_strategy += 0

st.divider()

# --- BÖLÜM 3: PSİKOLOJİK SAĞLAMLIK VE KAYGI ---
st.header("🧠 Bölüm 3: Sınav Psikolojisi ve Kaygı")

q12 = st.radio("12. Deneme sınavı sabahı veya sınav anında fiziksel belirtilerin olur mu?", 
     ["Midem bulanır, ellerim titrer, kalp çarpıntım olur.", "Biraz heyecanlanırım ama yönetebilirim.", "Gayet sakin girerim."], key="q12")
if q12 == "Gayet sakin girerim.": score_resilience += 3
elif q12 == "Biraz heyecanlanırım ama yönetebilirim.": score_resilience += 2
else: score_resilience += 0

q13 = st.radio("13. Başarısız olduğunda (düşük net geldiğinde) iç sesin ne der?", 
     ["'Ben aptalım, yapamayacağım.'", "'Bu sefer olmadı ama hallederiz.'", "'Nerede hata yaptım? Bunu düzeltmeliyim.'"], key="q13")
if q13 == "'Nerede hata yaptım? Bunu düzeltmeliyim.'": score_resilience += 3
elif q13 == "'Bu sefer olmadı ama hallederiz.'": score_resilience += 2
else: score_resilience += 0

q14 = st.radio("14. Uyku düzenin nasıldır?", 
     ["Çok düzensiz, bazen sabahlarım.", "Geç yatarım (02:00 gibi) ama uyurum.", "Düzenlidir, en geç 24:00'te yatarım."], key="q14")
if q14 == "Düzenlidir, en geç 24:00'te yatarım.": score_resilience += 3
elif q14 == "Geç yatarım (02:00 gibi) ama uyurum.": score_resilience += 1
else: score_resilience += 0

q15 = st.radio("15. Ailenin veya çevrenin beklentisi seni nasıl etkiliyor?", 
     ["Baskı altında eziliyorum, yapamazsam mahvolurum.", "Umursamamaya çalışıyorum.", "Onlar için değil kendim için çalışıyorum."], key="q15")
if q15 == "Onlar için değil kendim için çalışıyorum.": score_resilience += 3
elif q15 == "Umursamamaya çalışıyorum.": score_resilience += 2
else: score_resilience += 0

q16 = st.radio("16. Sınav yaklaştıkça çalışma isteğin ne durumda?", 
     ["Korkudan kitleniyorum, çalışamıyorum.", "Bıktım artık, bitsin istiyorum.", "Hedefime yaklaşıyorum, gaza basıyorum."], key="q16")
if q16 == "Hedefime yaklaşıyorum, gaza basıyorum.": score_resilience += 3
elif q16 == "Bıktım artık, bitsin istiyorum.": score_resilience += 1
else: score_resilience += 0

q17 = st.radio("17. Arkadaşlarınla kendini kıyaslar mısın?", 
     ["Sürekli. Onlar benden iyi diye üzülürüm.", "Bazen aklıma takılır.", "Hayır, herkesin süreci farklıdır."], key="q17")
if q17 == "Hayır, herkesin süreci farklıdır.": score_resilience += 3
elif q17 == "Bazen aklıma takılır.": score_resilience += 2
else: score_resilience += 0

st.markdown("---")

# --- HESAPLAMA VE SONUÇ EKRANI ---

if st.button("📊 Analizimi Oluştur", type="primary"):
    
    # Skorları Yüzdeye Çevirme
    # Focus: 5 soru * 3 puan = 15
    # Strategy: 6 soru * 3 puan = 18
    # Resilience: 6 soru * 3 puan = 18
    
    perc_focus = int((score_focus / 15) * 100)
    perc_strategy = int((score_strategy / 18) * 100)
    perc_resilience = int((score_resilience / 18) * 100)
    
    avg_score = int((perc_focus + perc_strategy + perc_resilience) / 3)

    st.success("Analiz Tamamlandı! Aşağıdaki sonuçlarını incele.")
    
    # 1. GENEL DURUM
    col1, col2, col3 = st.columns(3)
    col1.metric("Odaklanma Puanın", f"%{perc_focus}")
    col2.metric("Strateji Puanın", f"%{perc_strategy}")
    col3.metric("Psikolojik Sağlamlık", f"%{perc_resilience}")
    
    st.progress(avg_score, text=f"Genel Hazırbulunuşluk Seviyesi: %{avg_score}")

    # 2. DETAYLI YORUMLAR (Görselleştirilmiş)
    
    with st.expander("🔍 ODAK VE EKRAN ANALİZİ (Detay İçin Tıkla)", expanded=True):
        if perc_focus < 50:
            st.error("🚨 **Durum: KIRMIZI ALARM!**")
            st.write("Dijital dünya seni esir almış. Dikkat süren çok kısalmış. Bu şekilde masada 3 saat otursan da verimin 30 dakika.")
            st.markdown("**Öneriler:**\n* Telefonu odadan çıkar.\n* 'Forest' uygulamasını indir.\n* 25 dk ders + 5 dk mola (Pomodoro) ile başla.")
        elif perc_focus < 80:
            st.warning("⚠️ **Durum: GELİŞTİRİLMELİ**")
            st.write("Dikkatin fena değil ama dış uyaranlara (bildirim, ses) karşı hassassın.")
            st.markdown("**Öneriler:**\n* Bildirimleri kapat.\n* Çalışırken masanda sadece ders materyali olsun.")
        else:
            st.success("✅ **Durum: MÜKEMMEL**")
            st.write("Odaklanma sorunun yok. Derin çalışmayı biliyorsun. Aynen devam!")

    with st.expander("📈 STRATEJİ VE TEKNİK ANALİZİ (Detay İçin Tıkla)"):
        if perc_strategy < 50:
            st.error("🚨 **Durum: ROTASIZ GEMİ**")
            st.write("Çok çalışıyor olabilirsin ama 'yanlış' çalışıyorsun. Planın yok, tekrarların eksik.")
            st.markdown("**Öneriler:**\n* Rehberlik servisine gel, birlikte program yapalım.\n* Hata Defteri tutmaya bugün başla.\n* Turlama tekniğini öğren.")
        elif perc_strategy < 80:
            st.warning("⚠️ **Durum: İYİ AMA EKSİKLER VAR**")
            st.write("Doğru yoldasın ama süreklilik sorunun var. Bazen planı aksatıyorsun.")
            st.markdown("**Öneriler:**\n* Pazar akşamları haftalık planını gözden geçir.\n* Zorlandığın dersin üstüne git.")
        else:
            st.success("✅ **Durum: PROFESYONEL ÖĞRENCİ**")
            st.write("Nasıl ders çalışılacağını çözmüşsün. Artık sadece bol deneme çözerek hızlanmaya odaklan.")

    with st.expander("🧠 PSİKOLOJİK SAĞLAMLIK ANALİZİ (Detay İçin Tıkla)"):
        if perc_resilience < 50:
            st.error("🚨 **Durum: YÜKSEK KAYGI**")
            st.write("Bilgi eksiğin olmasa bile bu kaygı seni sınavda kilitler. Kendine çok acımasız davranıyorsun.")
            st.markdown("**Öneriler:**\n* Kendini başkalarıyla kıyaslamayı bırak.\n* Nefes egzersizleri yap.\n* 'Ben elimden geleni yapıyorum' cümlesini tekrarla.")
        else:
            st.success("✅ **Durum: ZİHİNSEL OLARAK HAZIRSIN**")
            st.write("Sınavı bir ölüm kalım meselesi yapmaman harika. Bu soğukkanlılık sana sınav kazandıracak.")

    st.info(f"Rapor Tarihi: {st.date_input('Tarih').strftime('%d/%m/%Y')} | Rehber Öğretmen Değerlendirmesi")