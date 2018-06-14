# Code used to create a new feature, "deleted_emails" in the dataset.
# The feature is a count of the number of deleted emails in a person's
# email directory.

# Sources:
# https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import os, os.path

def count_deleted(mail_directory):
	"""
	Takes a mail directory and returns counts of deleted emails
	for every person in that directory.
	"""

	child_directories = next(os.walk(mail_directory))[1]

	d = {}

	for element in child_directories:
		DIR = os.path.join(mail_directory, element, 'deleted_items')
		if os.path.isdir(DIR):
			number_of_files = len([name for name in os.listdir(DIR) 
				if os.path.isfile(os.path.join(DIR, name))])
		else: 
			number_of_files = 0
		d[element] = number_of_files
	return d

# Mail directory from 'ud-120-projects-master' folder from machine
# learning course
# Note that not everyone in the dataset was in the mail directory
# and vice versa
mail_directory = '/Users/asherades/Documents/Udacity Projects/Intro to Machine Learning/ud120-projects-master/maildir/'
# This line creates a dictionary of the counts for easy import into
# the poi_id.py file
counts_dict = count_deleted(mail_directory)

def update_dict(counts_dict, data_dict):
	"""
	Updates the full data dict with the counts of deleted emails
	"""

	# After running this function on the dataset, I checked to see if
	# any of the people in the dataset had the same last name
	# as those in the mail directory but were not the same person.
	# These people were mistakenly assigned a number of deleted emails
	# that did not belong to them.
	# This is a list of people whose names were incorrectly assigned
	# deleted emails and their value is set to 0 in this function.
	incorrect = ['LEWIS RICHARD', 'PEREIRA PAULO V. FERRAZ',
	'MARTIN AMANDA K', 'WHITE JR THOMAS E', 'TAYLOR MITCHELL S']

	for k,v in data_dict.iteritems():
		v['deleted_emails'] = 0
		# This allows me to compare the lowercase version of the 
		# last name to the last name in the mail directory.
		last_name = k.split(" ")[0].lower()

		for name, count in counts_dict.iteritems():
			split_name = name.split("-")[0]
			if split_name == last_name:
				if k not in incorrect:
					v['deleted_emails'] += count
					# Only add deleted emails from the first folder
					# under that last name
					break

	return data_dict
		 




