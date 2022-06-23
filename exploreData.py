import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utilsDatasets import getDataset

def exploreData(nom_pays):
    st.write("""
         ### Explorer le jeu de données
         """)

    
    dataset = getDataset(nom_pays)
    st.info('Jeu de données initial de ' + nom_pays +
            "  \n✨ Ce jeu de données contient " + str(dataset.shape[0]) + " lignes et " + str(dataset.shape[1]) + " colonnes")
      
    st.write(dataset)

    st.write(""" ### Statistiques de base """)
    st.write(dataset.describe())
    st.text('### Examiner la fréquence à laquelle les valeurs apparaissent dans une colonne')
    for colonne in ['title', 'channel_title', 'category_id', 'tags']:
        st.write(dataset[colonne].value_counts())

    
    
