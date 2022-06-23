import streamlit as st
import pandas as pd
from RegMultiple import regressionMultiple
import matplotlib.pyplot as plt

from utilsDatasets import *

def prepareData(nom_pays):
        
    st.write('### Préparation du dataset')
    
    dataset = getDataset(nom_pays)
    
    colonnes_a_supprimer = st.multiselect(
     'Choisir les colonnes à supprimer',
     dataset.columns)
    for colonne in colonnes_a_supprimer:
        del dataset[ colonne]
    st.write(dataset)
    
    
    st.write('### Analyse du dataset')
    methode = st.selectbox(
        "Choisir une méthode à appliquer sur le jeu de données", 
        (
            "Régression multiple",
            "ACP",
            "AFC",
            "ACM",
        ))
    
    st.write("### " + methode)
    
    ##
    #   Régression multiple
    ##
    if methode == "Régression multiple":
        regressionMultiple(dataset)
        
    if methode == "AFC":
        st.write("### Ajout du catégorie et de la taille du titre")
        addCategoryToDataset(dataset, nom_pays)
        addTailleToDataset(dataset) 
        st.write(dataset)
        
        st.write("AFC")
        rowACP, columnACP = AFC(dataset)
        st.write(rowACP)
        st.write(columnACP)

        
    if methode == "ACP":
        st.write("### -- AFC")
        
    if methode == "ACM":
        st.write("### -- ACM")
    

    

    
    
        

        
        
        
