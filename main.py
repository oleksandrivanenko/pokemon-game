import random
import pandas as pd

df = pd.read_csv("pokemon_data.csv")

def selectCard():  # Card selection function
    return df.iloc[random.randint(0, 799)]

print("******** POKEMON GAME ********")

print("\nHUMAN")
dfHuman = selectCard()
print(dfHuman)
dfComputer = selectCard()
characteric = input("\nPlease enter a characteristic on which the pokemons will complete: ")
valueHuman = dfHuman[characteric]
valueComputer = dfComputer[characteric]

print("\nCOMPUTER")
print(dfComputer)

if valueHuman > valueComputer:
    print("\nYou win!")
elif valueHuman < valueComputer:
    print("\nYou lose!")
else:
    print("\nDraw!")