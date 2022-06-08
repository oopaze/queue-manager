package ClientTS;

import ClientTS.implementations.Client;

public class RunClient {
    public static void run() {
        Client client = new Client();
        client.connect("127.0.0.1", 50000);

        String[] args = {"true"}; 

        String receivedMessage = client.send("next_ticket", args);

        System.out.println(receivedMessage);
    }
}
