# importing relevant modules and libraries
import streamlit as st
import pandas as pd
from notifypy import Notify
import requests
import time
# general page configurations
st.set_page_config(
    page_title="Ueab courses data",
    page_icon=":umbrella_with_rain_drops:",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# creating three columns
col1, col2, col3 = st.columns(3)
# importing as csv file using pandas
df = pd.read_csv('courses.csv')
# converting the Course Title column in the data to a list
data = (df['Course Title'].to_list())
# building a multiselector which contains a set of data as options 
with col2:
	courses = st.multiselect(':blue[Select your courses]', list(set(data)))
	# button to show selected courses
	submitted= st.button(':blue[Selected Courses]')
with col3:
	if submitted:
		if courses == []:
			st.write(":red[No courses Selected]")
		else:
			for iteration in courses:
				st.markdown(iteration)
# showing the number count of courses selected
courses_count = len(courses)
st.metric(f'courses count:', f'{courses_count}')
if courses_count > 7:
	# creating a notification when courses count > 7
	# Create a notification object
	notification = Notify()

	# Set the title and message for the notification
	notification.title = "Exceeded"
	notification.message = f"{courses_count-7} courses are exceeded"

	# Display the notification
	notification.send()
	# delete course button - deletes the last course in the list

	if st.button('Delete')	:
		courses.remove(courses[-1])

with col1:
	ds = pd.Series(courses_count, courses)
	st.bar_chart(ds)

