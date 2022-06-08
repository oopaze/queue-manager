package ClientTS.implementations;

import java.net.Socket;
import java.net.UnknownHostException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.BufferedReader;

import ClientTS.managers.MessageManager;

public class Client {
    private Socket socket;
    private BufferedReader input;
    private PrintWriter output;

    public void connect(String host, int port) {
        try {
            this.socket = new Socket(host, port);
            this.input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.output = new PrintWriter(socket.getOutputStream(), true);
        } catch (UnknownHostException e) {
            System.out.println("Host não encontrado");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String send(String message) {
        String encodedMessage = MessageManager.encode(message);
        this.output.write(encodedMessage);
        this.output.flush();

        return receive();
    }

    public String send(String message, String[] args) {
        String encodedMessage = MessageManager.encode(message, args);
        this.output.write(encodedMessage);
        this.output.flush();

        // return receive();
        return "";
    }

    public String receive() {
        try {
            String receivedMessage = new String(this.input.readLine());
            return MessageManager.decode(receivedMessage);
        } catch (IOException e) {
           return "Error";
        }
    }
}
