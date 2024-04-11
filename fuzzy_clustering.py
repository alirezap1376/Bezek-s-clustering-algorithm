import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

df = pd.DataFrame(  [(0,4),(0,2),(0,0),(1,3),(1,2),(1,1),(2,2),(3,2),(4,2),(5,3),(5,2),(5,1),(6,4),(6,0) ] , columns=['a' , 'b']     )
c = 2
m=1.5


def U_maker ( c):
    U = pd.DataFrame( index = list(  range(c)  )   , columns = list(range(len(df))) )
    for i in range(len(U.columns)):
        U.iloc[   random.choice(U.index) , i            ] = 1    
    return U

U= U_maker ( c)
firstcluster = []
secondcluster = []


for i in range( len(U_maker(c) ) ):
    if i == range( len(U_maker(c) ) )[0]:
        for j in range(len(U_maker(c).columns)):
            if U.iloc[i,j] ==1 :
                firstcluster.append(j)
    else:
        for j in range(len(U_maker(c).columns)):
            if U.iloc[i,j] ==1 :
                secondcluster.append(j)

            

    
firstcluster_x = sum(df.iloc[ firstcluster ,  0  ]) / len(firstcluster)
firstcluster_y = sum(df.iloc[ firstcluster ,  1  ]) / len(firstcluster)

secondcluster_x = sum(df.iloc[ secondcluster ,  0  ]) / len(secondcluster)
secondcluster_y = sum(df.iloc[ secondcluster ,  1  ]) / len(secondcluster)

counter = 0

while counter <100 :
    
    df["member_ship_first_cluster"] = 0
    df["member_ship_second_cluster"] = 0


    for i in range(len(df)):
        dist_from_first_cluster = np.sqrt((df.iloc[i , 0 ] - firstcluster_x)**2 + (df.iloc[i , 1] - firstcluster_y)**2)
        dist_from_second_cluster = np.sqrt((df.iloc[i , 0 ] - secondcluster_x)**2 + (df.iloc[i , 1] - secondcluster_y)**2)
        
        df.iloc[i, 2]= ( ( dist_from_first_cluster / (dist_from_first_cluster + dist_from_second_cluster) )**(2/(m-1))  )**-1           
        df.iloc[i, 3]= ( ( dist_from_second_cluster / (dist_from_first_cluster + dist_from_second_cluster) )**(2/(m-1))  )**-1           
    
    firstcluster=[]
    secondcluster=[]

    for i in range(len(df)):   
        if df.iloc[i, 2]   >= df.iloc[i, 3] :
            firstcluster.append( i)
        else:
            secondcluster.append( i)  
    
    firstcluster_x = sum(df.iloc[ firstcluster ,  0  ]) / len(firstcluster)
    firstcluster_y = sum(df.iloc[ firstcluster ,  1  ]) / len(firstcluster)

    secondcluster_x = sum(df.iloc[ secondcluster ,  0  ]) / len(secondcluster)
    secondcluster_y = sum(df.iloc[ secondcluster ,  1  ]) / len(secondcluster)

    
    counter = counter+1
    
    
    
   
plt.scatter(df.iloc[:,0] , df.iloc[: , 1 ] )
    
    
    
    
    
    
    
    
    
    

