import Polygon, Rectangle, Triangle

def main():
    p = Polygon.Polygon(40, 60)

    r = Rectangle.Rectangle(40, 30)

    t = Triangle.Triangle(10, 10)

    print("Polygon:")
    p.print_shape()

    print("Rectangle:")
    r.print_shape()
    r.set_shape(False)
    print("This shape is a square" if r.isSquare else "This shape is not a square")

    print("Triangle:")
    t.print_shape()
    t.print_area()



main()
