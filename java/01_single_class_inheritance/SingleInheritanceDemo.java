/** Demonstrates Java's single class inheritance rule. */
public class SingleInheritanceDemo {
    static class Device {
        String powerOn() {
            return "device is on";
        }
    }

    static class SmartDevice extends Device {
        String connect() {
            return "device connected";
        }
    }

    public static void main(String[] args) {
        SmartDevice device = new SmartDevice();

        System.out.println(device.powerOn());
        System.out.println(device.connect());
        System.out.println("Superclass: " + SmartDevice.class.getSuperclass().getSimpleName());
    }
}

