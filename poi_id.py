"""
  This was where the main work was done for the machine
  learning project.
  This file includes steps for outlier removal, feature selection,
  classifier creation, and hyperparameter tuning

  In order to conduct tests on your own, uncomment the desired
  lines below (depending on what you're testing), save this file,
  run it, and then run the tester.py file.

  Note that the lines of code related to creating a new feature
  have also been commented out, since they rely on a large mail
  directory that cannot be made available to all users. The code
  still functions the same without the new feature, because it was
  not one of the final features selected.

"""

import numpy as np
import pickle

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
#from find_deleted import counts_dict, update_dict


### Select features to start with
# After exploring the dataset, I removed "restricted_stock_deferred"
# and "director_fees" from the features list since no POIs were in
# either. I also removed "email_addresses" since it does not work with
# the feature_format function, which tries to convert values to floats.

# features_list is a list of strings, each of which is a feature name.
# The first feature must be "poi".
features_list = ['poi','salary', 'deferral_payments', 'total_payments',
 'loan_advances', 'bonus','restricted_stock_deferred',
  'deferred_income', 'total_stock_value','expenses',
  'exercised_stock_options', 'other', 'long_term_incentive', 
  'restricted_stock', 'director_fees', 'to_messages',
  'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi',
  'shared_receipt_with_poi',]


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


### Remove outliers
# See enron_outliers.py for code I used to identify outliers

# This was a total of all the values for financial features 
# that slipped into the dataset
# It was removed since it should not be there
data_dict.pop("TOTAL", 0)
# Mark A. Frevert was an outlier for almost every financial feature.
# He had a much higher salary, deferral payment, amount for loan
# advances and total payment than most people in the dataset.
# However, since he is not a Person of Interest, he is removed so that
# his high values don't potentially mess up testing.
data_dict.pop("FREVERT MARK A", 0)
# I found this while looking through the names in the dataset
# and decided to get rid of it since it is not a person.
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)


### Create new feature
# See code in find_deleted.py for functions used here to create
# the new feature, which was number of deleted_emails
#data_dict = update_dict(counts_dict, data_dict)

# Find number of people with deleted emails
# deleted_count = 0 
# for k, v in data_dict.iteritems():
#  	if v['deleted_emails'] != 0:
#  		deleted_count += 1
# print "Number of people with deleted emails: " + str(deleted_count)

# 19 people in the dataset have deleted emails

#features_list.append('deleted_emails')

# Store data dictionary to my_dataset for easy export below.
my_dataset = data_dict


### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)


### Find and select most important features in the dataset
from sklearn import tree

dtree = tree.DecisionTreeClassifier(random_state = 123)
dtree = dtree.fit(features, labels)

importances = dtree.feature_importances_
important_features = []

# Finding features with an importance level greater than .10
for element in importances:
	if element > .10:
		important_features.append(element)

# Uncomment lines below to print most important features 
# and their importance level
# for i in range(len(importances)):
# 	if importances[i] in important_features:
# 		# Using i + 1 here since the first feature in the feature
# 		# list is POI
# 		print "Important feature: " + str(features_list[i + 1]), \
# 			", Importance: " + str(importances[i])

# New features list after feature selection
# These were the only features used in testing different algorithms
features_list = ['poi', 'bonus', 'deferred_income', 'expenses', \
	'long_term_incentive', 'restricted_stock']

# Re-extract features and labels after selection
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)


### Try a varity of classifiers
# Keep classifier name as clf for easy export below.

from sklearn.model_selection import GridSearchCV

from sklearn.naive_bayes import GaussianNB

# Comment out this line if switching to Decision Trees algorithm
# Code for Decision Trees below
clf = GaussianNB()

# Hyperparameter tuning for Decision Trees:
# Out of the numbers I tested for 'min_samples_split',
# GridSearchCV retured 10 as the best value for that parameter
# Uncomment lines below to test parameters
# and change clf to Decision Trees

# parameters = {'min_samples_split': [2 , 4, 6, 8, 10, 12, 14, 16, 18, 20],}
# dt = tree.DecisionTreeClassifier(random_state = 0)
# clf = GridSearchCV(dt, parameters)
# clf.fit(features, labels)
# print clf.best_params_

# clf = tree.DecisionTreeClassifier(random_state = 0, 
	# min_samples_split = 10)


### Dump classifier, dataset, and features_list to check results in
### tester.py

dump_classifier_and_data(clf, my_dataset, features_list)