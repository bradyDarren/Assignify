import pandas as pd
import random

class Partners: 

    def __init__(self, employee_data):
        self.employee_data = employee_data

# returns a list of partners for the specified shift
    def employee_list(self, shift = None):
        e_list = []
        for id in self.employee_data:
            if self.employee_data[id]['Shift'] == shift:
                e_list.append(self.employee_data[id]["Name"])
        return e_list
                


    def lift_certified(Self):
        pass