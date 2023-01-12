from scheduler.scheduler import Scheduler

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.load_file('(...)/schedul_test.txt')
    scheduler.number_of_occurances()
    scheduler.insert_to_schedule()
    scheduler.get_value()