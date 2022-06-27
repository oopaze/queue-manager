# queue-manager

O queue é uma implementação de um software usado para o gerenciamento de filas de algum estabelecimento que distribua senhas. Ele conta com um servidor gerenciador e 3 tipos de clients:
- __TA:__ Client responsável por chamar os próximos tickets. Geralmente roda na máquina do atendente.
- __TS:__ Client responsável por gerar os tickets. Geralmente se encontra em uma máquina de auto atendimento.
- __TV:__ Client responsável por chamar os tickets. Geralmente fica em telas no estabelecimento mostrando a próxima senha a ser atendida.

Todos esses clientes contam com uma interface gráfica simples feita com `tkinter`, um módulo do `python`. O servidor foi totalmente desenvolvido em `python` e utiliza `sockets` para se comunicar com todos os clients. Toda a comunicação é feita por meio de um protocolo chamado TCP [saiba mais](https://www.tecmundo.com.br/o-que-e/780-o-que-e-tcp-ip-.htm).

### Dependencias

- [python >= 3.8](https://www.python.org/downloads/)

### Como Rodar o Server

Para rodar o servidor será necessário ter o `python3.7+` instalado e a porta `50000` disponível. Uma vez que este esteja instalado, na pasta do projeto rode o comando a seguir:

```sh
python runserver.py
```

e logo seu server iniciará.

### Como rodar os Client's

Para rodar algum Client, também será necessário ter o `python3.7+`  instalado. Inicialmente, roda o servidor. Uma vez que o servidor esteja `on`, abra um novo terminal e rode o comando a seguir:

```sh
# para rodar um client do tipo TS
python runclient_ts.py

# para rodar um client do tipo TA
python runclient_ta.py

# para rodar um client do tipo TV
python runclient_tv.py
```

Logo um janela abrirá com um `Client`. Note que toda vez que você precisar rodar um novo `client`, terá que abrir um novo terminal se quiser manter o anterior rodando.

<p float="left">
  <img src="./client_start_state.png" width="50%" />
  <img src="./client_running_state.png" width="45%" />
</p>
