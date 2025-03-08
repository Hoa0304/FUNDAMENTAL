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

    def predict(self, test_point):
        # Tính khoảng cách Euclid từ điểm cần dự đoán đến tất cả điểm huấn luyện
        distances = np.sqrt(np.sum((self.training_data - test_point)**2, axis=1))

        # Sắp xếp các chỉ số theo khoảng cách tăng dần
        sorted_indices = np.argsort(distances)

        # Lấy nhãn của k điểm gần nhất
        k_nearest_labels = self.labels[sorted_indices][:self.k]

        # Lấy nhãn xuất hiện nhiều nhất
        most_common = Counter(k_nearest_labels).most_common(1)

        return most_common[0][0]

# 1. Tạo dữ liệu gồm 50 điểm có 2 đặc trưng
X = np.random.rand(50, 2)
# Gán nhãn: nếu tổng 2 đặc trưng > 1 thì nhãn 1, ngược lại nhãn 0
y = ((X[:, 0] + X[:, 1]) > (1 + np.random.uniform(low=-0.2, high=0.2, size=50))).astype(int)

X_new = np.array([[0.3, 0.8]])

# 3. Khởi tạo và huấn luyện mô hình với các giá trị k khác nhau
knn3 = KNN(k=3)
knn5 = KNN(k=5)
knn7 = KNN(k=7)

knn3.fit(X, y)
knn5.fit(X, y)
knn7.fit(X, y)

# 4. Tạo một figure và axis cho animation
fig, ax = plt.subplots(figsize=(8, 6))

# Vẽ dữ liệu huấn luyện: nhãn 0 -> đỏ, nhãn 1 -> xanh
colors = ['red' if label == 0 else 'blue' for label in y]
sc = ax.scatter(X[:, 0], X[:, 1], c=colors, label="Dữ liệu huấn luyện (0->red, 1->blue)")

# Vẽ điểm cần dự đoán
sc_new = ax.scatter(X_new[:, 0], X_new[:, 1], c='green', marker='x', s=200, label="Điểm cần dự đoán")

def animate(i):
    ax.clear()
    
    # Vẽ lại dữ liệu huấn luyện: nhãn 0 -> đỏ, nhãn 1 -> xanh
    ax.scatter(X[:, 0], X[:, 1], c=colors, label="Dữ liệu huấn luyện (0->red, 1->blue)")

    # Vẽ lại điểm cần dự đoán
    ax.scatter(X_new[:, 0], X_new[:, 1], c='green', marker='x', s=200, label="Điểm cần dự đoán")
    
    # Chọn giá trị k tương ứng với frame (i)
    k_values = [3, 5, 7]
    k = k_values[i]  # Lấy k = 3, 5, 7 tương ứng với các frame 0, 1, 2
    
    annotate_knn(k)

    ax.set_title(f"Mô phỏng thuật toán kNN với k = {k}")
    ax.set_xlabel("Đặc trưng 1")
    ax.set_ylabel("Đặc trưng 2")
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
    circle = plt.Circle((X_new[0, 0], X_new[0, 1]), radius, color='black',
                        fill=False, linestyle='--', linewidth=1.5)
    ax.add_artist(circle)

# 5. Tạo animation
ani = FuncAnimation(fig, animate, frames=3, interval=1000, repeat=False)

# Hiển thị animation
plt.show()

# Lưu animation dưới dạng GIF
ani.save("knn_animation.gif", writer='imagemagick')
