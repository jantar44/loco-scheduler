from datetime import datetime, time

class Course:

    _courses = []

    def __init__(self, line) -> None:
        self.name = line[0].strip().capitalize()
        self.day_of_week = line[1].strip().lower()
        self.start_time = datetime.strptime(line[2].strip(),'%H:%M')
        self.end_time =  datetime.strptime(line[3].strip(),'%H:%M')
        self.duration = self.end_time - self.start_time
        self.assigned = False

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'{self.name[0:3]}'

    def get_count(self):
        return self.count

    def is_assigned(self):
        return self.assigned

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
        self.courses

    def sort_courses_by_number(self):
        self.courses.sort(key = lambda x: x.get_count())

    @staticmethod
    def weekdays_to_int(day:str) -> int:
        weekdays =	{'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
        return weekdays[day.strip().lower()]

    @staticmethod
    def int_to_weekdays(day:int) -> str:
            weekdays =	{0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
            return weekdays[day]

    def get_slot_of_time(self, time:datetime) -> int:
        slot = int((time.hour-self.beginning)*4 + time.minute/15)
        return slot

    def get_time_of_slot(self, slot:int) -> str:
        hour = slot//4 + self.beginning
        min = slot%4 * 15
        f"{min:02}"
        return '{}:{}'.format(f"{hour:02}", f"{min:02}")

    # def slot_not_occupied(self, slot, day, hour):
    #     if slot != 0:
    #         print('In {} at {} there is already a course.'.format(day.capitalize(), self.get_time_of_slot(hour)))
    #         return False
    #     else:
    #         return True

    def reset_slot(self, slots:tuple, day:int):
        for time in range(slots[0], slots[1]):
            self.week[day][time] = 0

    def set_slot(self, slots:list, day:int, course:Course):
        for time in range(slots[0], slots[1]):
            self.week[day][time] = course

    def insert_course(self, course):
        slots = []
        start_time, duration = self.get_slot_of_time(course.start_time), int(course.duration.total_seconds()/60/15)
        for hour in range(start_time, start_time + duration):
            existing_slot = self.week[Scheduler.weekdays_to_int(course.day_of_week)][hour]
            if existing_slot == 0:
                slots.append((course,hour))
            else:
                print(f'{course.name} - In {course.day_of_week.capitalize()} at {self.get_time_of_slot(hour)} there is already a course - {existing_slot}.')

        if len(slots) == course.duration.total_seconds()/60/15:
            self.set_slot([slots[0][1],slots[-1][1]], Scheduler.weekdays_to_int(course.day_of_week), slots[0][0])
            course.assigned = True

    def unmovable_to_schedule(self):
        self.sort_courses_by_number()
        for course in self.courses:
            if course.get_count() == 1:
                self.insert_course(course)

    def get_value(self):
        for day in self.week:
            print(day)




        # print(self.week)
        # print('self.courses_names ', self.courses)

        # print(self.course_time(self.courses[0][3], self.courses[0][4]))

        # time_start = course.start_time.hour*4 + course.start_time.minute/15
        # duration = course.duration
        # print((duration))
