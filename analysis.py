from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).parent
OUT=HERE/"outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(HERE/"campaigns.csv").drop_duplicates().dropna()
df["CTR_pct"]=df["Clicks"]/df["Impressions"]*100
df["ConversionRate_pct"]=df["Conversions"]/df["Clicks"]*100
df["CostPerConversion"]=df["Spend"]/df["Conversions"].replace(0, pd.NA)
print("\\nCampaign metrics:\\n",df[["CampaignID","Channel","CTR_pct","ConversionRate_pct","CostPerConversion"]].round(2).to_string(index=False))
print("\\nAverage metrics by channel:\\n",df.groupby("Channel")[["CTR_pct","ConversionRate_pct","CostPerConversion"]].mean().round(2))
df.to_csv(OUT/"campaign_metrics.csv",index=False)
df.groupby("Channel")["Conversions"].sum().plot(kind="bar", title="Conversions by Channel")
plt.ylabel("Conversions"); plt.tight_layout(); plt.savefig(OUT/"conversions_by_channel.png"); plt.close()
