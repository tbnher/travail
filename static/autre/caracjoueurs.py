import csv
import random as rd

with open('./Joueur.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
    csv_reader = csv.reader(read_obj)
    csv_writer = csv.writer(write_obj)
    for row in csv_reader:
        # Append the default text in the row / list
        age = rd.randint(10,35)
        row.append(age)
        if age<18:
            row.append("Junior")
        else:
            row.append("Adulte")

        row.append(rd.randint(30,100))
        row.append(rd.randint(30,100))
        row.append(rd.randint(30,100))
        row.append(rd.randint(30,100))
        row.append(rd.randint(30,100))
        row.append(rd.randint(30,100))
        # Add the updated row / list to the output file
        csv_writer.writerow(row)
