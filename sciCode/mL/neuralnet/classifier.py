import pandas as pd
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.model_selection import train_test_split


####################################################

# C l a s s i f i e r

####################################################

#
cols=['Book1',	'Book2','Book3',
      'Book4', 'Book5','Book6','Book7']

pool = pd.read_csv("~/Desktop/databit3b.csv",
                   names=cols, header=None)

print(pool.head())


#####################################################


prayer = pd.get_dummies(pool.Book1, prefix='Book1')
visits = pd.get_dummies(pool.Book2, prefix='Book2')
teaching = pd.get_dummies(pool.Book3, prefix='Book3')
fireside = pd.get_dummies(pool.Book4, prefix='Book4')
animator = pd.get_dummies(pool.Book5, prefix='Book5')
troop = pd.get_dummies(pool.Book6, prefix='Book6')
tutors = pd.get_dummies(pool.Book7, prefix='Book7')


######################################################


X = pd.concat([prayer,visits,teaching,
               fireside,animator,troop], axis=1)

y = tutors.values


X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.20, random_state=42)


###############################################################


input_layer = Input(shape=(X.shape[1]))
dense_layer_1 = Dense(15, activation='relu')(input_layer)
dense_layer_2 = Dense(10, activation='relu')(dense_layer_1)
output = Dense(y.shape[1], activation='softmax')(dense_layer_2)
# #
model = Model(inputs=input_layer, outputs=output)
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['acc'])

print(model.summary())


################################################################


history = model.fit(X_train, y_train, batch_size=8,
                    epochs=99, verbose=1, validation_split=0.2)


score = model.evaluate(X_test, y_test, verbose=1)

print("Test Score:", score[0])
print("Test Accuracy:", score[1])


################################################################