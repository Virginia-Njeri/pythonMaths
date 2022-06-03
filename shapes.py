# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pie=3.14
        area_circle=pie*self.radius **2
        return area_circle

    def Circumfrence(self):
        pie=3.14*2
        radius=self.radius*self.radius
        cirmcum_circle=radius*pie
        return cirmcum_circle


#         A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a
class Square:
    def __init__(self,side):
        self.side=side


    def area(self):
        square_area=self.side**2
        return square_area

    def perimeter(self):
        square_perimeter=4*(self.side)
        return square_perimeter

#         Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def rectangle_area(self):
        area_rect=self.width*self.length
        return area_rect


    def rectangle_peremeter(self):
        perimeter_rect=2*(self.width+self.length)
        return perimeter_rect



# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
# class Sphere:
#     def __init__(self,r):
#         self.r=r
        
def surface_area(self):
    pie=3.14
    radius=self.r*self.r
    sphere_area=4*radius*radius
    return sphere_area


def sphere_volume(self):
    pie3=3.14
    radius3=self.r*self.r*self.r
    sphere_volume=4/3*radius3*pie3
    return sphere_volume
    

    





        


        
        




        