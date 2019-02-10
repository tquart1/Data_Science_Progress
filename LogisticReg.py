from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()
#[Height, weight, shoe size]


X = [[185, 110, 34], [125, 70, 44], [195, 88, 52], [125, 68, 64], [165, 58, 48], [145, 48, 42],
     [155, 45, 33], [165, 89, 44], [129, 65, 42], [185, 92, 34]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

LR = LR.fit(X, Y)

prediction = LR.predict([190, 70, 43])

print (prediction)


