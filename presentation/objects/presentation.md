class: center, middle, inverse

# Introducción a la Programación I
Objects & Classes

---

# Agenda

- Object & Class (Methods)

---

# Object-oriented programming - OOP

- One of the most efective approaches to writing software
- Programming paradigm
  - Others: Structured programming, Functional programming
- In OOP we create *classes* that represents real-world things, then we create *objects* based on these classes
- Writing a **class**, defines the general behavior that a whole category of **objects** can have
- Making an object from a class is called *instantiation*, and you work with *instances* of a class

---

# What is an Object?

- Similar to real-world objects.
- They share two characteristics:
 - State
 - Behavior
- Identifying state and behavior of real-world objects is first step to start thinking in terms of OOP
- Two main questions:
 - What possible states can this object be in?
 - What possible behavior can this object perform?

???

Objects are key to understanding object-oriented technology. Look around right now and you'll find many examples of real-world objects: your dog, your desk, your television set, your bicycle.
Real-world objects share two characteristics: They all have state and behavior. Dogs have state (name, color, breed, hungry) and behavior (barking, fetching, wagging tail). Bicycles also have state (current gear, current pedal cadence, current speed) and behavior (changing gear, changing pedal cadence, applying brakes). Identifying the state and behavior for real-world objects is a great way to begin thinking in terms of object-oriented programming.
Take a minute right now to observe the real-world objects that are in your immediate area. For each object that you see, ask yourself two questions: "What possible states can this object be in?" and "What possible behavior can this object perform?". Make sure to write down your observations. As you do, you'll notice that real-world objects vary in complexity; your desktop lamp may have only two possible states (on and off) and two possible behaviors (turn on, turn off), but your desktop radio might have additional states (on, off, current volume, current station) and behavior (turn on, turn off, increase volume, decrease volume, seek, scan, and tune). You may also notice that some objects, in turn, will also contain other objects. These real-world observations all translate into the world of object-oriented programming.

---

# A software object

- Stores its state in fields.
- Exposes its behavior through methods.

.center[![]({{site.baseurl}}/presentation/objects/object.jpg)]

???

Software objects are conceptually similar to real-world objects: they too consist of state and related behavior. An object stores its state in fields (variables in some programming languages) and exposes its behavior through methods (functions in some programming languages).

---

# Example: Bicycle

.center[![]({{site.baseurl}}/presentation/objects/object-bicycle.jpg)]

???

By attributing state (current speed, current pedal cadence, and current gear) and providing methods for changing that state, the object remains in control of how the outside world is allowed to use it. For example, if the bicycle only has 6 gears, a method to change gears could reject any value that is less than 1 or greater than 6.

---

# Methods

- Methods
 - Operates object's internal state
 - Serves as primary mechanism for object-to-object communication.
- Encapsulation:
 - Hiding internal state.
 - Require all interaction through object's methods.
- Examples:
```python
def printStates():
```
```python
def changeGears(newGear):
```
```python
def length():
```

???

Methods operate on an object's internal state and serve as the primary mechanism for object-to-object communication. Hiding internal state and requiring all interaction to be performed through an object's methods is known as data encapsulation — a fundamental principle of object-oriented programming.

---

# What is a Class?

- Individual real world objects can be of the same kind
 - Eg: Many types of bicycles
- Each bicycle was built from the same blueprint (same components)
- In OO:
 - Each bicycle is an instance of the class of objects known as bicycles
- Class is the blueprint from which individual objects are created

???

In the real world, you'll often find many individual objects all of the same kind. There may be thousands of other bicycles in existence, all of the same make and model. Each bicycle was built from the same set of blueprints and therefore contains the same components. In object-oriented terms, we say that your bicycle is an instance of the class of objects known as bicycles. A class is the blueprint from which individual objects are created.

---

# Bicycle class

```python
class Bicycle:

  cadence = 0
  speed = 0
  gear = 1

  def change_cadence(self, cadence):
    self.cadence = cadence

  def change_gear(self, gear):
    self.gear = gear

  def speed_up(self, increment):
    self.speed = self.speed + increment

  def apply_brakes(self, decrement):
    self.speed = self.speed - decrement

  def print_state(self):
    print(f'cadence: {self.cadence}, speed: {self.speed}, gear: {self.gear}')
```

---

# The *self* parameter

- The *self* parameter is required in the method definition, and it must come first before the other parameters
- It must be included in the definition because when Python calls this method later, the method call will automatically pass the *self* argument
- Every method call associated with an instance automatically passes *self*, which is a reference to the instance itself
- It gives the individual instance access to the attributes and methods in the class

---

# Using our Bicycle class

```python
#Create two different Bicycle objects
bike1 = Bicycle()
bike2 = Bicycle()

#invoke methods on those objects
bike1.change_cadence(50)
bike1.speed_up(10)
bike1.change_gear(2)
bike1.print_state() #prints: cadence: 50, speed: 10, gear: 2

bike2.change_cadence(50)
bike2.speed_up(10)
bike2.change_cadence(40)
bike2.speed_up(10)
bike2.change_gear(3)
bike2.print_state() #prints: cadence: 40, speed: 20, gear: 3
```

---

# Constructor methods: The __init__() Method

- In previous example, when we run the following line:

```python
bike1 = Bicycle()
```

- some magic happens and we get an object of the Bicycle class
- That magic is basically Python calling a *constructor* method
- A constructor method is a special method which is used for initializing the instance variables during object creation
- An object **cannot** be created if we don’t have a constructor in our program. This is why when we do not explicitly declare a constructor in our program, Python does it for us
- We have two types of constructors in Python:
  1. **default constructor** – this is the one, which we have seen in the above example. This constructor doesn’t accept any arguments
  2. **parameterized constructor** – constructor with parameters is known as parameterized constructor
- Let's add the default constructor explicitly to our Bicycle class:

---

# Bicycle class

```python
class Bicycle:

  cadence = 0
  speed = 0
  gear = 1

  def __init__(self):
    # no body, does nothing.

  def change_cadence(self, cadence):
    self.cadence = cadence

  def change_gear(self, gear):
    self.gear = gear

  def speed_up(self, increment):
    self.speed = self.speed + increment

  def apply_brakes(self, decrement):
    self.speed = self.speed - decrement

  def print_state(self):
    print(f'cadence: {self.cadence}, speed: {self.speed}, gear: {self.gear}')
```

---

# Parameterized constructor

- As every method, the constructor can have parameters
- Let's suppose we can create a Bicycle with some initial *gear*

```python
class Bicycle:

  cadence = 0
  speed = 0

  def __init__(self, gear):
    self.gear = gear

  def change_cadence(self, cadence):
    self.cadence = cadence

  def change_gear(self, gear):
    self.gear = gear

  def speed_up(self, increment):
    self.speed = self.speed + increment

  def apply_brakes(self, decrement):
    self.speed = self.speed - decrement

  def print_state(self):
    print(f'cadence: {self.cadence}, speed: {self.speed}, gear: {self.gear}')
```

---

# One last thing

- Now that we have an explicit constructor, we don't need to declare our fields outside it
- The following code also works:

```python
class Bicycle:

  def __init__(self, gear):
    self.gear = gear
    self.cadence = 0
    self.speed = 0

  def change_cadence(self, cadence):
    self.cadence = cadence

  def change_gear(self, gear):
    self.gear = gear

  def speed_up(self, increment):
    self.speed = self.speed + increment

  def apply_brakes(self, decrement):
    self.speed = self.speed - decrement

  def print_state(self):
    print(f'cadence: {self.cadence}, speed: {self.speed}, gear: {self.gear}')
```


