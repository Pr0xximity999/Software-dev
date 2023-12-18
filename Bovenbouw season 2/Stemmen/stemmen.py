import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read data out of the csv
df = pd.read_csv("results.csv")

#Define a plot
fig, axes = plt.subplots(nrows=2, ncols=2)

#Vote Count Per Province
votesPerParty = df["ChosenParty"].value_counts()
votesPerParty.plot(kind='bar', title="Stemmen Per Partij", xlabel="", ax=axes[0, 0], figsize=(25,15))

#Vote Count Per Party
voteCountPerProvince = df.groupby(["Province"]).count()["ChosenParty"]
voteCountPerProvince.plot(kind='bar', title="Stemmen Per Provincie", ax=axes[1, 0])

#Vote Count Per BSN
voteCountPerBSN = df.groupby(["BSN"]).count()["ChosenParty"]
voteCountPerBSN.plot(kind='bar', title="Stemmen Per BSN", ax=axes[1, 1])

#Vote parties Per Province
partyVotesPerProvince = df.groupby(['Province', 'ChosenParty']).size().reset_index(name='Votes')
partyVotesPerProvincePivot = partyVotesPerProvince.pivot(index='Province', columns='ChosenParty', values='Votes').fillna(0)
partyVotesPerProvincePivot.plot(kind='bar', title="Stemmen Per Partij Per Provincie", stacked=True, ax=axes[0, 1])

#Save The Plot
plt.savefig("Results.png", dpi=100)

#Show The Plot
plt.show()