"""The Diamond Problem and Python's deterministic MRO."""


class A:
    def describe(self) -> list[str]:
        return ["A"]


class B(A):
    def describe(self) -> list[str]:
        return ["B", *super().describe()]


class C(A):
    def describe(self) -> list[str]:
        return ["C", *super().describe()]


class D(B, C):
    def describe(self) -> list[str]:
        return ["D", *super().describe()]


def main() -> None:
    print("D's MRO:", " -> ".join(cls.__name__ for cls in D.__mro__))
    print("Call order:", " -> ".join(D().describe()))
    print("A appears once:", D().describe().count("A") == 1)


if __name__ == "__main__":
    main()

