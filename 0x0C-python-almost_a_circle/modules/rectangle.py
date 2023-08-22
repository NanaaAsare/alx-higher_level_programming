<<<<<<< HEAD
#!/usr/bin/python3
'''rectangle'''


Base = __import__('base').Base


class Rectangle(Base):
    '''
    Declares the Rectangle class and inherits
    from the Base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Instantiates a Rectangle with width, height, x, y and id

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int), y(int)
            id (int): id of rectangle
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # getters
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # setters
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''displays the rectangle to stdout using #'''
        if self.width == 0 or self.height == 0:
            print('')
            return

        for a in range(self.y):
            print('')
        for i in range(self.height):
            for b in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        '''updates the attributes of the rectangle'''
        if len(args) == 0 and len(kwargs) == 0:
            return self

        if len(args) == 0:
            if len(kwargs) > 0:
                if 'id' in kwargs.keys():
                    self.id = kwargs['id']
                if 'width' in kwargs.keys():
                    self.width = kwargs['width']
                if 'height' in kwargs.keys():
                    self.height = kwargs['height']
                if 'x' in kwargs.keys():
                    self.x = kwargs['x']
                if 'y' in kwargs.keys():
                    self.y = kwargs['y']
        else:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) >= 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]

    def to_dictionary(self):
        '''
        function to return the dictionary representation
        of the rectangle
        '''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) \
=======
#!/usr/bin/python3
'''rectangle'''


Base = __import__('base').Base


class Rectangle(Base):
    '''
    Declares the Rectangle class and inherits
    from the Base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Instantiates a Rectangle with width, height, x, y and id

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int), y(int)
            id (int): id of rectangle
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # getters
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # setters
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''displays the rectangle to stdout using #'''
        if self.width == 0 or self.height == 0:
            print('')
            return

        for a in range(self.y):
            print('')
        for i in range(self.height):
            for b in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        '''updates the attributes of the rectangle'''
        if len(args) == 0 and len(kwargs) == 0:
            return self

        if len(args) == 0:
            if len(kwargs) > 0:
                if 'id' in kwargs.keys():
                    self.id = kwargs['id']
                if 'width' in kwargs.keys():
                    self.width = kwargs['width']
                if 'height' in kwargs.keys():
                    self.height = kwargs['height']
                if 'x' in kwargs.keys():
                    self.x = kwargs['x']
                if 'y' in kwargs.keys():
                    self.y = kwargs['y']
        else:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) >= 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]

    def to_dictionary(self):
        '''
        function to return the dictionary representation
        of the rectangle
        '''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) \
>>>>>>> ce5a8ed37eb6209caf780c151d7a30b13611efb7
{self.x}/{self.y} {self.width}/{self.height}'