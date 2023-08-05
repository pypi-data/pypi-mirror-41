# privatebroker

PrivateBroker (beta) is a module for encapsulation.

It allows you to hide methods of classes that are undesirable in the implementation of child elements. Private methods become unavailable in instances of classes and classes of heirs.

Private methods are kept in the "broker", which allows you to access the private method if necessary.

## Installation

Use the package manager [pip](https://pip.pypa.io/...) to install foobar.

```bash
pip install privatebroker
```

## Usage

the privateclass decorator accepts a class whose specific methods must be hidden. the decorator privatemethod accepts the method and puts it in the broker.

The broker returns the necessary function (attribute of the private method) by taking two arguments: the class (from example A (!! not self !!)) and the name of the method (the string is required).

To get the result of a private method, you need to refer to the attribute of the private method and pass it the arguments expected by the private method.

```python

from privatebroker import privateclass, privatemethod

@privateclass
class A(object):
    
    def __init__(self, *args, **kwargs):
        self.some_one = {}
    
    
    @privatemethod
    def a_private2(self):
        pass
    
    
    @privatemethod
    def a_private(self, key, value):
        self.some_one[key] = value
    
    
    def test(self, x, y):
        private = self.broker(A, 'a_private') # call to private
        return private(self, x, y)
    
    
    def a_public(self):
        return self.some_one

#a = A()
#print(a.a_private())  - >  Error

@privateclass
class B(A):
    
    @privatemethod
    def b_private(self):
        return 'Я могу быть только у объекта B'
    
    def b_public(self):
        self.test('a', 11)
        return self.some_one


b = B()
print(b.b_public())
```

## Contributing

Important!
This is the first test version and so far the expediency of using this module is questionable!
Traction requests are welcome. For major changes, please first open the question to discuss
what you would like to change.

Please remember to update the tests as needed.

## License
[MIT](https://choosealicense.com/licenses/mit/)