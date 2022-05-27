import pickle
def get_linear_prediction(dt,options_to_choose2):
    x = dt[options_to_choose2]
    y = dt['price']

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    from sklearn.linear_model import LinearRegression
    lin_r = LinearRegression()
    lin_r.fit(x_train, y_train)
    predictions = lin_r.predict(x_test)

    import pickle
    pickle.dump(lin_r, open('./model.sav','wb'))

