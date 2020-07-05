import matplotlib.pyplot as plt

def plotar(nome, tipo=1, colorG="blue"):
    
    with open( "{}.txt".format(nome)) as arquivo:
        data = arquivo.read()
        linhas = list(map(float, data.split()))
        x_meu=[]
        y_meu=[]
        for k in range(0, len(linhas)-1, 2):
            x_meu.append(linhas[k])
            y_meu.append(linhas[k+1])
        
        plt.plot(x_meu,y_meu, color=colorG)
        plt.xscale('log')
        plt.grid(True)
        plt.xlabel("Energia do Elétron Incidente (eV)")
        plt.ylabel("Seção de Choque (cm²^-16)")
        path = "{}-grafico.png".format(nome)
        plt.savefig(path)
        plt.close()
        
    print("[INFO]-Pronto")
