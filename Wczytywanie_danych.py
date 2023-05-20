import pandas as pd
import requests

glowna_sciezka_danych = '/home/student/'
plik = glowna_sciezka_danych + "nypd-motor-vehicle-collisions.csv"
collisions_data = pd.read_csv(plik)
#collisions_data = pd.read_csv("data/nypd-motor-vehicle-collisions.csv")
collisions_data

#ciezka_wynikowa = glowna_sciezka + "plik_wynikowy.csv"