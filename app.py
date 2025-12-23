import streamlit as st

st.set_page_config(page_title="Sınav Savaşçısı Testi", page_icon="📝")

st.title("Hangi Sınav Öğrenci Tipisin? 🕵️‍♂️")
st.write("Soruları dürüstçe cevapla, tarzını öğren!")

# Puanları tutacak sözlük
scores = {"Panik": 0, "Rahat": 0, "Stratejik": 0}

# Soru 1
q1 = st.radio(
    "1. Sınavda zor bir soruyla karşılaştın. İlk tepkin ne olur?",
    ("Eyvah, bittim ben! (Ter basar)", 
     "Aman canım, sonra bakarım. (Geçersin)", 
     "Yanına işaret koyar, turlama yaparım. (Planlısın)")
)

if q1 == "Eyvah, bittim ben! (Ter basar)":
    scores["Panik"] += 1
elif q1 == "Aman canım, sonra bakarım. (Geçersin)":
    scores["Rahat"] += 1
else:
    scores["Stratejik"] += 1

# ... Buraya 4-5 soru daha eklersin ...

if st.button("Sonucumu Göster"):
    result = max(scores, key=scores.get)
    
    st.markdown("---")
    if result == "Panik":
        st.error("Sonuç: PANİK PİLOTU! 🚨")
        st.write("Çok çalışıyorsun ama heyecanına yeniliyorsun. Nefes egzersizlerine ihtiyacın var.")
    elif result == "Rahat":
        st.warning("Sonuç: ERTELEYİCİ FİLOZOF! 🐢")
        st.write("Zekisin ama potansiyelini harcıyorsun. Biraz disipline ihtiyacın var.")
    else:
        st.success("Sonuç: STRATEJİK NİNJA! 🥷")
        st.write("Süreci harika yönetiyorsun. Aynen devam!")