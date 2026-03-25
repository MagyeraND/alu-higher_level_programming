def __str__(self):
        """Returns a string of the rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]
