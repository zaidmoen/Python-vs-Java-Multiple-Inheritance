/** Demonstrates implementing multiple interfaces in Java. */
public class MultipleInterfacesDemo {
    interface Printable {
        String print();
    }

    interface Scannable {
        String scan();
    }

    static class MultiFunctionPrinter implements Printable, Scannable {
        @Override
        public String print() {
            return "printing document";
        }

        @Override
        public String scan() {
            return "scanning document";
        }
    }

    public static void main(String[] args) {
        MultiFunctionPrinter printer = new MultiFunctionPrinter();

        System.out.println(printer.print());
        System.out.println(printer.scan());
        System.out.println("Interfaces: " + MultiFunctionPrinter.class.getInterfaces().length);
    }
}

