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
                "**Dijital Detoks:** Çalışırken telefonunu mutlaka başka bir odaya bırak (Sessize almak yetmez).",
                "**Forest Uygulaması:** Telefona dokunmamanı sağlayan bu uygulamayı indir ve ağaçlarını büyüt.",
                "**Pomodoro:** 25 dk ders + 5 dk mola kuralını uygula. 25 dakika dünyayla bağlantını kes."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 GELİŞTİRİLMELİ: Dikkat Kaçakları Var"
            feedback["yorum"] = """Fena gitmiyorsun ama dış uyaranlara karşı hassassın. Odaklanma süren henüz bir sınav süresi kadar uzun değil. 
            40. dakikadan sonra kopuşlar yaşıyorsun."""
            feedback["oneri"] = [
                "**Süre Uzatma:** Odaklanma süreni artırmak için çalışma bloklarını kademeli olarak 40-50 dakikaya çıkar.",
                "**Masa Düzeni:** Masanda ders materyali dışında hiçbir şey (kalemlik, süs, oyuncak) bulundurma."
            ]
        else:
            feedback["durum"] = "🟢 MÜKEMMEL: Derin Odaklanma Ustası"
            feedback["yorum"] = """Harika bir disiplinin var. 'Flow' (akış) durumuna geçebiliyorsun. 
            Bu odaklanma gücü sana sınavı kazandıracak en büyük silahın."""
            feedback["oneri"] = [
                "**Zor Sorular:** Bu yüksek odak gücünü, en zorlandığın dersin en karmaşık konularını halletmek için kullan.",
                "**Bu Düzeni Bozma:** Sınav anında dikkatin dağılsa bile kendini hemen toparlayabilirsin."
            ]

    # 2. STRATEJİ VE TEKNİK
    elif category == "Strateji":
        if score < 50:
            feedback["durum"] = "🔴 ROTASIZ GEMİ: Verimsiz Çalışma"
            feedback["yorum"] = """Çok çalışıyor olabilirsin ama 'yanlış' çalışıyorsun. Plansızsın, tekrarların eksik ve yanlışlarınla yüzleşmiyorsun. 
            Bu şekilde yerinde sayarsın."""
            feedback["oneri"] = [
                "**Hata Defteri:** Bugünden itibaren kestiğin yapamadığın sorulardan bir defter veya kutu oluştur.",
                "**Haftalık Plan:** Pazar akşamı oturup haftalık programını yazılı olarak yap ve duvara as.",
                "**Soru Çöz:** Sadece konu okumak çalışma değildir. Kalemi eline al ve soru çöz."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 İYİ AMA EKSİK: Taktiksel Hatalar"
            feedback["yorum"] = """Genel hatlarıyla doğrusun ama detaylarda kaçırıyorsun. Bazen planı aksatıyor, bazen zor derslerden kaçıyorsun. 
            Turlama tekniğini tam oturtamamışsın."""
            feedback["oneri"] = [
                "**Turlama Tekniği:** Denemelerde bir soruyla 2 dakikadan fazla inatlaşmayı bırak. İşaret koy ve geç.",
                "**Nokta Atışı:** Bildiğin konuları tekrar çalışmayı bırak, bilmediğin o gıcık konunun üzerine git."
            ]
        else:
            feedback["durum"] = "🟢 PROFESYONEL ÖĞRENCİ: Doğru Strateji"
            feedback["yorum"] = """Sınavın bir bilgi değil, strateji sınavı olduğunu çözmüşsün. Yanlış analizlerin ve planlaman harika. 
            Sen bu işi biliyorsun."""
            feedback["oneri"] = [
                "**Hızlanma:** Artık süre tutarak branş denemeleri çözmeye ağırlık ver.",
                "**MEB Kitapları:** Detaylarda boğulmamak için MEB kitaplarını taramaya başla."
            ]

    # 3. PSİKOLOJİK SAĞLAMLIK
    elif category == "Psikoloji":
        if score < 50:
            feedback["durum"] = "🔴 YÜKSEK KAYGI: Performans Blokajı"
            feedback["yorum"] = """Bilgi eksiğin olmasa bile bu kaygı seviyesi seni kilitliyor. Sınavı bir 'ölüm-kalım' meselesi haline getirmişsin. 
            Kendine çok acımasız davranıyorsun."""
            feedback["oneri"] = [
                "**Nefes Egzersizi:** Sınav anında panikleyince 4 saniye al, 4 saniye tut, 8 saniye ver.",
                "**Kıyaslamayı Bırak:** Başkalarının netleri seni ilgilendirmez. Kendi gelişimine odaklan.",
                "**Uyku:** Gece 12'den önce yatakta ol. Uykusuz beyin kaygı üretir."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 YÖNETİLEBİLİR STRES: Heyecan Var"
            feedback["yorum"] = """Belli bir düzeyde heyecan normaldir ve diri tutar. Ancak zor sorularda moralin çabuk bozulabiliyor. 
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
                "**Mentorluk:** Bu sakinliğini panik yapan arkadaşlarına destek olarak kullanabilirsin, anlatmak sana da iyi gelir."
            ]

    # 4. HEDEF VE MOTİVASYON
    elif category == "Hedef":
        if score < 50:
            feedback["durum"] = "🔴 BELİRSİZLİK: Yakıtın Bitiyor"
            feedback["yorum"] = """Neden çalıştığını tam bilmiyorsun. 'Ailem istiyor' veya 'Mecburum' diyerek çalışıyorsun. 
            İçsel motivasyonun olmadığı için masa başına oturmak işkence gibi geliyor."""
            feedback["oneri"] = [
                "**Görselleştirme:** İstediğin üniversitenin kampüsünü, o mesleği yapanları izle.",
                "**Hedef Panosu:** Masana seni heyecanlandıran bir söz veya görsel as."
            ]
        elif score < 80:
            feedback["durum"] = "🟡 BULANIK HEDEF: Biraz Daha Netlik"
            feedback["yorum"] = """Bir hedefin var ama ona ne kadar tutkulusun? Zorluk görünce vazgeçme eğilimin var. 
            Hedefini biraz daha somutlaştırmamız lazım."""
            feedback["oneri"] = [
                "**B Planı Yok:** Aklındaki o hedefe odaklan ve 'olmazsa ne olur' diye düşünme.",
                "**Netleştir:** 'İyi bir yer olsun' değil, 'X Üniversitesi Y Bölümü' şeklinde hedefini netleştir."
            ]
        else:
            feedback["durum"] = "🟢 GÖREV ADAMI: Yüksek Motivasyon"
            feedback["yorum"] = """Gözünü hedefe dikmişsin ve hiçbir engel seni durduramaz. 
            Sabah seni yataktan kaldıran o tutkuya sahipsin."""
            feedback["oneri"] = [
                "**İlham Ol:** Motivasyonunu korumak için başarı hikayeleri okumaya devam et."
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
    with c