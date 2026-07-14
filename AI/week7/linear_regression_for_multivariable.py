import numpy as np
from sklearn.linear_model import LinearRegression
# X=np.array([
#      [2,90],
#     [3,80],
#     [5,95]
# ], dtype=float)
# W=np.array([
#      10,
#     0.5
# ], dtype=float)
# b=20
# predictions= X@W +b
# print(predictions)
x=np.array([-2,-1,0,1,2])
y=np.array([4,1,0,1,4])

X= np.column_stack((x,x**2))

print(X)
model=LinearRegression()
model.fit(X,y)
print(model.coef_)
print(model.intercept_)
print(model.predict(X))
