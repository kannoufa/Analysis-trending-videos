import pandas as pd
import streamlit as st
import prince
import matplotlib.pyplot as plt

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

# cette fonction permet de récupérer le nom d'une catégorie à partir de son id
def getCategoryById(category_id, nom_pays):
    pays = getPays(nom_pays)
    df = pd.read_json('Dataset/' + pays +'_category_id.json')
    
    for item in df["items"]:
        if int(item["id"]) == int(category_id):
            return item["snippet"]["title"]
        
def addCategoryToDataset(dataset, nom_pays):
    # ajout de la colonne catégory juste après category_id
    dataset.insert(5, "category", "", allow_duplicates=False)

    # insérer pour chaque colonne le nom de la catégorie qui lui correspond
    for row in dataset.index:
        dataset.at[row,'category'] =  getCategoryById(dataset.at[row,'category_id'], nom_pays)

    return dataset

# ajout du taille du titre
def addTailleToDataset(dataset):
    dataset.insert(3, "taille_title", "court", allow_duplicates=False)
    for row in dataset.index:
        taille= len(dataset.at[row,'title'])
        if taille<=15:
            dataset.at[row,'taille_title'] =  'court'
        elif taille>50:
            dataset.at[row,'taille_title'] = 'long'
        else:
            dataset.at[row,'taille_title'] = 'moyen'


def contgTable(dataset):
    table_contingence = pd.crosstab(dataset['taille_title'], 
                                    dataset['category'],  
                                    margins = False) 
    new_df = pd.DataFrame(table_contingence)
    return new_df 

         
def AFC(dataset):
    tableConting = contgTable(dataset)
    
    ca = prince.CA(
     n_components=2,
     n_iter=3,
     copy=True,
     check_input=True,
     engine='auto',
     random_state=42
    )
    
    tableConting.columns.rename('Category', inplace=True)
    tableConting.index.rename('Taille_title', inplace=True)
    
    ca = ca.fit(tableConting)
    
    rowACP = ca.row_coordinates(tableConting)
    
    columnACP = ca.column_coordinates(tableConting)
    
    fig = plt.figure()

    ax = ca.plot_coordinates(
            X=tableConting,
            ax=None,
            figsize=(6, 6),
            x_component=0,
            y_component=1,
            show_row_labels=True,
            show_col_labels=True,
    )
    
    st.pyplot(fig)
    
    return rowACP, columnACP
    
   