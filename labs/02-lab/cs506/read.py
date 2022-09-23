import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    list = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            toAdd = []
            for item in row:
                # print("first char is " + item[0])
                # if (ord(item[0]) >= 97 and ord(item[0]) <= 122) or (ord(item[0]) >= 65 and ord(item[0]) <= 90):
                if (item[0] == "\""):
                    # print("found word")
                    toAdd += [item[1]+item[2]+item[3]]
                else:
                    toAdd += [int(item)]
            list += [toAdd]
            # list += [[int(row[0]), int(row[1])]]
    # print(list)
    return list

# read_csv("dataset_2.csv")
