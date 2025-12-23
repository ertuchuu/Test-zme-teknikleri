import streamlit as st
import pandas as pd
import plotly.express as px # Grafik kütüphanesi
import os
from datetime import datetime

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Rehberlik Gelişim Karnesi", page_icon="🎓", layout="wide")

# --- VERİ KAYDETME FONKSİYONU ---
def save_data(data):
    file_name = "ogrenci_sonuclar.csv"
    if not os.path.isfile(file_name):
        df = pd.DataFrame(columns=data.keys())
        df.to_csv(file_name, index=False, encoding="utf-8-sig")
    df_new = pd.DataFrame([data])
    df_new.to_csv(file_name, mode='a', header=False, index=False, encoding="utf-8-sig")

# --- YORUM VE ÖNERİ FONKSİYONU ---
def get_feedback(score, category):
    feedback = {}
    
    # 1. ODAK VE EKRAN YÖNETİMİ
    if category == "Odak":
        if score < 50:
            feedback["durum"] = "🔴 DİJİTAL KAOS: Acil Müdahale Gerekli"
            feedback["yorum"] = "Dijital dünya seni esir almış durumda. Masaya otursan bile zihnin sürekli bildirimlerde veya oyunlarda. Bu dikkat dağınıklığıyla potansiyelinin sadece %20'sini kullanabiliyorsun."
            feedback["oneri"] = [
                "**Dijital Detoks:** Çalışırken telefonunu mutlaka başka bir odaya bırak.",
                "**Pomodoro Tekniği:** 25 dk ders + 5 dk mola kuralını uygula. 25 dakika boyunca dünyayla bağlantını kes.",
                "**Forest Uygulaması:** Telefona dokunmamanı sağlayan bu uygulamayı indir."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 GELİŞTİRİLMELİ: Dikkat Kaçakları Var"
            feedback["yorum"] = "Fena gitmiyorsun ama dış uyaranlara karşı hala hassassın. Odaklanma süren sınav süresi kadar uzun değil. 40. dakikadan sonra kopuşlar yaşıyorsun."
            feedback["oneri"] = [
                "**Blok Çalışma:** Odaklanma süreni artırmak için çalışma sürelerini kademeli olarak 40-50 dakikaya çıkar.",
                "**Masa Düzeni:** Masanda ders materyali dışında hiçbir şey (kalemlik, süs vb.) bulundurma."
            ]
        else:
            feedback["durum"] = "🟢 MÜKEMMEL: Derin Odaklanma Ustası"
            feedback["yorum"] = "Harika bir disiplinin var. 'Flow' (akış) durumuna geçebiliyorsun. Bu odaklanma gücü sana sınavı kazandıracak en büyük silahın."
            feedback["oneri"] = [
                "**Aynen Devam:** Bu düzeni bozma.",
                "**Zor Sorular:** Bu yüksek odak gücünü, en zorlandığın dersin en karmaşık konularını halletmek için kullan."
            ]

    # 2. STRATEJİ VE TEKNİK
    elif category == "Strateji":
        if score < 50:
            feedback["durum"] = "🔴 ROTASIZ GEMİ: Verimsiz Çalışma"
            feedback["yorum"] = "Çok çalışıyor olabilirsin ama 'yanlış' çalışıyorsun. Plansızsın, tekrarların eksik ve yanlışlarınla yüzleşmiyorsun. Bu şekilde patinaj çekersin."
            feedback["oneri"] = [
                "**Hata Defteri:** Bugünden itibaren kestiğin yapamadığın sorulardan bir defter oluştur.",
                "**Haftalık Plan:** Pazar akşamı oturup haftalık programını yazılı olarak yap.",
                "**Konu/Soru Dengesi:** Sadece konu okuma, kalemi eline al ve soru çöz."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 İYİ AMA EKSİK: Taktiksel Hatalar"
            feedback["yorum"] = "Genel hatlarıyla doğrusun ama detaylarda kaçırıyorsun. Bazen planı aksatıyor, bazen zor derslerden kaçıyorsun. Turlama tekniğini tam oturtamamışsın."
            feedback["oneri"] = [
                "**Turlama Tekniği:** Denemelerde bir soruyla 2 dakikadan fazla inatlaşmayı bırak.",
                "**Nokta Atışı:** Bildiğin konuları tekrar çalışmayı bırak, bilmediğin o gıcık konunun üzerine git."
            ]
        else:
            feedback["durum"] = "🟢 PROFESYONEL ÖĞRENCİ: Doğru Strateji"
            feedback["yorum"] = "Sınavın bir bilgi değil, strateji sınavı olduğunu çözmüşsün. Yanlış analizlerin ve planlaman harika."
            feedback["oneri"] = [
                "**Hızlanma:** Artık süre tutarak branş denemeleri çözmeye ağırlık ver.",
                "**MEB Kitapları:** Detaylarda boğulmamak için MEB kitaplarını taramaya başla."
            ]

    # 3. PSİKOLOJİK SAĞLAMLIK
    elif category == "Psikoloji":
        if score < 50:
            feedback["durum"] = "🔴 YÜKSEK KAYGI: Performans Blokajı"
            feedback["yorum"] = "Bilgi eksiğin olmasa bile bu kaygı seviyesi seni kilitliyor. Sınavı bir 'ölüm-kalım' meselesi haline getirmişsin. Kendine çok acımasız davranıyorsun."
            feedback["oneri"] = [
                "**Nefes Egzersizi:** Sınav anında panikleyince 4 saniye al, 4 saniye tut, 8 saniye ver.",
                "**Kıyaslamayı Bırak:** Başkalarının netleri seni ilgilendirmez. Kendi gelişimine odaklan.",
                "**Uyku Düzeni:** Gece 12'den önce yatakta ol."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 YÖNETİLEBİLİR STRES: Heyecan Var"
            feedback["yorum"] = "Belli bir düzeyde heyecan normaldir ve diri tutar. Ancak zor sorularda moralin çabuk bozulabiliyor. 'Yapamayacağım' düşüncesi ara ara seni yokluyor."
            feedback["oneri"] = [
                "**Olumlu İç Konuşma:** 'Yapamıyorum' yerine 'Şu an zorlanıyorum ama öğrenebilirim' de.",
                "**Mola Yönetimi:** Çalışırken bunaldığında 5 dakika temiz hava al."
            ]
        else:
            feedback["durum"] = "🟢 ÇELİK GİBİ SİNİRLER: Sınav Savaşçısı"
            feedback["yorum"] = "Süreci çok olgun karşılıyorsun. Başarısızlığı bir son değil, öğrenme fırsatı olarak görüyorsun. Bu soğukkanlılık sana +10 net kazandırır."
            feedback["oneri"] = [
                "**Mentorluk:** Bu sakinliğini panik yapan arkadaşlarına destek olarak kullanabilirsin, anlatmak sana da iyi gelir."
            ]

    # 4. HEDEF VE MOTİVASYON
    elif category == "Hedef":
        if score < 50:
            feedback["durum"] = "🔴 BELİRSİZLİK: Yakıtın Bitiyor"
            feedback["yorum"] = "Neden çalıştığını tam bilmiyorsun. 'Ailem istiyor' veya 'Mecburum' diyerek çalışıyorsun. İçsel motivasyonun olmadığı için masa başına oturmak işkence gibi geliyor."
            feedback["oneri"] = [
                "**Hedef Panosu:** İstediğin üniversitenin/bölümün fotoğrafını çıktı alıp masana as.",
                "**Araştırma:** Hangi mesleğin seni heyecanlandırdığını bulmak için videolar izle."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 BULANIK HEDEF: Biraz Daha Netlik"
            feedback["yorum"] = "Bir hedefin var ama ona ne kadar tutkulusun? Zorluk görünce vazgeçme eğilimin var. Hedefini biraz daha somutlaştırmamız lazım."
            feedback["oneri"] = [
                "**B Planı Yok:** Aklındaki o hedefe odaklan ve 'olmazsa ne olur' diye düşünme.",
                "**Net Hedefi:** 'İyi bir yer olsun' değil, 'X Üniversitesi Y Bölümü' şeklinde netleştir."
            ]
        else:
            feedback["durum"] = "🟢 GÖREV ADAMI: Yüksek Motivasyon"
            feedback["yorum"] = "Gözünü hedefe dikmişsin ve hiçbir engel seni durduramaz. Sabah seni yataktan kaldıran o tutkuya sahipsin."
            feedback["oneri"] = [
                "**İlham Ol:** Motivasyonunu korumak için başarı hikayeleri okumaya devam et."
            ]
            
    return feedback

# --- YAN MENÜ ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3407/3407024.png", width=100)
    st.header("Öğrenci Girişi")
    ad_soyad = st.text_input("Adın Soyadın:", placeholder="Ad Soyad")
    sinif = st.selectbox("Sınıfın:", ["Seçiniz...", "6. Sınıf", "7. Sınıf", "8. Sınıf (LGS)", "9. Sınıf", "10. Sınıf", "11. Sınıf", "12. Sınıf (YKS)", "Mezun"])
    
    st.markdown("---")
    st.write("🔒 **Öğretmen Paneli**")
    pwd = st.text_input("Şifre", type="password")
    if pwd == "rehberlik123":
        if os.path.isfile("ogrenci_sonuclar.csv"):
            df = pd.read_csv("ogrenci_sonuclar.csv")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("📥 Excel İndir", csv, "sonuclar.csv", "text/csv")
        else:
            st.warning("Veri yok.")

# --- ANA GÖVDE ---
if sinif != "Seçiniz..." and ad_soyad:
    st.title(f"📊 {ad_soyad} - Kapsamlı Gelişim Analizi")
    st.info("Lütfen aşağıdaki soruları en samimi halinle cevapla. Sistem sana özel, detaylı bir rapor hazırlayacak.")
    
    # --- SORULAR (Kısaltılmış kod için mantık aynı, arayüzü temiz tutuyoruz) ---
    # Skor değişkenleri
    scores = {"Odak": 0, "Strateji": 0, "Psikoloji": 0, "Hedef": 0}

    # BÖLÜM 1: ODAK
    st.header("📱 1. Odak ve Ekran Yönetimi")
    c1, c2 = st.columns(2)
    with c1:
        if st.radio("Telefonun nerede?", ["Elimde", "Sessizde", "Başka odada"], key="q1") == "Başka odada": scores["Odak"] += 5
        elif st.session_state.q1 == "Sessizde": scores["Odak"] += 3
        
        if st.radio("Günlük ekran süren?", ["4+ saat", "2-4 saat", "<2 saat"], key="q2") == "<2 saat": scores["Odak"] += 5
        elif st.session_state.q2 == "2-4 saat": scores["Odak"] += 3
    with c2:
        if st.radio("Odaklanma süren?", ["Bölünüyorum", "20-30 dk", "40+ dk"], key="q3") == "40+ dk": scores["Odak"] += 5
        elif st.session_state.q3 == "20-30 dk": scores["Odak"] += 3

    st.divider()

    # BÖLÜM 2: STRATEJİ
    st.header("📝 2. Akademik Strateji")
    c3, c4 = st.columns(2)
    with c3:
        if st.radio("Haftalık plan?", ["Yok", "Kafamda", "Yazılı/Uyarım"], key="q4") == "Yazılı/Uyarım": scores["Strateji"] += 5
        elif st.session_state.q4 == "Kafamda": scores["Strateji"] += 3
        
        if st.radio("Hata analizi?", ["Yapmam", "Sonra", "Aynı gün"], key="q5") == "Aynı gün": scores["Strateji"] += 5
        elif st.session_state.q5 == "Sonra": scores["Strateji"] += 3
    with c4:
        if st.radio("Turlama Tekniği?", ["Hayır", "Bazen", "Evet"], key="q6") == "Evet": scores["Strateji"] += 5
        elif st.session_state.q6 == "Bazen": scores["Strateji"] += 3

    st.divider()

    # BÖLÜM 3: PSİKOLOJİ
    st.header("🧠 3. Psikolojik Sağlamlık")
    c5, c6 = st.columns(2)
    with c5:
        if st.radio("Sınav anı?", ["Panik", "Heyecanlı", "Sakin"], key="q7") == "Sakin": scores["Psikoloji"] += 5
        elif st.session_state.q7 == "Heyecanlı": scores["Psikoloji"] += 3
        
        if st.radio("Başarısızlık tepkisi?", ["Bırakırım", "Üzülürüm", "Analiz ederim"], key="q8") == "Analiz ederim": scores["Psikoloji"] += 5
        elif st.session_state.q8 == "Üzülürüm": scores["Psikoloji"] += 3
    with c6:
        if st.radio("Uyku düzeni?", ["Düzensiz", "Geç yatarım", "Düzenli"], key="q9") == "Düzenli": scores["Psikoloji"] += 5
        elif st.session_state.q9 == "Geç yatarım": scores["Psikoloji"] += 3

    st.divider()

    # BÖLÜM 4: HEDEF
    st.header("🎯 4. Hedef ve Motivasyon")
    c7, c8 = st.columns(2)
    with c7:
        if st.radio("Çalışma sebebin?", ["Aile/Zorunluluk", "Gelecek", "Tutku/Hayal"], key="q10") == "Tutku/Hayal": scores["Hedef"] += 5
        elif st.session_state.q10 == "Gelecek": scores["Hedef"] += 3
        
        if st.radio("Hedef netliği?", ["Yok", "Puanım nereye yeterse", "Net"], key="q11") == "Net": scores["Hedef"] += 5
        elif st.session_state.q11 == "Puanım nereye yeterse": scores["Hedef"] += 3
    with c8:
        if st.radio("Sabah kalkma gücü?", ["Alarm", "Mecburiyet", "İstek"], key="q12") == "İstek": scores["Hedef"] += 5
        elif st.session_state.q12 == "Mecburiyet": scores["Hedef"] += 3

    st.markdown("---")

    if st.button("Raporumu Oluştur 🚀", type="primary"):
        
        # Puan Hesaplama (Basitleştirilmiş max 15 puan üzerinden yüzde)
        results = {k: int((v/15)*100) for k, v in scores.items()}
        avg_score = sum(results.values()) // 4
        
        # Veri Kaydetme
        save_data({"Tarih": datetime.now().strftime("%Y-%m-%d"), "Ad": ad_soyad, "Sınıf": sinif, **results})
        
        st.balloons()
        
        # --- SONUÇ EKRANI BAŞLANGICI ---
        st.header(f"🎓 {ad_soyad} İçin Gelişim Karnesi")
        
        # 1. RADAR GRAFİĞİ (GÖRSEL ŞÖLEN)
        df_radar = pd.DataFrame(dict(
            r=list(results.values()),
            theta=list(results.keys())
        ))
        fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, range_r=[0,100], 
                            title="Performans Dağılım Grafiği")
        fig.update_traces(fill='toself', line_color='#FF4B4B') # Streamlit kırmızısı
        
        col_g1, col_g2 = st.columns([1, 2])
        with col_g1:
            st.metric("Genel Hazırbulunuşluk", f"%{avg_score}")
            st.progress(avg_score)
            if avg_score < 50: st.error("Genel Durum: Kritik Seviye")
            elif avg_score < 80: st.warning("Genel Durum: Gelişime Açık")
            else: st.success("Genel Durum: Harika")
            
        with col_g2:
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📋 Detaylı Analiz ve Reçeteler")
        
        # 2. DETAYLI SEKMELER (TABS)
        tab1, tab2, tab3, tab4 = st.tabs(["📱 Odak Analizi", "📝 Strateji Analizi", "🧠 Psikoloji Analizi", "🎯 Hedef Analizi"])
        
        with tab1:
            f = get_feedback(results["Odak"], "Odak")
            st.subheader(f"Puanın: %{results['Odak']} - {f['durum']}")
            st.write(f['yorum'])
            st.info("**🚀 Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")
            
        with tab2:
            f = get_feedback(results["Strateji"], "Strateji")
            st.subheader(f"Puanın: %{results['Strateji']} - {f['durum']}")
            st.write(f['yorum'])
            st.info("**🚀 Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")

        with tab3:
            f = get_feedback(results["Psikoloji"], "Psikoloji")
            st.subheader(f"Puanın: %{results['Psikoloji']} - {f['durum']}")
            st.write(f['yorum'])
            st.info("**🚀 Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")

        with tab4:
            f = get_feedback(results["Hedef"], "Hedef")
            st.subheader(f"Puanın: %{results['Hedef']} - {f['durum']}")
            st.write(f['yorum'])
            st.info("**🚀 Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")

else:
    st.warning("Lütfen başlamak için sol menüden bilgilerinizi giriniz.")