from tkinter import *
from tkinter import ttk
import numpy as np

class parameter_window:
    def __init__(self, root):
        self.root = root
        self.mainFrame = ttk.Frame(root, padding="30 30 30 30")
        #self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainFrame.pack(fill=BOTH)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Setup variable store
        # inital array with 0 and one "empty" model
        self.valArray = np.zeros((6,1))

        self.Ion = StringVar()
        self.Ioff = StringVar()
        self.Vt = StringVar()
        self.SS = StringVar()
        self.lamb = StringVar()
        #self.mobility = StringVar()
        self.Ion.set(f'{self.valArray[0][0]:e}')
        self.Ioff.set(f'{self.valArray[1][0]:e}')
        self.Vt.set(f'{self.valArray[2][0]:e}')
        self.SS.set(f'{self.valArray[3][0]:e}')
        self.lamb.set(f'{self.valArray[4][0]:e}')
        #self.mobility.set(f'{self.valArray[5][0]:e}')

        # Setup model choice spinbox
        self.modelChoiceLabel = Label(self.mainFrame, text="Model:")
        self.spinBoxVal = StringVar()
        self.initialModelName = 'No model'
        self.modelList = [self.initialModelName]
        self.modelChoiceSpinbox = ttk.Spinbox(self.mainFrame,
                                              values=self.modelList,
                                              wrap=True,
                                              textvariable=self.spinBoxVal,
                                              command=self.spinboxChangedHandler)
        self.modelChoiceLabel.grid(column=1, row=1)
        self.modelChoiceSpinbox.grid(column=2, row=1, columnspan=2, sticky=E)

        # Setup variable name labels
        self.IonLabel = Label(self.mainFrame, text="Ion")
        self.IoffLabel = Label(self.mainFrame, text="Ioff")
        self.VtLabel = Label(self.mainFrame, text="Vt")
        self.SSLabel = Label(self.mainFrame, text="SS")
        self.lambdaLabel = Label(self.mainFrame, text="\u03BB")
        #self.mobilityLabel = Label(self.mainFrame, text="\u03BDd")
        self.IonLabel.grid(column=1, row=2)
        self.IoffLabel.grid(column=1, row=3)
        self.VtLabel.grid(column=1, row=4)
        self.SSLabel.grid(column=1, row=5)
        self.lambdaLabel.grid(column=1, row=6)
        #self.mobilityLabel.grid(column=1, row=7)

        # Setup variable value labels
        variableLabelWidth = 10
        variableLabelpadx = 5
        self.IonValLabel = Label(self.mainFrame, textvariable=self.Ion, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.IoffValLabel = Label(self.mainFrame, textvariable=self.Ioff, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.VtValLabel = Label(self.mainFrame, textvariable=self.Vt, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.SSValLabel = Label(self.mainFrame, textvariable=self.SS, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.lambdaValLabel = Label(self.mainFrame, textvariable=self.lamb, borderwidth=3, relief="sunken", width=variableLabelWidth)
        #self.mobilityValLabel = Label(self.mainFrame, textvariable=self.mobility, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.IonValLabel.grid(column=2, row=2, sticky=E, pady=10, padx=variableLabelpadx)
        self.IoffValLabel.grid(column=2, row=3, sticky=E, pady=10, padx=variableLabelpadx)
        self.VtValLabel.grid(column=2, row=4, sticky=E, pady=10, padx=variableLabelpadx)
        self.SSValLabel.grid(column=2, row=5, sticky=E, pady=10, padx=variableLabelpadx)
        self.lambdaValLabel.grid(column=2, row=6, sticky=E, pady=10, padx=variableLabelpadx)
        #self.mobilityValLabel.grid(column=2, row=7, sticky=E, pady=10, padx=variableLabelpadx)


        # Setup units labels
        self.IonUintLabel = Label(self.mainFrame, text="A")
        self.IoffUintLabel = Label(self.mainFrame, text="A")
        self.VtUintLabel = Label(self.mainFrame, text="V")
        self.SSUintLabel = Label(self.mainFrame, text="V/dec")
        self.lambdaUintLabel = Label(self.mainFrame, text=" ")
        #self.mobilityUintLabel = Label(self.mainFrame, text="cm2/(V⋅s)")
        self.IonUintLabel.grid(column=3, row=2, sticky=W)
        self.IoffUintLabel.grid(column=3, row=3, sticky=W)
        self.VtUintLabel.grid(column=3, row=4, sticky=W)
        self.SSUintLabel.grid(column=3, row=5, sticky=W)
        self.lambdaUintLabel.grid(column=3, row=6, sticky=W)
        #self.mobilityUintLabel.grid(column=3, row=7, sticky=W)
    def get_parameter_widget(self) -> ttk.Frame:
        return self.mainFrame

    def set_Ion(self, val):
        self.Ion.set(f'{val:e}')

    def set_Ioff(self, val):
        self.Ioff.set(f'{val:e}')

    def set_Vt(self, val):
        self.Vt.set(f'{val:e}')

    def set_SS(self, val):
        self.SS.set(f'{val:e}')

    def set_lambda(self, val):
        self.lamb.set(f'{val:e}')

    # def set_mobility(self, val):
    #    self.mobility.set(f'{val:e}')

    def updateDisplayedVariables(self, modelIndex):
        self.set_Ion(self.valArray[0][modelIndex])
        self.set_Ioff(self.valArray[1][modelIndex])
        self.set_Vt(self.valArray[2][modelIndex])
        self.set_SS(self.valArray[3][modelIndex])
        self.set_lambda(self.valArray[4][modelIndex])
        # self.set_mobility(self.valArray[0][modelIndex])
        pass

    def addModelParameters(self, modelName, Ion, Ioff, Vt, SS, lamb, mobility):
        if self.modelList[0] == self.initialModelName:  # There is no model loaded yet
            self.modelList[0] = modelName
            self.valArray[0][0] = Ion
            self.valArray[1][0] = Ioff
            self.valArray[2][0] = Vt
            self.valArray[3][0] = SS
            self.valArray[4][0] = lamb
            self.valArray[5][0] = mobility
        else:  # there are models loaded, append new model
            self.modelList.append(modelName)
            columnToAdd = np.array([[Ion], [Ioff], [Vt], [SS], [lamb], [mobility]])
            self.valArray = np.append(self.valArray, columnToAdd, axis=1)

        self.modelChoiceSpinbox.configure(values=self.modelList)  # update model list of the spinbox
        # display parameters of currently added model
        modelIndex = self.modelList.index(modelName)  # find index of the model parameters column
        self.updateDisplayedVariables(modelIndex)
        self.modelChoiceSpinbox.set(modelName)

    def removeModelParameters(self, modelName):
        # TODO: dodać wyjątek obsługujący usunięcie nieistniejącego modelu
        modelIndex = self.modelList.index(modelName)
        self.modelList.pop(modelIndex)  # delete selected model name
        self.valArray = np.delete(self.valArray, modelIndex, 1)  # delete selected column
        print(self.spinBoxVal.get())
        if len(self.modelList) > 0:  # there are still models to be displayed
            if self.spinBoxVal.get() == modelName:  # deleted model was displayed
                if modelIndex == 0:  # deleted model was first in the list
                    # display new first model
                    self.modelChoiceSpinbox.set(self.modelList[0])
                    self.updateDisplayedVariables(0)
                else:
                    # display previous element
                    self.modelChoiceSpinbox.set(self.modelList[modelIndex-1])
                    self.updateDisplayedVariables(modelIndex-1)
        else:  # there are no models, set the spinbox to "No model" state
            self.modelList.append(self.initialModelName)
            self.modelChoiceSpinbox.set(self.modelList[0])
            self.valArray = np.zeros((6, 1))

            self.Ion.set(f'{self.valArray[0][0]:e}')
            self.Ioff.set(f'{self.valArray[1][0]:e}')
            self.Vt.set(f'{self.valArray[2][0]:e}')
            self.SS.set(f'{self.valArray[3][0]:e}')
            self.lamb.set(f'{self.valArray[4][0]:e}')
            # self.mobility.set(f'{self.valArray[5][0]:e}')

        self.modelChoiceSpinbox.configure(values=self.modelList)  # update model list of the spinbox

    def spinboxChangedHandler(self):
        currModel = self.modelChoiceSpinbox.get()
        modelIndex = self.modelList.index(currModel)  # find index of the model parameters column
        self.updateDisplayedVariables(modelIndex)
