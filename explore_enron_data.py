""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with 
    that person.
    
    For example:
    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("final_project_dataset.pkl", "r"))

poi_count = 0 
salary_count = 0
email_count = 0
deferral = 0

# Find number of POIs in the dataset
for k,v in enron_data.iteritems():
    if v['poi'] == 1:
        poi_count += 1
print poi_count


def count_values(variable):
    """ Used to count how many people in the dataset do not have 
    missing values for that variable """
    
    variable_count = 0
    for k,v in enron_data.iteritems():

	   if v[variable] != "NaN":
		  variable_count += 1

    print(variable, variable_count)

    return None

# Original features list
features = ['salary', 'deferral_payments', 'total_payments',
 'loan_advances', 'bonus','restricted_stock_deferred',
  'deferred_income', 'total_stock_value','expenses',
  'exercised_stock_options', 'other', 'long_term_incentive', 
  'restricted_stock', 'director_fees', 'to_messages','email_address',
  'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi',
  'shared_receipt_with_poi', 'poi']

for element in features:
    count_values(element)

# The following variables are missing more than half of their values:
# Deferral payments - 39
# Loan advances - 4
# Restricted stock deferred - 18
# Deferred income - 49
# Long term incentive - 66
# Director fees - 17

def count_pois(variable):
    """ Count the number of POI's who have a non-missing value
    for that variable """
    
    number_of_pois = 0
    for k,v in enron_data.iteritems():
        if v[variable] != 'NaN':
            if v['poi'] == 1:
                number_of_pois += 1

    print(variable, number_of_pois)

# Checking the number of POIs for variables missing more than half
# of their values
small_features = ['deferral_payments', 'loan_advances', 
'restricted_stock_deferred', 'deferred_income', 'long_term_incentive',
'director_fees']

print("\n")
for element in small_features:
    count_pois(element)

# Remove restircted stock deffered and director fees off the bat
# because there are zero POI's in each, 
# these features tell you nothing about POI's
# This is done in poi_id.py
        


