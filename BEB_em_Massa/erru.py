#!/usr/bin/python
# -*- coding: <encoding name> -*-

def erro(Molecula, x_nist, y_nist, x_meu, y_meu):
    
    erro=[]
    x_novo=[]
    y_novo=[]
    x_nist_novo=[]
    y_nist_novo=[]


    for i in range(0, len(x_nist)):

        for j in range(0, len(x_meu)):
            if x_nist[i]==x_meu[j]:

                x_nist_novo.append(x_nist[i])
                y_nist_novo.append(y_nist[i])
                x_novo.append(x_meu[j])
                y_novo.append(y_meu[j])

    
    for k in range(0, len(y_nist_novo)):
        try:
            erro.append((y_novo[k]-y_nist_novo[k])/(y_nist_novo[k]))
        except:
            pass
            
    if max(erro)*100>5:

        return [str(max(erro)*100), Molecula, "*****SIM*****"]
    else:
        return [str(max(erro)*100), Molecula, "NAO"]
        

              
