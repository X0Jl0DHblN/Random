from graph import*

color = ['green','red','yellow','gray','orange']

i = 0

def Circl(color,i):
    for x in range(20,101,20):
        brushColor(color[i])
        circle(x,20,5)
        i=i+1
        print()
        

for y in range(20,101,20):
    circle(20,y,5)
    
    
   
        





run()
