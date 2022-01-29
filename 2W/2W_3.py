file_path = "./data-01-test-score.CSV"

def read_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
        data = [line.strip().split(",") for line in lines]
        return data


print(read_file(file_path))