# Linearity - WIP
Project "Linearity" - linear algebra in Python. This repository is for educational purposes to understand Linear Algebra through coding ^^ 

## Features

Vector initialization
```python
from linearity.core.engine import Vector

# Initialize 1D vector 
v = Vector([1,2,3])
v

# Output: Vector(data=[1, 2, 3])

# Initialize 2D Vector
t = Vector([[1,3,4], [3,6,8]])
# Output:
#[
#  Vector(data=[1, 3, 4])
#  Vector(data=[3, 6, 8])
#]
```

Get the shape of the vector
```python
from linearity.core.engine import Vector

# Initialize 1D vector 
v = Vector([1,2,3])
v.shape
# Output: (3,)
```

## Log
- 20 Sep 2022 - created Vector class, added 3 methods: __repr__, __len__, and defined a function which finds the shape of the vector

## TODO
- Add float type conversion when creating a vector
- Allow user to choose the data type (optional)