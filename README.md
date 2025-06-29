# Dataset de Blocos Bitcoin e Ethereum para Análise de Eficiência Computacional

Este repositório contém um *dataset* público e padronizado com 2000 blocos extraídos das blockchains **Bitcoin** e **Ethereum**, além do código-fonte e scripts utilizados para a coleta, limpeza, visualização e documentação dos dados.

---
## 📊 Descrição dos Dados

Cada linha do *dataset* representa um bloco. O arquivo final `dataset_blockchains_final.csv` contém 2000 blocos (1000 de cada rede) com as seguintes colunas:

| Coluna          | Tipo       | Descrição |
|-----------------|------------|-----------|
| `blockchain`    | string     | Rede de origem do bloco (`bitcoin` ou `ethereum`) |
| `block_number`  | inteiro    | Altura do bloco na blockchain |
| `block_size`    | float      | Tamanho do bloco em bytes (apenas para Bitcoin) |
| `gas_used`      | float      | Unidades de gas consumidas no bloco (apenas para Ethereum) |
| `tx_count`      | inteiro    | Número total de transações no bloco |
| `timestamp`     | datetime   | Data e hora da mineração do bloco |
| `tx_por_kb`     | float      | Densidade de transações por kilobyte |
| `dia_semana`    | string     | Dia da semana correspondente ao timestamp |

---

## ⚙️ Scripts de Coleta

A coleta foi feita utilizando **Python** com bibliotecas como `requests`, `pandas` e `datetime`. Os scrapers acessam APIs públicas das respectivas blockchains:

- **Bitcoin:** Coleta via [Blockstream API](https://blockstream.info/api/)
- **Ethereum:** Coleta via [Etherscan API](https://etherscan.io/apis) (chave de API necessária)

Cada script salva os blocos extraídos em CSV, que posteriormente foram unidos e tratados no notebook principal.

---

## 📈 Notebook de Análise

O notebook `limpeza_e_visualizacoes.ipynb` documenta o processo completo de:
- Leitura e inspeção dos dados
- Conversão de tipos e tratamento de *missing values*
- Recalculo da métrica `tx_por_kb`
- Geração de visualizações como histogramas, dispersões e gráficos de distribuição

As visualizações geradas abordam:
- Distribuição de transações por bloco
- Ocupação de espaço em bytes
- Eficiência transacional por kilobyte
- Atividade por dia da semana

---

## 📎 Reutilização e Expansão

Este *dataset* pode ser utilizado para:
- Estudos sobre escalabilidade de blockchains públicas
- Treinamento de modelos de machine learning para detecção de anomalias ou previsão de carga
- Visualizações exploratórias e aplicações acadêmicas

Contribuições são bem-vindas! Sinta-se livre para abrir *issues* ou *pull requests* para sugerir melhorias ou estender os dados coletados.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
