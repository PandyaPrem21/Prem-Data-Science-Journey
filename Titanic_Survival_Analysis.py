import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
'Survived': [0,1,1,1,0,0,1,0,1,0],
'Pclass':[3,1,3,1,3,3,1,3,2,3],
'Gender':['Male','Female','Female','Female','Male','Male','Male','Male','Female','Male'],
'Age':[22,38,26,35,35,27,54,7,27,.18],
'fare':[7.25,71.28,7.92,53.1,8.05,8.45,51.86,21.07,11.13,7.85]
}
df = pd.DataFrame(data)
plt.style.use("dark_background")
plt.figure(figsize=(10,8))
sns.scatterplot(
    data=df,
    x="Age",
    y="fare",
    hue="Survived",
    style="Gender",
    palette=["red","lime"],# red=died,lime= survived
    edgecolor="white",
    #glowing white border
    s=180,
    linewidth=1.2
)
plt.title("Titanic Survival: Glowing Graph",fontsize=16,color='white')
plt.xlabel("Age",fontsize=12)
plt.ylabel("Fare",fontsize=12)
plt.grid(True,linestyle='--',alpha=0.5)
plt.legend(title="Survived",loc="upper right")
plt.show()





