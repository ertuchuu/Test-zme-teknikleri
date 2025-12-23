import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Rehberlik Analiz Sistemi", page_icon="📈", layout="wide")

# --- VERİ KAYDETME FONKSİYONU ---
def save_data(data):
    file_name = "ogrenci_sonuclar.csv"
    # Eğer dosya yoksa başlıklarla oluştur
    if not os.path.isfile(file_name):
        df = pd.DataFrame(columns=data.keys())
        df.to_csv(file_name, index=False, encoding="utf-8-sig")
    
    # Veriyi ekle
    df_new = pd.DataFrame([data])
    df_new.to_csv(file_name, mode='a', header=False, index=False, encoding="utf-8-sig")

# --- YAN MENÜ (KİMLİK VE ÖĞRETMEN GİRİŞİ) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3407/3407024.png", width=80)
    st.header("Öğrenci Girişi")
    
    ad_soyad = st.text_input("Adın Soyadın:", placeholder="Örn: Ayşe Yılmaz")
    
    # YENİ SINIF SEVİYELERİ EKLENDİ
    sinif = st.selectbox("Sınıfın:", [
        "Seçiniz...",
        "6. Sınıf", "7. Sınıf", "8. Sınıf (LGS)",
        "9. Sınıf", "10. Sınıf", 
        "11. Sınıf", "12. Sınıf (YKS)", 
        "Mezun"
    ])
    
    st.markdown("---")
    
    # ÖĞRETMEN ÖZEL PANELİ
    st.header("🔒 Öğretmen Paneli")
    admin_password = st.text_input("Şifre:", type="password")
    
    if admin_password == "rehberlik123": # Şifreyi buradan değiştirebilirsin
        st.success("Giriş Başarılı!")
        if os.path.isfile("ogrenci_sonuclar.csv"):
            st.write("### Kayıtlı Sonuçlar")
            df = pd.read_csv("ogrenci_sonuclar.csv")
            st.dataframe(df) # Tabloyu göster
            
            # İndirme Butonu
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="📥 Listeyi Excel Olarak İndir",
                data=csv,
                file_name='tum_ogrenciler.csv',
                mime='text/csv',
            )
        else:
            st.warning("Henüz hiç veri girişi yapılmamış.")
    elif admin_password:
        st.error("Hatalı Şifre!")

# --- ANA GÖVDE ---

if sinif != "Seçiniz..." and ad_soyad:
    st.title(f"📊 {ad_soyad} - Performans ve Alışkanlık Analizi")
    st.info("Aşağıdaki soruları dürüstçe cevapla, sistem sana özel bir karne çıkarsın.")
    
    # PUAN DEĞİŞKENLERİ
    score_focus = 0      # Odak & Teknoloji (15 Puan)
    score_strategy = 0   # Teknik & Planlama (15 Puan)
    score_resilience = 0 # Psikoloji & Kaygı (15 Puan)
    score_goal = 0       # Hedef & Motivasyon (YENİ - 15 Puan)

    # --- BÖLÜM 1: ODAK ---
    st.header("📱 1. Odaklanma ve Ekran Yönetimi")
    c1, c2 = st.columns(2)
    
    with c1:
        q1 = st.radio("Ders çalışırken telefonun nerede?", 
             ["Elimin altında.", "Sessizde/Uçak modunda.", "Başka odada."], key="q1")
        if q1 == "Başka odada.": score_focus += 5
        elif q1 == "Sessizde/Uçak modunda.": score_focus += 3
        
        q2 = st.radio("Günlük sosyal medya/oyun süren?", 
             ["3 saatten fazla.", "1-3 saat arası.", "1 saatten az."], key="q2")
        if q2 == "1 saatten az.": score_focus += 5
        elif q2 == "1-3 saat arası.": score_focus += 3

    with c2:
        q3 = st.radio("Odaklanma süren ne kadar?", 
             ["Çok sık bölünüyorum.", "20-30 dk dayanabiliyorum.", "40 dk ve üzeri blok çalışabilirim."], key="q3")
        if q3 == "40 dk ve üzeri blok çalışabilirim.": score_focus += 5
        elif q3 == "20-30 dk dayanabiliyorum.": score_focus += 3

    st.divider()

    # --- BÖLÜM 2: STRATEJİ ---
    st.header("📝 2. Çalışma Stratejisi")
    c3, c4 = st.columns(2)
    
    with c3:
        q4 = st.radio("Haftalık planın var mı?", 
             ["Yok/Uymuyorum.", "Kafamda var.", "Yazılı planım var ve uyarım."], key="q4")
        if q4 == "Yazılı planım var ve uyarım.": score_strategy += 5
        elif q4 == "Kafamda var.": score_strategy += 3
        
        q5 = st.radio("Yanlışlarına ne zaman bakarsın?", 
             ["Bakmam/Nadiren.", "Sonra bakarım.", "Aynı gün analiz ederim."], key="q5")
        if q5 == "Aynı gün analiz ederim.": score_strategy += 5
        elif q5 == "Sonra bakarım.": score_strategy += 3

    with c4:
        q6 = st.radio("Denemede Turlama Tekniği kullanır mısın?", 
             ["Hayır, inatlaşırım.", "Bazen.", "Evet, takılınca geçerim."], key="q6")
        if q6 == "Evet, takılınca geçerim.": score_strategy += 5
        elif q6 == "Bazen.": score_strategy += 3

    st.divider()

    # --- BÖLÜM 3: PSİKOLOJİ ---
    st.header("🧠 3. Sınav Psikolojisi")
    c5, c6 = st.columns(2)

    with c5:
        q7 = st.radio("Sınav anında fiziksel belirtin olur mu?", 
             ["Elim ayağım titrer/Mide bulantısı.", "Biraz heyecan.", "Sakiniyimdir."], key="q7")
        if q7 == "Sakiniyimdir.": score_resilience += 5
        elif q7 == "Biraz heyecan.": score_resilience += 3
        
        q8 = st.radio("Başarısız olunca tepkin?", 
             ["Kendime kızarım/Bırakırım.", "Üzülürüm ama devam ederim.", "Hatamı ararım."], key="q8")
        if q8 == "Hatamı ararım.": score_resilience += 5
        elif q8 == "Üzülürüm ama devam ederim.": score_resilience += 3

    with c6:
        q9 = st.radio("Uyku düzenin?", 
             ["Çok karışık.", "Geç yatarım.", "Düzenlidir."], key="q9")
        if q9 == "Düzenlidir.": score_resilience += 5
        elif q9 == "Geç yatarım.": score_resilience += 3

    st.divider()

    # --- BÖLÜM 4: HEDEF VE MOTİVASYON (YENİ) ---
    st.header("🎯 4. Hedef ve Motivasyon")
    c7, c8 = st.columns(2)

    with c7:
        q10 = st.radio("Neden çalışıyorsun?", 
             ["Ailem istiyor/Mecburum.", "İyi bir gelecek için.", "Hayalimdeki o meslek için tutkuluyum."], key="q10")
        if q10 == "Hayalimdeki o meslek için tutkuluyum.": score_goal += 5
        elif q10 == "İyi bir gelecek için.": score_goal += 3
        
        q11 = st.radio("Hedefin net mi?", 
             ["Bilmiyorum.", "Puanım nereye yeterse.", "Evet, bölüm ve üniversite net."], key="q11")
        if q11 == "Evet, bölüm ve üniversite net.": score_goal += 5
        elif q11 == "Puanım nereye yeterse.": score_goal += 3

    with c8:
        q12 = st.radio("Sabah seni yataktan kaldıran güç?", 
             ["Alarmın sesi.", "Mecburiyet hissi.", "Hedefime ulaşma isteği."], key="q12")
        if q12 == "Hedefime ulaşma isteği.": score_goal += 5
        elif q12 == "Mecburiyet hissi.": score_goal += 3

    st.markdown("---")

    # --- HESAPLAMA BUTONU ---
    if st.button("Analizi Tamamla ve Kaydet ✅", type="primary"):
        
        # Puanları 100 üzerinden hesapla
        p_focus = int((score_focus / 15) * 100)
        p_strategy = int((score_strategy / 15) * 100)
        p_resilience = int((score_resilience / 15) * 100)
        p_goal = int((score_goal / 15) * 100)
        
        avg = int((p_focus + p_strategy + p_resilience + p_goal) / 4)
        
        # --- VERİLERİ KAYDETME KISMI ---
        data_to_save = {
            "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Ad Soyad": ad_soyad,
            "Sınıf": sinif,
            "Genel Puan": avg,
            "Odak Puanı": p_focus,
            "Strateji Puanı": p_strategy,
            "Psikoloji Puanı": p_resilience,
            "Hedef Puanı": p_goal
        }
        save_data(data_to_save)
        
        st.success("Sonuçların başarıyla kaydedildi! İşte karnen:")
        st.balloons()
        
        # --- SONUÇ GÖRSELLEŞTİRME ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📱 Odak", f"%{p_focus}")
        col2.metric("📝 Strateji", f"%{p_strategy}")
        col3.metric("🧠 Psikoloji", f"%{p_resilience}")
        col4.metric("🎯 Hedef", f"%{p_goal}")
        
        st.progress(avg, text=f"Genel Başarı Skoru: %{avg}")
        
        # YORUMLAR
        if p_goal < 50:
            st.error("🚨 **Hedef Sorunu:** Rotası olmayan gemiye hiçbir rüzgar yardım etmez. Önce 'Neden?' sorusunu cevaplamalıyız.")
        elif p_focus < 50:
            st.warning("⚠️ **Odak Sorunu:** Potansiyelin var ama teknoloji senin enerjini çalıyor.")
        elif p_strategy < 50:
            st.warning("⚠️ **Teknik Sorun:** Çok çalışıyorsun ama verimsiz çalışıyorsun. Taktik değiştirmeliyiz.")
        else:
            st.success("✅ **Harika:** Dengeli ve güçlü bir profilin var. Aynen devam!")

else:
    st.warning("Lütfen başlamak için sol taraftan Adını ve Sınıfını gir.")
 