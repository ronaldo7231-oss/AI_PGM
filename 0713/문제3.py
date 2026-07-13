# NumPy와 TensorFlow 라이브러리 불러오기
import numpy as np
import tensorflow as tf

# NumPy 배열 생성
array = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

# -------------------------
# 3.1 Tensor로 변환
# -------------------------

# NumPy 배열을 TensorFlow Tensor로 변환
tensor = tf.convert_to_tensor(array)

# Tensor 출력
print("Tensor")
print(tensor)

# -------------------------
# 3.2 shape 출력
# -------------------------

# Tensor의 크기(행과 열) 출력
print("\nShape :", tensor.shape)

# -------------------------
# 3.3 dtype 출력
# -------------------------

# Tensor의 데이터 타입 출력
print("Dtype :", tensor.dtype)

# -------------------------
# 3.4 모든 값에 10을 더한 결과 출력
# -------------------------

# Tensor의 모든 원소에 10 더하기
result = tensor + 10

# 결과 출력
print("\n10을 더한 결과")
print(result)