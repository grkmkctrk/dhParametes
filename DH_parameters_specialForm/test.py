from main import DHs


rs = DHs(theta = [ 0, 0,  0,  90,  -90,  0],
        alpha =  [90, 90, 0, 90, -90, 0],
        a     =  [0, 0, 0, 0, 0, 0], 
        d     =  [0, 40, 50, 0, 0, 40]
        )

#  theta alpha a   d
#  0     90    50  50
#  90    270   40  0


#print(rs.DH())
#print(rs.multDT())


print(rs.pointInPlane(      # axis 'global' : to find where the defined point on the local plane is in the global plane                            
    [0, 0, 10],            # axis 'local' : to find where the defined point on the global plane is in the local plane 
    axis = 'global')  
    )  

