public class Client {
    public static void main(String[] args) {
        Image image = new ProxyImage("test.jpg");
        // Image is not loaded from disk until display() is called
        image.display();
        // Image is already loaded, so display() is fast
        image.display();
    }
}
