import pandas as pd
import streamlit as st

def getPays(nom_pays):
    if nom_pays == 'France (FR)':
        pays = "FR"
    elif nom_pays == 'États-Unis (US)':
        pays = "US"
    elif nom_pays == 'Grande-Bretagne (GB)':
        pays = "GB"    
    elif nom_pays == 'Allemagne (DE)':
        pays = "DE"    
    elif nom_pays == 'Russie (RU)':
        pays = "RU"
    elif nom_pays == 'Canada (CA)':
        pays = "CA"
    elif nom_pays == 'Mexique (MX)':
        pays = "MX"
    elif nom_pays == 'Corée du Sud (KR)':
        pays = "KR"
    elif nom_pays == 'Japon (JP)':
        pays = "JP"
    elif nom_pays == 'Inde (IN)':
        pays = "IN"
    
    return pays

def getDataset(nom_pays):
    pays = getPays(nom_pays)
    dataset_name = 'Dataset/' + pays + "videos.csv"
    df = pd.read_csv(dataset_name)
    
    return df

def getCategoryById(category_id, nom_pays):
    pays = getPays(nom_pays)
    df = pd.read_json('Dataset/' + pays +'_category_id.json')
    
    for item in df["items"]:
        if int(item["id"]) == category_id:
            return item["snippet"]["title"]
        
def addCategoryToDataset(dataset):
    for row in dataset:
        st.write(row)

    return dataset

