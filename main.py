import pandas as pd
import random
from partners import Partners

# reading of our CSV file containing partner information
partner_data = pd.read_csv(filepath_or_buffer = "Partners.csv")

# added Employess ID into csv file - making it what it is now. 
# partner_data.insert(0,'ID',range(1,len(partner_data)+1))
# partner_data.to_csv('Partners.csv', index=False)

# Create a dictionary from the Partner.csv file.
partner_dict = {row.ID:{'Name':row.Name,'Shift':row.Team, 
                          'Lift': row.lift_cert} 
                          for (_, row) in partner_data.iterrows()}
# print(partner_dict)

p = Partners(partner_dict)
print(p.lift_certified(False))

