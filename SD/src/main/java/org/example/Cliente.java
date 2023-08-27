package org.example;

import java.io.*;
import java.net.*;
import org.json.JSONObject;

public class Cliente {
    public static void main(String[] args) {
        String serverAddress = "127.0.0.1";
        int serverPort = 12345;

        try {
            Socket socket = new Socket(serverAddress, serverPort);

            OutputStream outputStream = socket.getOutputStream();
            PrintWriter out = new PrintWriter(outputStream, true);

            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            for (int i = 0; i < 5; i++) {
                System.out.println("Digite os dados (Nome, CPF, idade, mensagem) na seguinte forma:");

                String inputData = reader.readLine();
                String[] dataParts = inputData.split(",");

                if (dataParts.length != 4) {
                    System.out.println("Formato incorreto. Certifique-se de inserir Nome, CPF, idade e mensagem separados por vírgula.");
                    continue;
                }

                String nome = dataParts[0].trim();
                String cpf = dataParts[1].trim();
                int idade = 0;
                String mensagem = "";

                try {
                    idade = Integer.parseInt(dataParts[2].trim());
                } catch (NumberFormatException e) {
                    System.out.println("Idade deve ser um número inteiro.");
                    continue;
                }

                mensagem = dataParts[3].trim();

                JSONObject jsonMessage = new JSONObject();
                jsonMessage.put("Nome", nome);
                jsonMessage.put("CPF", cpf);
                jsonMessage.put("idade", idade);
                jsonMessage.put("mensagem", mensagem);

                out.println(jsonMessage.toString());
            }

            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
