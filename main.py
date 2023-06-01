from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import requests


paginas = np.arange(1, 5, 50)
headers = {'Accept-Language' : 'pt-BR,pt;q=0.8'}

titulo = []
anos = []
generos= []
tempo_duracao =[]
votos = []
ratings = []
imdb_ratings = []
imdb_ratings_standardized = []

for pagina in paginas: 

    response = get('https://www.imdb.com/search/title?genres=sci-fi&' 
                   
    + 'start=' + str(pagina) + '&explore=title_type,genres&ref_=adv_prv', headers=headers )
    
    sleep(randint(8,16))
    if response.status_code != 200:
        warn(f'O pedido : {requests} retornou o código: {response.status_code}')

    #pegando informações da páginas

    pagina_html = BeautifulSoup(response.text,'html.parser')



#pegando informações por contairners
    movie_containers = pagina_html.find_all('div', class_ = 'lister-item mode-advanced')

print(movie_containers)