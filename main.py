import streamlit as st
import numpy     as np
import joblib

# Le modèle pré-entraîné
with open("rfr_model.pkl", "rb") as model_file:
    model = joblib.load(model_file)

st.markdown("""<h1 style="text-align:center;color:green;">Prédiction du prix d'une maison 🏠 en Californie</h1>""", unsafe_allow_html=True)
st.markdown("""<div style="background-color:#FFFACD;padding:15px 15px;border-radius:50px;color:#00008B;font-weight:extra-bold;font-size:20px;text-align:center;marign:auto;">Le prix est estimé à partir du revenu médian, de l’âge des maisons,<br>du nombre de pièces, la population et la proximité de l’océan.</div>""", unsafe_allow_html=True)
st.markdown("""<div style="text-align:center;"><br><b>Choisissez les caractéristiques</b><br><br></div>""",unsafe_allow_html=True)

# Les variables
median_income      = st.number_input("Quel votre revenu médian (en dizaines de milliers de $) ? (de 0 20)", min_value=0,  max_value=20,   value=4)
housing_median_age = st.slider("Choisissez l'age moyen des maisons (années) ? (Jusqu'à 50 ans)",            min_value=1,  max_value=50,   value=20)
total_rooms        = st.slider("Quel est le nombre moyen de pièces (d'1 à 10 pièces)",                      min_value=1,  max_value=10,   value=6)
total_bedrooms     = st.slider("Quel est le nombre moyen de chambres (d'1 à 5)",                            min_value=1,  max_value=5,    value=3)
households         = st.slider("Quelle est l'occupation moyenne ? (de 1 à 10)",                             min_value=1,  max_value=10,   value=2)
population         = st.number_input("Quelle serait la population du quartier ? (de 10 à 5000 habitants)",  min_value=10, max_value=5000, value=500)
latitude           =   34.0
longitude          = -120.0

# Variables catégorielles
ocean_proximity_options = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
ocean_proximity         = st.selectbox("Proximité de l'océan", ocean_proximity_options)
ocean_prox_encoded      = [1 if ocean_proximity == option else 0 for option in ocean_proximity_options]

# Bouton de prédiction
if st.button("Prédire le prix"):
    # Déclarer toutes les variables dans l'ordre d'entraînement
    X_new = np.array([[longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income] + ocean_prox_encoded])
    prediction = model.predict(X_new)
    
    # Affichage centré et stylisé
    st.markdown(f"""<div style="text-align:center; font-weight:bold; color:green; margin-top:10px;">Prix médian éstimé 👉 {prediction[0]:,.2f} $</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color:#FFFACD;padding:15px 15px;border-radius:50px;color:#00008B;font-weight:extra-bold;font-size:20px;text-align:center;marign:auto;">
👀 Aucune donnée personnelle n'est collectée ou stockée.<br>Les entrées saisies ne servent qu'à la prédiction. 👀</div>
""", unsafe_allow_html=True)