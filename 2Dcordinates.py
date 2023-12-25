''' 
    Write oop classes to handle the following request
    
    1. A user can create and view 2d coordinate
    2. A user can find out the distance between two cordinates
    3. A user can find the distance of a coordinate from origin
    4. A user can check if a point lies on a given line
    5. A user can find the distance between a given 2d point and a given line
'''

class Point:
    
    # intializing constructor
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
        
    # print coordinates
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    # function to find distance between two point
    def two_cordinate_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2) ** 0.5
    
    # distance from origin
    def distance_from_origin(self):
        #return (self.x_cod**2 + self.y_cod**2)**0.5
        return self.two_cordinate_distance(Point(0,0))

class Line:
    
    #constructor function
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        
    # print line equation
    def __str__(self):
        if self.A > 0 and self.B > 0 and self.C > 0:
            return '{}x+{}y+{}==0'.format(self.A,self.B,self.C)
        elif self.A > 0 and self.B > 0 and self.C < 0:
            return '{}x+{}y{}==0'.format(self.A,self.B,self.C)
        elif self.A > 0 and self.B < 0 and self.C > 0:
            return '{}x{}y+{}==0'.format(self.A,self.B,self.C)
        elif self.A < 0 and self.B > 0 and self.C > 0:
            return '{}x+{}y+{}==0'.format(self.A,self.B,self.C)
        elif self.A < 0 and self.B < 0 and self.C > 0:
            return '{}x{}y+{}==0'.format(self.A,self.B,self.C)
        elif self.A < 0 and self.B > 0 and self.C < 0:
            return '{}x+{}y{}==0'.format(self.A,self.B,self.C)
        elif self.A > 0 and self.B < 0 and self.C < 0:
            return '{}x{}y{}==0'.format(self.A,self.B,self.C)
        else:
            return '{}x{}y{}==0'.format(self.A,self.B,self.C)
              
    # method to check point lie on line
    def point_on_line(line,point):
        if line.A * point.x_cod + line.B*point.y_cod + line.C == 0:
            return "lies on line"
        else:
            return "does not lies on line"
        
    # find the distance between a given 2D point and a given line
    def shortest_distance_between_point_and_line(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C) / (line.A**2+line.B**2)**0.5
        
        
    
p1 = Point(4,5)
print(p1)
p2 = Point(5,6)
print(p2)
print(p1.two_cordinate_distance(p2))
s = p1.distance_from_origin()
print(s)
