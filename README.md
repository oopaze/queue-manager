# queue-manager

Gerenciador de filas e senhas de atendimento

<p float="left">
  <img src="./client_start_state.png" width="50%" /> 
  <img src="./client_running_state.png" width="45%" />
</p>



#### Como Rodar o Server

Para rodar o servidor será necessário ter o python instalado e a porta `50000` disponível. Uma vez que este esteja instalado, na pasta do projeto rode o comando a seguir:
```sh
python runserver.py
```

e logo seu server iniciará.

#### Como rodar os Client's

Para rodar o TSClient, também será necessário ter o python instalado. Inicialmente, roda o servidor. Uma vez que o servidor esteja `on`, abra um novo terminal e rode o comando a seguir:
```sh
# para rodar um client do tipo TS
python runclient_ts.py

# para rodar um client do tipo TA
python runclient_ta.py

# para rodar um client do tipo TV
python runclient_tv.py
```

Logo um janela abrirá com um `Client` do estilo `TS`. Note que toda vez que você precisar rodar um novo `client`, terá que abrir um novo terminal se quiser manter o anterior rodando.
