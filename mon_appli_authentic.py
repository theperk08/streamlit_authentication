import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

rep_images = "images/"
rep_users = "users"

# import des donnée utilisateurs
df_users = pd.read_csv(rep_users+'users.csv', sep=',')
dico = df_users.to_dict(orient='records')

# mise en forme des données utilisateur pour l'appli
lesDonneesDesComptes = {'usernames': {}}

for row in dico:    
    lesDonneesDesComptes['usernames'][row['name']] = row

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


def accueil(name):
      # Using object notation
    # Le bouton de déconnexion    
    
    # Using "with" notation

    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenu(e) {name}",)
        selection = option_menu(
            menu_title=None,
            options=["🤗Accueil", "🐘Les photos d'éléphant"]

        )

    
    
    if selection == "🤗Accueil":
        st.write('Bienvenue')
        st.image(rep_images+"home.jpg")
    elif selection == "🐘Les photos d'éléphant":
        st.header("Voici des photos d'éléphants 🐘")
        col1, col2, col3 = st.columns(3)

        with col1:            
            st.image(rep_images+"elephant-1.jpg")

        with col2:
            st.image(rep_images+"elephant-2.jpg")

        with col3:
            st.image(rep_images+"elephant-3.jpg")

  


    

if st.session_state["authentication_status"]:
  accueil(st.session_state['name'])

  

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')