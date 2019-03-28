# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:44:48 2016

@author: Filipe Damasceno
"""
import random as rr
import math as mat
class Aleatorio(object):
    
    Nmax = 52
    cartas = []
    cartasRetiradas =[]
    iniciarBaralho = False
    
    ''' from random'''
    randexp = rr.expovariate
    randNormal = rr.gauss
    rolaDado = lambda: rr.randint(1,6)
    
    @staticmethod
    def rand(a,b=None):
        """
        engloba as funcoes:
        -> rand con double,long com um ou dois parametros
        -> escolhe
        """
        if b:
            if type(float()) in [type(a),type(b)]:
                return a+rr.random()*(b-a)
            else:
                return rr.randint(a,b)
        elif type(float()) == type(a):
            return rr.random()*a
        else: return rr.randint(0,a)               
    
    @staticmethod
    def setBaralho():
        Aleatorio.cartas = [ i for i in range(Aleatorio.Nmax)]
        Aleatorio.iniciarBaralho =True

    @staticmethod
    def tiraCarta(n):
        if not Aleatorio.iniciarBaralho:
            Aleatorio.setBaralho()
        Aleatorio.cartasRetiradas = rr.sample(Aleatorio.cartas,n)
        
    @staticmethod
    def randBernou(p):
        return 1 if rr.random < p else 0
    
    @staticmethod
    def randBinom(p,n):
        Nsucessos = 0
        for _ in range(n): Nsucessos += Aleatorio.randBernou(p)
        return Nsucessos
    
    @staticmethod
    def randgeo(p=0,log1p=None):# verificar
        if not log1p:
            log1p = mat.log(1-p)
        return mat.floor(mat.log(rr.random()/log1p))

    @staticmethod
    def randpoi(expmlambda):
        k,p = 0,1
        while(p>expmlambda):
            k+=1
            p*=rr.random()
        return k
    
    @staticmethod
    def randRayleigh(sig):
        return sig*mat.sqrt(-2*mat.log(rr.random()))