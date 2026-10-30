
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import joblib
import pytest
import requests

# Example hockey data
games = pd.DataFrame({
    "team": ["Toronto", "Montreal", "Toronto", "Montreal"],
    "goals_for": [4, 2, 3, 1],
    "goals_against": [2, 3, 1, 4],
})

games["win"] = (
    games["goals_for"] > games["goals_against"]
)

print("HockeyLab setup successful!")
print()
print("Sample data:")
print(games)
print()
print("Win rate by team:")
print(games.groupby("team")["win"].mean())
print()
print("scikit-learn version:", sklearn.__version__)
