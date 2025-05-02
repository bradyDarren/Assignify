import pandas as pd

class Tasks:  

    def __init__(self, assignment_data):
        self.assignment_data = assignment_data
        self.df = None

    def read_assignment(self):
        self.df = pd.read_csv(filepath_or_buffer = self.assignment_data)
        return self.df
    
    def task_list(self):
        
        if self.df is None: 
            raise ValueError("Assignment Data has note been read yet. Please call the read_assignment() first.")
        
        required_columns = ["Quantity", "Assignment"]
        for col in required_columns: 
            if col not in self.df.columns: 
                raise ValueError(f"Column {col} is missing from the dataset, Please ensure it is included.")
        
        assignment_dict = {row.Assignment:row.Quantity 
                           for (_, row) in self.df.iterrows()}
        
        return assignment_dict