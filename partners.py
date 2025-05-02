
class Partners: 

    def __init__(self, employee_data):
        self.employee_data = employee_data

# returns a list of partners for the specified shift
    def employee_list(self, shift = None):
        e_list = []
        shift_found = False
        for id in self.employee_data:
            if self.employee_data[id]['Shift'] == shift:
                e_list.append(self.employee_data[id]["Name"])
                shift_found = True

        if not shift_found: 
            raise ValueError("Selected shift does not exist within the database")
        
        return e_list
# returns a list of certifed or uncertified forklift employees           
    def lift_certified(self, status):
        cert_list = []
        status_found = False
        for id in self.employee_data:
            if self.employee_data[id]['Lift'] == status:
                cert_list.append(self.employee_data[id]['Name'])
                status_found = True
        
        if not status_found: 
            raise ValueError("Selected status does not exist within the database")
        
        return cert_list

