from circle import Circle

if __name__ == "__main__":
    radius = input("Radius: ")

    circle = Circle(radius=float(radius))
    perimeter = circle.get_perimeter()
    area = circle.get_area()

    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")
