import streamlit as st
import pandas as pd

from utilsDatasets import addCategoryToDataset, getDataset

def exploreData(nom_pays):
    st.write("""
         ### Explorer le jeu de données
         """)

    
    dataset = getDataset(nom_pays)
    st.info('Jeu de données initial de ' + nom_pays +
            "  \n✨ Ce jeu de données contient " + str(dataset.shape[0]) + " lignes et " + str(dataset.shape[1]) + " colonnes")
      
    st.write(dataset)
    
   
    st.write(""" ### CATEGORIE""")
    #dataset['category_name'] = getCategoryById(1, nom_pays)
    #dataset = dataset.assign(new_column=lambda x: getCategoryById(x.category_id))
    dataset = dataset.assign(new_column=lambda x: x.category_id)
    #dataset['New Col'] = pd.Series([getCategoryById(dataset.iloc[x]['category_id']) for x in range(len(dataset.index))])
    
    #dataset = addCategoryToDataset(dataset)
    
    # 
    st.write(dataset)
    
    
    dataset = dataset.assign(category=lambda x: getCategoryById(x.category_id))
    st.write(dataset)
    
    st.write(""" ### Statistiques de base """)
    st.write(dataset.describe())
    st.text('Examiner la fréquence à laquelle les valeurs apparaissent dans une colonne')
    for colonne in ['title', 'channel_title', 'category_id', 'tags']:
        st.write(dataset[colonne].value_counts())
        
def calcul(x):
    return x+ 10

def getCategoryById(category_id):
    df = pd.read_json('Dataset/' + 'FR' +'_category_id.json')
    
    for item in df["items"]:
        if int(item["id"]) == int(category_id):
            return item["snippet"]["title"]
    
    
