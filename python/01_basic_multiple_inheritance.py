"""A minimal example of multiple inheritance in Python."""


class Printable:
    def print_document(self) -> str:
        return "printing document"


class Scannable:
    def scan_document(self) -> str:
        return "scanning document"


class MultiFunctionPrinter(Printable, Scannable):
    """Inherits behavior from two independent parent classes."""


def main() -> None:
    printer = MultiFunctionPrinter()

    print(printer.print_document())
    print(printer.scan_document())
    print("MRO:", " -> ".join(cls.__name__ for cls in MultiFunctionPrinter.__mro__))


if __name__ == "__main__":
    main()

