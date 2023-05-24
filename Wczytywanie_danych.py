import pandas as pd
import requests

nypd_df = pd.read_csv("/home/student/nypd-motor-vehicle-collisions.csv")
nypd_df

Unsafe_speed_selectes_data = nypd_df[
    (nypd_df['CONTRIBUTING FACTOR VEHICLE 1'] == 'Unsafe Speed')
    | (nypd_df['CONTRIBUTING FACTOR VEHICLE 2'] == 'Unsafe Speed')
    | (nypd_df['CONTRIBUTING FACTOR VEHICLE 3'] == 'Unsafe Speed')
    | (nypd_df['CONTRIBUTING FACTOR VEHICLE 4'] == 'Unsafe Speed')
    | (nypd_df['CONTRIBUTING FACTOR VEHICLE 5'] == 'Unsafe Speed')]
Unsafe_speed_selectes_data

Unsafe_speed_selectes_data_columns = Unsafe_speed_selectes_data[['BOROUGH','NUMBER OF PERSONS INJURED','NUMBER OF PERSONS KILLED','NUMBER OF PEDESTRIANS INJURED','NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED','NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED','NUMBER OF MOTORIST KILLED','CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3','CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5']]
Unsafe_speed_selectes_data_columns
#ciezka_wynikowa = glowna_sciezka + "plik_wynikowy.csv"