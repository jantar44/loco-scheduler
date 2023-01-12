import pandas as pd

class File:
    def __init__(self):
        pass

    def load_file(self):
        try:
            return pd.read_csv(self.full_path)
        except FileNotFoundError:
            print('File doesn\'t exist under path: {}'.format(self.full_path))
