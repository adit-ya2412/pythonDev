import pandas as pd

students=pd.DataFrame({
     "hours_studied":[1,2,3,4,5],
    "attendance":[60,70,80,90,95],
    "marks":[30,45,60,75,90]
})


X=students[["hours_studied","attendance"]]
Y=students["marks"]

print(X)
print(Y)

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