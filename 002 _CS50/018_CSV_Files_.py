# Edit This To Make it Dict
import csv

file = open("PhoneBook.csv" , "a")
# file = open("PhoneBook.csv" , "a") as file # Here We Can Ignor  => file.close()

name = input("Enter The Name You Want To Add ")
nmuber = input("Enter The Number You Want To Add ")

writer = csv.writer(file)
writer.writerow([ f"{name}", f"{nmuber}"])

file.close()
