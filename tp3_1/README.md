# Instruções para testes do ray tracer

Primeiramente, o arquivo `autores.json` deve ser preenchido. Ele contém
as seguintes informações:

```json
{
    "autores": [
        "Adamastor Carmargo",
        "Custódio Fonseca"
    ],
    "linguagem": "java"
}
```

...sendo que você deve preencher os nomes dos autores e definir
o nome da linguagem que foi usada (`java` ou `cpp`).

Para executar os testes é necessário ter o [Node.js][node] instalado e,
então, digitar na pasta raiz o comando:

```bash
npm install
```

Em seguida, o script `corrigir.js` deve ser tornado executável e,
então, deve ser executado:

```bash
chmod +x corrigir.js
./corrigir.js
```

Após a execução, o navegador será aberto mostrando o resultado de todos
os testes.


[node]: https://nodejs.org/en/