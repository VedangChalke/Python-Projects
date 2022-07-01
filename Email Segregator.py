# Problem Statement :
#The task you have to perform is “Email Extractor.”
#Suppose you are a student and want to get an internship. You have to contact your professors and some companies to get an internship. For that, you need their email so that you can contact them.
#The task you have to do is to extract the email from text data using Regex Expressions.
#When you go to a website and click on the contact section, by pressing CTRL+A, all the content of the website gets added to the clipboard. Paste the data in your python file or in a string. Extract an email from the above data, and after extracting email, write it into a file with a new line character. Your text file after writing data should look similar to this:
#abc123@gmail.com
#cdf456@gmail.com


import re


str = """
Email:enquiry@alliance.edu.in   Helpline: +91 80 3093 8100 / 8200 / 4619 9100
 Media  Library  News  Webmail  Careers
 Alliance University
 Conferences
 Admissions Open
 Select Language
UPDATES:
ABOUT US 
WHY AU 
COLLEGES 
FACULTY
INTERNATIONAL PROGRAMS
PROGRAMS
RESEARCH
ADMISSIONS 
PLACEMENTS
CONTACT US
Contact UsHome Contact Us
 Contact Us Back
 Vice-Chancellor
Dr. Pavana Dibbur
 : vc@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Pro Vice-Chancellor (Academics, Research & Strategy)
Dr. Anubha Singh
 : anubha@alliance.edu.in
 : +91 80 3093 8102

 Registrar
Mr. Madhu Sudan Mishra
 : registrar@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Registrar (Examination & Evaluation)
Dr. Sajan Mathew
 : registrar.exams@alliance.edu.in
 : +91 80 3093 8141 """
#1st METHOD
email = re.findall(r"[0-9a-zA-Z.+%]+@[0-9a-zA-Z.+%]+[.][0-9a-z.A-Z]+", str)
print(email)

