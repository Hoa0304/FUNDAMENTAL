import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

df = pd.read_csv("dataset.csv")

if 'Ngày' in df.columns:
    df['Ngày'] = pd.to_datetime(df['Ngày'], errors='coerce')
    df['year'] = df['Ngày'].dt.year
    df['month'] = df['Ngày'].dt.month
    df['day'] = df['Ngày'].dt.day
    df = df.drop(columns=['Ngày'])

# 48 m²-> 48
def convert_to_numeric(value):
    try:
        return float(value.split()[0].replace(',', ''))
    except:
        return np.nan

df['Diện tích'] = df['Diện tích'].apply(convert_to_numeric)
df['Dài'] = df['Dài'].apply(convert_to_numeric)
df['Rộng'] = df['Rộng'].apply(convert_to_numeric)
df['Giá/m2'] = df['Giá/m2'].apply(convert_to_numeric)

df = df.select_dtypes(include=[np.number])

# thay thế NaN bằng giá trị trung bình của cột
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df))

X = df_imputed.iloc[:, :-1].values
y = df_imputed.iloc[:, -1].values   # Cột cuối cùng là giá trị mục tiêu

regressor = RandomForestRegressor(n_estimators=10)

regressor.fit(X, y)

# Dự đoán giá trị cho dữ liệu huấn luyện
y_pred = regressor.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, color='blue')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--')
plt.title('So sánh Dự đoán và Giá trị Thực tế')
plt.xlabel('Giá trị thực tế (Giá/m²)')
plt.ylabel('Giá trị dự đoán (Giá/m²)')
plt.show()
