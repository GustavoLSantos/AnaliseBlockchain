import requests
import pandas as pd
import time
from datetime import datetime

def coletar_bitcoin(qtd=1000):
    print("⛏️  Iniciando coleta do Bitcoin...")
    url = "https://blockchain.info/latestblock"
    r = requests.get(url)
    bloco_atual = r.json().get("hash")
    dados = []

    for i in range(qtd):
        print(f"🔹 Bloco Bitcoin {i+1}/{qtd}")
        r = requests.get(f"https://blockchain.info/rawblock/{bloco_atual}")
        if r.status_code != 200:
            break
        b = r.json()
        dados.append({
            "blockchain": "bitcoin",
            "block_number": b["height"],
            "block_size": b["size"],
            "gas_used": None,
            "tx_count": b["n_tx"],
            "cpu_cost": None,
            "timestamp": datetime.utcfromtimestamp(b["time"])
        })
        bloco_atual = b.get("prev_block")
        time.sleep(1)
    print(f"✅ Bitcoin finalizado com {len(dados)} blocos.")
    return dados

def coletar_ethereum(qtd=1000):
    print("⛏️  Iniciando coleta do Ethereum...")
    api_key = "6ZPX6A3KV62MMFZ9R8CIDXUP64RK26TQ73"
    r = requests.get(f"https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey={api_key}")
    bloco_atual = int(r.json()["result"], 16)
    dados = []

    for i in range(qtd):
        print(f"🔹 Bloco Ethereum {i+1}/{qtd}")
        tag = hex(bloco_atual - i)
        url = f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={tag}&boolean=true&apikey={api_key}"
        r = requests.get(url)
        if r.status_code != 200:
            break
        b = r.json()["result"]
        dados.append({
            "blockchain": "ethereum",
            "block_number": int(b["number"], 16),
            "block_size": None,
            "gas_used": int(b["gasUsed"], 16),
            "tx_count": len(b["transactions"]),
            "cpu_cost": None,
            "timestamp": datetime.utcfromtimestamp(int(b["timestamp"], 16))
        })
        time.sleep(1)
    print(f"✅ Ethereum finalizado com {len(dados)} blocos.")
    return dados

def gerar_dataset_publicas():
    print("📊 Coletando dados públicos: Bitcoin e Ethereum...")
    btc = coletar_bitcoin()
    eth = coletar_ethereum()
    df = pd.DataFrame(btc + eth)
    df["tx_por_kb"] = df["tx_count"] / (df["block_size"] / 1024).replace({0: None})
    df["dia_semana"] = df["timestamp"].dt.day_name()
    df["timestamp"] = df["timestamp"].apply(lambda x: x.isoformat() if pd.notnull(x) else None)
    df.to_csv("dataset_blockchains_pub.csv", index=False)
    print("✅ Dados públicos salvos como 'dataset_blockchains_pub.csv'.")

if __name__ == "__main__":
    gerar_dataset_publicas()  # Bitcoin + Ethereum
