import pickle

from account import Account


class FileManager():
    DB_FILE_NAME = "data.db"

    def save(self, data):
        with open(self.DB_FILE_NAME, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read(self):
        try:
            return pickle.load(open(self.DB_FILE_NAME, 'rb'))
        except FileNotFoundError:
            return Account()
