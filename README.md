## Data Analyst Nanodegree Project: Identify Enron Persons of Interest

In this project, I used supervised machine learning techniques in Python to identify people who committed fraud in the Enron scandal 
of the early 2000's. In the process, I removed outliers in the data, selected for the features that would create the best classifier, 
and picked the algorithm and parameters that would yield the best results.

Files in this repository:

* `Identify Enron Fraud Report.pdf` - start here to understand the different steps performed in the Person of Interest identifier code
* `References.rtf` - a list of web sites referred to or used in this project
* `enron61702insiderpay.pdf` - a list of people in the dataset and the financial features associated with them
(e.g. salary, bonus, expenses), used to identify data points in the enron_outliers.py file
* `enron_outliers.py` - code to plot each of the financial features and identify outliers (not needed to understand main code)
* `explore_enron_data.py` - code used to find basic information on the dataset (not needed to understand main code)
* `feature_format.py` - python file created by Udacity staff to help convert a data dictionary into a set of features and labels
* `final_project_dataset.pkl` - data of 144 Enron employees, with information on their financial record, the emails they sent, and whether
they are considered a Person of Interest
* `find_deleted.py` - code to create a new feature that denotes the number of emails a person deleted
* `poi_id.py` - main code used to create the classifier
* `tester.py` - used to evaluate performance of classifier created in poi_id.py (poi_id.py must be run before this file so that the code
has something to test)

Installation:

To run the code in this repository, Python 2.7 is specifically required. In addition, the matplotlib, scikit-learn, and numpy packages
need to be installed.
