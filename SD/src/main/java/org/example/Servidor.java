package org.example;

import java.io.*;
import java.net.*;
import org.json.JSONObject;

public class Servidor {
    public static void main(String[] args) {
        int port = 12345;

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Servidor esperando por conexões...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Cliente conectado: " + clientSocket.getInetAddress());

            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

            for (int i = 0; i < 5; i++) {
                String userInput = in.readLine();

                JSONObject jsonObject = new JSONObject(userInput);

                String nome = jsonObject.getString("Nome");
                String cpf = jsonObject.getString("CPF");
                int idade = jsonObject.getInt("idade");
                String mensagem = jsonObject.getString("mensagem");

                System.out.println();
                switch (i) {
                    case 0:
                        System.out.println("Formato CSV:");
                        String formattedMessageCSV = "{\"Nome\":\"" + nome + "\", \"CPF\":\"" + cpf + "\", \"idade\":" + idade + ", \"mensagem\":\"" + mensagem + "\"}";
                        System.out.println(formattedMessageCSV +"\n");
                        break;
                    case 1:
                        System.out.println("Formato JSON:");
                        String orderedJsonString = "{"
                                + "\"Nome\":\"" + nome + "\", "
                                + "\"CPF\":\"" + cpf + "\", "
                                + "\"idade\":" + idade + ", "
                                + "\"mensagem\":\"" + mensagem + "\""
                                + "}";
                        System.out.println(orderedJsonString +"\n");

                        break;
                    case 2:
                        System.out.println("Formato XML:");
                        String xmlMessage =
                                "<dados>\n" +
                                        "    <Nome>" + nome + "</Nome>\n" +
                                        "    <CPF>" + cpf + "</CPF>\n" +
                                        "    <idade>" + idade + "</idade>\n" +
                                        "    <mensagem>" + mensagem + "</mensagem>\n" +
                                        "</dados>";
                        System.out.println(xmlMessage + "\n");
                        break;
                    case 3:
                        System.out.println("Formato YAML:");
                        String yamlMessage =
                                "Nome: " + nome + "\n" +
                                        "CPF: '" + cpf + "'\n" +
                                        "idade: " + idade + "\n" +
                                        "mensagem: \"" + mensagem + "\"";
                        System.out.println(yamlMessage + "\n");
                        break;
                    case 4:
                        System.out.println("Formato TOML:");
                        String tomlMessage = "Nome = \"" + nome + "\"\n" +
                                "CPF = \"" + cpf + "\"\n" +
                                "idade = " + idade + "\n" +
                                "mensagem = \"" + mensagem + "\"";
                        System.out.println(tomlMessage +"\n");
                        break;
                }
            }

            clientSocket.close();
            serverSocket.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
