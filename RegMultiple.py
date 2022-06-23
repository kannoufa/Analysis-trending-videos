import statsmodels.api as sm
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

# prédire
def predict_nb_views(likes, dislikes):
    return 85.5304 * likes + 18.4712 * dislikes +  4.238e+04

def predict_all(lst_likes, lst_dislikes, dataset):
    predicted_views = []
    for n in range(0, len(dataset['views'])):
        predicted_views.append(predict_nb_views(lst_likes[n], lst_dislikes[n]))
    return predicted_views

def regressionMultiple(dataset):
    y = dataset['views']
    X = [dataset['likes'],
        dataset['dislikes']]
    st.write(reg_m(y, X).summary())
    st.write("### prédiction")
    likes = st.slider("likes", 1000, 1500000)
    dislikes = st.slider("dislikes", 1000, 150000)
    predire = st.button("Prédire")
    if predire:
        st.write("un vidéo qui a " + str(likes) + " likes et " + str(dislikes) + " dislikes peut avoir environ " + str(predict_nb_views(likes, dislikes)) + " views")
    fig = plt.figure()
    ax = fig.add_subplot(1,2,1, projection='3d')
    ax.scatter(dataset['likes'], dataset['dislikes'], dataset['views'], c='r', marker='o')

    ax.set_xlabel('likes')
    ax.set_ylabel('dislikes')
    ax.set_zlabel('views')


    ax = fig.add_subplot(1, 2, 2, projection='3d')

    ax.plot_trisurf(dataset["likes"], dataset["dislikes"], predict_all(dataset["likes"], dataset["dislikes"], dataset))
    st.pyplot(fig)
    
    scat_plot = ax.scatter(xs = dataset["likes"], ys = dataset["dislikes"], zs = dataset["views"])

    cb = plt.colorbar(scat_plot, pad=0.2)

    cb.set_ticks([0,1])

    cb.set_ticklabels(["Male", "Female"])
    st.pyplot(scat_plot)


    