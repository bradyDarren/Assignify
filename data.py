import pandas as pd

class PartnerData: 

    def __init__(self, d):
        self.d = d
        self.df = None

# reading the data with pandas
    def read_data(self):
        self.df = pd.read_csv(filepath_or_buffer = self.d)
        return self.df

# converting the data using a dictionary_list
    def convert_data(self):

        if self.df is None: 
            raise ValueError("Data has not been read yet. Please call read_data() first.")
        
        required_columns = ['ID', 'Name', 'Team', 'lift_cert']
        for col in required_columns: 
            if col not in self.df.columns: 
                raise ValueError(f"Column {col} is missing from the dataset, Please ensure it is included")

        data_dict = {row.ID:{'Name':row.Name,'Shift':row.Team, 
                          'Lift': row.lift_cert} 
                          for (_, row) in self.df.iterrows()}
        return data_dict