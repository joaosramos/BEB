<img src="Imagens_Repositorio/UFPR.jpg" height=150 width=250>

# BEB
## *Abstract*
  This code is the implementation of BEB (Binary-Encounter-Bethe) Cross Section in Python (3.x), developed for an Undergraduate Research Project at UFPR (Federal University of Parana) in Brazil. 

## *Resumo*
  Este repositório contém a implementação do calculo da Seção de Choque de Ionização pelo Método de BEB (Binary-Encounter-Bethe). Feito no meu projeto de Iniciação Cienficia no Grupo de Física Atomica e Molecular(GFAM).
  
## Estrutura deste Repositório

0. Por que este repositório foi feito?
1. O que é o BEB?
2. Como utlizar o programa?
3. Como realizar e plotar seções de choque em massa?
4. Agradecimentos

### 0. Por que este repositório foi feito?

  Este repositório foi desenvolvido no âmbito do meu Plano de Trabalho de iniciação cientifica no Grupo de Física Atomica e Molecular (GFAM), na UFPR. Fiz parte do projeto na modalidade PIBIC-AF, como aluno bolsista. O objetivo principal desse plano de trabalho era a implementação computacional do calculo das Seções de Choque de Ionização utilizando o método de BEB, que será melhor descrito ao longo desse Readme.
  A partir das necessidades da industria brasileira e internacional, o estudo de tratamentos de materiais
com implatação de íons vem se tornando cada vez mais necessario. Para entender a natureza desses tratamentos, recorremos ao entendimento da complexa Seção de Choque de Ionização, para este
calculo, no entanto, pode ser necessario diversos parametros experimentais. O Método de BEB, por
sua vez, substituí a dependencia experimental, alienando o resultado ao calculo da estrutura eletronica
para softwares como o GAMESS. Ao implementar em python o método de BEB e obter os resultados,
observamos que esse método é altamente preciso mediante a escolha correta da base utilizada para
o calculo da estrutura eletronica.
### 1. O que é o BEB?
Apesar dos avanços em Mecânica Quântica, o calculo das seções de choque de ionização muitas
vezes é subordinado a parametros experimentais que não são necessariamente viaveis de se adquirir
ou mensurar. Para contornar esse problema, podemos nos utilizar do calculo dessas seções de choque
através do Método de BEB(BINARY-ENCOUNTER-BETHE), nesse calculo utilizamos apenas os resultados advindos de softwares de calculo de estrutura eletronica, como o GAMESS. Basicamente, a seção de choque de ionização é, para os efeitos do método de BEB, a área sobre uma molécula, que mede a chance de colisão de um elétron da molécula com um elétron disparado contra ela, sendo que o processo resulta na ionização da molécula e consequente retirada do elétron.

A Equação de BEB é, portanto

<img src="Imagens_Repositorio/beb.png">



  
