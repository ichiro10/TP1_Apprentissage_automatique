# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:18:39 2023

@author: erimo
"""

import numpy as np
import scipy.signal as scs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nom_du_fichier_excel = "C:/Users/erimo/Downloads/dry+bean+dataset/DryBeanDataset/Dry_Bean_Dataset.xlsx"

# Utilisez la fonction read_excel pour charger le fichier Excel
data = pd.read_excel(nom_du_fichier_excel)
