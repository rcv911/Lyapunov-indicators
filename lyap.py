from numpy import *
from multiprocessing import *

def lap(arg):
    lam,x0,Ntrans,N,eps=arg
    x=x0
    for i in range(Ntrans):
        x=lam-x*x

    L=0
    for i in range(N):
        xt=eps
        xt=-2*x*xt
        x=lam-x*x
        L+=log(abs(xt/eps))
    L/=N
    return L

if __name__ == "__main__":
	N=1000
	Ntrans=200
	eps=0.0001
	lambdas=loadtxt('lambdas.txt')
	x0=0.34
	p=Pool()
	
	args=[(lam, x0, Ntrans, N, eps) for lam in lambdas]
	Lyapunovski=p.map(lap,args)
	
	print (Lyapunovski)
	
