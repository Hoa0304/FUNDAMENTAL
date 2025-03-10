import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.animation import FuncAnimation

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, training_data, labels):
        self.training_data = training_data
        self.labels = labels

X = np.random.rand(50, 2)
y = ((X[:, 0] + X[:, 1]) > (1 + np.random.uniform(low=-0.2, high=0.2, size=50))).astype(int)

X_new = np.array([[0.3, 0.8]])

# Khởi tạo mô hình với các giá trị k khác nhau
knn3 = KNN(k=3)
knn5 = KNN(k=5)
knn7 = KNN(k=7)

# Tạo một figure và axis cho animation
fig, ax = plt.subplots(figsize=(8, 6))

# Vẽ dữ liệu huấn luyện: nhãn 0 -> đỏ, nhãn 1 -> xanh
colors = ['red' if label == 0 else 'blue' for label in y]
sc = ax.scatter(X[:, 0], X[:, 1], c=colors, label="Training data (0->red, 1->blue)")

# Vẽ điểm cần dự đoán
sc_new = ax.scatter(X_new[:, 0], X_new[:, 1], c='green', marker='x', s=200, label="Points to predict")

def animate(i):
    ax.clear()
    
    ax.scatter(X[:, 0], X[:, 1], c=colors, label="Training data (0->red, 1->blue)")

    ax.scatter(X_new[:, 0], X_new[:, 1], c='green', marker='x', s=200, label="Points to predict")
    
    k_values = [3, 5, 7]
    k = k_values[i]
    
    annotate_knn(k)

    ax.set_title(f"Simulate kNN algorithm with k = {k}")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.legend()
    ax.grid(True)

def annotate_knn(k):
    # Tính khoảng cách từ điểm cần dự đoán đến tất cả các điểm huấn luyện
    distances = np.sqrt(np.sum((X - X_new)**2, axis=1))
    sorted_indices = np.argsort(distances)
    # Lấy k điểm gần nhất
    nearest_indices = sorted_indices[:k]
    # Vẽ đường nối từ điểm cần dự đoán đến từng điểm trong k điểm gần nhất
    for i, idx in enumerate(nearest_indices):
        x_neighbor = X[idx]
        ax.plot([X_new[0, 0], x_neighbor[0]], [X_new[0, 1], x_neighbor[1]], 
                color='black', linestyle='--', linewidth=1)
    
    # Vẽ vòng tròn bao quanh k điểm: bán kính bằng khoảng cách xa nhất trong k điểm
    radius = distances[sorted_indices[k - 1]]
    circle = plt.Circle((X_new[0, 0], X_new[0, 1]), radius, color='purple',
                        fill=False, linestyle='--', linewidth=1.5)
    ax.add_artist(circle)

ani = FuncAnimation(fig, animate, frames=3, interval=1000, repeat=False)

plt.show()

ani.save("knn_animation.gif", writer='imagemagick')
