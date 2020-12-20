import numpy as np

class DHs:
    def __init__(self, **kwargs):
        self.alpha = kwargs['alpha']
        self.theta = kwargs['theta']
        self.d = kwargs['d']
        self.a = kwargs['a']

    def DH(self):

        wholeDT = []
        

        for i in range(len(self.theta)): # you can use others it doesnt matter
            aco = 0 if ((np.cos(np.deg2rad(self.alpha[i] % 360)) < 1e-10) & (np.cos(np.deg2rad(self.alpha[i] % 360)) > -1e-10)) else np.cos(np.deg2rad(self.alpha[i] % 360)) 
            asi = 0 if ((np.sin(np.deg2rad(self.alpha[i] % 360)) < 1e-10) & (np.sin(np.deg2rad(self.alpha[i] % 360)) > -1e-10)) else np.sin(np.deg2rad(self.alpha[i] % 360)) 
            tco = 0 if ((np.cos(np.deg2rad(self.theta[i] % 360)) < 1e-10) & (np.cos(np.deg2rad(self.theta[i] % 360)) > -1e-10)) else np.cos(np.deg2rad(self.theta[i] % 360)) 
            tsi = 0 if ((np.sin(np.deg2rad(self.theta[i] % 360)) < 1e-10) & (np.sin(np.deg2rad(self.theta[i] % 360)) > -1e-10)) else np.sin(np.deg2rad(self.theta[i] % 360)) 

            DT = [
                [tco, -tsi, 0, self.a[i]],
                [tsi*aco, tco*aco, -asi, -self.d[i]*asi],
                [asi*tsi, asi*tco, aco, self.d[i]*aco],
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

                             
                                        

