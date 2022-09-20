from typing import Tuple

class Module:
    def find_shape(self, ndarray) -> Tuple[int,...]:
        if isinstance(ndarray, list):
            # More dimensions make a recursive call
            outermost_size = len(ndarray)
            row_shape = self.find_shape(ndarray[0])
            return (outermost_size, *row_shape)
        else:
            # No more dimensions
            return ()

class Vector(Module):
    """
    Core data structure of Linearity: Vector

    Algebraic definition
    ====================
    Vector - an ordered collection of some numeric data.

    Geometric definition
    ====================
    Directed line segment which has specified beginning (head)
    and end (tail). It has 2 main characteristics:
    1. Length
    2. Direction
    """
    def __init__(self, data):
        """
        Constructor

        self: represents instance of a 'Vector' class
        data: data to be stored
        """
        
        self.data = data
        self.shape = self.find_shape(data)

    def __repr__(self):
        default_print = f"Vector(data={self.data})"
        multiline_print = "[\n" + "\n".join(f"Vector(data={row})".rjust(len(f"Vector(data={row})") + 2) for row in self.data) + "\n]"
        return multiline_print if len(self.shape) > 1 else default_print

    def __len__(self):
        return len(self.data)
