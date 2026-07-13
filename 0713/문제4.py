import numpy as np
import tensorflow as tf
# 학습 데이터
x_train = np.array([1, 2, 3, 4, 5], dtype=np.float32).reshape(-1, 1)
y_train = np.array([3, 6, 9, 12, 15], dtype=np.float32)
# 모델 생성
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(1)
])
# 모델 컴파일
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss="mse"
)
# 모델 학습
model.fit(x_train, y_train, epochs=300, verbose=0)
# 테스트 데이터
x_test = np.array([6, 7, 8], dtype=np.float32).reshape(-1, 1)
# 예측
prediction = model.predict(x_test)
print(prediction)

loss = model.evaluate(x_train, y_train, verbose=0)
print(loss)

print(model.layers[0].get_weights())