import pandas as pd
class vgs_sweep:
    VGS=[]
    IDS=[]
    VDS=0
    def load(self,input):
        self.VGS=input.iloc[1:,1].dropna().to_list()
        self.IDS=input.iloc[1:,2].dropna().to_list()
class multi_vgs_vds_sweep:
    VGS=[]
    VDS=[]
    IDS=[]

    def load(self,input):
        self.VGS=[0, 1, 2, 3, 4, 5]
        self.VDS=input.iloc[1:,4].dropna().to_list()
        for i in range(0,6):
            self.IDS.append(input.iloc[1:,5+i].dropna().to_list())
class measurement:
    vgs_sweep=vgs_sweep()
    multi_vgs_vds_sweep=multi_vgs_vds_sweep()
    def load(self,input):
        self.vgs_sweep.load(input)
        self.multi_vgs_vds_sweep.load(input)