#!/usr/bin/env node
const { exec } = require('child_process');
const fs = require('fs');
const handler = require('serve-handler');
const http = require('http');
const open = require('open');
const ProgressBar = require('progress');
const cenas = [
    'cena-simples',
    'cena-primitivas',
    'cena-2-fontes-luz',
    'cena-arvore',
    'cena-empilhadas',
    'cena-whitted',
    'cena-cornell-box'
];
const progresso = new ProgressBar('Arquivos de teste: [:bar] :percent :etas', { total: cenas.length });

console.log('Iniciando execução dos testes do ray tracer...');

// TODO: baixa as imagens de objetivo

// pega a configuração: qual linguagem foi usada
const config = JSON.parse(fs.readFileSync('./autores.json'));
const linguagem = config.linguagem;

// executa o raytracer da linguagem usada para cada caso de teste
let promessasDeExecucao = [];
switch (linguagem) {
    case 'cpp':
        promessasDeExecucao = cenas.map(c => {
            return _ => new Promise((resolve, reject) => {
                const makeTarget = `run-${c.substr(c.indexOf('cena-') + 'cena-'.length)}`
                exec(`cd cpp/Makefile && make ${makeTarget}`, (err, stdout, stderr) => {
                    if (err) {
                        reject(err);
                        return;
                    }
                    progresso.tick();
                    resolve();
                });
            });
        });
        break;
    case 'java':
        promessasDeExecucao = cenas.map(c => {
            return _ => new Promise((resolve, reject) => {
                const cena = c + '.txt';
                exec(`chmod +x java/dist/raytracer.jar && java -jar java/dist/raytracer.jar ${cena}`, (err, stdout, stderr) => {
                    if (err) {
                        reject(err);
                        return;
                    }
                    progresso.tick();
                    resolve();
                });
            });
        });
        break;
    default:
        throw new Error(`A linguagem está incorreta no arquivo autores.json: ${linguagem}. Deveria ser cpp ou java`);
}

// executa as promessas em sequencialmente
// TODO: achar um jeito de executar promessas em sequência
promessasDeExecucao[0]()
    .then(_ => promessasDeExecucao[1]()
        .then(_ => promessasDeExecucao[2]()
            .then(_ => promessasDeExecucao[3]()
                .then(_ => promessasDeExecucao[4]()
                    .then(_ => promessasDeExecucao[5]()
                        .then(_ => promessasDeExecucao[6]()
                            .then(_ => {
                                // abre o navegador servindo index.html
                                const porta = 8085;
                                const servidor = http.createServer((request, response) => {
                                    return handler(request, response);
                                })

                                servidor.listen(porta, () => {
                                    console.log(`Servidor executando em http://localhost:${porta}`);
                                    open(`http://localhost:${porta}`);
                                });                            
                            })
                        )
                    )
                )
            )
        )
    );
            
