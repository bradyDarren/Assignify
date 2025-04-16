
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
# returns a list of certifed or uncertified forklift employees           
    def lift_certified(self, status):
        cert_list = []
        for id in self.employee_data:
            if self.employee_data[id]['Lift'] == status:
                cert_list.append(self.employee_data[id]['Name'])
        return cert_list
        