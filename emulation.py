from constants import *
from tkinter import *
import time
import math
import random

root = Tk()

def emulation(NIJ, KW, IJK, JO1, NIT1, IPR, Ruav):
    R2min = 1.0E39
    ZMAX = 0.0
    KPR = 0
    JO = JO1
    CK = 200.0
    NIT = NIT1
    ALF = 0.986;
    ith = 0
    r0 = rb + math.exp(math.log10(6.0*aa/bb)/14.0)
    IST = 0
    K = 0
    print(KW)
    for j in range(1, KW):
        for i in range(1, KW):
            K = K+1
            X[K] = a*i/30.0+35.0
            Y[K] = a*j/30.0+24.0
            Z[K] = 15.00
            VX[K] = 0.0
            VY[K] = 0.0
            VZ[K] = 0.0
    
    canvas = Canvas(root, width=1700, height=1200, bg='white')
    canvas.pack()

    for i in range(1, K):
        i1 = int(20.0*X[i])
        j1 = int(20.0*Y[i])
        i2 = int(Z[i]/5.0)
        j2 = int(Z[i]/16.0)
        canvas.create_rectangle(i1-i2, j1-j2, i1+i2, j1+j2)
        canvas.create_rectangle(i1-j2, j1-i2, i1+j2, j1+i2)
        root.update()
        time.sleep(0.05)
    time.sleep(2);

    if JO > 0:
        for i in range(1, JO):
            XA[i] = 10.0+10.0*random.uniform(0, 1)
            YA[i] = 10.0+10.0*random.uniform(0, 1)
            WX[i] = 600.0+600.0*random.uniform(0, 1)
            WY[i] = 600.0+600.0*random.uniform(0, 1)
            PX[i] = -30.0+60.0*random.uniform(0, 1)
            PY[i] = -30.0+60.0*random.uniform(0, 1)
        
    KC = 6
    for  JT in range(NIJ, KC):
        canvas.create_rectangle(0,0,1740,40)
        ST = int(JT);

    if JT == 1:
        JO = 1
        Y[K+1] = 25.0
        X[K+1] = -90.0
        Z[K+1] = 120.0
        ALF = 0.986;
        KPR = 0
        X[0] = 25.0
        Y[0] = 25.0
        Z[0] = 15.0
        NIT = 2*NIT1
        for i in range(1,K):
            X[-i] = 0.0
            Y[-i] = 0.0
            Z[-i] = 0.0
    if JT == 2:
        NIT = 2*NIT1
        KPR = 0
        JO = 0
        ALF = 0.986
        X[0] = 25.0
        Y[0] = 25.0
        Z[0] = 15.0
        for i in range(1, K):
            X[-i] = 0.0
            Y[-i] = 0.0
            Z[-i] = 0.0

    if JT == 3:
        NIT = 2*NIT1
        X[0] = 25.0
        Y[0] = 25.0
        Z[0] = 15.0
        ALF = 0.986
        for i in range(1, K):
            X[-i] = a*(i-K / 2)/30.0
            Y[-i] = X[-i]
            Z[-i] = 30.0

    if JT == 4:
        NIT = 2*NIT1
        X[0] = 25.0
        Y[0] = 25.0
        Z[0] = 15.0
        ALF = 0.986
        k1 = 0
        for j in range(1, KW):
            for i in range(1, KW):
                k1 = k1+1
                X[-k1] = a*(i-KW)/20.0
                Y[-k1] = a*(j-KW)/20.0
                Z[-k1] = 20.0

    if JT == 5:
        if KW == 10:
            NIT = 2*NIT1
            X[0] = 25.0
            Y[0] = 25.0
            Z[0] = 25.0
            ALF = 0.986
            k1 = 0
            for j in range(4):
                for i in range(49):
                    if H[j,i] == 1:
                        k1 = k1+1
                        X[-k1] = 2.5*i-80
                        Y[-k1] = 2.5*j
                        Z[-k1] = 20.0
        else: 
            KPR = 1

    if JT == 6:
        NIT = NIT1
        X[0] = 25.0
        Y[0] = 25.0
        Z[0] = 15.0
        NIT = NIT1
        KPR = 0
        ALF = 0.986
        for i in range(1, K):
            X[-i] = 0.0; Y[-i] = 0.0; Z[-i] = 0.0;

    if KPR == 0:
        for it in range(1,NIT):
            ith = ith+1; dt = 1.0E20
            ZS = 0;
            for i in range(1,K):
                ZS = ZS+Z[i]
                if ith<10000:
                    ZS = (ith/10000.0)*ZS/K
                else:
                    ZS = ZS/K;

        if JT>2:
            JO = JO1;
        if JO>0:
            for i in range(1,JO):
                X[i+K] = 35.0+XA[i]*math.sin(0.2*ith/WX[i]+PX[i]);
                Y[i+K] = 25.0+YA[i]*math.cos(0.2*ith/WY[i]+PY[i]); Z[i+K] = ZS
            for i in range(1,K):
                DX = X[i]-(X[0]+X[-i]); DY = Y[i]-(Y[0]+Y[-i]);DZ = Z[i]-(Z[0]+Z[-i]);
                r2 = DX*DX+DY*DY+DZ*DZ; F = -2.0*CK; u2 = CK*r2;
                dtt = td*math.pi*math.sqrt(1.0/abs(u2));
                if dtt<dt:
                    dt = dtt;
                fx = F*DX; fy = F*DY; fz = F*DZ;
                for j in range(1,K):
                    if i != j:
                        DX = X[i]-X[j]; DY = Y[i]-Y[j]; DZ = Z[i]-Z[j];
                        r2 = DX*DX+DY*DY+DZ*DZ
                        if r2 < R2min:
                            R2min = r2; w1 = math.sqrt(r2);
                        if w1<Ruav:
                            IST = IST+1;
                    if w1>rb:
                        w1 = w1-rb; w2 = w1*w1; w12 = w2*w2; w12 = w12*w12*w12;
                        w14 = w12*w2; u2 = aa/w12+bb*w2; F = 12.0*aa/w14-2.0*bb
                    else:
                        w2 = r2;  w12 = w2*w2; w12 = w12*w12*w12; w14 = w12*w2;
                        u2 = aa/w12; F = 12.0*aa/w14
                    dtt = td*math.pi*math.sqrt(1.0/u2);
                    if dtt<dt:
                        dt = dtt
                    fx = fx+F*DX; fy = fy+F*DY;fz = fz+F*DZ
                if JO>0:
                    for j in range(1,JO):
                        DX = X[i]-X[j+K]; DY = Y[i]-Y[j+K]; DZ = Z[i]-Z[j+K];
                        r2 = DX*DX+DY*DY+DZ*DZ;
                        if r2<R2min:
                            R2min = r2; w1 = math.sqrt(r2)
                        if w1<Ruav:
                            IST = IST+1
                    if IPR == 1:
                        if w1>rb:
                            w1 = w1-rb; w2 = w1*w1; w12 = w2*w2; w12 = w12*w12*w12;
                            w14 = w12*w2;u2 = aa/w12+bb*22; F = 12.0*aa/w14-2.0*bb
                        else:
                            w2 = r2;  w12 = w2*w2; w12 = w12*w12*w12; w14 = w12*w2;
                            u2 = aa/w12; F = 12.0*aa/w14
                        dtt = td*math.pi*math.sqrt(1.0/u2)
                        if dtt<dt:
                            dt = dtt
                        fx = fx+F*DX; fy = fy+F*DY;fz = fz+F*DZ
            VX[i] = VX[i]+fx*dt; VY[i] = VY[i]+fy*dt; VZ[i] = VZ[i]+fz*dt
            for i in range(1,K):
                VX[i] = ALF*VX[i];  VY[i] = ALF*VY[i]; VZ[i] = ALF*VZ[i];
                X[i] = X[i]+VX[i]*dt; Y[i] = Y[i]+VY[i]*dt; Z[i] = Z[i]+VZ[i]*dt
                if Z[i]>ZMAX:
                    ZMAX = Z[i]
            if (ith % IJK) == 0: 
                canvas.create_rectangle(0,40,1700,1200);
                for i in range(1, K):
                    i1 = int(20.0*X[i]);  j1 = int(20.0*Y[i]);
                    i2 = int(Z[i]/8.0);
                    j2 = int(Z[i]/20.0)
                    if j2<2:
                        j2 = 2;
                    if i2<1:
                        i2 = 1;
                    if j1>50:
                        canvas.create_rectangle(i1-i2, j1-j2, i1+i2, j1+j2)
                        canvas.create_rectangle(i1-j2, j1-i2, i1+j2, j1+i2)
                        root.update()
                        time.sleep(0.05)
            if JT == 2:
                for i in range(1,K):
                    i1 = int(20.0*X[i]);  j1 = int(390.0-5.0*Z[i]);
                    i2 = 2; j2 = 2
                    canvas.create_rectangle(i1-i2, j1-j2, i1+i2, j1+j2)
                    canvas.create_rectangle(i1-j2, j1-i2, i1+j2, j1+i2)
                    root.update()
                    time.sleep(0.05)
                    if JO>0:
                        for i in range(1,JO):
                            i1 = int(20.0*X[i+K])
                            j1 = int(20.0*Y[i+K])
                            i2 = int(Z[i+K]/8.0)
                            if i2<1:
                                i2 = 1;
                            if j1>50:
                                canvas.create_oval(i1-i2, j1-i2, i1+i2, j1+i2)

            if JT == 2:
                canvas.create_rectangle(400,int(390.0-5*Z[1+K]),720,int(390.0-5*Z[1+K])+2);
                canvas.create_rectangle(int(560.0-20.0*RO),int(390.0-5*Z[1+K]),int(560.0+20.0*RO),int(390.0-5*Z[1+K])+2, fill='white');
                root.update()
                time.sleep(0.05)
        time.sleep(2)

    # if JT>2:
    #     if int(it)< NIT / 3:
    #         X[0] = X[0]+DELT
    #     else:
    #         X[0] = X[0]-DELT;
    #     if it< NIT / 3:
    #         Y[0] =  Y[0]+DELT
    #     else:
    #         if it < 2*NIT / 3:
    #             Y[0] =  Y[0]-DELT
    # else:
    #     Z[0] = 10.0+40.0/(1.0+math.exp(25.0-it/1200.0)); Y[0] = 25.0; X[0] = it/1200.0

    # if JT == 1:
    #     X[K+1] = X[K+1]+1.0/200.0
    # if (it==NIT1) or (it==3*NIT1 / 2):
    #     CK = -CK

    # if (JT==2) and (it==NIT / 8):
    #     JO = 0
    #     for j in range(19,31):
    #         for i in range(20,36):
    #             if (j-25.0)**2+(i-28.0)**2>(RO)**2:
    #                 JO = JO+1; Y[JO+K] = j; X[JO+K] = i; Z[JO+K] = 20.0

    # for j in range(19,30):
    #     for i in range(20,35):
    #         if (j+0.5-25.0)**2 + (i+0.5-28.0)**2>(RO)**2:
    #             JO = JO+1; Y[JO+K] = j+0.5; X[JO+K] = i+0.5; Z[JO+K] = 20.0
