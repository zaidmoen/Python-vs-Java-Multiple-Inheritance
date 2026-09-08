/**
 * Java avoids the class-based Diamond Problem by using interfaces and an
 * explicit implementation at the point of conflict.
 */
public class DiamondResolutionDemo {
    interface A {
        default String path() {
            return "A";
        }
    }

    interface B extends A {
        @Override
        default String path() {
            return "B -> " + A.super.path();
        }
    }

    interface C extends A {
        @Override
        default String path() {
            return "C -> " + A.super.path();
        }
    }

    static class D implements B, C {
        @Override
        public String path() {
            // B and C both override path(), so D must choose explicitly.
            return "D -> " + B.super.path();
        }
    }

    public static void main(String[] args) {
        System.out.println(new D().path());
        System.out.println("Java requires D to resolve the conflict");
    }
}

