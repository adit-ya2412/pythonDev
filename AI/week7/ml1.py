import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
# students=pd.DataFrame({
#      "hours_studied":[1,2,3,4,5],
#     "attendance":[60,70,80,90,95],
#     "marks":[30,45,60,75,90]
# })


# X=students[["hours_studied","attendance"]]
# Y=students["marks"]

# print(X)
# print(Y)

###
# random guess
# ->
# make predictions
# ->
# calculate error(loss function)

# -> 
# adjust parameters
# -> repeat
# -> better predictions

###

students=pd.DataFrame({
    "hours_studied":[1,2,3,4,5,6,7,8],
    "marks":[30,40,50,60,70,80,90,100]
})
print(students)


X=students[["hours_studied"]]
Y=students["marks"]

print(X.shape)
print(Y)

X_train,X_test,y_train,y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print(X_train)
print("  ")
print(X_test)

model=LinearRegression()
model.fit(X_train,y_train)

print(model.coef_)

print(model.intercept_)

pediction=model.predict([[9]])
print(pediction)


y_pred=model.predict(X_test)
print(y_pred)


mse=mean_squared_error(
    y_test,
    y_pred
)
print(mse)
score=r2_score(y_test,y_pred)
print(score)