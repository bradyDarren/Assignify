import pandas as pd
import random

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

class TaskSelection: 

    def __init__(self, task_data):
        self.task_data = task_data
        self.rand_assign = None

    def assign_task(self):
        self.rand_assign = random.choice(self.task_data)
        return self.rand_assign
    
    def remove_assignment(self):
        if self.rand_assign in self.task_data:
            if self.task_data[self.rand_assign] > 0:
                self.task_data[self.rand_assign] = self.task_data[self.rand_assign] - 1
            else: 
                self.assign_task()
                self.remove_assignment()


