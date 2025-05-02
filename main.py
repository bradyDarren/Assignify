from partners import Partners
from data import PartnerData
from tasks import Tasks

partner_data = PartnerData('Partners.csv')
partner_data.read_data()
data_dict = partner_data.convert_data()

assignment_data = Tasks('Assignments.csv')
assignment_data.read_assignment()
assignment_dict = assignment_data.task_list()


# # reading of our CSV file containing partner information
# partner_data = pd.read_csv(filepath_or_buffer = "Partners.csv")

# # added Employess ID into csv file - making it what it is now. 
# # partner_data.insert(0,'ID',range(1,len(partner_data)+1))
# # partner_data.to_csv('Partners.csv', index=False)

# # Create a dictionary from the Partner.csv file.
# partner_dict = {row.ID:{'Name':row.Name,'Shift':row.Team, 
#                           'Lift': row.lift_cert} 
#                           for (_, row) in partner_data.iterrows()}
# # print(partner_dict)

