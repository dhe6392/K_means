import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report,confusion_matrix

#-----------extracao dos dados e separacao em features e label
df = pd.read_csv(r'cap17_kmeans\College_Data.csv', index_col=0) 
X = df.drop('Private', axis=1)
Y = df['Private'].apply(lambda label: 1 if label=='yes' else 0)

#---------treinamento do modelo---------------------------
k = 2 #numero de grupos
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
centros = kmeans.cluster_centers_

#--------calibra o modelo para garantir que 0 representa nao e 1 representa yes 
df['Cluster'] = kmeans.labels_
labels = kmeans.labels_ if (kmeans.labels_[Y.values == 1].mean() < 0.5) else 1 - kmeans.labels_
# ...existing code...
#--------resultados da precisao do modelo-----------------
cr = classification_report(Y,labels)
cmat = confusion_matrix(Y,labels)

print(cr)
print(cmat)