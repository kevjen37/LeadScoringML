import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn import metrics 
from scipy.spatial.distance import cdist

#read pipeline data into pandas
df_2 = pd.read_excel('PoppyPipelineAbbrev.xlsx', sheet_name='clean')
df_pipeline = df_2.groupby('Deal_ID').mean() #if repeat customer, take mean of columns
df_pipeline.columns = ['Budget', 'Guest_Count', 'Days_From_Lead_To_Event']
df_pipeline.dropna(subset = ['Budget', 'Guest_Count', 'Days_From_Lead_To_Event'], inplace = True)
#print(df_pipeline.head())



# Read data	
df = pd.read_excel('DataFull.xlsx', sheet_name='won')
#print(df.head())

#Group by Deal ID, establish columns, drop NaN entries
df_customers = df.groupby('Deal_ID').mean() #if repeat customer, take mean of columns
df_customers.columns = ['Budget', 'Guest_Count', 'Days_From_Lead_To_Event']
df_customers.dropna(subset = ['Budget', 'Guest_Count', 'Days_From_Lead_To_Event'], inplace = True)
#print(df_customers.head())

df_output_pipeline = pd.DataFrame()
#df_output_pipeline.columns = ['Budget', 'Guest_Count', 'Days_From_Lead_To_Event']



for x in range(0, len(df_pipeline)):

  
  print(df_pipeline.iloc[[x]])
  #add pipeline row to cluster data 
  df_combined = pd.concat([df_customers, df_pipeline.iloc[[x]]], ignore_index = True)
  newlen = len(df_combined)-1
  print(df_combined.iloc[[newlen]])


  #Transform data by centering mean around 1, and standard deviation around 0
  df_rank = df_combined.rank(method='first') 
  df_normalized = (df_rank - df_rank.mean()) / df_rank.std()
  #print(df_normalized.head())
  #print(df_normalized.describe())

  # Calculate Silhouette coefficients for different k
  for n_cluster in [2, 3, 4, 5, 6, 7, 8]:
      kmeans = KMeans(n_clusters=n_cluster,
                      max_iter=400,
                      n_init=20).fit(df_normalized[['Budget',
                                                    'Guest_Count',
                                                    'Days_From_Lead_To_Event']])
      silhouette_avg = silhouette_score(df_normalized[['Budget',
                                                    'Guest_Count',
                                                    'Days_From_Lead_To_Event']],
                                        kmeans.labels_) 
      #print('Silhouette coefficient for %i clusters: %0.3f' % (n_cluster, silhouette_avg))


  # Build k-means clustering model
  kmeans = KMeans(n_clusters=5,
                  max_iter=400,
                  n_init=20).fit(df_normalized[['Budget',
                                                'Guest_Count',
                                                'Days_From_Lead_To_Event']])

  # Get centres of the clusters
  cluster_centres = kmeans.cluster_centers_
  df_cluster_centres = pd.DataFrame(cluster_centres, columns=['Budget',
                                                    			'Guest_Count',
                                                    			'Days_From_Lead_To_Event'])
  df_cluster_centres['Cluster'] = df_cluster_centres.index



  # Mark each customer with its cluster
  df_four_clusters = df_normalized[['Budget',
                                    'Guest_Count',
                                    'Days_From_Lead_To_Event']].copy(deep=True)
  df_four_clusters['Cluster'] = kmeans.labels_
  #print(df_four_clusters.head())
  #print(df_four_clusters['Cluster'].value_counts())
  #print(df_cluster_centres)


  df_excel_output = df_combined[['Budget',
                               'Guest_Count',
                               'Days_From_Lead_To_Event']].copy(deep=True)
  df_excel_output['Cluster'] = kmeans.labels_


  df_excel_output_length = len(df_excel_output)-1

  df_output_pipeline = pd.concat([df_output_pipeline, df_excel_output.iloc[[df_excel_output_length]]], ignore_index = True)
  #df_output_pipeline.iloc[[x]] = df_excel_output.iloc[[df_excel_output_length]]
  print(df_combined.tail(1))
  df_combined.drop(df_combined.tail(1).index,inplace=True)




file_name = 'DataOutputPipeline.xlsx'
df_output_pipeline.to_excel(file_name)

print('printed to excel')











