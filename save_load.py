import pickle

def saveTr(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)
            
def loadTr(file_name):
    with open(file_name, 'rb') as pickle_file:
        return pickle.load(pickle_file)
