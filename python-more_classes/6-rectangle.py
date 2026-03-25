class Rectangle:
    number_of_instances = 0  # Class attribute

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
