from math import pi, log
from plotar import plotar
import re

def BEB(ar):
    
    with open(ar+".txt", "r") as data:
        #importação dos dados
        dados = data.read().split('\n')
        d=[]

        for i in range(0, len(dados)):
            dados[i]=list(map(float, dados[i].split('\t')))

        #fim da importação

        T=5
        Tf=500
        a=0.5292
        R=13.61
        soma = 0
        Tx=[]
        Secao=[]
        
        while T<Tf:
            soma = 0

            for j in range(0, len(dados)):

                U=dados[j][0]
                B=dados[j][1]
                N=dados[j][2]
                
                t=T/B
                u=U/B
                S=4*pi*(a**2)*N*((R**2)/(B**2))
                sBEB = (S/(t+u+1))*( (log(t)/2)*(1-(1/(t**2))) + 1 - (1/t) - (log(t)/(t+1)) )
                if T>B:
                    soma = soma + sBEB
                

            Tx.append(T)
            Secao.append(soma)
            T = T + 1

        with open(ar+"-grafico"+".txt", "w") as n:
            

            for u in range(0, len(Tx)):
                n.write(str(Tx[u])+" "+str(Secao[u])+"\n")

    
    plotar(ar+"-grafico", colorG="green")
    
