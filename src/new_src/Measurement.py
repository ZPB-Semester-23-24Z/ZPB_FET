import numpy as np
import matplotlib.pyplot as plt
import threading

class Measurement(threading.Thread):
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

    def plot_fet_parameters(self):
        Vgs = self.vgs[0:-1]
        gm = self.calc_gm()
        dgm = self.calc_dgm()
        #lamda = self.calc_lambda_()
        gds, xgds = self.calc_gds()

        # Wykres transkonduktancji (gm)
        plt.subplot(2, 2, 1)
        plt.plot(Vgs, gm, label='gm')
        plt.xlabel('Vgs (V)')
        plt.ylabel('gm (S)')
        plt.legend()

        # Wykres pochodnej transkonduktancji (dgm)
        plt.subplot(2, 2, 2)
        plt.plot(Vgs[0:-1], dgm, label='dgm/dVgs')
        plt.xlabel('Vgs (V)')
        plt.ylabel('dgm/dVgs (S/V)')
        plt.legend()

        # Wykres przewodnienia dren-źródło (gds)
        plt.subplot(2, 2, 4)
        plt.plot(xgds, gds, label='gds')
        plt.xlabel('Vgs (V)')
        plt.ylabel('gds (S)')
        plt.legend()

        # Wyświetlenie wykresów
        plt.tight_layout()
        #plt.ion()
        plt.show()
       # plt.draw()
        #plt.pause(0.001)

    def __repr__(self):
        I_on = self.calc_I_on()
        I_off = self.calc_I_off()
        dgm = self.calc_dgm()
        vth = self.calc_Vth()
        ss = self.calc_SS()
        lamda = self.calc_lambda_()
        gds, xgds = self.calc_gds()
    
        return f'I_on:{I_on}\n I_off:{I_off}\n lamda:{lamda[0]} vth:{vth[0]}\n ss:{ss}'

    def __init__(self,input) -> None:
        self.vds=input[1:52,4]
        self.ids_vgs=input[1:72,2]
        self.ids_vds=input[1:52,5:11]
        self.vgs=input[1:72,1]
        pass
    def calc_I_off(self):
        a=np.argmin(abs(self.vgs))
        self.I_off=self.ids_vgs[a]
        return self.I_off
    def calc_I_on(self):
        self.I_on=self.ids_vgs[-1]
        return self.I_on
    def calc_gm(self):
        self.xgm=self.vgs
        a=np.diff(self.ids_vgs,1)
  
        b=np.diff(self.xgm)
    
        c=np.divide(a,b)
   
        self.xgm=self.xgm[1:]
        self.gm=c
        return self.gm
    def calc_gds(self):
        self.xgds=self.vds
        self.gds=[]
        for i in range(0,self.ids_vds.shape[1]):
            #print(i)
            a=np.diff(self.ids_vds[:,i],1)
            b=np.diff(self.xgds)
            c=np.divide(a,b)
            self.gds.append(c)
        self.xgds=self.xgds[1:]
        self.gds=np.array(self.gds).T.tolist()
        return self.gds, self.xgds
        
    def calc_dgm(self):
        self.xdgm=self.vgs
        a=np.diff(self.ids_vgs,2)
        b=np.diff(self.xdgm)[1:]
        c=np.divide(a,b)
        self.xdgm=self.xdgm[2:]
        self.dgm=c
        return self.dgm
    
    def calc_Vth(self):
        a=np.argmax(self.gm)
        b=self.vgs
        c=self.ids_vgs
        p=np.polyfit([b[a-1],b[a],b[a+1]],[c[a-1],c[a],c[a+1]],1)
        Vcross=np.roots(p)
        self.vth=Vcross
        return self.vth
    
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
        return self.SS

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
        return self.lambda_2