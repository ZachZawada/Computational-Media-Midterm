'''
    Name:               Zach Zawada
    Current Date:       03/04/2019
    Sources Consulted:  processing.py tutorials on the website,py.processing.org,
                        examples created in class

    By submitting this work, I attest that it is my 
    original work and that i did not violate the
    University of Mississippi academic policies 
    set forth in the M book
    
    The project creates multiple rotating triangles
    by moving the cursor from the left to right 
    of the window.  the triangles also change color using 
    a rainbow gradient
    The background will also chang color based on the gray scale
'''

fillChange = 0

def setup():
    size(600,600)
    noFill()
    strokeWeight(3)
    frameRate(30)
    colorMode(HSB)

#time variable        
t = 0 
NUM_TRIS = 90

def draw():
    global t, fillChange
    background(fillChange)
    if mouseX < 300:
        fillChange +=1
    elif mouseX > 300:
        fillChange -=1
    else:
        fillChange = 0
        
    if fillChange >= (313, 0, 255):
        fillChange = (313, 0, 255)
    elif fillChange <= 0:
        fillChange = 0
    
    translate(width/2, height/2)

    #changes the number of triangles by mapping
    #the mouse location to the variable
    NUM_TRIS = map(mouseX,0,width,3,120)
    for i in range(int(NUM_TRIS)):
        rotate(radians(360/NUM_TRIS))
        
        #save this orientation
        pushMatrix()
        translate(200,0)
        rotate(radians(t+2 * i * 360/NUM_TRIS))
        
        #Rainbow color
        stroke(3*i,255,255)
        #stroke('#FFEB08')
        #fill(3*i,255,255)
        
        tri(100)
        
        #return to saved orientation
        popMatrix()
    t += 0.5
    
def tri(length):
    '''Draws an equilateral triangle of
    given length around the center of the triangle'''
    triangle(0,-length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)

    #Displays the location of the cursor in the command prompt    
    
    print('Coordinate location of the mouse', mouseX, mouseY)
