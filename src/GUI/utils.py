import pandas as pd
from transistors import Transistor

def updata_parameter_window(parameterWindow, t):
    parameterWindow.set_Ion(t.I_on)
    parameterWindow.set_Ioff(t.I_off)
    parameterWindow.set_Vt(t.vth[0])
    parameterWindow.set_SS(t.SS)
    parameterWindow.set_lambda(t.lambda_2[0])

def update_graph_window(graphWindow, t):    
    graphWindow.add_tab("Transfer characteristics", "Transfer characteristics", "X", "Y", t.vgs, t.ids_vgs)
    graphWindow.add_tab("Output characteristics", "Output characteristics", "X", "Y", t.vds, t.ids_vds)
    graphWindow.add_tab("gm", "gm", "X", "Y", t.xgm, t.gm)
    graphWindow.add_tab("gds", "gds", "X", "Y", t.xgds, t.gds)

    graphWindow.remove_tab(0)

def calc_all_data_for_new_file(filename):
    # TODO: Przeniesc
    dataframe1 = pd.read_excel(r'res\FETs.xlsx')
    input=dataframe1.to_numpy()
    t=Transistor(input)
    t.calc_I_on()
    t.calc_I_off()
    t.calc_gm()
    t.calc_dgm()
    t.calc_Vth()
    t.calc_SS()
    t.calc_lambda_()
    t.calc_gds()
    print(t.gds)
    return t