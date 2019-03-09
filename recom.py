import numpy as np
import text_code as text

def recommend(n):
    lim=2
    lable=text.lables
    features=text.features[:,-1:]
    dist=0
    li=[]
    #print(features)
    for i in range(len(lable)):
        if(lable[i]==n):
            dist=features[i,0]
            break
    #print(dist)
    for i in range(len(lable)):
        if(lable[i]!=n):
            if(-lim<=(features[i,0]-dist) and (features[i,0]-dist)<=lim):
                if(lable[i,0] not in li):
                    li.append(lable[i,0])

    return li

