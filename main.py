import streamlit as st
from AnalyseData import AnalyseData
from exploreData import exploreData
from prepareDeta import prepareData


st.set_page_config(
  page_title="Tendance des vidéos sur YOUTUBE",
  page_icon="chart_with_upwards_trend",
  layout="wide"
)

st.title("Tendance des vidéos sur YOUTUBE")

st.write("""
         ### Annalyser la tendance des vidéos avec ACP, AFC, ACM ...
         """)




#########################################################
#                       sidebar                         #
#########################################################

nom_pays = st.sidebar.selectbox("Choisir le jeu de données selon le pays", 
                                    ("France (FR)",
                                     "États-Unis (US)",
                                     "Grande-Bretagne (GB)",
                                     "Allemagne (DE)",
                                     "Russie (RU)",
                                     "Canada (CA)",
                                     "Mexique (MX)",
                                     "Corée du Sud (KR)",
                                     "Japon (JP)",
                                     "Inde (IN)"
                                    ))

st.sidebar.write("### Options")
option = st.sidebar.radio(
     "Choisir une option",
     ('Exploration du jeu de données',
      'Préparation du jeu de données',
      'Commencer l\'analyse'))

if option == 'Exploration du jeu de données':
    exploreData(nom_pays)
elif option == 'Préparation du jeu de données':
    prepareData(nom_pays)
else:
    AnalyseData(nom_pays)



