# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import random
import sys
import math

max_iter = 500
mut_rates = [20,100,150]
plot_x=[]
plot_y=[]
plot_x1=[]
plot_y1=[]
niz=["red","black","blue","yellow","green"]


"Funkcija troska"
"Funkcija troska je Mekormikova fukcija"

def trosak(hromozom):
    x=hromozom[0]
    y=hromozom[1]
    return (math.sin(x+y))+((x-y)**2)-(1.5*x)+(2.5*y+1)
    
"Metoda mutacije "
"Tackasta normalna mutacija za kontinualni genetski algoritam"

def mutiraj(hromozom, rate, opsegx,opsegy):
    
    sigma=0.5
    if random.random() < rate:
        for i in range(len(hromozom)):
            hromozom[i] += random.gauss(0, 1)*sigma


     
    if(hromozom[0]>=opsegx[1]):
        hromozom[0]=opsegx[1]
    elif(hromozom[0]<=opsegx[0]):
        hromozom[0]=opsegx[0]
    elif(hromozom[1]>=opsegy[1]):
        hromozom[1]=opsegy[1]
    elif(hromozom[1]<=opsegy[0]):
        hromozom[1]=opsegy[0]

    return hromozom

def turnir(fja, pop, vel):
    z = []
    while len(z) < vel:
        z.append(random.choice(pop))
        najbolji = None
        najbolji_f = None
        for e in z:
            ff = fja(e)
            if najbolji is None or ff < najbolji_f:
               najbolji_f = ff
               najbolji = e
            
    return najbolji
   
"Metoda ukrstanja"
"Redcliff metoda"
def ukrsti(h1, h2):
    beta = random.uniform(0,1)
    l = [[], []]
    for i in range(len(l)):
        for j in range(2):
            l[i].append(h1[j]*beta+h2[j]*(1-beta))
    return l


"Genetski algoriam"
"Kontinualni genetski algoritam"

def genetski(mut_rate):

    pop_vel = mut_rate
    
    npop_vel = mut_rate
    opsegx = [-1.5,4]
    opsegy = [-3,4]
    
    outfile = sys.stdout
    s_trosak = 0
    s_iteracija = 0
    best_ever_sol = None
    best_ever_f = None
    suma=0
    min=-1.913222954981037
    nova_suma=0
    
    "pet pokretanja genetskog algoritma"
    for k in range(5):
        print('Pokretanje: GA', mut_rat, k, file=outfile)
        best = None
        best_f = None
        t = 0
    
        pop = [[random.uniform(*opsegx), random.uniform(*opsegy)] for j in range(pop_vel)]


        
        while best_f!=min and t < 500:

            n_pop = pop[:]
            while len(n_pop) < pop_vel + npop_vel:
                h1 = turnir(trosak, pop, 3)
                h2 = turnir(trosak, pop, 3)
              
                h3, h4 = ukrsti(h1, h2)
                mutiraj(h3, 0.5, opsegx,opsegy)
                mutiraj(h4, 0.5, opsegx,opsegy)
        
                n_pop.append(h3)
                n_pop.append(h4)
                
                
            pop = sorted(n_pop, key=lambda x : trosak(x))[:pop_vel]
            
          
            
            for i in pop:
                suma=suma+trosak(i)
                
            suma_ispis=suma/pop_vel
            
            plot_y1.append(suma_ispis)
            
            f = trosak(pop[0])
            
            suma=0
            suma_ispis=0

            if best_f is None or best_f > f:
                best_f = f
                best = pop[0]
            
            
            t += 1
            
            plot_y.append(best_f)
            plot_x.append(t)
            plot_x1.append(t)
            
       
        for s in plot_y1:
            nova_suma=nova_suma+s
            
        print(t)

            
        najnovija=nova_suma/t
 
    
        plt.plot(plot_x,plot_y,color=niz[k])
        plt.xlabel('Generacija')
        plt.ylabel('Prosecna prilagodjenost')
        plt.title('Pojedinacno')
        plt.grid(True)
        plt.savefig(str(mut_rate)+str(k)+"lala.png")    
        plt.show()
            
        plot_x.clear()
        plot_y.clear()
        plot_y1.clear()
        plot_x1.clear()
                
              
     
        s_trosak += best_f
        s_iteracija += t
        if best_ever_f is None or best_ever_f > best_f:
            best_ever_f = best_f
            best_ever_sol = best
        
           
        print("Prilagodjenost najboljeg resenja: %s" % best_ever_f)
        print("Prosecna prilagodjenost populacije %s" %najnovija)
        
        nova_suma=0
        najnovija=0

   
    s_trosak /= 5
    s_iteracija /= 5

    print('Sastav najboljeg hromozoma: %s' % best_ever_sol, file=outfile)
    
    plt.savefig(str(mut_rate)+"aaaalala.png")    
    plt.show()
     
"Pokretanje algoritmа"


for mut_rat in mut_rates:
    genetski(mut_rat)
 

