import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "similarity": [0.9, 0.2, 0.75, 0.3],
    "label": [1, 0, 1, 0]
})

X = data[["similarity"]]
y = data["label"]

model = LogisticRegression()
model.fit(X, y)

pred = model.predict([[score]])

print("Final Selection:", "Selected" if pred[0] == 1 else "Rejected")