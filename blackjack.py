# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:30:20 2019

@author: alest
"""

def blackjack (x):
    import random
    a = []*13
    i = 2
    while i <= 10:
        a[i-2] = i
        i += 1
        Valete = 10
        Dama = 10
        Rei = 10 
        Ás = 11 
        a [9] = Valete
        a [10] = Dama
        a [11] = Rei
        a [12] = Ás
    dinheiro = 200
    valorinicial = 10
    aposta = x*valorinicial
    dinheiro -= aposta
    contador = 0
    contadordeas = 0
    if aposta >= valorinicial:
        y = random.randint(a[0],a[13])
        z = random.randint(a[0],a[13])
        contador = y + z
        if y == a[12] or z == a[12]:
            contadordeas += 1
        if contador == 21:
            dinheiro = dinheiro + aposta + aposta * 1.5
        else:
               while contador < 21:
                    j = input("Você quer parar ou receber mais uma carta?")
                    if j == "receber mais uma carta":
                        b = random.randint(a[0],a[13])
                        contador += b
                    else:
                        contador = contador
                        if contador == 21:
                                dinheiro = dinheiro + aposta + aposta * 1.5
                        elif contador > 21:
                            if contadordeas >= 1:
                                    contador -= 10
                                    dinheiro = dinheiro 
                            else:
                                c = random.randint(a[0],a[13])
                                d = random.randint(a[0],a[13])
                                computador = c + d
                                contadordeas2 = 0
                                if c == a[12] or d == a[12]:
                                    contadordeas2 += 1
                                if computador >= 17:
                                    computador = computador
                                    if computador <=16:
                                        computador = computador + random.randint(a[0],a[13])
                                        if computador > 21:
                                            if contadordeas > 0:
                                                computador -= 10
                                            dinheiro += aposta
                                if computador <= 21:
                                    if computador > contador:
                                        dinheiro = dinheiro
                                    else:
                                        dinheiro = dinheiro + aposta
                                        
                                        
                                        
                                        
                        
                        
                        
                        
                
            
            
        
        
        
        

    