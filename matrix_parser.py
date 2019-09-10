""" This script has the text parser """

class MatrixParser:
    """ Parse the matrix """

    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = self.set_lines()

    def set_lines(self):
        with open(self.file_path, 'r') as file:
            return [f.replace('\n', '') for f in file]
