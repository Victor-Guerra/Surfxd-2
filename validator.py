import csv

class validator:
    def __init__(self):
        pass

    @staticmethod
    def validate_path(path):
        """Checks the existence of the provided file path"""
        try:
            faile = open(path)
            faile.close()
            return True
        except FileNotFoundError:
            return False

        #return os.path.exists(path)

    @staticmethod
    def validate_format(path):
        """Checks if the provided file path is actually\nin a csv format"""
        if ".csv" in path:
            return True
        else:
            return False
