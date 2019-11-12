import csv
from participant import Participant

class fileManager:
    def __init__(self):
        pass

    @staticmethod
    def get_path():
        """Retreives the path to the file\n
        to evaluate from the file it is \nstored in"""
        try:
            with open('pathname', 'r') as pathfile:
                path = pathfile.readline()
                pathfile.close()
                return path
        except FileNotFoundError:
            print("No valid path was found.")
            exit(0)
                

    @staticmethod
    def parse_file(path):
        pathfile = open(str(path), 'r')
        reader = csv.reader(pathfile)
        lista = []
        for row in reader:
            print(row)
            lista.append(Participant(row[0],row[1]))

        return lista
       #Reader es el straight up diccionario, hay que meter los elementos
       #En objetos de tipo Participant y hacer una lista de ellos.

