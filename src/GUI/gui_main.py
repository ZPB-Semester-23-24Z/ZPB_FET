from tkinter import *
from tkinter import ttk
from menu_bar import *
from graph_window import *
from parameter_window import *
import numpy as np
import pandas as pd




class Transistor:
    xgm=0
    xdgm=0
    xgds=0
    gm=0
    SS=0
    dgm=0
    vth=0
    vgs=0
    ids_vgs=0
    ids_vds=0
    vds=0
    I_off=0
    I_on=0
    lambda_=0
    lambda_2=0
    VGS=[0,1,2,3,4,5]

    def __init__(self,input) -> None:
        self.vds=input[1:52,4]
        self.ids_vgs=input[1:72,2]
        self.ids_vds=input[1:52,5:11]
        self.vgs=input[1:72,1]
        pass
    def calc_I_off(self):
        a=np.argmin(abs(self.vgs))
        self.I_off=self.ids_vgs[a]
    def calc_I_on(self):
        self.I_on=self.ids_vgs[-1]
    def calc_gm(self):
        self.xgm=self.vgs
        a=np.diff(self.ids_vgs,1)
  
        b=np.diff(self.xgm)
    
        c=np.divide(a,b)
   
        self.xgm=self.xgm[1:]
        self.gm=c
    def calc_gds(self):
        self.xgds=self.vds
        self.gds=[]
        for i in range(0,self.ids_vds.shape[1]):
            print(i)
            a=np.diff(self.ids_vds[:,i],1)
            b=np.diff(self.xgds)
            c=np.divide(a,b)
            self.gds.append(c)
        self.xgds=self.xgds[1:]
        self.gds=np.array(self.gds).T.tolist()
        

    def calc_dgm(self):
        self.xdgm=self.vgs
        a=np.diff(self.ids_vgs,2)
        b=np.diff(self.xdgm)[1:]
        c=np.divide(a,b)
        self.xdgm=self.xdgm[2:]
        self.dgm=c
    def calc_Vth(self):
        a=np.argmax(self.gm)
        b=self.vgs
        c=self.ids_vgs
        p=np.polyfit([b[a-1],b[a],b[a+1]],[c[a-1],c[a],c[a+1]],1)
        Vcross=np.roots(p)
        self.vth=Vcross
    def calc_SS(self):
        a=self.vgs
        b=self.ids_vgs.tolist()

        c=np.divide(np.diff(a),np.diff(np.log10(b)))
        SSc=c
        d=np.argmin(abs(a-self.vth+25e-3))
        e=np.argmin(abs(a-25e-3))
        f=SSc[e+1:d+1]
        g=np.average(f)
        self.SS=g
    def calc_lambda_(self):
        #a=np.diff(self.vds)
        #b=np.diff(np.transpose(self.ids_vds))
        #c=np.divide(b,a)
        d=[]
        g=[]
        h=[]
        k=self.VGS
        e=self.vds
        f=self.ids_vds
        m=[]
        #self.lambda_=np.divide(b,np.transpose(self.ids_vds[1:,]))
        for j in range(0,f.shape[1]):
            d=[]
            hh=k[j]-self.vth+50e-3
            h=max(hh[0],100e-3)
            m.append(np.argmin(abs(e-h)))
            for i in range(0,len(self.vds)-1 ): 
                d.append(np.divide((f[i+1,j]-f[i,j]),(f[i,j]*e[i+1]-f[i+1,j]*e[i])))
            g.append(np.transpose(d))
        
        
        n=[]
        for j in range(0,f.shape[1]):
            #print(g[j][m[j]:])
            n.append(np.average(g[j][m[j]:]))

       
            
        
        self.lambda_2=n



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
root = Tk()
root.title("ZPB FET")

# Add menu bar to the program window
menu = menu_bar(root)
root.config(menu=menu.get_menu_bar())

# Create paned window for display widgets
pw = PanedWindow(orient='horizontal')
# Insert display widgets into paned window
# Graph window
graphWindow = graph_window(pw)
pw.add(graphWindow.get_graph_widget())

# Parameters display
parameterWindow = parameter_window(pw)
pw.add(parameterWindow.get_parameter_widget())
parameterWindow.set_Ion(t.I_on)
parameterWindow.set_Ioff(t.I_off)
parameterWindow.set_Vt(t.vth[0])
parameterWindow.set_SS(t.SS)
parameterWindow.set_lambda(t.lambda_2[0])

pw.pack(fill=BOTH, expand=True)
pw.configure(sashrelief=RAISED)

# Setup dummy data
xdata = np.arange(0, 3, .01)
ydata = 2 * np.sin(2 * np.pi * xdata)

graphWindow.add_tab("Transfer characteristics", "Transfer characteristics", "X", "Y", t.vgs, t.ids_vgs)
graphWindow.add_tab("Output characteristics", "Output characteristics", "X", "Y", t.vds, t.ids_vds)
graphWindow.add_tab("gm", "gm", "X", "Y", t.xgm, t.gm)
graphWindow.add_tab("gds", "gds", "X", "Y", t.xgds, t.gds)

graphWindow.remove_tab(0)


root.mainloop()
