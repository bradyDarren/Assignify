import pandas as pd
import random

# reading of our CSV file containing partner information
partner_data = pd.read_csv(filepath_or_buffer = "Partners.csv")
print(partner_data)

# Create a dictionary from the Partner.csv file.
partner_dict = {row.Name:{'Shift':row.Team, "Lift": row.lift_cert} for (_, row) in partner_data.iterrows()}

for p in partner_dict:
    if partner_dict[p]['Shift'] == 'BED': 
        print(p)
# for p in partner_data.iterrows():
#     partner_dict[partner_data['Name']] = {'Shift':partner_data['Team'],'Lift':partner_data['lift_cert']}

