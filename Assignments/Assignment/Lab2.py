def add(x,y):
    return x+y

print add(1,2)

def add(x,y=None):
    if y is None:
        return x+1
    else:
        return x+y
    
print add(1)

def add(y=2,x=3):
    return x+y

print add(5)

def add(x,y):
    print ("add x+y :%d\n"%(x+y))
    return x+y

add(1,2)

def linear_congruential(a,c,m,seed,n):
    if((m>0 and m>a and m>c and m>seed and a>=0 and c>=0 and seed>=0)):
        list=[]
        print len(list)
        list.append(seed)
        for i in range(n):
            list.append((a*seed+c)%m)
            seed=list[len(list)-1]
    else:
        return
       
    return list

print linear_congruential(17,0,100,13,20)
print linear_congruential(16,0,100,13,20)
print linear_congruential(16,0,100,13,100)
            
        
