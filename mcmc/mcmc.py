import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# matplotlib configuration
matplotlib.rc('font', size = 16)
plt.rcParams['figure.figsize'] = (10, 8)
plt.rc('font', family='serif')

# Integral of a^{-x^2/2}=sqrt(2Pi/log(a)), so N(a)=sqrt(log(a)/2Pi) a>=1

p_a=1

def p_xa(x,a):
    N=np.sqrt(np.log(a)/2/np.pi)
    p=N*a**(-x**2/2)
    return p

xa=np.array([])
for i in range(0,100):
    xa=np.append(xa,np.random.normal(0,1))

def likelihood(a,x):
    l=1
    for i in range(0,100):
        l=l*p_xa(x[i],a)
    return l

p_x=0
for a in np.linspace(1,100,9901):
    p_x=p_x+likelihood(a,xa)*0.01


def posterior(a,x):
    return likelihood(a,x)*p_a/p_x

aa=np.linspace(1,100,10000)
p_ax=posterior(aa,xa)
plt.plot(aa,p_ax,label='posterior')
plt.xlim(1, 100)
plt.xlabel('a')
plt.ylabel('probability density')
plt.grid()
plt.legend()
plt.savefig('posterior.png')
plt.clf()

def g(x1,x2,s):
    return np.exp(-((x1-x2)/s)**2)/np.sqrt(2*np.pi)/s

def A(x1,x2,s):
    return np.minimum(1,posterior(x1,xa)*g(x2,x1,s)/posterior(x2,xa)/g(x1,x2,s))

para=np.array([])
x0=100
xt=x0
for i in range(0,10000):
    xp=np.random.normal(xt,0.5)
    u=np.random.uniform(0,1)
    if u<=A(xp,xt,1):
        xt=xp
    para=np.append(para,xt)

plt.hist(para,1000)
plt.xlim(1, 110)
plt.xlabel('a')
plt.ylabel('number')
plt.grid()
plt.savefig('histogram.png')
plt.clf()

a=np.linspace(0,9999,10000)
plt.plot(a,para,label='trace')
plt.xlim(1, 10000)
plt.ylim(0, 110)
plt.xlabel('step')
plt.ylabel('a')
plt.grid()
plt.legend()
plt.savefig('trace.png')
plt.clf()