# Deep comparison: Python and Java

## 1. Multiple inheritance

Multiple inheritance means that one type receives behavior from more than one parent type.

Python supports it directly:

```python
class Report(Printable, Exportable):
    pass
```

Java allows only one class in the `extends` clause:

```java
class Report extends Document {
}
```

Java can implement several interfaces:

```java
class Report extends Document implements Printable, Exportable {
}
```

An interface is primarily a contract. Modern Java interfaces may also contain default methods, but they do not turn Java into unrestricted multiple class inheritance.

## 2. The Diamond Problem

Consider this graph:

```text
       A
      / \
     B   C
      \ /
       D
```

Both `B` and `C` inherit from `A`, while `D` inherits from both `B` and `C`. If the parents provide the same operation, the language must answer:

1. Which implementation should run?
2. In what order should parent initialization happen?
3. Should `A` run once or twice?
4. Which inherited field represents shared state?

These questions become even more difficult when classes have constructors, mutable fields, side effects, and partially cooperative parent methods.

## 3. Python's MRO

Python calculates a Method Resolution Order for every class. You can inspect it with:

```python
print(MyClass.__mro__)
```

For the common diamond:

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

the order is:

```text
D → B → C → A → object
```

When Python evaluates `instance.method()`, it searches that sequence from left to right. The first matching implementation wins.

## 4. C3 Linearization

Python uses C3 Linearization to construct a consistent MRO. At a high level, the algorithm combines the local parent order with the parents' own MROs while preserving three properties:

- child classes appear before their parents;
- the declared order of direct parents is respected;
- every class appears only once.

This is why changing `class D(B, C)` to `class D(C, B)` can change which method is selected.

## 5. What `super()` really means in Python

In simple single inheritance, developers often think of `super()` as “my parent.” In multiple inheritance, the more accurate description is:

> Continue method lookup after the current class in the MRO.

For cooperative inheritance, each implementation should perform its work and then call `super()`:

```python
class LoggingMixin:
    def process(self):
        log_request()
        super().process()
```

If one class directly calls `Parent.method(self)` instead, it can skip another class in the MRO and break the cooperative chain.

## 6. Java's rule

Java intentionally separates class inheritance from interface implementation:

```java
class Child extends Parent implements First, Second {
}
```

There may be only one class after `extends`, but there may be multiple interfaces after `implements`.

This gives Java a simpler rule for object state: the object has one class-inheritance path. Interfaces add contracts and, in some cases, reusable default behavior without introducing multiple class layouts.

## 7. Java default-method conflicts

If two interfaces provide the same default method, the implementing class must override it:

```java
interface First {
    default void show() { }
}

interface Second {
    default void show() { }
}

class Child implements First, Second {
    @Override
    public void show() {
        First.super.show();
    }
}
```

Java makes the decision explicit. The class may select one interface implementation, combine both behaviors, or provide an entirely new implementation.

## 8. Why Java chose this design

The restriction is a trade-off, not a technical limitation. Java's design emphasizes:

- one clear superclass for inherited state;
- predictable constructor and initialization rules;
- explicit conflict handling;
- easier reasoning for tooling and large codebases;
- compatibility with a statically typed class model.

Python favors flexibility and runtime introspection. That flexibility is powerful, but it requires developers to understand MRO and to write cooperative classes carefully.

## 9. Multiple inheritance versus composition

Inheritance models an “is-a” relationship. Composition models a “has-a” relationship.

Use multiple inheritance or mixins when behavior is small, orthogonal, and intentionally cooperative. Use composition when the components have independent responsibilities or state:

```python
class Copier:
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner
```

Composition reduces hidden lookup rules and makes dependencies visible in the constructor.

## 10. Interview-ready answer

> Python supports multiple class inheritance and resolves method lookup using MRO, which is built with C3 Linearization. In a diamond hierarchy, `super()` follows the next class in the MRO, so a cooperative chain can execute each class once. Java does not support multiple class inheritance because it would introduce ambiguity around methods, state, constructors, and initialization. Instead, Java allows multiple interfaces and requires the implementing class to explicitly resolve conflicting default methods.

