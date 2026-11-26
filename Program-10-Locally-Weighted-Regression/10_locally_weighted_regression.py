# Program 10: Non-Parametric Locally Weighted Regression using LOWESS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

data = pd.read_csv("house_price.csv")

X = data["Area"]
Y = data["Price"]

result = lowess(endog=Y, exog=X, frac=0.3)

plt.scatter(X, Y, label="Actual Data")
plt.plot(result[:, 0], result[:, 1], color="red", label="LWR Curve")

plt.title("Locally Weighted Regression")
plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()
