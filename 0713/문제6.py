import tensorflow as tf
# 데이터 불러오기
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# 데이터 전처리
x_train = x_train / 255.0
x_test = x_test / 255.0
# 모델 생성
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
# 컴파일
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
# 학습
model.fit(x_train, y_train, epochs=5)
# 평가
model.evaluate(x_test, y_test)
# 예측
prediction = model.predict(x_test)