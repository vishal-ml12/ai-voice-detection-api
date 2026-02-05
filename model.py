from sklearn.ensemble import RandomForestClassifier
import numpy as np

model = RandomForestClassifier(n_estimators=100, random_state=42)

X = np.random.rand(100, 17)
y = np.random.randint(0, 2, 100)

model.fit(X, y)
