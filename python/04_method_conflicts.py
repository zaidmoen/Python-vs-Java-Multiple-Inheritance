"""How Python resolves a method conflict using the MRO."""


class A:
    def speak(self) -> str:
        return "A"


class B(A):
    def speak(self) -> str:
        return "B"


class C(A):
    def speak(self) -> str:
        return "C"


class D(B, C):
    pass


def main() -> None:
    instance = D()

    print("D.speak():", instance.speak())
    print("Selected class:", D.__mro__[1].__name__)
    print("Explicit B call:", B.speak(instance))
    print("Explicit C call:", C.speak(instance))


if __name__ == "__main__":
    main()

