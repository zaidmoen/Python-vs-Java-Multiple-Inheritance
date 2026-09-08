/** Resolve a default-method conflict explicitly in the implementing class. */
public class DefaultMethodConflictDemo {
    interface Printable {
        default String show() {
            return "Printable implementation";
        }
    }

    interface Scannable {
        default String show() {
            return "Scannable implementation";
        }
    }

    static class Document implements Printable, Scannable {
        @Override
        public String show() {
            // Java requires this decision because both interfaces define show().
            return Printable.super.show();
        }
    }

    public static void main(String[] args) {
        Document document = new Document();
        System.out.println(document.show());
        System.out.println("Conflict resolved explicitly by Document");
    }
}

