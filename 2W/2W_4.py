from pprint import pprint

file_path = "./data-01-test-score.CSV"

class ReadCSV():
    def __init__(self, path):
        self.path = path
        self.data = self.read_file()

    def read_file(self):
        with open(self.path, "r") as f:
            lines = f.readlines()
            data = [[int(v) for v in line.strip().split(",")] for line in lines]
        return data

    def merge_list(self):
        return list(map(sum, self.data))


read_csv = ReadCSV(file_path)
pprint(read_csv.read_file())
print(read_csv.merge_list())