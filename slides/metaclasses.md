---
# title: Metaclasses
# separator: <!--s-->
# verticalSeparator: <!--v-->
theme: solarized
# revealOptions:
#   transition: 'fade'
# translated from PT to EN by ChatGPT4
---

# Metaclasses

## What are they for?

## Where do they live?

## How do they reproduce?

Leonardo Rochael Almeida

October 23, 2022

Note:

Intro: 5 min.

Launch IPython in %doctest_mode

Launch x11vnc

Launch Remote Desktop Viewer

---

![Cover Fluent Python 2nd Ed.](img/fluent-python.png)

Note:

I have been working with Python for 21 years.

My first job with Python was having Luciano Ramalho as a boss.

And I had the honor of reviewing both the 1st and 2nd ed. of Fluent Python.

And I was a victim of the curse of knowledge.

---

## But first: two types of methods

* Normal methods:
  * How to declare: `def method(self):`
  * How to use: `object.method()`
* Special methods
  * How to declare: `def __str__(self):`
  * How to use: `print(object)`

Note:

A normal method is what you access with a "dot".

A special method is one that is usually accessed by Python
to do something special with an instance of your class.

---

![Table of special methods for mathematical operations](img/special-methods-operators.png)

Note:

Source: Fluent Python Second Edition

For example, these are all the special methods that your class can
implement, and they allow the class instance to participate in operations with
mathematical operators, plus, times, etc.

---

![Table of special methods except for mathematical operations](img/special-methods-noop.png)

Note:

Source: Fluent Python Second Edition

These special methods are all the others that do not have to do with
participating in operations.

There are special methods for your class to be called as if it were a function,
indexed as if it were a list or dictionary, provide a length with
`len()`, specify its representation on the console, etc.

---

![Attribute search sequence](img/method-resolution-order.png)

Note:

[Source](https://excalidraw.com/#room=1c8d72d1ecb12684899d,44bhxgUJPAwiO3oXuNRoJw)

Show `slides/code/slide0_methods.py`

```text
from slide0_methods import *

m1 = MyClass()

m2 = MySubClass()

m1.double()

m1.x = 7

m1.double()

m2.double()

m1

m2

def __call__(self, other):
    return self.x + other

MyClass.__call__ = __call__

m2(7)
```

---

## Search Sequence: Normal Methods

(and normal attributes)

0. instance
1. class
2. superclasses

---

## Search Sequence: Special Methods

("dunder" methods: `__...__`)

0. ~~instance~~ **NO**!
1. class
2. superclasses

---

## It's Always *Runtime*

In Python, function and class declarations "happen" at
**runtime**.

Note:

Classes are created at runtime,

But imports only "run" the module once.

Demonstrate with prints all around:

* `slides/code/slide1_runtime.py`

---

## Everything is an Object (1)

![Labels, not Boxes](img/labels-not-boxes.png)

<font size="1">
Image © Luciano Ramalho, used with permission
</font>

Classes are values too!

Note:

In Python, all declared things have assigned variables, including
functions and classes!

Classes (and functions) can be assigned to variables, lists, and dictionaries.

Demonstrate overriding the variables in which the classes were declared,
and instantiate the classes through the variables in which they were saved.

```text
a = [1, 2, 3]
b = a
b.append(4)
b
a
```

I can assign classes to other variables

```text
MyClass2 = MyClass

instance2 = MyClass2()

MyClass = None

instance = MyClass()
```

I can put classes in lists, or place them in dictionaries

Moreover, the content of imported modules is in a dictionary:

```text
slide1_runtime.__dict__.keys()

{key: value for key, value in slide1_runtime.__dict__.items() if not key.startswith('__')}
```

As well as the content of classes and instances:

```python
m1.__dict__
MySubClass.__dict__
```

As my friend Lalo Martins would say:

> Python is made only of dictionaries and tons of syntactic sugar

---

## The Two Responsibilities of `class`

```python
class Duck:
    ...
```

* Generate a class
* Assign the class to a variable
  * With the same name as the class

Note:

`class` is not a "declaration". It's a structured command.

The same two responsibilities apply to `def` and functions.

What this means is that you can create classes inside functions.

And it is also possible to create functions inside functions.

---

## Everything is an Object (2)

All values have a class

* including classes!

Note:

Demonstrate `obj.__class__`, `type(obj)`, and `isinstance(obj, class)`

```text
duck.__class__
type(duck)

duck.__class__ is type(duck)

duck.__class__ is slide1_runtime.Duck

```

---

## Everything is an Object (3)

* Creating classes dynamically

Note:

demonstrate `slides/code/slide5_dynamic_class.py`

```text
from slide5_dynamic_class import *

m3 = MySubClass()
m3.double()
m3.add()

MySubClass.__class__

MyOtherSubClass = my_subclass_generator(27)

m4 = MyOtherSubClass()
m4.double()
m4.add()

MyOtherSubClass.__bases__
MyOtherSubClass.__name__
MyOtherSubClass.__class__

MyMostDynamicSubClass = type(
    'MyMostDynamicSubClass',  # the class name
    (MyClass, MyMixin),  # superclasses
    {'x': 27},  # class "namespace"
)

# Including with methods

def __init__(self, x):
    self.x = x

MyReallyDynamicSubClass = type(
    'MyReallyDynamicSubClass',
    (MyClass, MyMixin),
    {'__init__': __init__},
)
```

To create an instance, I invoke the class.

To dynamically create a class, I invoke the class of the class.

---

![Class Relationships](img/class-relationships-1.svg)

Note:

[Origin](https://excalidraw.com/#room=238469586b20a3132da2,8WP2bHrBNSR7GZ257qVWRA)

---

## Metaclass: The Class of the Class

* `type`: the default class of classes
  * 1 parameter: returns the class of an object
  * 3 parameters: creates a new class

Note:

Metaclass is the name we give to the class of a class

And `type` is the default metaclass for all classes

---

## "`type`" & "`object`"

a peculiar relationship

![Relationships between type and object](img/object-type-relationship.png)

Note:

[Origin](https://excalidraw.com/#room=1f3517d27415d387d3ff,go5T1JAv3yH1fx5wenTlqA)

But if `type` is a (meta)class, whose subclass is it?

And if `object`, which is a class, is also an instance, who is the class of
`object`?

```text
>>> type(object)
<class 'type'>
>>> type(type)
<class 'type'>
>>> type.__class__
<class 'type'>
>>> type.__bases__
(<class 'object'>,)
>>> object.__bases__
()
```

**The relationship between `object` and `type` cannot be constructed in Python.**

It is part of the language definition.

---

## Creating New Metaclasses

* Inheriting from `type`

$$$python
class better_repr_type(type):
    ...
$$$

Note:

If `type` is a class, can I inherit from `type`?

`slides/code/slide9_better_repr.py`

$$$text

from slide9_better_repr import *

MySubClassWithRepr = better_repr_type(
    'MySubClassWithRepr',  # name
    (MyClass, MyMixin),  # bases
    {'__init__': __init__},   # attributes / methods
)
$$$

---

![Class relationships with metaclass](img/class-relationships-2.png)

Note:

[Source](https://excalidraw.com/#room=1076797d69bd2c569513,l33QvHS3xBgAcPXs-WptjA)

---

## Using Metaclasses in "Normal" Classes

$$$python
class MyClass(Super, ..., metaclass=MyMetaClass):
    ...
$$$

Note:

$$$python
class MySubClassWithRepr2(MyClass, metaclass=better_repr_type):
    def __init__(self, x):
        self.x = x
$$$

---

## But What Are They For After All? (1)

* Provide special methods to classes
  * `__repr__`
  * `__getitem__`
  * `__(...)__`

---

## But What Are They For After All? (2)

* Prepare the `namespace` (`.__dict__`) of a class
* Intercept/register/customize class creation
* Manipulate methods and attributes of the class during creation
* Intercept/customize instance creation

Note:

`slides/code/slide12_walkthru.py`

Complete walkthrough of the class declaration process

Debug step by step in vs.code

Override the `__call__` of the metaclass to return `None`.

* Intercept/customize instance creation
  * `__call__`
    * Redundant with `__new__` of the class

---

## What They Are NOT For

* Influence instances after they are created
* Provide **normal** attributes or methods to classes
  * only special methods!

Note:

MRO of normal attributes never passes through the metaclass.

---

## You (Probably) Will Never Need Metaclasses (1)

* `SuperClass.__init_subclass__()`
  * Invoked for each declared subclass
    * Even in indirect subclasses
  * But not in the class where it is declared

---

## You (Probably) Will Never Need Metaclasses (2)

Decorators:

$$$python
@decorator
class MyClass:
    ...
$$$

* A good example:
  * `@dataclasses.dataclass`

Note:

A decorator receives the class already made, and has the opportunity to modify it, and
even replace it, before returning it.

A good existing example is `@dataclass`, which creates methods in your classes.

---

## You (Probably) Will Never Need Metaclasses (3)

* `__class_getitem__`
  * Used by Python for *type hints*

$$$python
def print_steps(steps: list[str]): ...
$$$

Note:

Show `slides/code/slide20_meta_alternatives.py`

$$$python
from slide20_meta_alternatives import *

Anseriformes['Duck']

@check_anseriformes
class Dog(Duck):
    def quack(self):
        print("woof, woof!")

class Cat(Duck):
    def quack(self):
        print("meow!")

Anseriformes['Dog']

$$$

---

## Classes Also Accept Keywords

$$$python
class MySubClass(SuperCls, keyword='Key', number=42):
    ...
$$$

* But it is necessary to consume them:
  * Where:
    * `MetaClass.__new__()`
    * `SuperClass.__init_subclass__()`
  * Because `object.__init_subclass__()` does not accept them.

Note:

And since we are talking about class customization, an interesting thing is
that classes accept *keyword arguments* beyond `metaclass=`

They must be consumed in the `__new__` of the metaclass, or in the `__init_subclass__` of
a parent class.

Open `slides/code/slide12_walkthru.py` next to
`slides/code/slide23_keywords.py` and debug.

---

## SQLModel: An Example of Keyword in Classes

$$$python
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    secret_name: str
    age: int
$$$

* https://sqlmodel.tiangolo.com/

Note:

The absence of `table=` indicates that the ORM should not create
a table for records of this class.

But subclasses of such a class may declare `table`.

---

## In Summary

* Everything has classes, including the classes
* Metaclasses provide special methods for classes
  * And only special methods
* Metaclasses have no influence over instances of the class
  * method/attribute search does not flow to the metaclass
* You can create (meta)classes for your classes
  * But you probably don't need to

Note:

Some people think that Python is an objectifying language... Everything is an object!

I prefer to think that Python is a very classy language! Everything has a lot of class!

Metaclasses help the language evolve (`__init_subclass__`, `__class_getitem__`).

Metaclass is for those making frameworks, like SQLAlchemy or Pydantic.

If you're wondering if you need to use metaclasses, you definitely don't need to ;-)

Those who need them know exactly why they need them.

---

## Questions?

----

$$$python
from autostring import AutoString

class IceCreamFlavor(AutoString):
    cream
    strawberry
    chocolate
$$$

---

## Thank You!

GH: [leorochael/2022-10-23-Talk-PythonBrasil-Metaclasses](https://github.com/leorochael/2022-10-23-Talk-PythonBrasil-Metaclasses)

![QR Code for the URL of this talk's github](img/github-talk-qrcode.png#img-float-right)

https://www.linkedin.com/in/leorochael/

Telegram: `@LeoRochael`

email: `leorochael@gmail.com`

<font size="4" style="text-align: left">
PS: Want to work in Berlin? Talk to me! Senior Dev or Sr Data Eng.
</font>
