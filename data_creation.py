import numpy as np
import pandas as pd

np.random.seed(42)

def generate_portfolio_data():
    dates = pd.date_range(start="2024-01-01", end="2026-10-01", freq="ME")

    asset_classes = ["Osakkeet", "Korkosijoitukset", "Kiinteistöt", "Johdannaiset"]
    portfolio_data = []

    for date in dates:
        for ac in asset_classes:
            # Generoidaan näennäissatunnaisia mutta realistisia tuottoja ja arvoja
            value = np.random.uniform(500000, 2000000)
            benchmark = value * (1 + np.random.uniform(-0.02, 0.04))
            ret = np.random.uniform(-0.05, 0.08)

            portfolio_data.append(
                {
                    "Päivämäärä": date,
                    "Omaisuusluokka": ac,
                    "Salkun Arvo (€)": round(value, 2),
                    "Vertailuindeksi (€)": round(benchmark, 2),
                    "Kuukausituotto (%)": round(ret * 100, 2),
                }
            )

    df = pd.DataFrame(portfolio_data)
    df.to_csv("sijoitusdata.csv", index=False)
    print("Data luotu tiedostoon sijoitusdata.csv!")

def main():
    generate_portfolio_data()
