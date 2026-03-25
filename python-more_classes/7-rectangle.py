class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        # Use str(self.print_symbol) to handle lists/tuples passed as symbols
        line = str(self.print_symbol) * self.__width
        return ((line + "\n") * self.__height)[:-1]
