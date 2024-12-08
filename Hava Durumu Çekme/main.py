import streamlit as st
import requests


# CSS Bölümü
st.markdown("""
    <style>
        .big-font {
        color: #364bb7; 
        font-size: 40px;
    }
    </style>
""", unsafe_allow_html=True)

response = requests.get("https://wttr.in/London?format=3")

st.markdown('<p class="big-font">Hava Durumu Aracı</p>', unsafe_allow_html=True)

# Sidebar Kısmı Start
st.sidebar.image("anlikhava.jpg", use_container_width=True)
st.sidebar.image("ulkeler.jpg", caption="Dünya'nın dört bir tarafında bulunan şehirlerin hava durumunu kısa sürede öğrenin.", use_container_width=True)
st.sidebar.image("diller.jpg", caption="Dil farketmeksizin her dili algılayıp hava durumu sonucunu verir.", use_container_width=True)

# Sidebar Kısmı End


sehirler = st.text_input("Şehir / Şehirler Giriniz: ", placeholder="Ör: İstanbul, Londra, Paris...")
kisanot = st.info("!!! Birden fazla şehir girişi yaptığınızda lütfen araya ' VİRGÜL(,) ' koyun. Aksi taktirde hava durumu yanlış gösterilebilir.")

btn = st.button("Hava Durumu Bul")

if btn:
    if len(sehirler) == 0:
        st.error("Şehir Girmediniz! Lütfen Şehir Girerek Tekrar Deneyiniz.")
        st.stop()
    else:
        st.success("Girdiğiniz Şehirin/Şehirlerin Hava Durumu Aşağıdadır.")
    konumlar = sehirler.split(",")
    for konum in konumlar:
        response = requests.get(f"https://wttr.in/{konum}?format=3")
        veri = response.text
        st.subheader(veri.capitalize())