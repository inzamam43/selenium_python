import json
class Utility:
    @staticmethod
    def read_data_file(file_name):
        with open(f"data/{file_name}.json") as file:
            data = json.load(file)
            return data