import numpy as np
import pandas as pd
import json

def get_area_factor(row, comps):
    area_row = row['area']
    area_coef = row['area_coefficient']
    comps_area = comps.copy()[['built_area']].to_numpy(dtype=float)
    condition = (comps_area <= area_row + 5) & (comps_area >= area_row - 5)
    area_factor = np.where(condition, 1, ((comps_area / area_row) * area_coef) + (1 - area_coef))

    return area_factor

def area_normalization(row, comparables):
    comparables['area_factor'] = get_area_factor(row, comparables)
    comparables['price_m2_norm'] = comparables['price_m2'] * comparables['area_factor']
    comparables['sale_value_norm'] = comparables['price_m2_norm'] * comparables['built_area']

    return comparables

def main(file):
    f = open(file)
    data = json.load(f)
    row = data['pricing_lead']
    comps = pd.DataFrame(data['comps'])
    new_comps = area_normalization(row, comps)
    
    new_file = file.split('.')[0]
    new_file += '.xlsx'
    new_comps.to_excel(new_file, index=False)