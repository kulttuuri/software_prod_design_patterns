'''
Prototype is used for cloning / copying existing instances.
Note that design patterns, like prototype, can be used in conjunction with each another.

Examples:
    - Graphic editors: Create a duplicate of existing rectangle, circle etc...
    - Game development: Clone existing characters, trees, buildings...
'''

import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        pass
        


class Car(Prototype):
    def __init__(self) -> None:
        self.manufacturer = None
        self.color = None
    
    def set_manufacturer(self, manufacturer) -> "Car":
        self.manufacturer = manufacturer
        return self
    
    def set_color(self, color) -> "Car":
        self.color = color
        return self
    
    def clone(self) -> "Car":
        return copy.deepcopy(self)


###
# Usage
###

# Method chaining
tesla_green = Car().set_manufacturer("Tesla").set_color("Green")
print(tesla_green.color)

tesla_red = tesla_green.clone().set_color("Red")
print(tesla_red.color)
print(tesla_green.color)
