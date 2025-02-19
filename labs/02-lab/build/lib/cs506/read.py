import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    list = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            toAdd = []
            for item in row:
                toAdd += [item]
            list += [toAdd]
            # list += [[int(row[0]), int(row[1])]]
    # print(list)
    return list

# read_csv("dataset_1.csv")
