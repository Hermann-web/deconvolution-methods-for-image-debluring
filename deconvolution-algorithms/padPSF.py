import numpy as np


def padPSF (PSF,m, n):

    #PSF
    im = fits.getdata("C:/Python37/pic.jpg")
    PSF = np.where(im == np.max(pic))

    '''xc = int(cents[1])
    yc = int(cents[0])

    center = [xc,yc]'''
    
    if np.shape(m) == n:
        n = m

    else :
        n = m[2]
        m = m[1]

    P = np.zeros(m,n)

    P[1:np.shape(PSF,1), 1:np.shape(PSF,2)] = PSF

    return (P)
