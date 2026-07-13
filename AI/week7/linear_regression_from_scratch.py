import numpy as np

import matplotlib.pyplot as plt

#step 1 make a array for learning
x= np.array([1,2,3,4],dtype=float)

y=np.array([30,40,50,60],dtype=float)

print(x)
print(y)

# step 2 make intial guess aka m=0, c=0

m=0.0
c=0.0

#learning rate aka how big of a step i should take

learning_rate=0.01

losses = []

for epoch in range(500):

    predictions=m*x +c
    print(predictions)

    # now comes the error 
    error=y-predictions
    print(error)

    # now the loss function aka mse

    loss= np.mean(error**2)
    print(loss)
    losses.append(loss)
    #now dm, dc, and m 

    dm= -2 * np.mean(x*error)

    #dc is just differentiating Loss function ie (y-(mx+c))^2
    # which makes dc as = 2(y-y^)

    dc= -2* np.mean(error)

    #now we update the values

    m=m-learning_rate *dm
    c=c-learning_rate *dc

    print(
    f"Epoch {epoch}: "
    f"Loss={loss:.2f}, "
    f"m={m:.4f}, "
    f"c={c:.4f}"
    )

plt.plot(losses)

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("Gradient Descent")

plt.show()