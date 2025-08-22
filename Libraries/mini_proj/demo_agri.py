import yeilds

import prices

print(yeilds.mean_yeilds([125,345,785]))

print(prices.total_cost(120,754))

import pandas as pd

df = pd.DataFrame({"crops": ["cotton", "maize", "legumes"], "yeild": [2300,3400,2800]})

print(df[df["yeild"]>2500])