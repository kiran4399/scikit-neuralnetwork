# Based on scikit-learn examples.
#   - File: auto_examples/ensemble/plot_adaboost_regression.py
#   - Author: Noel Dawe <noel.dawe@gmail.com>

import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

from sknn.nn import SimpleNeuralRegressor


# Create the dataset
rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])

# Fit regression model
clf_0 = SimpleNeuralRegressor(layers=[("Linear",)])
clf_1 = DecisionTreeRegressor(max_depth=4)

clf_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=300, random_state=rng)

clf_0.fit(X, y, n_iter=100)
clf_1.fit(X, y)
clf_2.fit(X, y)

# Predict
y_0 = clf_0.predict(X)
y_1 = clf_1.predict(X)
y_2 = clf_2.predict(X)

# Plot the results
plt.figure()
plt.scatter(X, y, c="k", label="training samples")
plt.plot(X, y_0, c="b", label="linear network", linewidth=2)
plt.plot(X, y_1, c="g", label="decision tree", linewidth=1)
plt.plot(X, y_2, c="r", label="tree ensemble", linewidth=1)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Machine Learning Comparison")
plt.legend()
plt.show()