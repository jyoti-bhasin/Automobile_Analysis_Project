import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

def get_customer_seg(dt,selected_segment,selected_segment2):
    X = dt.iloc[:, [selected_segment,selected_segment2]].values
    print(X)

    # finding wcss value for different number of clusters

    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)

        wcss.append(kmeans.inertia_)

    sns.set()
    plt.plot(range(1, 11), wcss)
    plt.title('The Elbow Point Graph')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.show()

    kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
    # return a label for each data point based on their cluster
    Y = kmeans.fit_predict(X)

    print(Y)

    plt.figure(figsize=(8, 8))
    plt.scatter(X[Y == 0, 0], X[Y == 0, 1], s=50, c='green', label='Cluster 1')
    plt.scatter(X[Y == 1, 0], X[Y == 1, 1], s=50, c='red', label='Cluster 2')
    plt.scatter(X[Y == 2, 0], X[Y == 2, 1], s=50, c='yellow', label='Cluster 3')

    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='cyan', label='Centroids')

    plt.title('Groups')
    plt.xlabel('Engine size')
    plt.ylabel('Horse power')
    plt.show()
    st.pyplot(plt)
