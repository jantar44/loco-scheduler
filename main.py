from scheduler.scheduler import Scheduler
from scheduler.path import Path

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.load_file(Path.path)
    scheduler.number_of_occurances()
    scheduler.unmovable_to_schedule()
    scheduler.get_value()
