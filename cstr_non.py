import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import math
from scipy.integrate import odeint
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk

class cstr_non():

    def calculo(self):
        try:
            self.k1 = float(self.k.get())
            self.Er1 = float(self.Er.get())
            self.F1 = float(self.F.get())
            self.Te1 = float(self.Te.get())
            self.UA1 = float(self.UA.get())
            self.Twe1 = float(self.Twe.get())
            self.Fw1 = float(self.Fw.get())
            self.Hr1 = float(self.Hr.get())
            self.Vr1 = float(self.Vr.get())
            self.Cp1 = float(self.Cp.get())
            self.rhor1 = float(self.rhor.get())
            self.Cpw1 = float(self.Cpw.get())
            self.rhow1 = float(self.rhow.get())
            self.tf1 = float(self.tf.get())
            self.step1 = int(self.step.get())
            self.Vc1 = float(self.Vc.get())
        
            #---reag----
            self.Cae11 = float(self.Cae1.get())
            self.Ca011 = float(self.Ca01.get())
            self.er11 = float(self.er1.get())

            #----prod----
            self.Cce11 = float(self.Cce1.get())
            self.Cc011 = float(self.Cc01.get())
            self.ep11 = float(self.ep1.get())
            R = 8.314

            #---condições iniciais de temperatura
            self.T01 = float(self.Tr0.get())
            self.Tw01 = float(self.Tw0.get())

            #----tempo
            self.t = np.linspace(0,self.tf1,self.step1)
            self.it_r2 = self.rr.get() #seleção do método
            if(self.qtd_cadp <=30 and self.qtd_cads <=30):
                if(self.it_r2 == "Em equilíbrio"):
                    self.Kc1 = float(self.Kc.get()) 
                    def edo1a(x,t,F,Fw,Cae,Cbe,Vr,Vc,k0,E,R,UA,Te,Twe,Hr,esteqr,esteqp,Cpr,Cpw,rhor,rhow,Kc1):
                        Ca = x[0]
                        Cb = x[1]
                        T = x[2]
                        Tw = x[3]
                        k = k0*math.exp(-E/(R*T))
                        dCadt = F*(Cae - Ca)/Vr - k*(Ca**esteqr - (Cb**esteqp)/Kc1)/esteqp
                        dCbdt = F*(Cbe - Cb)/Vr + k*(Ca**esteqr - (Cb**esteqp)/Kc1)/esteqr
                        dTdt =  F*(Te - T)/Vr - UA*(T - Tw)/(rhor*Cpr*Vr) - k*(Ca**esteqr - (Cb**esteqp)/Kc1)*Hr*Vr/(rhor*Vr*Cpr)
                        dTwdt = Fw*(Twe - Tw)/Vc + UA*(T - Tw)/(rhow*Cpw*Vc)
                        return [dCadt,dCbdt,dTdt,dTwdt]
                    self.y = odeint(edo1a,[self.Ca011,self.Cc011,self.T01,self.Tw01],self.t,args=(self.F1,self.Fw1,self.Cae11,self.Cce11,self.Vr1,self.Vc1,self.k1,self.Er1,R,self.UA1,self.Te1,self.Twe1,self.Hr1,self.er11,self.ep11,self.Cp1,self.Cpw1,self.rhor1,self.rhow1,self.Kc1))
                    
                else:
                    def edo1(x,t,F,Fw,Cae,Cbe,Vr,Vc,k0,E,R,UA,Te,Twe,Hr,esteqr,esteqp,Cpr,Cpw,rhor,rhow):
                        Ca = x[0]
                        Cb = x[1]
                        T = x[2]
                        Tw = x[3]
                        k = k0*math.exp(-E/(R*T))
                        dCadt = F*(Cae - Ca)/Vr - k*(Ca**esteqr)/esteqp
                        dCbdt = F*(Cbe - Cb)/Vr + k*(Ca**esteqr)/esteqr
                        dTdt =  F*(Te - T)/Vr - UA*(T - Tw)/(rhor*Cpr*Vr) - k*(Ca**esteqr)*Hr*Vr/(rhor*Vr*Cpr)
                        dTwdt = Fw*(Twe - Tw)/Vc + UA*(T - Tw)/(rhow*Cpw*Vc)
                        return [dCadt,dCbdt,dTdt,dTwdt]
                    self.y = odeint(edo1,[self.Ca011,self.Cc011,self.T01,self.Tw01],self.t,args=(self.F1,self.Fw1,self.Cae11,self.Cce11,
                    self.Vr1,self.Vc1,self.k1,self.Er1,R,self.UA1,self.Te1,self.Twe1,self.Hr1,self.er11,self.ep11,self.Cp1,self.Cpw1,self.rhor1,self.rhow1))
                
                self.fig = Figure(figsize=(9.9,5.25),dpi=51)
                self.fig.patch.set_facecolor('xkcd:tan')
                self.a_r1 = self.fig.add_subplot(111)
                self.a_r1.grid(True)
                self.a_r1.set_xlabel('Tempo (s)',fontsize=18)
                self.a_r1.set_ylabel('Concentração (mol/m³)',fontsize=18)
                self.a_r1.set_title('Perfil reacional de concentração',fontsize=22)
                self.a_r1.plot(self.t,self.y[:,0],'b',self.t,self.y[:,1],'r')
                self.a_r1.legend(['Concentração de Reagente','Concentração de Produto'],fontsize=16)
                self.a_r1.tick_params(axis='both', which='major', labelsize=15)
                self.canvas = FigureCanvasTkAgg(self.fig,master=self.frame2)
                self.canvas.get_tk_widget().place(relx=0.02,rely=0.02)
                self.canvas.draw()

                self.fig2 = Figure(figsize=(9.9,5.25),dpi=51)
                self.fig2.patch.set_facecolor('xkcd:tan')
                self.a_r12 = self.fig2.add_subplot(111)
                self.a_r12.grid(True)
                self.a_r12.set_xlabel('Tempo (s)',fontsize=18)
                self.a_r12.set_ylabel('Concentração (mol/m³)',fontsize=18)
                self.a_r12.set_title('Perfil reacional de temperatura',fontsize=22)
                self.a_r12.plot(self.t,self.y[:,2],'g',self.t,self.y[:,3],'y')
                self.a_r12.legend(['Temperatura no reator','Temperatura na camisa'],fontsize=16)
                self.a_r12.tick_params(axis='both', which='major', labelsize=15)
                self.canvas2 = FigureCanvasTkAgg(self.fig2,master=self.frame2)
                self.canvas2.get_tk_widget().place(relx=0.53,rely=0.02)
                self.canvas2.draw()

                self.dfedo1 = pd.DataFrame([self.t,self.y[:,0],self.y[:,1],self.y[:,2],self.y[:,3]]).T
                self.dfedo1.columns = ["Tempo (s)","Concentração de Reagente (mol/m³)","Concentração de produto (mol/m³)","T(K)","Tw(K)"]
                
                self.listaCli.delete(*self.listaCli.get_children())
                for i,j,k,o,p in zip(list(self.t),list(self.y[:,0]),list(self.y[:,1]),list(self.y[:,2]),list(self.y[:,3])):
                    self.listaCli.insert("","end",values = ("{:.2f}".format(i),"{:.2f}".format(j),"-","{:.2f}".format(k),"-",
                                                            "{:.2f}".format(o),"{:.2f}".format(p)))

            #2 reagentes e 1 produto
            if(self.qtd_cads > 30 and self.qtd_cadp <=30):
                 #---reag----
                self.Cbe11 = float(self.Cbe1.get())
                self.Cb011 = float(self.Cb01.get())
                self.er12 = float(self.er2.get())
                def edo2(x,t,F,Fw,Cae,Cbe,Vr,Vc,k0,E,R,UA,Te,Twe,Hr,esteqr,esteqp,Cpr,Cpw,rhor,rhow,Cce,esteqr1):
                    Ca = x[0]
                    Cb = x[2]
                    Cc = x[1]
                    T = x[3]
                    Tw = x[4]
                    k = k0*math.exp(-E/(R*T))
                    rA = k*(Ca**esteqr)*(Cc**esteqr1)
                    dCadt = F*(Cae - Ca)/Vr - rA/esteqp #reagente 1
                    dCbdt = F*(Cbe - Cb)/Vr + rA/esteqr #produto 1
                    dCcdt = F*(Cce - Cc)/Vr - rA/esteqp #reagente 2
                    dTdt =  F*(Te - T)/Vr - UA*(T - Tw)/(rhor*Cpr*Vr) - rA*Hr*Vr/(rhor*Vr*Cpr)
                    dTwdt = Fw*(Twe - Tw)/Vc + UA*(T - Tw)/(rhow*Cpw*Vc)
                    return [dCadt,dCbdt,dCcdt,dTdt,dTwdt]
                
                self.y = odeint(edo2,[self.Ca011,self.Cc011,self.Cb011,self.T01,self.Tw01],self.t,args=(self.F1,self.Fw1,
                self.Cae11,self.Cce11,self.Vr1,self.Vc1,self.k1,self.Er1,R,self.UA1,self.Te1,self.Twe1,self.Hr1,self.er11,self.ep11,self.Cp1,self.Cpw1,self.rhor1,
                self.rhow1,self.Cbe11,self.er12))
                self.fig = Figure(figsize=(9.9,5.25),dpi=51)
                self.fig.patch.set_facecolor('xkcd:tan')
                self.a_r1 = self.fig.add_subplot(111)
                self.a_r1.grid(True)
                self.a_r1.set_xlabel('Tempo (s)',fontsize=18)
                self.a_r1.set_ylabel('Concentração (mol/m³)',fontsize=18)
                self.a_r1.set_title('Perfil reacional de concentração',fontsize=22)
                self.a_r1.plot(self.t,self.y[:,0],'b',self.t,self.y[:,1],'r',self.t,self.y[:,2],'y')
                self.a_r1.legend(['Concentração de Reagente A','Concentração de Produto','Concentração de Reagente B'],fontsize=16)
                self.a_r1.tick_params(axis='both', which='major', labelsize=15)
                self.canvas = FigureCanvasTkAgg(self.fig,master=self.frame2)
                self.canvas.get_tk_widget().place(relx=0.02,rely=0.02)
                self.canvas.draw()

                self.fig2 = Figure(figsize=(9.9,5.25),dpi=51)
                self.fig2.patch.set_facecolor('xkcd:tan')
                self.a_r12 = self.fig2.add_subplot(111)
                self.a_r12.grid(True)
                self.a_r12.set_xlabel('Tempo (s)',fontsize=18)
                self.a_r12.set_ylabel('Concentração (mol/m³)',fontsize=18)
                self.a_r12.set_title('Perfil reacional de temperatura',fontsize=22)
                self.a_r12.plot(self.t,self.y[:,3],'r',self.t,self.y[:,4],'b')
                self.a_r12.legend(['Temperatura no reator','Temperatura na camisa'],fontsize=16)
                self.a_r12.tick_params(axis='both', which='major', labelsize=15)
                self.canvas2 = FigureCanvasTkAgg(self.fig2,master=self.frame2)
                self.canvas2.get_tk_widget().place(relx=0.53,rely=0.02)
                self.canvas2.draw()

                self.dfedo1 = pd.DataFrame([self.t,self.y[:,0],self.y[:,1],self.y[:,2],self.y[:,3],self.y[:,4]]).T
                self.dfedo1.columns = ["Tempo (s)","Concentração de Reagente A(mol/m³)","Concentração de produto (mol/m³)",
                                       "Concentração de Reagente B(mol/m³)","T(K)","Tw(K)"]
                #print(self.dfedo1)
        except ValueError:
            messagebox.showinfo("Simulador de reações químicas","Há campos não preenchidos")

    def exportar(self):
        #print(self.dfedo1)
        self.dfedo1.to_excel("Resultado_modelagem.xlsx")
        messagebox.showinfo("Simulador de reações químicas","Exportação realizada com sucesso")
            

    
