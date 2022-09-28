import numpy as np
import random
import pandas as pd
import json
import os

directory = '/Users/nicolasnino/Documents/semillero/ejercicio_0'
os.chdir(directory)

priceadores = ['alejandro', 'sharil', 'jorge', 'karen', 'carlos', 'adrian', 'alondra']

def build_examples():
    area_coefficient = random.choice([0.18, 0.22, 0.15, 0.16, 0.2, 0.17, 0.14])
    initial_area = np.random.randint(100, 200, dtype=int)
    sample_size = np.random.randint(15, 25, dtype=int)
    W = np.random.randint(low=[int(initial_area*0.8), 800000], 
                          high=[int(initial_area*1.2), 1200000], 
                          size=(sample_size,2), dtype=int)
    
    valores_mt2 = np.round((W[:,1] / W[:,0]), 2).reshape(sample_size,1)
    W = np.append(W, valores_mt2, axis=1)
    comps = pd.DataFrame(W)
    comps.reset_index(inplace=True)
    comps.columns = ['id', 'built_area', 'sale_value', 'price_m2']
    comps_dict = comps.to_dict('records')
    pricing_lead = {'area': initial_area, 'area_coefficient': area_coefficient}
    return_dict = {'pricing_lead': pricing_lead, 'comps': comps_dict}

    return return_dict

for priceador in priceadores:
    exercise = build_examples()
    with open(f'{priceador}.json', 'w') as f:
        json.dump(exercise, f)