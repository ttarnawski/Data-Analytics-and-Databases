import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int):
        result = pd.read_sql(f"""
            select title, language.name as languge, category.name as category from category
            inner join film_category on category.category_id = film_category.category_id
            inner join film on film_category.film_id = film.film_id
            inner join language on film.language_id = language.language_id 
            where category.category_id = {category}
            order by title, language.name
            """, con=connection)
        return result
    
    elif isinstance(category, str):
        result = pd.read_sql(f"""
            select title, language.name as languge, category.name as category from category
            inner join film_category on category.category_id = film_category.category_id
            inner join film on film_category.film_id = film.film_id
            inner join language on film.language_id = language.language_id 
            where category.name like '{category}'
            order by title, language.name
            """, con=connection)
        return result
    
    return None
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int):
        result = pd.read_sql(f"""
            select title, language.name as languge, category.name as category from category
            inner join film_category on category.category_id = film_category.category_id
            inner join film on film_category.film_id = film.film_id
            inner join language on film.language_id = language.language_id 
            where category.category_id = {category}
            order by title, language.name
            """, con=connection)
        return result
    
    elif isinstance(category, str):
        result = pd.read_sql(f"""
            select title, language.name as languge, category.name as category from category
            inner join film_category on category.category_id = film_category.category_id
            inner join film on film_category.film_id = film.film_id
            inner join language on film.language_id = language.language_id 
            where category.name ilike '{category}'
            order by title, language.name
            """, con=connection)
        return result
    
    return None
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(title, str):
        result = pd.read_sql(f"""
            select first_name, last_name from film
            inner join film_actor on film.film_id = film_actor.film_id
            inner join actor on film_actor.actor_id = actor.actor_id
            where title like '{title}'
            order by last_name, first_name
            """, con=connection)
        return result
    
    return None
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(words, list):
        words = '|'.join(words)
        result = pd.read_sql(f"""
            select title from film
            inner join inventory on film.film_id = inventory.film_id
            inner join rental on inventory.inventory_id = rental.inventory_id
            inner join customer on rental.customer_id = customer.customer_id
            where title alike '(?:^| ){words}(?:$| )'
            order by last_name, first_name
            """, con=connection)
        return result
    
    return None