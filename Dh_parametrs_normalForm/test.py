from main import DHs


rs = DHs(theta = [ 0,  0, -90,  0,  0,  0],
        alpha =  [0, -90, 0, -90, 90, -90],
        a     =  [0, 0, 1, 1, 0,0], 
        d     =  [0, 0, 1, 1, 0, 0]
        )

#  theta alpha a   d
#  0     90    50  50
#  90    270   40  0


#print(rs.DH())
#print(rs.DH())
#print(rs.multDT())


print(rs.pointInPlane(      # axis 'global' : to find where the defined point on the local plane is in the global plane                            
    [0, 0, 10],            # axis 'local' : to find where the defined point on the global plane is in the local plane 
    axis = 'global')  
    )  

