from datetime import datetime
import pandas as pd

class Course:

    _courses = []

    def __init__(self, line) -> None:
        self.name = line[0].strip().capitalize()
        self.day_of_week = line[1].strip().lower()
        self.start_time = datetime.strptime(line[2].strip(),'%H:%M')
        self.end_time =  datetime.strptime(line[3].strip(),'%H:%M')
        self.duration = self.end_time - self.start_time

    def __str__(self):
        return f'Course({self.name})'

    def __repr__(self) -> str:
        return f'{self.name[0:3]}'

class Scheduler:

    def __init__(self, beginning = 8, end = 20):
        self.beginning = beginning
        self.end = end                  #needed?
        self.week = [[0 for i in range((self.end-self.beginning)*4)] for i in range(7)]

    def __str__(self) -> str:
        return f'{self.week}'

    def load_file(self, full_path):
        try:
            with open(full_path, 'r') as file:
                self.courses = [Course(line.split(',')) for line in file]
        except FileNotFoundError:
            print('File doesn\'t exist under path: {}'.format(full_path))

    def number_of_occurances(self):
        courses_names = {}
        for course in self.courses:
            if course.name not in courses_names:
                courses_names[course.name] = 1
            else:
                courses_names[course.name] += 1
        for course in self.courses:
            course.count = courses_names[course.name]

    @staticmethod
    def weekdays(day:str):
        weekdays =	{
            'monday': 0,
            'tuesday': 1,
            'wednesday': 2,
            'thursday': 3,
            'friday':4,
            'saturday':5,
            'sunday':6
            }
        return weekdays[day.strip().lower()]

    def course_time(self, start_time, end_time):
        start_int = int(start_time.hour-self.beginning*4 + start_time.minute/15)
        duration = int((end_time - start_time).total_seconds()/60/15)
        return start_int, start_int + duration

    def insert_to_schedule(self):
        #first put immovable
        for course in self.courses:
            if course.count == 1:
                for hour in range(self.course_time(course.start_time, course.end_time)[0],self.course_time(course.start_time, course.end_time)[1]):
                    self.week[self.weekdays(course.day_of_week)][hour] = course

    def get_value(self):
        for day in self.week:
            print(day)
        # print(self.week)
        # print('self.courses_names ', self.courses)

        # print(self.course_time(self.courses[0][3], self.courses[0][4]))

        # time_start = course.start_time.hour*4 + course.start_time.minute/15
        # duration = course.duration
        # print((duration))

