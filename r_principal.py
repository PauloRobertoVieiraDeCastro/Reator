from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate
import webbrowser
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import cstr_non
from placeholder import EntPlaceHold


root = tix.Tk() #instanciando a classe tk

class Principal(cstr_non.cstr_non):
    def __init__(self):
        self.root = root
        self.nome_fantasia3 = StringVar()
        self.tela_principal()
        self.frame_da_tela()
        self.w_frame_1()
        self.grafi()
        self.Menus()
        self.root.mainloop()

    def tela_principal(self):
        """
        Configurando a tela
        """
        self.root.title("Cálculo de reatores")
        self.a = '#D1B26F'#'#C79FEF'#'#380282'#'slate blue'
        self.aa = 'black'
        self.root.configure(background=self.a)#'#1e3743')
        self.root.geometry("1050x700") #geometria inicial
        self.root.resizable(True,True) #redimensiona nos eixos
        self.root.maxsize(width=1150,height=650) #dimensões máximas
        self.root.minsize(width=1150,height=600)#dimensões mínimas

        #mudo o favicon
        self.favicon = PhotoImage(file = "eng.png")
        self.root.iconphoto(False,self.favicon)

    def frame_da_tela(self):
        
        self.frame1 = Frame(self.root, bd=4,bg=self.a,highlightbackground = self.aa) #crio uma borda, uma cor de background, uma cor de borda e uma espessura de borda
        self.frame1.place(relx = 0.01, rely = 0.0, relwidth = 0.98, relheight=0.53)

        self.frame2 = Frame(self.root, bd=4,bg=self.a,
                            highlightbackground = self.aa,highlightthickness=3) #crio uma borda, uma cor de background, uma cor de borda e uma espessura de borda
        self.frame2.place(relx = 0.01, rely = 0.54, relwidth = 0.98, relheight=0.44)

    def w_frame_1(self):
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba3 = Frame(self.abas)
        self.aba1.configure(background=self.a)
        self.aba2.configure(background=self.a)
        self.aba3.configure(background=self.a)
        self.abas.add(self.aba1, text = "Entrada de dados do reator")
        self.abas.add(self.aba2, text = "Entrada de reagentes e produtos")
        self.abas.add(self.aba3, text = "Resultados tabulares")

        self.abas.place(relx=0,rely=0,relwidth=1.0,relheight=1.0)
        
        
        #Entradas e labels-------------------------------------------------------------------------------------------------------------------------------------------
    
        #-------------------------------------------eVENTO CODIGO--------------------------------------------
        Label(self.aba1,text="Constante reacional",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.02,rely=0.02)
        self.k = EntPlaceHold(self.aba1,"Em SI",font = ('verdana', 9),justify="center")
        self.k.place(relx=0.02,rely=0.1)
        
        
        #-------------------------------------------------------FINAL DO AUTOCOMPLETE POR NOME----------------------------------------------
        
        Label(self.aba1,text="Energia de ativação",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.02,rely=0.2)
        self.Er = EntPlaceHold(self.aba1,"Em J/mol",font = ('verdana', 9),justify="center")
        self.Er.place(relx=0.02,rely=0.28)

        Label(self.aba1,text="Vazão de entrada no reator",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.02,rely=0.38)
        self.F = EntPlaceHold(self.aba1,"Em m³/s",font = ('verdana', 9),justify="center")
        self.F.place(relx=0.02,rely=0.46)

        Label(self.aba1,text="Temperatura de entrada no reator",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.02,rely=0.56)
        self.Te = EntPlaceHold(self.aba1,"Em K",font = ('verdana', 9),justify="center")
        self.Te.place(relx=0.02,rely=0.64)
       
        Label(self.aba1,text="Valor de UA",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.02,rely=0.74)
        self.UA = EntPlaceHold(self.aba1,"Em J/s.K",font = ('verdana', 9),justify="center")
        self.UA.place(relx=0.02,rely=0.82)

        Label(self.aba1,text="Temperatura de entrada na camisa",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.26,rely=0.02)
        self.Twe = EntPlaceHold(self.aba1,"Em K",font = ('verdana', 9),justify="center")#Entry(self.aba1,font = ('verdana', 9),justify="center")
        self.Twe.place(relx=0.26,rely=0.1)

        Label(self.aba1,text="Vazão de entrada na camisa",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.26,rely=0.2)
        self.Fw = EntPlaceHold(self.aba1,"Em m³/s",font = ('verdana', 9),justify="center")#Entry(self.aba1,font = ('verdana', 9),justify="center")
        self.Fw.place(relx=0.26,rely=0.28)

        Label(self.aba1,text="Variação de entalpia reacional",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.26,rely=0.38)
        self.Hr = EntPlaceHold(self.aba1,"Em J/mol",font = ('verdana', 9),justify="center")
        self.Hr.place(relx=0.26,rely=0.46)

        Label(self.aba1,text="Volume do reator",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.26,rely=0.56)
        self.Vr = EntPlaceHold(self.aba1,"Em m³",font = ('verdana', 9),justify="center")#Entry(self.aba1,font = ('verdana', 9),justify="center")
        self.Vr.place(relx=0.26,rely=0.64)

        Label(self.aba1,text="Cp do líquido no reator",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.26,rely=0.74)
        self.Cp = EntPlaceHold(self.aba1,"Em J/kg.K³",font = ('verdana', 9),justify="center")
        self.Cp.place(relx=0.26,rely=0.82)

        Label(self.aba1,text="Densidade do líquido no reator",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.5,rely=0.02)
        self.rhor = EntPlaceHold(self.aba1,"Em kg/m³",font = ('verdana', 9),justify="center")#Entry(self.aba1,font = ('verdana', 9),justify="center")
        self.rhor.place(relx=0.5,rely=0.1)

        Label(self.aba1,text="Cp do líquido na camisa",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.5,rely=0.2)
        self.Cpw = EntPlaceHold(self.aba1,"Em J/kg.K³",font = ('verdana', 9),justify="center")
        self.Cpw.place(relx=0.5,rely=0.28)

        Label(self.aba1,text="Densidade do líquido na camisa",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.5,rely=0.38)
        self.rhow = EntPlaceHold(self.aba1,"Em kg/m³",font = ('verdana', 9),justify="center")
        self.rhow.place(relx=0.5,rely=0.46)

        Label(self.aba1,text="Tempo final de reação",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.5,rely=0.56)
        self.tf = EntPlaceHold(self.aba1,"Em s",font = ('verdana', 9),justify="center")
        self.tf.place(relx=0.5,rely=0.64)

        Label(self.aba1,text="Número de passos",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.5,rely=0.74)
        self.step = EntPlaceHold(self.aba1,"Número inteiro",font = ('verdana', 9),justify="center")
        self.step.place(relx=0.5,rely=0.82)

        Label(self.aba1,text="Temperatura inicial do reator",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.74,rely=0.02)
        self.Tr0 = EntPlaceHold(self.aba1,"Em K",font = ('verdana', 9),justify="center")#Entry(self.aba1,font = ('verdana', 9),justify="center")
        self.Tr0.place(relx=0.74,rely=0.1)

        Label(self.aba1,text="Temperatura inicial da camisa",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.74,rely=0.2)
        self.Tw0 = EntPlaceHold(self.aba1,"Em K",font = ('verdana', 9),justify="center")
        self.Tw0.place(relx=0.74,rely=0.28)

        Label(self.aba1,text="Volume da camisa",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.74,rely=0.38)
        self.Vc = EntPlaceHold(self.aba1,"Em m³",font = ('verdana', 9),justify="center")
        self.Vc.place(relx=0.74,rely=0.46)

        self.met1 = ['Irreversível','Em equilíbrio']
        self.rr= StringVar()
        Spinbox(self.aba1,values=self.met1,justify = "center",textvariable=self.rr,command=self.evento).place(relx = 0.74,rely = 0.64,relwidth= 0.15) 
        Label(self.aba1,text="Tipo de reação",bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.74,rely=0.56)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------Inserindo na aba2 - produtos e reagentes----------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.aba2,text="Reagentes",bg=self.a,font = ('Helvetica', 15, 'bold'),fg=self.aa).place(relx=0.215,rely=0.02)
        Label(self.aba2,text="Produtos",bg=self.a,font = ('Helvetica', 15, 'bold'),fg=self.aa).place(relx=0.675,rely=0.02)

        Termos_r = ["Concent de entrada","Concentração Inicial","Estequiometria"]
        kk = 0.12
        for i in Termos_r:
            Label(self.aba2,text=i,bg=self.a,font = ('Helvetica', 10, 'bold'),fg=self.aa).place(relx=-0.06+kk,rely=0.15)
            kk+=0.14

        self.Cae1 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ('verdana', 9),justify="center")
        self.Cae1.place(relx=0.08,rely=0.23,relwidth=0.08)
        self.Ca01 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ('verdana', 9),justify="center")
        self.Ca01.place(relx=0.22,rely=0.23,relwidth=0.08)
        self.er1 = EntPlaceHold(self.aba2,"Coeficiente",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ('verdana', 9),justify="center")
        self.er1.place(relx=0.345,rely=0.23,relwidth=0.08)
            
        Termos_r = ["Concent de entrada","Concentração Inicial","Estequiometria"]
        kkr = 0.12
        for i in Termos_r:
            Label(self.aba2,text=i,bg=self.a,font = ('Helvetica', 10, 'bold'),fg=self.aa).place(relx=0.4+kkr,rely=0.15)
            kkr+=0.14
        self.Cce1 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ('verdana', 9),justify="center")
        self.Cce1.place(relx=0.54,rely=0.23,relwidth=0.08)
        self.Cc01 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ('verdana', 9),justify="center")
        self.Cc01.place(relx=0.68,rely=0.23,relwidth=0.08)
        self.ep1 = EntPlaceHold(self.aba2,"Coeficiente",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ('verdana', 9),justify="center")
        self.ep1.place(relx=0.805,rely=0.23,relwidth=0.08)
        
        Button(self.aba2,command=self.calculo,text="Iniciar simulação",width=16,font=('verdana',10,'bold'),bg='gray',fg='white').place(relx=0.42,rely=0.76)
        Button(self.aba2,command=self.exportar,text="Exportar resultados",width=16,font=('verdana',10,'bold'),bg='gray',fg='white').place(relx=0.42,rely=0.89)
        Button(self.aba2,command=self.adicionars,text="Adicionar reagente",width=16,font=('verdana',9,'bold'),bg='gray',fg='white').place(relx=0.2,rely=0.46)
        Button(self.aba2,command=self.removers,text="Remover reagente",width=16,font=('verdana',9,'bold'),bg='gray',fg='white').place(relx=0.2,rely=0.56)
        Button(self.aba2,command=self.adicionarp,text="Adicionar produto",width=16,font=('verdana',9,'bold'),bg='gray',fg='white').place(relx=0.65,rely=0.46)
        Button(self.aba2,command=self.removerp,text="Remover produto",width=16,font=('verdana',9,'bold'),bg='gray',fg='white').place(relx=0.65,rely=0.56)

        

        ##----------------------------tabela----------------------------------------------------------------------------------------------------------------
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica",10,"bold"),bg="blue",justify='center')
        self.listaCli = ttk.Treeview(self.aba3, height=2,
                                     column=("Tempo (s)","Reagente A (mol/m³)","Reagente B (mol/m³)","Produto A (mol/m³)",
                                             "Produto B (mol/m³)","Temperatura do reator (K)","Temperatura da camisa (K)"),selectmode='browse')

        self.listaCli["columns"] = ("1", "2","3","4","5","6","7")
        self.listaCli['show'] = 'headings'
        self.listaCli.heading("#1", text="Tempo (s)")
        self.listaCli.heading("#2", text="Reagente A (mol/m³)")
        self.listaCli.heading("#3", text="Reagente B (mol/m³)")
        self.listaCli.heading("#4", text="Produto A (mol/m³)")
        self.listaCli.heading("#5", text="Produto B (mol/m³)")
        self.listaCli.heading("#6", text="Temperatura do reator (K)")
        self.listaCli.heading("#7", text="Temperatura da camisa (K)")
        
       
        self.listaCli.column("#1", width=30, anchor='c')
        self.listaCli.column("#2", width=80, anchor='c')
        self.listaCli.column("#3", width=80, anchor='c')
        self.listaCli.column("#4", width=80, anchor='c')
        self.listaCli.column("#5", width=80, anchor='c')
        self.listaCli.column("#6", width=130, anchor='c')
        self.listaCli.column("#7", width=130, anchor='c')
        self.listaCli.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.90)
        self.scroolLista = Scrollbar(self.aba3, orient='vertical',command=self.listaCli.yview)
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.05, relwidth=0.015, relheight=0.90)

        
        self.qtd_cads = 30
        self.qtd_cadp = 30
        
    #------------------------------adicionando reagente -----------------------------------------------------------------------------------------------------------------   
    def adicionars(self):
        if self.qtd_cads <= 30:
            #print('readd',self.qtd_cads)
            self.Cbe1 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ("verdana",9),justify = 'center')
            self.Cbe1.place(relx=0.08,rely=0.23 + 0.003*self.qtd_cads, relwidth=0.08)
            self.Cb01 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ("verdana",9),justify = 'center')
            self.Cb01.place(relx=0.22,rely=0.23 + 0.003*self.qtd_cads, relwidth=0.08)
            self.er2 = EntPlaceHold(self.aba2,"Coeficiente",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ("verdana",9),justify = 'center')
            self.er2.place(relx=0.345,rely=0.23 + 0.003*self.qtd_cads, relwidth=0.08)
            self.qtd_cads += 30

    #------------------------------removendo reagente--------------------------------------------------------------------------------------------------------
    def removers(self):
        if self.qtd_cads >30:
            #print('rea',self.qtd_cads)
            Label(self.aba2,text = " ",bg = self.a,font = ("Arial",11), width = 11).place(relx=0.08,rely = 0.23 + 0.0015*self.qtd_cads)
            Label(self.aba2,text = " ",bg = self.a,font = ("Arial",11), width = 11).place(relx=0.22,rely = 0.23 + 0.0015*self.qtd_cads)
            Label(self.aba2,text = " ",bg = self.a,font = ("Arial",11), width = 11).place(relx=0.345,rely = 0.23 + 0.0015*self.qtd_cads)
            self.qtd_cads -= 30

     #------------------------------adicionando produto-----------------------------------------------------------------------------------------------------------------   
    def adicionarp(self):
        if self.qtd_cadp <= 30:
            #print('prod',self.qtd_cadp)
            self.Cde1 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ("verdana",9),justify = 'center')
            self.Cde1.place(relx=0.54,rely=0.23 + 0.003*self.qtd_cadp, relwidth=0.08)
            self.Cd01 = EntPlaceHold(self.aba2,"Em mol/m³",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ("verdana",9),justify = 'center')
            self.Cd01.place(relx=0.68,rely=0.23 + 0.003*self.qtd_cadp, relwidth=0.08)
            self.ep2 = EntPlaceHold(self.aba2,"Coeficiente",font = ('verdana', 9),justify="center")#Entry(self.aba2,font = ("verdana",9),justify = 'center')
            self.ep2.place(relx=0.805,rely=0.23 + 0.003*self.qtd_cadp, relwidth=0.08)
            self.qtd_cadp += 30

    #------------------------------removendo produto--------------------------------------------------------------------------------------------------------
    def removerp(self):
        if self.qtd_cadp >30:
            Label(self.aba2,text = " ",bg = self.a,font = ("Arial",11), width = 11).place(relx=0.54,rely = 0.23 + 0.0015*self.qtd_cadp)
            Label(self.aba2,text = " ",bg = self.a,font = ("Arial",11), width = 11).place(relx=0.68,rely = 0.23 + 0.0015*self.qtd_cadp)
            Label(self.aba2,text = " ",bg = self.a,font = ("Arial",11), width = 11).place(relx=0.805,rely = 0.23 + 0.0015*self.qtd_cadp)
            self.qtd_cadp -= 30

    def evento(self):
        self.it_r2 = self.rr.get()
        #self.x02 = StringVar()
        if self.it_r2 == "Em equilíbrio":
            Label(self.aba1,text='Insira a constante de equilíbrio',bg=self.a,font = ('Helvetica', 9, 'bold'),fg=self.aa).place(relx=0.74, rely=0.74)
            self.Kc = EntPlaceHold(self.aba1,"Em SI",font = ('verdana', 9),justify="center")
            self.Kc.place(relx= 0.74, rely= 0.82)#chute inicial
        else:
            Label(self.aba1,text='                           ',bg = self.a,font = ("Arial",11), width = 11).place(relx=0.74, rely=0.74, relwidth = 0.5)
            Label(self.aba1,text='                           ',bg = self.a,font = ("Arial",11), width = 11).place(relx=0.74, rely=0.82, relwidth = 0.5)
                
                    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------TABELA COM BANCO DE DADOS----------------------------------------------------------------

        
#-----------------------GRAFICOS-----------------------------------------------------------------------------------------------------------------
    def grafi(self):
        self.fig = Figure(figsize=(9.9,5.25),dpi=51)
        self.fig.patch.set_facecolor('xkcd:tan')
        self.a_r1 = self.fig.add_subplot(111)
        self.a_r1.grid(True)
        self.a_r1.set_xlabel('Tempo (s)',fontsize=18)
        self.a_r1.set_ylabel('Concentração (mol/m³)',fontsize=18)
        self.a_r1.set_title('Perfil reacional de concentração',fontsize=22)
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
        self.a_r12.tick_params(axis='both', which='major', labelsize=15)
        self.canvas2 = FigureCanvasTkAgg(self.fig2,master=self.frame2)
        self.canvas2.get_tk_widget().place(relx=0.53,rely=0.02)
        self.canvas2.draw()
    

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label = "Opções", menu = filemenu) #menu dentro do filemenu
        menubar.add_cascade(label = "Relatórios", menu = filemenu2)
        

        filemenu.add_command(label="Sair",command = Quit) #opções dentro do file
        filemenu.add_command(label="Limpa Tela",command = None)
        
        filemenu2.add_command(label="Imprimir relatório",command = None)
        filemenu2.add_command(label="Ajuda",command = None)
                
Principal()
