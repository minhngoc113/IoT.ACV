#Chargement les libraires
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#cd c:\Users\APC
#python tp2.py
#streamlit run tp2.py

st.write("Hello,world! This is a Streamlit app.")
print('Hello Streamlit')

st.title("Analyse des Performances des Étudiants")
st.subheader("Bienvenue dans l'application interactive !")
st.text("Téléchargez un fichier CSV et explorez les données facilement.")

# Demande du nom de l'utilisateur
user_name = st.text_input("👤 Entrez votre prénom :")
if user_name:
    st.success(f"Bonjour {user_name} 👋 Bienvenue dans l'application !")

# Chargement les données
uploaded_file = st.file_uploader("📁 Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Affichage du DataFrame
    df = pd.read_csv(uploaded_file)
    st.subheader("🗂️ Aperçu des données")
    st.dataframe(df.head())



    # Calcul et affichage des corrélations
    st.subheader("📉 Matrice de corrélation")
    corr = df.select_dtypes(include='number').corr()
    st.dataframe(corr)

# Graphique des données
if "math score" in df.columns:
    st.subheader("📊 Histogramme des scores en mathématiques")
    fig = px.histogram(df, x="math score", nbins=20, title="Distribution des scores en math")
    st.plotly_chart(fig)
else:
    st.info("La colonne 'math score' n'existe pas dans les données.")

# Affichage d’un tableau aléatoire
if st.checkbox("📋 Afficher un tableau aléatoire"):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']))

# Message de fin
st.write("✅ Merci d'avoir utilisé notre application Streamlit !")








