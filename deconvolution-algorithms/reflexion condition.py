import numpy as np


def dcts(x):
    print("entry = ", x)
    n,m = np.shape(x)
    
    pi = np.pi
    omega = np.exp(-1j*pi/(2*n))
    
    mat = np.array([i for i in range(1,n)])
    d = [1/np.sqrt(2)] + list(omega**mat)
    d = d/np.sqrt(2*n)
    d = np.array(d,dtype=float)
    print("d= ",d)
    d = d.take(np.ones((1,m),dtype=int)) 
    
    #xt = np.concatenate((x,flipud(x)), axis=0)
    
    xt = np.concatenate((x,x[::-1,] ), axis=0)
    
    yt = np.fft.fft(xt)
    y = (d*yt[:n,:]).real
    print("y = ",y)
    return y

def dcts2(x):
    y = dcts(dcts(x).T).T
    return y

def dctshift(PSF,center=None):
    m,n = np.shape(PSF)
    
    if center==None:
        print("an error occured")
        return
    i = center[0]
    j = center[1]
    k = min([i-1,m-i,j-1,n-j])
    
    PP = PSF[i-k-1:i+k,j-k-1:j+k]
    Z1 = np.diag(np.ones((k+1,1)) , k)
    Z1 = Z1.reshape((Z1.size,1))
    #Z2 = np.diag(np.ones((k,1)) , -(k-2))
    Z2 = np.diag(np.ones((k+1,1)) , k)
    Z2 = Z2.reshape((Z2.size,1))
    print("Z2 =",Z2)
    print("Z1.shape: ",Z1.shape)
    print("PP.shape: ",PP.shape)
    print("Z2.shape: ",Z2.shape)
    print(Z1@(PP@Z1.T)); print(Z1@(PP@Z2.T));
    print(Z2@(PP@Z1.T));print(Z2@(PP@Z2.T))
    PP = Z1@(PP@Z1.T) + Z1@(PP@Z2.T)+ Z2@(PP@Z1.T)+ Z2@(PP@Z2.T) 
    Ps = np.zeros((m,n))
    print("PP =",PP)  
    Ps[0:2*k+1,0:2*k+1] = PP #heeee
    #Ps = np.diag(PP)
    #Ps = Ps.reshape((Ps.size))
    return Ps

def idcts(x):
    m,n = np.shape(x)
    pi = np.pi
    omega = np.exp(1j*pi/(2*n))
    mat = np.array([i for i in range(0,n)])
    d = np.sqrt(2*n)* (omega**mat)
    d[0] = np.sqrt(2)*d[0]

    d = np.array(d,dtype=int)
    #d = d.take(np.ones((1,m),dtype=int))  #heee
 
    print("x_like = ",x)
    print("d_like = ",d)
    
    xt1 = np.concatenate((d*x,np.zeros((1,m))), axis=0)
    #xt2 = -1j* d[1:n,:] * flipud(x[1:n,:])
    toFlip = x[1:n,:]
    d = d.reshape((d.size,1)) ###adds on!!
    xt2 = -1j* d[1:n,:] * toFlip[::-1,]
    xt = np.concatenate((xt1,xt2), axis=0)
    
    yt = np.fft.ifft(xt)
    y = (d*yt[0:n,:]).real
    return y
    
def gcv_tsvd (U,b):
    L = []
    H = []
    h = 0
    [N,M] = np.shape(U)
    for k in range (1,N-1):
        if N-k**2 ==0 : h = 0
        if N-k**2 != 0: h = 1/(N-k**2)
        t = np.transpose (U)
        G = 0 #G(k)
        v = 0
        for i in range(k+1, N-1):
            v = (U.T[i]*b)**2
            G += h*v
        L.append(G)
    H = list(L)
    mini = min(L)
    return (mini)


#reflexive boundary condition

def tsvd_dct(B,PSF,center=None,tol=None):
    if center==None:
        print("Error: B, BST and the center center must be given")
        return
    elif tol==None :
        tol=[]
    e1 = np.zeros(np.shape(PSF))
    e1[0][0]=1
    
    bhat = dcts2(B)
    
    #retrieve S
    dc = dcts2(e1)
    for i in range (len(dc)):
        for j in range (len(dc[0])):
            if dc[i][j] !=0:
               dc[i][j] = 1/dc[i][j]
    S = dcts2(dctshift(PSF,center)) * dc #un vecteur
    print("S= ",S)
    
    #find the regulzrisation parameter if not given
    if not tol or tol.isalpha():
        tol = gcv_tsvd(S[:],bhat[:])
    
    #regularisation
    Phi = np.array ((abs(S)>=tol),dtype=int)
    idX = np.array ((Phi>=tol),dtype=float)
    Sfilt = np.zeros(len(Phi))
    for i in range (len(Phi)):
        print("hope",Phi[i][i]/S[i])
        if idX[i].any(): Sfilt[i] = Phi[i][i]/S[i][i]
        else: Sfilt[i] = 0
    X = idcts(bhat*Sfilt)
    return X
    

PSF = (1/16)*np.array([
                    [1,2,1],
                    [2,4,2],
                    [1,2,1]
                        ])
B = (1/16)*np.array([
                    [1,2,1],
                    [2,4,2],
                    [1,2,1]
                        ])
print(tsvd_dct(B,PSF,center=(1,1))) 
    
    
    