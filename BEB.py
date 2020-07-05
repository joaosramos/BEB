def BEB(nome, initial_energy=1, final_energy=500):
    nomef=nome
    #Retira a extensão do nome do input
    nome = nome.replace(".txt", "")

    #Seta as variaveis de dentro da função
    ar = nome
    T = energia_inicio
    Tf = energia_fim

    #Variaveis do BEB e definição da lista vazia
    a = 0.5292
    R = 13.61
    soma = 0
    Tx = []
    Secao = []

    #Abre o arquivo que foi enviado e que esta salvo e executa o BEB em si
    with open("{}.txt".format(nome), "r") as data:
        dados = data.read().split('\n')
        d=[]

        for i in range(0, len(dados)):
            dados[i]=list(map(float, dados[i].split('\t')))
        
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

        #Salva no arquivo resposta
        with open("CrossSection.txt", "w") as n:
            
            for u in range(0, len(Tx)):
                n.write(str(Tx[u])+" "+str(Secao[u])+"\n")
