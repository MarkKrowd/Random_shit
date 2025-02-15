# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:39:15 2020

@author: RMichaud
"""

import pickle

data = {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'name': 'Chill Out', 'website': 'https://age.heig-vd.ch/localchillout/', 'Couleurs': ['Blanche', 'Blonde', 'Ambrée', 'Rousse', 'Brune', 'Noire'], 'Styles': ['Altbier', 'Bière de garde', 'Blanche', 'Brown Ale', 'Fumée', 'India Pale Ale', 'Lager / Pils', 'Pale Ale', 'Red Ale', 'Sour', 'Spéciale', 'Stout / Porter', 'Strong Ale', 'Style Belge', 'Autres'], 'Tel': 'Keine'}, 'geometry': {'type': 'Point', 'coordinates': [741341.2438333641, 5906070.939836291]}, 'id': '741341.24383336415906070.939836291'}]}
# Source: https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python
# Saving the objects:
with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(data,f)


# Getting back the objects:
with open('objs.pkl', "rb") as f:  # Python 3: open(..., 'rb')
    retrieved_data = pickle.load(f)