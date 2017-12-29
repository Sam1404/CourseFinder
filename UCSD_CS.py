url = 'http://www.ucsd.edu/catalog/courses/CSE.html'

from bs4 import BeautifulSoup as bs
import requests


r = requests.get(url)
soup = bs(r.content,'html.parser')
course_list = soup.findAll(class_="course-name")

courses = []
for course in course_list:
	courses.append(course.getText())

course_names = []
for course in courses:
	course_tk = course.split(' ')
	course_names.append(course_tk)



lower_division =[]
upper_division =[]
graduate =[]

for course in course_names:
	number = course[1]
	if(len(number) == 3):
		index = course_names.index(course)
		lower_division.append(courses[index])
	elif(number[0] == '1'):
	    index = course_names.index(course)
	    upper_division.append(courses[index])
	elif(len(number) number[0] == '2' or number[0] == '5'):
		index = course_names.index(course)
		graduate.append(courses[index])

for course in graduate:
	print(course)

