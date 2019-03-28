# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:07:31 2016

@author: Filipe Damasceno
"""
import math

class Distri:
    r2 = 0.70710678118654752440
    aa_beta,bb_beta = 0,0
    
    @staticmethod
    def comb(n,k):
        if n<0 or k<0 or n<k:
            print("Erro de parâmetros na comb")
            return
        c=1
        ka = n-k if n-k < k else k
        if ka == 0:
            return c
        for i in range(1,ka+1):
            c*=(n-i+1)/i
        return c
    
    @staticmethod
    def fatorial(n):
        if n<=1:
            return 1
        f = 1
        for i in range(2,n+1):
            f*=i
        return f
    
    @staticmethod
    def binomCDF(n,p,k1,k2):
        
        if n < 0 or k1 < 0 or k2 < 0 or n < k1 or n < k2 or k1 > k2:
            print("Erro de parâmetros na binomCDF")
            return
        s,q= 0,1-p
        for k in range(k1,k2+1):
            s+= Distri.comb(n,k)*(p**k)*(q**(n-k))
        return s
        
    @staticmethod
    def binomPDF(n,p,k):
        return Distri.binomCDF(n,p,k,k)
    
    @staticmethod    
    def hipergeomPDF(k,m,N,n):
        
        if n<0 or k<0 or n<k or m<k or N<k or n>N or N<2:
            print("Erro de parâmetros na hipergeomPDF")
            return
        return Distri.comb(m,k)*Distri.comb(N-m,n-k)/Distri.comb(N,n)
    
    @staticmethod    
    def hipergeomCDF(k1,k2,m,N,n):
        
        if k2<k1:
            print("Erro na hipergeomCDF: k1 deve ser menor ou igual que k2")
            return
        s=0
        for k in range(k1,k2+1):
            s+= Distri.hipergeomCDF(k,m,N,n)
        return s
    
    @staticmethod
    def funcaoErro(x):
        p,a1,a2,a3,a4,a5=0.3275911,0.254829592,-0.284496736,1.421413741,-1.453152027,1.061405429
        
        xx= x if x>0 else -x
        t=1/(1+p*xx)
        tt=((((a5*t+a4)*t+a3)*t+a2)*t+a1)*t
        ef=1-(-xx**xx)*tt
        return -ef if x<0 else ef
    @staticmethod
    def invErro(r):
        if abs(r)>1:
            print("Erro na invErro: r deve ser menor que 1.")
            return
        return Distri.r2*Distri.invnormal((r+1)/2)
    @staticmethod
    def normalPDF(z):
        return math.exp(-z*z/2)/math.sqrt(2*math.pi)
    
    @staticmethod
    def normalCDF(z,z1=None,d1=None,d2=None):
        if z1 == None:
            if z < 0:
                return 1-Distri.normalCDF(-z)
            
            b1,b2,b3,b4,b5,t=0.319381530, -0.356563782, 1.781477937, -1.821255978, 1.330274429, 1/(1+0.2316419*z)
            
            return 1-Distri.normalPDF(z)*(((((b5*t+b4)*t+b3)*t+b2)*t+b1)*t)
        elif z1 != None == d1 == d2:
            if z > z1:
                print("Erro na normalCDF: z1 deve ser menor que z2.")
                return
            return Distri.normalCDF(z)-Distri.normalCDF(z1)
        elif not None in [z,z1,d1,d2]:
            if z > z1 or d2 <=0:
                print("Erro na normalCDF: x1 deve ser menor que x2.")
                return
            v1,v2 = (z-d1)/d2,(z1-d1)/d2
            return Distri.normalCDF(v1,v2)
        else:
            if d1<=0:
                print("Erro na normalCDF: o desvio deve ser positivo.")
                return
            return Distri.normalCDF((z-z1)/d1)    
    
    @staticmethod    
    def invnormal(p):
        if p<0 or p>1:
            print("Erro na invnormal: p deve estar no intervalo [0,1] ")
            return
        if p > 0.999968:
            return 4
        if p < 0.000032:
            return -4
        if p > 0.5:
            return -Distri.invnormal(1-p)
        t = math.sqrt(math.log(1/(p**2)))
        c0,c1,c2 = 2.515517,0.802853,0.010328
        d1,d2,d3 = 1.432788,0.189269,0.001308
        
        pn,pd = c0+t*(c1+c2*t), ((d3*t+d2)*t+d1)*t+1
        x = pn/pd - t
        for i in range(1,3+1):
            x-=(Distri.normalCDF(x)-p)/Distri.normalPDF(x)
        return x
    
    @staticmethod    
    def exponencialCDF(x,d1,d2=None):
        if d2 == None:
            return 1 - math.exp(-x/d1)
        
        if d1 < x  or d2 <=0:
            print("Erro na exponencialCDF: x2 deve ser maior que x1")
            return
        return Distri.exponencialCDF(d1,d2)-Distri.exponencialCDF(x,d2)
    
    @staticmethod
    def possionCDF(lam,k1,k2):
        p,el = 0,math.exp(-lam)
        
        for k in range(k1,k2+1):
            p+=math.pow(lam,k)/Distri.fatorial(k)
        return p*el
        
    
    @staticmethod
    def possionPDF(lam, k):
        return Distri.possionCDF(lam,k,k)
    
    @staticmethod
    def rayleighCDF(x,sig):
        sig2 = 2*sig**2
        return 1-math.exp(-x**2/sig2)
    
    @staticmethod
    def rayleighPDF(x,sig):
        sig2 = 2*sig**2
        return x/sig2*math.exp(-x**2/sig2)
    
    @staticmethod
    def gamma(x):
        if math.abs(x) < 1e-4:
            print("erro!!")
            return
        s = 1.000000000190015
        p = [76.18009172947146,-86.50532032941677,
             24.01409824083091,-1.231739572450155,
             1.208650973866179E-3,-5.395239384953E-6]
        r2pi = 2.5066282746310005
        for n,i in enumerate(p,1):
            s+=i/(x+n)
        s*=r2pi/x
        return s*math.pow(x+5.5,x+0.5)*math.exp(-x-5.5)
    
    @staticmethod
    def betaPDF(a,b,x):
        return math.pow(x,a-1)*math.pow(1-x,b-1)/Distri.beta(a,b)
    
    @staticmethod
    def betaCDF(a,b,x):
        Distri.aa_beta,Distri.bb_beta = a,b
        return Distri.integral(0,x)
    
    @staticmethod
    def beta(x,y):
        return (Distri.gamma(x)*Distri.gamma(y))/Distri.gamma(x+y)
    
    @staticmethod
    def integral(a,b,tol=None):
        return Distri.adap(a,b,1e-15 if tol else tol)
    
    @staticmethod
    def adap(a,b,tol):
        cont,c = 0,(a+b)/2
        sab,sac,scb=Distri.simp(a,b),Distri.simp(a,c),Distri.simp(c,b)
        if math.abs(sab-sac-scb) < tol or cont>=300:
            ad = sac+scb
        else:
            ad = Distri.adap(a,c,tol/2)+Distri.adap(c,c,tol/2)
        cont+=1
        return ad
        
    @staticmethod
    def simp(a,b):
        return (b-a)/6*(Distri.FunPDF(a)+4*Distri.FunPDF(a+b/2)+Distri.FunPDF(b))
    
    @staticmethod
    def FunPDF(x):
        return Distri.betaPDF(Distri.aa_beta,Distri.bb_beta,x)