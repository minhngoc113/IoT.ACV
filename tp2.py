
#Chargement les libraires
import streamlit as st
import pandas as pd
import numpy as np
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
    # 4. Affichage du DataFrame
    df = pd.read_csv(uploaded_file)
    st.subheader("🗂️ Aperçu des données")
    st.dataframe(df.head())

    # Graphique en fonction du choix
    graph_type = st.selectbox("Choissisez un type de graphique:",["Ligne","Barres","Aucun"])
    if graph_type == "Ligne":
        st.line_chart(df.select_dtypes(include='number'))
    elif graph_type == "Barres":
        st.bar_chart(df.select_dtypes(include='number'))
    elif graph_type == "Dispersion":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        if len(num_cols) >= 2:
            x_axis = st.selectbox("Choisissez la variable X :", num_cols, index=0)
            y_axis = st.selectbox("Choisissez la variable Y :", num_cols, index=1)
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        else:
            st.warning("Pas assez de colonnes numériques pour un graphique de dispersion.")

    else:
        st.write("Aucun graphique sélectionné.")

    # Calcul et affichage des corrélations
    st.subheader("📉 Matrice de corrélation")
    corr = df.select_dtypes(include='number').corr()
    st.dataframe(corr)


# Affichage d’un tableau aléatoire
if st.checkbox("📋 Afficher un tableau aléatoire"):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']))

# Message de fin
st.write("✅ Merci d'avoir utilisé notre application Streamlit !")
