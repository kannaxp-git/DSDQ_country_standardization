# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:50:57 2020

@author: kach
"""

import pandas as pd
import pycountry

def standardize_Country(country):
    country=country.replace('"','')
    try:
        std=pycountry.countries.search_fuzzy(country)[0]
        return std.name
    except:
        return None

def clean_country(country):
    country=str(country)
    country=country.replace('"','')
    country=country.title()
    return country


#Reading
df_card=pd.read_csv('country_names_card.csv')
df_dnb=pd.read_csv('country_names_dnb.csv')

#Cleaning CARD country
df_card['n_countryname']=df_card['countryname'].apply(clean_country)
df_dnb['n_countryname']=df_dnb['country'].apply(clean_country)


#joining Card & Dnb
df_card=pd.merge(df_card, df_dnb, how='left', on='n_countryname')


#Writing
df_card.to_excel('country_output_card.xlsx',index=False)
df_dnb.to_excel('country_output_dnb.xlsx',index=False)


print(pycountry.countries)

addr='england'
print(pycountry.countries.search_fuzzy(addr))

addr='london'
print(pycountry.countries.search_fuzzy(addr))

addr='delhi'
print(pycountry.countries.search_fuzzy(addr))

addr='chennai'
print(pycountry.countries.search_fuzzy(addr))


for c in pycountry.countries:
    print(c.name)


"""
import spacy 
nlp = spacy.load('en_core_web_sm') 

description = "SCMITCHELL LIMITED is an accounting company based out of 21 HILBERT ROAD, SUTTON, United Kingdom."

description = "FUGLESTAD KUNST is an electrical/electronic manufacturing company based out of Fossingveien 74, HELLE, Kragerø, Norway."

#description = "L'EXPLORATEUR is a company based out of 24 ROUTE DE HAGUENAU, MORSBRONN LES BAINS, France."

doc = nlp(description) 
for ent in doc.ents:
    if ent.label_=="GPE":
        print(ent.text,ent.start_char, ent.end_char, ent.label_)

"""