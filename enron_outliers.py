# This code was used to help identify outliers in the financial
# features. 
# Outliers are removed from the final dataset in poi_id.py

import pickle
import matplotlib.pyplot
from feature_format import featureFormat, targetFeatureSplit

# Read in data dictionary
data_dict = pickle.load( open("final_project_dataset.pkl", "r") )
# Removes the "Total" from the dictionary after it was found as an
# outlier in this file
data_dict.pop("TOTAL", 0)
# This outlier was discovered later on so it is removed as well
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)

# Use these lines of code to filter out outliers in some graphs
# and identify more outliers
# data_dict.pop("LAY KENNETH L", 0)
# data_dict.pop("SKILLING JEFFREY K", 0)
# data_dict.pop("FREVERT MARK A", 0)

# Uncomment any of the print statments below in order to see the plots
# created to identify outliers.
# To find the strange data points, check the original data dictionary,
# entitled "enron61702insiderpay.pdf", where values for financial
# features are listed under the names in the dataset

def plot_features(feature1, feature2, dictionary = data_dict):
	""" Create scatterplot of two given financial features """

	features = [feature1, feature2]
	data = featureFormat(dictionary, features)

	for point in data:
		variable1 = point[0]
		variable2 = point[1]
		matplotlib.pyplot.scatter( variable1, variable2 )

	matplotlib.pyplot.xlabel(feature1)
	matplotlib.pyplot.ylabel(feature2)
	matplotlib.pyplot.show()

	return "Plotted {} and {}".format(feature1, feature2)

# print(plot_features("salary", "bonus"))	

# print(plot_features("deferral_payments", "total_payments"))

# print(plot_features("loan_advances", "total_payments"))

# print(plot_features("salary", "deferred_income"))

# print(plot_features("total_stock_value", "exercised_stock_options"))

# print(plot_features("salary", "expenses"))

# print(plot_features("salary", "other"))

# print(plot_features("long_term_incentive", "bonus"))

# print(plot_features("exercised_stock_options", "restricted_stock"))
