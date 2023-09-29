from math import *
import matplotlib.pyplot as plt
import numpy as np
import time

class Projectile:
    def Draw(self, H, R):
        X = list(range(0, int(R)+1)); y = []
        for x in X:y.append(((-H*((x-(R/2))**2))/((R/2)**2))+H)
        plt.plot(X,y)
        plt.xlim([0, max(X)+0.5])
        plt.ylim([0, max(y)+0.5])
        plt.show()
    def Relationships(self):
        def r0():
            if ('H' in self.keys) and ('R' in self.keys) and ('c' not in self.keys):
                self.dict['c'] = atan((4*self.dict['H'])/(self.dict['R']))*(180/pi)
                print("(c)==> tan(c) = 4H/R")
                self.keys = self.dict.keys()
        def r1():  # T = 2t  (T, t)
            if ('T' in self.keys and 't' not in self.keys) or ('T' not in self.keys and 't' in self.keys):
                if 't' in self.keys and 'T' not in self.keys:
                    self.dict['T'] = 2 * self.dict['t']; print("(T)==> T = 2t")
                else:
                    self.dict['t'] = self.dict['T']/2; print("(t)==> T = 2t")
                self.keys = self.dict.keys()
        def r2():  # vfy = viy - gt  (vfy, viy, t)
            if ('vfy' in self.keys and 'viy' in self.keys and 't' not in self.keys) or ('vfy' in self.keys and 'viy' not in self.keys and 't' in self.keys) or ('vfy' not in self.keys and 'viy' in self.keys and 't' in self.keys):
                if 'vfy' in self.keys and 'viy' in self.keys:  # t
                    self.dict['t'] = (self.dict['vfy']-self.dict['viy']/-10); print("(t)==> vfy = viy - gt")
                elif 'viy' in self.keys and  't' in self.keys:  # vfy
                    self.dict['vfy'] = (self.dict['viy']-(10*self.dict['t'])); print("(vfy)==> vfy = viy - gt")
                else:  # viy
                    self.dict['viy'] = ((self.dict['t']*10)+ self.dict['vfy']); print("(viy)==> vfy = viy - gt")
                self.keys = self.dict.keys()
        def r3():  # viy = visin(c)   vx = vicos(c)
            if (('c' in self.keys) and ('vi' in self.keys)) or ('vx' in self.keys and 'vi' in self.keys) or ('viy' in self.keys and 'vi' in self.keys):
                if ('c' in self.keys) and ('vi' in self.keys):
                    if ('viy' not in self.keys):
                        self.dict['viy'] = self.dict['vi'] * sin(self.dict['c']*(pi/180)); print('(viy)==> viy = visin(c)')
                    if ('vx' not in self.keys):
                        self.dict['vx'] = self.dict['vi'] * cos(self.dict['c']*(pi/180)); print('(vx)==> vx = vicos(c)')
                if ('vx' in self.keys) and ('vi' in self.keys) and ('c' not in self.keys):
                    self.dict['c'] = acos(self.dict['vx']/self.dict['vi'])*(180/pi); print('(c)==> vx = vicos(c)')
                if ('viy' in self.keys) and ('vi' in self.keys) and ('c' not in self.keys):
                    self.dict['c'] = asin(self.dict['viy']/self.dict['vi'])*(180/pi); print('(c)==> viy = visin(c)')
                self.keys = self.dict.keys()
        def r4():  # t = (visin(c))/10  [vi, c, t]
            if ('vi' in self.keys and 't' in self.keys and 'c' not in self.keys) or ('vi' in self.keys and 't' not in self.keys and 'c' in self.keys) or ('vi' not in self.keys and 't' in self.keys and 'c' in self.keys):
                if ('vi' in self.keys and 't' in self.keys and 'c' not in self.keys):
                    self.dict['c'] = asin(10*self.dict['t']/self.dict['vi'])*(180/pi); print("(c)==> t = (visin(c))/10")
                elif ('vi' in self.keys and 't' not in self.keys and 'c' in self.keys):
                    self.dict['t'] = ((self.dict['vi']*sin(self.dict['c']*(pi/180)))/10); print("(t)==> t = (visin(c))/10")
                else:
                    self.dict['vi'] = ((10*self.dict['t'])/(sin(self.dict['c']*(pi/180)))); print("(vi)==> t = (visin(c))/10")
                self.keys = self.dict.keys()
        def r5():  # dy = viyt - (g*(t**2))/2  [dy, t, viy]
            if ('viy' in self.keys and 't' in self.keys and 'dy' not in self.keys) or ('viy' in self.keys and 't' not in self.keys and 'dy' in self.keys) or ('viy' not in self.keys and 't' in self.keys and 'dy' in self.keys):
                if ('viy' in self.keys and 't' in self.keys and 'dy' not in self.keys):
                    self.dict['dy'] = self.dict['viy']*self.dict['t'] - ((10*(self.dict['t']**2))/2); print("(dy)==> dy = viyt - (g*(t**2))/2")
                elif ('viy' in self.keys and 't' not in self.keys and 'dy' in self.keys):
                    pass #TODO
                else:
                    self.dict['viy'] = (self.dict['dy'] + (5 * (self.dict['t']**2)))/self.dict['t']; print("(viy)==> dy = viyt - (g*(t**2))/2")
                self.keys = self.dict.keys()
        def r6():  # (vfy**2) = (viy**2) - 20*dy  [vfy, viy, dy]
            if (('vfy' in self.keys) and ('viy' in self.keys) and ('dy' not in self.keys)) or (('vfy' in self.keys) and ('viy' not in self.keys) and ('dy' in self.keys)) or (('vfy' not in self.keys) and ('viy' in self.keys) and ('dy' in self.keys)):
                if ('vfy' in self.keys and 'viy' in self.keys and 'dy' not in self.keys):
                    self.dict['dy'] = ((self.dict['vfy']**2)-(self.dict['viy']**2)/-20); print("(dy)==> (vfy**2) = (viy**2) - 20*dy")
                elif ('vfy' in self.keys and 'viy' not in self.keys and 'dy' in self.keys):
                    self.dict['viy'] = ((self.dict['vfy']**2)+(20*self.dict['dy']))**.5; print("(viy)==> (vfy**2) = (viy**2) - 20*dy")
                else:
                    self.dict['vfy'] = ((self.dict['viy']**2)-(20*self.dict['dy']))**.5; print("(vfy)==> (vfy**2) = (viy**2) - 20*dy")
                self.keys = self.dict.keys()
        def r7():  # H = (((sin(c)**2)*(vi**2))/2*g)  [H, vi, c]
            if ('H' in self.keys and 'vi' in self.keys and 'c' not in self.keys) or ('H' in self.keys and 'vi' not in self.keys and 'c' in self.keys) or ('H' not in self.keys and 'vi' in self.keys and 'c' in self.keys):
                if ('H' in self.keys and 'vi' in self.keys and 'c' not in self.keys):
                    self.dict['c'] = asin(((20*self.dict['H'])/(self.dict['vi']**2))**.5)*(180/pi); print("(c)==> H = (((sin(c)**2)*(vi**2))/2*g)")
                elif ('H' in self.keys and 'vi' not in self.keys and 'c' in self.keys):
                    c = sin(self.dict['c']*(pi/180))**2
                    h = 20*self.dict['H']
                    self.dict['vi'] = ((h)/(c))**.5; print("(vi)==> H = (((sin(c)**2)*(vi**2))/2*g)")
                else:
                    self.dict['H'] = ((sin(self.dict['c']*(pi/180))**2)*(self.dict['vi']**2))/20; print("(H)==> H = (((sin(c)**2)*(vi**2))/2*g)")
                self.keys = self.dict.keys()
        def r8():  # R = vx*T  [R, vx, T]
            if ('R' in self.keys and 'vx' in self.keys and 'T' not in self.keys) or ('R' in self.keys and 'vx' not in self.keys and 'T' in self.keys) or ('R' not in self.keys and 'vx' in self.keys and 'T' in self.keys):
                if ('R' in self.keys and 'vx' in self.keys and 'T' not in self.keys):
                    self.dict['T'] = (self.dict['R']/self.dict['vx']); print("(T)==> R = vx*T")
                elif ('R' in self.keys and 'vx' not in self.keys and 'T' in self.keys):
                    self.dict['vx'] = (self.dict['R']/self.dict['T']); print("(vx)==> R = vx*T")
                else:
                    self.dict['R'] = self.dict['T'] * self.dict['vx']; print("(R)==> R = vx*T")
                self.keys = self.dict.keys()
        def r9():  # vf = ((vx**2)+(vfy**2))**.5  [vf, vfy, vx]
            if 'vfy' in self.keys and 'vx' in self.keys and 'vf' not in self.keys:
                self.dict['vf'] = ((self.dict['vx']**2)+(self.dict['vfy']**2))**.5
                print("(vf)==> vf = ((vx**2)+(vfy**2))**.5")
                self.keys = self.dict.keys()
        def r10():  # R =(((vi**2)*sin(2*c))/10)  [R, c, vi]
            if (('R' in self.keys) and ('c' in self.keys) and ('vi' not in self.keys)) or (('R' in self.keys) and ('c' not in self.keys) and ('vi' in self.keys)) or (('R' not in self.keys) and ('c' in self.keys) and ('vi' in self.keys)):
                if ('R' in self.keys) and ('c' in self.keys) and ('vi' not in self.keys):
                    self.dict['vi'] = ((10*self.dict['R'])/(sin((2*self.dict['c'])*(pi/180))))**.5; print("(vi)==> R =(((vi**2)*sin(2*c))/10)")
                elif ('R' in self.keys) and ('c' not in self.keys) and ('vi' in self.keys):
                    self.dict['c'] = (asin((10*self.dict['R'])/(self.dict['vi']**2))*(180/pi))/2; print("(c)==> R =(((vi**2)*sin(2*c))/10)")
                else:
                    self.dict['R'] = ((self.dict['vi']**2)*(sin((2*self.dict['c'])*(pi/180))/10)); print("(R)==> R =(((vi**2)*sin(2*c))/10)")
                self.keys = self.dict.keys()
        self.max = 0
        for i in range(10):
            self.max += 1
            if len(self.keys) != 11:
                for func in [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]:
                    func()
            else:
                self.max +=1
                break
        print(F"===========\nPredictions ({len(self.keys)}/11):")
        for i in self.keys:
            print(F"  {i} : {self.dict[i]}")
            
    def __init__(self, **kwargs):
        self.time = time.time()
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nGiven Data:")
        for i in kwargs.keys():
            print(F"  {i} : {kwargs[i]}")
        print("===========")
        self.dict = kwargs
        self.keys = list(self.dict.keys())
        self.Relationships()
        print(F"===========\nDuration: {time.time() - self.time} sec  ({self.max})")
        if 'H' in self.keys and 'R' in self.keys: 
            self.Draw(self.dict['H'], self.dict['R'])
        else:
            print("GraphingError: Incomplete Data (Either 'H' or 'R' or may both of them are missing...)")

#@================================>>
# Vi:vi  R:H  Vx:vx  vfy:vfy  g:g
# Viy:viy  Θ:c  H:H  t:t  T:T  Δy=dy
Projectile(H=45, R=240)
