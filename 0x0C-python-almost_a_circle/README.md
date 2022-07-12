All your files, classes and methods must be unit tested and be PEP 8 validated.
Create a folder named models with an empty file init.py inside - with this file, the folder will become a Python package
Write the class Rectangle that inherits from Base
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
Update the class Rectangle by overriding the str method
Update the class Rectangle by improving the public method def display(self)
Update the class Rectangle by adding the public method def update(self, *args)
Update the class Rectangle by updating the public method def update(self, *args)
Write the class Square that inherits from Rectangle
Update the class Square by adding the public getter and setter size
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:
Update the class Rectangle by adding the public method def to_dictionary(self)
Update the class Square by adding the public method def to_dictionary(self)
JSON is one of the standard formats for sharing data representation
Update the class Base by adding the class method def save_to_file(cls, list_objs)
Update the class Base by adding the static method def from_json_string(json_string)
Update the class Base by adding the class method def create(cls, **dictionary)
Update the class Base by adding the class method def load_from_file(cls)
