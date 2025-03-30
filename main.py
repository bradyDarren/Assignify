import pandas as pd
import random


partners = pd.read_csv(filepath_or_buffer='Partners.csv')
filtered_data = partners[partners['Team'] == 'BEN']
print(filtered_data['Name'])