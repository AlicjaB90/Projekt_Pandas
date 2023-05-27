import pandas as pd
import requests

nypd_df = pd.read_csv("/home/student/nypd-motor-vehicle-collisions.csv")
nypd_df

nypd_df_factors_data = nypd_df[['CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3','CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5']].apply(pd.Series.value_counts)
nypd_df_factors_dat

#reset index and rename name
df = nypd_df_factors_data.reset_index()
df = df.rename(columns={df.columns[0]: 'CONTRIBUTING FACTORS'})
df['Sum'] = df[['CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3','CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5']].sum(axis=1)
df
#sum of factors for CONTRIBUTING FACTOR VEHICLE 1, 2, 3, 4, 5

df.drop(['CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3','CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5'], axis=1, inplace=True)
df

df = df.sort_values(by='Sum', ascending=False)
df.head(5)