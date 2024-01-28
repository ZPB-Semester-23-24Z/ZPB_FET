import pandas as pd
from transistors import Transistor
from scipy.optimize import curve_fit
import numpy as np
from scipy.interpolate import CubicSpline
def updata_parameter_window(parameterWindow, t):
    parameterWindow.set_Ion(t.I_on)
    parameterWindow.set_Ioff(t.I_off)
    parameterWindow.set_Vt(t.vth[0])
    parameterWindow.set_SS(t.SS)
    parameterWindow.set_lambda(t.lambda_2[0])
   
def update_model(parameterWindow,t):
    a=[]
    for i in parameterWindow.Transistors:
        a.append(i.name)
    parameterWindow.modelDropdown['values']=a
    parameterWindow.modelList=a
    parameterWindow.modelDropdown.set(a[-1])

def update_graph_window(graphWindow, t):
    graphWindow.clear_tabs()    
    graphWindow.add_tab("Transfer characteristics", "Transfer characteristics", "X", "Y", t.vgs, t.ids_vgs)
    graphWindow.add_tab("Transfer characteristics-log", "Transfer characteristics-log", "X", "Y", t.vgs, t.ids_vgs,log=True)
    graphWindow.add_tab("Output characteristics", "Output characteristics", "X", "Y", t.i_vds, t.i_ids_vds)
    graphWindow.add_tab("gm", "gm", "X", "Y", t.xgm, t.gm)
    graphWindow.add_tab("gds", "gds", "X", "Y", t.xgds, t.gds)
    #graphWindow.remove_tab(0)

def calc_all_data_for_new_file(filename):
    # TODO: Przeniesc
    dataframe1 = pd.read_excel(filename)
    input=dataframe1.to_numpy()
    t=Transistor(input, filename.split("/")[-1].split(".")[0])
    t.interpolate_gds()
    t.interpolate_ivgs()
    t.calc_I_on()
    t.calc_I_off()
    t.calc_gm()
    t.calc_dgm()
    t.calc_Vth()
    t.calc_SS()
    t.calc_lambda_()
    t.calc_gds()
    #print(t.gds)
    return t