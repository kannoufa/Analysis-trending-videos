from distutils.ccompiler import gen_preprocess_options
import streamlit as st

from utilsDatasets import getDataset

def AnalyseData(nom_pays):
    dataset = getDataset(nom_pays)
        
    st.sidebar.write("### Analyse")
    methode = st.sidebar.selectbox(
        "Choisir une méthode à appliquer sur le jeu de données", 
        (
            "ACP",
            "AFC",
            "ACM",
        ))
    
    st.write("### " + methode)