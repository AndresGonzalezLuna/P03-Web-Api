X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=0.33,
                                                    random_state=42)
model: SVC = SVC()
model.fit(X_train,y_train)

y_hat = model.predict(X_test)
print(y_hat)


with open("./model.pkl","wb") as file:
    pickle.dump(model, file)

