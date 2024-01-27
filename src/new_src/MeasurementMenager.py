from Measurement import Measurement
import pandas as pd
import threading

class MeasurementMenager(threading.Thread):

    Measurements = []

    def __init__(self, pathToExcelFile):
        self.filePath = pathToExcelFile
        dataframe = pd.read_excel(pathToExcelFile)
        input=dataframe.to_numpy()
        self.Measurements.append(Measurement(input))

    def GenerateChars(self, Measurement):
        try:
            self.Measurements[Measurement].plot_fet_parameters()
            return 0
        except IndexError:
            return -1

    def Display(self, Measurement):
        try:
            return self.Measurements[Measurement]
        except IndexError:
            return -1
