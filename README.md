# Edit or Delete a List of People from a CSV File.

This code is intended to provide a starting point for editing or deleting multiple people, based on a list of email addresses in a CSV file.

Currently, the edit_people_emails_from_csv.py file works for Python 3.
delete_people_from_csv.py works for Python 2.

The only real difference between them is how the quote function is imported, so either can be updated to work for either Python version fairly easily.

For Python 2:
## from urllib import quote

For Python 3:
## from urllib.parse import quote
