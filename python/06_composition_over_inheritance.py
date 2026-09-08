"""Composition as a simpler alternative to multiple inheritance."""


class Printer:
    def print_document(self, document: str) -> str:
        return f"printed: {document}"


class Scanner:
    def scan_document(self, document: str) -> str:
        return f"scanned: {document}"


class Copier:
    def __init__(self, printer: Printer, scanner: Scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def copy(self, document: str) -> tuple[str, str]:
        scanned = self.scanner.scan_document(document)
        printed = self.printer.print_document(scanned)
        return scanned, printed


def main() -> None:
    copier = Copier(printer=Printer(), scanner=Scanner())
    scanned, printed = copier.copy("report.pdf")

    print(scanned)
    print(printed)
    print("Copier MRO:", " -> ".join(cls.__name__ for cls in Copier.__mro__))


if __name__ == "__main__":
    main()

