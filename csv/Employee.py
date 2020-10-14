import csv
class Employee:

    def __init__(self, filename):
        self._filename = filename

    def read_all(self):
        results = []
        with open(self._filename, newline='\n') as csvfile:
            datas = csv.reader(csvfile, delimiter=',')
            for row in datas:
                results.append(row)
        return results

if __name__ == '__main__':
    e = Employee('employees.csv')
    datas = e.read_all()
    for row in datas:
        print(row[0], row[1])