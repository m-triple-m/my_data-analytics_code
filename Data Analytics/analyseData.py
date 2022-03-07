import pandas as pd


class AnalyseData:

    def __init__(self, path):

        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        print('data cleaned')

