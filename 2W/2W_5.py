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

    def avg_list(self):
        return sorted(list(map(lambda x: sum(x)/len(x), self.data)))


read_csv = ReadCSV(file_path)
print(read_csv.avg_list())