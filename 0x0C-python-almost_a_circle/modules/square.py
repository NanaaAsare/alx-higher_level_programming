#!/usr/bin/python3
'''square'''


Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    '''
    Declares a square and inherits from the rectangle class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Instantiates a new square
        '''
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates the attributes of the rectangle'''
        if len(args) == 0 and len(kwargs) == 0:
            return self

        if len(args) == 0:
            if len(kwargs) > 0:
                if 'id' in kwargs.keys():
                    self.id = kwargs['id']
                if 'size' in kwargs.keys():
                    self.width = kwargs['size']
                    self.height = kwargs['size']
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
                self.height = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]

    def to_dictionary(self):
        '''
        returns the dictionary representation of the
        square
        '''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.size}'
