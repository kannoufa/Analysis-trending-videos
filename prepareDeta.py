import streamlit as st
from AnalyseData import AnalyseData

from utilsDatasets import getDataset

def prepareData(nom_pays):
        
    st.write('### Préparation du dataset')
    
    dataset['Catégorie'] = 'coll'
    
    dataset = getDataset(nom_pays)
    colonnes_a_supprimer = st.multiselect(
     'Choisir les colonnes à supprimer',
     dataset.columns)
    for colonne in colonnes_a_supprimer:
        del dataset[ colonne]
    st.write(dataset)
    
        

    