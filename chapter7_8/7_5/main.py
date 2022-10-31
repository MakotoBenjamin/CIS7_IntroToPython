from ClassRegularPolygon import RegularPolygon

def main():
    poly1 = RegularPolygon()

    poly2 = RegularPolygon(6, 4)

    poly3 = RegularPolygon(10, 4, 5.6, 7.8)

    print("Polygon 1 | Perimeter: {:.2f} | Area: {:.2f}".format(poly1.getPerimeter(), poly1.getArea()))

    print("Polygon 2 | Perimeter: {:.2f} | Area: {:.2f}".format(poly2.getPerimeter(), poly2.getArea()))

    print("Polygon 3 | Perimeter: {:.2f} | Area: {:.2f}".format(poly3.getPerimeter(), poly3.getArea()))

main()
