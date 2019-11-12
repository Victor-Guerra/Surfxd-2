from sys import argv
from sys import exit
#import csv
from validator import validator
from fileManager import fileManager


if __name__ == "__main__":

    if len(argv) > 1:
        script, score_file = argv

        #csv.register_dialect('scores', delimiter = ',', skipinitialspace = True)

        if validator.validate_path(score_file) and validator.validate_format(score_file):

            confirm = input("Use the provided path? y/n\n")

            if 'n' in confirm or 'N' in confirm:

                print("Exiting...")
                exit(0)

            elif 'y' in confirm or 'Y' in confirm:

                with open('pathname', 'w') as pathfile:
                    pathfile.write(score_file)
                    print('Successfully uploaded path.')
                    exit(0)
        else:
            print("Please, provide a valid file path.")
            exit(0)
    elif len(argv) == 1:
        path = fileManager.get_path()
        lista = fileManager.parse_file(path)
        for elmt in lista:
            print(lista)
            
    

