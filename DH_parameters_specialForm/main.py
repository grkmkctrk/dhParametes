import numpy as np

class DHs:
    def __init__(self, **kwargs):
        self.alpha = kwargs['alpha']
        self.theta = kwargs['theta']
        self.d = kwargs['d']
        self.a = kwargs['a']

    def DH(self):

        wholeDT = []
        
        #  T = np.where((T < 0) & (T > -0.01) , 0, T) <= it is not inportant 
        for i in range(0,len(self.theta)): # you can use others it doesnt matter
            aco = 0 if ((np.cos(np.deg2rad(self.alpha[i] % 360)) < 1e-10) & (np.cos(np.deg2rad(self.alpha[i] % 360)) > -1e-10)) else np.cos(np.deg2rad(self.alpha[i] % 360)) 
            asi = 0 if ((np.sin(np.deg2rad(self.alpha[i] % 360)) < 1e-10) & (np.sin(np.deg2rad(self.alpha[i] % 360)) > -1e-10)) else np.sin(np.deg2rad(self.alpha[i] % 360)) 
            tco = 0 if ((np.cos(np.deg2rad(self.theta[i] % 360)) < 1e-10) & (np.cos(np.deg2rad(self.theta[i] % 360)) > -1e-10)) else np.cos(np.deg2rad(self.theta[i] % 360)) 
            tsi = 0 if ((np.sin(np.deg2rad(self.theta[i] % 360)) < 1e-10) & (np.sin(np.deg2rad(self.theta[i] % 360)) > -1e-10)) else np.sin(np.deg2rad(self.theta[i] % 360)) 

            DT = [
                [tco, -tsi*aco, tsi*asi, self.a[i]*tco],
                [tsi, tco*aco, -tco*asi, self.a[i]*tsi],
                [0, asi, aco, self.d[i]],
                [0, 0, 0, 1]
                ]

            wholeDT.append(DT)
        return np.reshape(wholeDT, [len(self.theta), 4, 4]), len(self.theta)
    
    def multDT(self):

        multipliedDTs = np.matmul(
            self.DH()[0][self.DH()[1] - 2],
            self.DH()[0][self.DH()[1] - 1]
            )

        if self.DH()[1] > 2:  
            for i in range(self.DH()[1] - 3, -1, -1):
                multipliedDTs = np.matmul(
                    self.DH()[0][i],
                    multipliedDTs
                    )
        return multipliedDTs
    
    def pointInPlane(self, nokta, **axis):
        if axis['axis'] == 'global':
            return np.matmul(self.multDT(), np.reshape(np.append(nokta, [1]), [4, 1]))
        else:
            return np.matmul(np.linalg.inv(self.multDT()), np.reshape(np.append(nokta, [1]), [4, 1]))

                             
                                        

