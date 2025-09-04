from graph import*

color=['red','green','blue','yellow','grey']
i = 0
for y in range(20,101,20):
    circle(20,y,5)
    print()
    for x in range(20,101,20):
        brushColor(color[i])
        circle(x,20,5)
        i=i+1


run()    
