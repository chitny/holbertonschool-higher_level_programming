#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """this class will create a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """A new square instance"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__width

    @size.setter
    """Sets the size attribute."""

    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width mus be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance."""
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        dict = {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
        return dict