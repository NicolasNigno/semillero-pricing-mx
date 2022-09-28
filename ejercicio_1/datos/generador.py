import numpy as np
import random
import pandas as pd
import json

def build_examples():
    land_values = [1280.0, 5121.0, 5381.0, 1410.0, 5390.0, 898.0, 1349.5, 10812.0, 1160.0, 1800.0]
    land_value = random.choice(land_values)
    
    initial_area = np.random.randint(100, 200, dtype=int)
    initial_ground = np.random.randint(100, 200, dtype=int)
    sample_size = np.random.randint(15, 25, dtype=int)
    
    W = np.random.randint(low=[int(initial_area*0.7), int(initial_ground*0.7), 1000000], 
                          high=[int(initial_area*1.3), int(initial_ground*1.3), 1500000], 
                          size=(sample_size, 3), dtype=int)
    
    valores_mt2 = np.round((W[:,2] / W[:,0]), 2).reshape(sample_size,1)
    W = np.append(W, valores_mt2, axis=1)
    comps = pd.DataFrame(W)
    comps.reset_index(inplace=True)
    comps.columns = ['id', 'built_area', 'ground_area', 'sale_value', 'price_m2']
    comps_dict = comps.to_dict('records')
    pricing_lead = {'area': initial_area, 'ground_area': initial_ground, 'land_value_coefficient': land_value}
    return_dict = {'pricing_lead': pricing_lead, 'comps': comps_dict}

    return return_dict

priceadores = ['alejandro', 'sharil', 'jorge', 'karen', 'carlos', 'adrian', 'alondra']
for priceador in priceadores:
    exercise = build_examples()
    with open(f'{priceador}.json', 'w') as f:
        json.dump(exercise, f)