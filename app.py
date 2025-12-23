import streamlit as st
import pandas as pd
import plotly.express as px # Grafik kütüphanesi
from datetime import datetime

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Rehberlik Gelişim Sistemi", page_icon="🎓", layout="wide")

# --- YORUM VE ÖNERİ FONKSİYONU ---
def get_feedback(score, category):
    feedback = {}
    
    # 1. ODAK VE EKRAN YÖNETİMİ
    if category == "Odak":
        if score < 50:
            feedback["durum"] = "🔴 DİJİTAL KAOS: Acil Müdahale Gerekli"
            feedback["yorum"] = """Dijital dünya seni esir almış durumda. Masaya otursan bile zihnin sürekli bildirimlerde. 
            Bu dikkat dağınıklığıyla potansiyelinin sadece %20'sini kullanabiliyorsun."""
            feedback["oneri"] = [
                "**Dijital Detoks:** Çalışırken telefonunu mutlaka başka bir odaya bırak.",
                "**Forest Uygulaması:** Telefona dokunmamanı sağlayan bu uygulamayı indir.",
                "**Pomodoro:** 25 dk ders + 5 dk mola kuralını uygula."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 GELİŞTİRİLMELİ: Dikkat Kaçakları Var"
            feedback["yorum"] = """Fena gitmiyorsun ama dış uyaranlara karşı hassassın. Odaklanma süren henüz bir sınav süresi kadar uzun değil. 
            40. dakikadan sonra kopuşlar yaşıyorsun."""
            feedback["oneri"] = [
                "**Süre Uzatma:** Odaklanma süreni artırmak için çalışma bloklarını 40-50 dakikaya çıkar.",
                "**Masa Düzeni:** Masanda ders materyali dışında hiçbir şey bulundurma."
            ]
        else:
            feedback["durum"] = "🟢 MÜKEMMEL: Derin Odaklanma Ustası"
            feedback["yorum"] = """Harika bir disiplinin var. 'Flow' (akış) durumuna geçebiliyorsun. 
            Bu odaklanma gücü sana sınavı kazandıracak en büyük silahın."""
            feedback["oneri"] = [
                "**Zor Sorular:** Bu yüksek odak gücünü, en zorlandığın dersin konularını halletmek için kullan.",
                "**Bu Düzeni Bozma:** Sınav anında dikkatin dağılsa bile kendini hemen toparlayabilirsin."
            ]

    # 2. STRATEJİ VE TEKNİK
    elif category == "Strateji":
        if score < 50:
            feedback["durum"] = "🔴 ROTASIZ GEMİ: Verimsiz Çalışma"
            feedback["yorum"] = """Çok çalışıyor olabilirsin ama 'yanlış' çalışıyorsun. Plansızsın, tekrarların eksik. 
            Bu şekilde yerinde sayarsın."""
            feedback["oneri"] = [
                "**Hata Defteri:** Yapamadığın sorulardan bir defter oluştur.",
                "**Haftalık Plan:** Pazar akşamı haftalık programını yazılı olarak yap.",
                "**Soru Çöz:** Sadece konu okumak çalışma değildir. Kalemi eline al."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 İYİ AMA EKSİK: Taktiksel Hatalar"
            feedback["yorum"] = """Genel hatlarıyla doğrusun ama detaylarda kaçırıyorsun. Bazen planı aksatıyor, bazen zor derslerden kaçıyorsun. 
            Turlama tekniğini tam oturtamamışsın."""
            feedback["oneri"] = [
                "**Turlama Tekniği:** Bir soruyla 2 dakikadan fazla inatlaşmayı bırak.",
                "**Nokta Atışı:** Bildiğin konuları değil, bilmediğin konuları çalış."
            ]
        else:
            feedback["durum"] = "🟢 PROFESYONEL ÖĞRENCİ: Doğru Strateji"
            feedback["yorum"] = """Sınavın bir bilgi değil, strateji sınavı olduğunu çözmüşsün. Yanlış analizlerin ve planlaman harika. 
            Sen bu işi biliyorsun."""
            feedback["oneri"] = [
                "**Hızlanma:** Artık süre tutarak branş denemeleri çöz.",
                "**MEB Kitapları:** Detaylarda boğulmamak için MEB kitaplarını tara."
            ]

    # 3. PSİKOLOJİK SAĞLAMLIK
    elif category == "Psikoloji":
        if score < 50:
            feedback["durum"] = "🔴 YÜKSEK KAYGI: Performans Blokajı"
            feedback["yorum"] = """Bilgi eksiğin olmasa bile bu kaygı seviyesi seni kilitliyor. Sınavı bir 'ölüm-kalım' meselesi haline getirmişsin. 
            Kendine çok acımasız davranıyorsun."""
            feedback["oneri"] = [
                "**Nefes Egzersizi:** Panikleyince 4 saniye al, 4 saniye tut, 8 saniye ver.",
                "**Kıyaslamayı Bırak:** Başkalarının netleri seni ilgilendirmez.",
                "**Uyku:** Gece 12'den önce yatakta ol."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 YÖNETİLEBİLİR STRES: Heyecan Var"
            feedback["yorum"] = """Belli bir düzeyde heyecan normaldir. Ancak zor sorularda moralin çabuk bozulabiliyor. 
            'Yapamayacağım' düşüncesi ara ara seni yokluyor."""
            feedback["oneri"] = [
                "**Olumlu İç Konuşma:** 'Yapamıyorum' yerine 'Şu an zorlanıyorum ama öğrenebilirim' de.",
                "**Mola Yönetimi:** Çalışırken bunaldığında 5 dakika temiz hava al."
            ]
        else:
            feedback["durum"] = "🟢 ÇELİK GİBİ SİNİRLER: Sınav Savaşçısı"
            feedback["yorum"] = """Süreci çok olgun karşılıyorsun. Başarısızlığı bir son değil, öğrenme fırsatı olarak görüyorsun. 
            Bu soğukkanlılık sana +10 net kazandırır."""
            feedback["oneri"] = [
                "**Mentorluk:** Bu sakinliğini panik yapan arkadaşlarına destek olarak kullanabilirsin."
            ]

    # 4. HEDEF VE MOTİVASYON
    elif category == "Hedef":
        if score < 50:
            feedback["durum"] = "🔴 BELİRSİZLİK: Yakıtın Bitiyor"
            feedback["yorum"] = """Neden çalıştığını tam bilmiyorsun. 'Mecburum' diyerek çalışıyorsun. 
            İçsel motivasyonun olmadığı için masa başına oturmak işkence gibi geliyor."""
            feedback["oneri"] = [
                "**Görselleştirme:** İstediğin üniversitenin kampüsünü izle.",
                "**Hedef Panosu:** Masana seni heyecanlandıran bir görsel as."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 BULANIK HEDEF: Biraz Daha Netlik"
            feedback["yorum"] = """Bir hedefin var ama ona ne kadar tutkulusun? Zorluk görünce vazgeçme eğilimin var. 
            Hedefini biraz daha somutlaştırmamız lazım."""
            feedback["oneri"] = [
                "**B Planı Yok:** Aklındaki o hedefe odaklan.",
                "**Netleştir:** 'İyi bir yer olsun' değil, 'X Üniversitesi Y Bölümü' şeklinde hedefini netleştir."
            ]
        else:
            feedback["durum"] = "🟢 GÖREV ADAMI: Yüksek Motivasyon"
            feedback["yorum"] = """Gözünü hedefe dikmişsin ve hiçbir engel seni durduramaz. 
            Sabah seni yataktan kaldıran o tutkuya sahipsin."""
            feedback["oneri"] = [
                "**İlham Ol:** Motivasyonunu korumak için başarı hikayeleri oku."
            ]
            
    return feedback

# --- YAN MENÜ (Sadece Öğrenci) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3407/3407024.png", width=120)
    st.header("Öğrenci Bilgileri")
    ad_soyad = st.text_input("Adın Soyadın:", placeholder="Örn: Ali Yılmaz")
    sinif = st.selectbox("Sınıfın:", ["Seçiniz...", "6. Sınıf", "7. Sınıf", "8. Sınıf (LGS)", "9. Sınıf", "10. Sınıf", "11. Sınıf", "12. Sınıf (YKS)", "Mezun"])
    st.info("💡 Soruları dürüstçe cevapla, sistem sana özel bir karne çıkarsın.")

# --- ANA GÖVDE ---
if sinif != "Seçiniz..." and ad_soyad:
    st.title(f"📊 {ad_soyad} - Kapsamlı Gelişim Analizi")
    st.markdown("Aşağıdaki **4 Ana Başlıktaki** soruları cevapla, analizini hemen gör.")
    
    # Skor değişkenleri
    scores = {"Odak": 0, "Strateji": 0, "Psikoloji": 0, "Hedef": 0}

    # BÖLÜM 1: ODAK
    st.header("📱 1. Odak ve Ekran Yönetimi")
    c1, c2 = st.columns(2)
    with c1:
        q1 = st.radio("Ders çalışırken telefonun nerede durur?", ["Elimin altında/Masada", "Sessizde/Uçak modunda", "Başka bir odada"], key="q1")
        if q1 == "Başka bir odada": scores["Odak"] += 5
        elif q1 == "Sessizde/Uçak modunda": scores["Odak"] += 3
        
        q2 = st.radio("Günlük ortalama ekran süren (Oyun/Sosyal Medya)?", ["4 saatten fazla", "2-4 saat arası", "2 saatten az"], key="q2")
        if q2 == "2 saatten az": scores["Odak"] += 5
        elif q2 == "2-4 saat arası": scores["Odak"] += 3
    with c2:
        q3 = st.radio("Masa başında kesintisiz ne kadar odaklanabiliyorsun?", ["Sürekli bölünüyorum", "20-30 dakika", "40 dakika ve üzeri"], key="q3")
        if q3 == "40 dakika ve üzeri": scores["Odak"] += 5
        elif q3 == "20-30 dakika": scores["Odak"] += 3

    st.divider()

    # BÖLÜM 2: STRATEJİ
    st.header("📝 2. Akademik Strateji")
    c3, c4 = st.columns(2)
    with c3:
        q4 = st.radio("Haftalık çalışma planın var mı?", ["Yok veya uymuyorum", "Kafamda var", "Yazılı planım var ve uyarım"], key="q4")
        if q4 == "Yazılı planım var ve uyarım": scores["Strateji"] += 5
        elif q4 == "Kafamda var": scores["Strateji"] += 3
        
        q5 = st.radio("Deneme/Test yanlışlarına ne zaman bakarsın?", ["Bakmam/Nadiren", "Sonra bakarım", "Aynı gün mutlaka analiz ederim"], key="q5")
        if q5 == "Aynı gün mutlaka analiz ederim": scores["Strateji"] += 5
        elif q5 == "Sonra bakarım": scores["Strateji"] += 3
    with c4:
        q6 = st.radio("Sınavda Turlama Tekniği (Yapamadığını geçme) kullanır mısın?", ["Hayır, inatlaşırım", "Bazen denerim", "Evet, takılınca hemen geçerim"], key="q6")
        if q6 == "Evet, takılınca hemen geçerim": scores["Strateji"] += 5
        elif q6 == "Bazen denerim": scores["Strateji"] += 3

    st.divider()

    # BÖLÜM 3: PSİKOLOJİ
    st.header("🧠 3. Psikolojik Sağlamlık")
    c5, c6 = st.columns(2)
    with c5:
        q7 = st.radio("Sınav anında fiziksel stres belirtin olur mu?", ["Elim ayağım titrer/Mide bulantısı", "Biraz heyecanlanırım", "Sakiniyimdir"], key="q7")
        if q7 == "Sakiniyimdir": scores["Psikoloji"] += 5
        elif q7 == "Biraz heyecanlanırım": scores["Psikoloji"] += 3
        
        q8 = st.radio("Başarısız olduğunda ilk tepkin ne olur?", ["Kendime kızarım/Bırakırım", "Üzülürüm ama devam ederim", "Hatamı ararım ve ders çıkarırım"], key="q8")
        if q8 == "Hatamı ararım ve ders çıkarırım": scores["Psikoloji"] += 5
        elif q8 == "Üzülürüm ama devam ederim": scores["Psikoloji"] += 3
    with c6:
        q9 = st.radio("Uyku düzenin nasıldır?", ["Çok düzensiz/Sabahlarım", "Geç yatarım (01:00 sonrası)", "Düzenlidir (24:00 öncesi)"], key="q9")
        if q9 == "Düzenlidir (24:00 öncesi)": scores["Psikoloji"] += 5
        elif q9 == "Geç yatarım (01:00 sonrası)": scores["Psikoloji"] += 3

    st.divider()

    # BÖLÜM 4: HEDEF
    st.header("🎯 4. Hedef ve Motivasyon")
    c7, c8 = st.columns(2)
    with c7:
        q10 = st.radio("Temel çalışma motivasyonun nedir?", ["Aile baskısı/Mecburiyet", "Gelecek kaygısı/İyi bir iş", "Hayalimdeki mesleğe olan tutkum"], key="q10")
        if q10 == "Hayalimdeki mesleğe olan tutkum": scores["Hedef"] += 5
        elif q10 == "Gelecek kaygısı/İyi bir iş": scores["Hedef"] += 3
        
        q11 = st.radio("Hedefin ne kadar net?", ["Bilmiyorum/Kararsızım", "Puanım nereye yeterse", "Üniversite ve bölümüm net"], key="q11")
        if q11 == "Üniversite ve bölümüm net": scores["Hedef"] += 5
        elif q11 == "Puanım nereye yeterse": scores["Hedef"] += 3
    with c8:
        q12 = st.radio("Sabah seni yataktan kaldıran güç nedir?", ["Alarmın sesi/Okul saati", "Zorunluluk hissi", "Hedefime ulaşma isteği"], key="q12")
        if q12 == "Hedefime ulaşma isteği": scores["Hedef"] += 5
        elif q12 == "Zorunluluk hissi": scores["Hedef"] += 3

    st.markdown("---")

    if st.button("Raporumu Oluştur ve Analiz Et 🚀", type="primary"):
        
        # Puan Hesaplama
        results = {k: int((v/15)*100) for k, v in scores.items()}
        avg_score = sum(results.values()) // 4
        
        st.balloons()
        
        # --- SONUÇ EKRANI ---
        st.success(f"Tebrikler {ad_soyad}! Analizin tamamlandı. İşte sonuçların:")
        
        # Grafik için veriyi hazırlıyoruz
        df_radar = pd.DataFrame(dict(
            r=list(results.values()),
            theta=list(results.keys())
        ))
        
        fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, range_r=[0,100])
        fig.update_traces(fill='toself', line_color='#FF4B4B') 
        fig.update_layout(title_text="Kişisel Performans Haritan", title_x=0.3)
        
        col_g1, col_g2 = st.columns([1, 2])
        with col_g1:
            st.metric("Genel Hazırbulunuşluk", f"%{avg_score}")
            st.progress(avg_score)
            if avg_score < 50: 
                st.error("Durum: KRİTİK SEVİYE")
            elif avg_score < 80: 
                st.warning("Durum: GELİŞİME AÇIK")
            else: 
                st.success("Durum: HARİKA")
            
        with col_g2:
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📋 Detaylı Karne ve Reçeteler")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📱 Odak", "📝 Strateji", "🧠 Psikoloji", "🎯 Hedef"])
        
        with tab1:
            f = get_feedback(results["Odak"], "Odak")
            st.subheader(f"{f['durum']}")
            st.write(f['yorum'])
            st.warning("🚀 **Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")
            
        with tab2:
            f = get_feedback(results["Strateji"], "Strateji")
            st.subheader(f"{f['durum']}")
            st.write(f['yorum'])
            st.warning("🚀 **Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")

        with tab3:
            f = get_feedback(results["Psikoloji"], "Psikoloji")
            st.subheader(f"{f['durum']}")
            st.write(f['yorum'])
            st.warning("🚀 **Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")

        with tab4:
            f = get_feedback(results["Hedef"], "Hedef")
            st.subheader(f"{f['durum']}")
            st.write(f['yorum'])
            st.warning("🚀 **Senin İçin Aksiyon Planı:**")
            for item in f['oneri']: st.markdown(f"- {item}")

else:
    st.warning("⬅️ Lütfen teste başlamak için sol taraftan Adını ve Sınıfını gir.")