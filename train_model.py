from sklearn.linear_model import LinearRegression
import joblib
from data_loader import prepare_data

# 获取清洗后的数据
X, y = prepare_data()

# 训练模型
model = LinearRegression()
model.fit(X, y)

# 将训练好的模型持久化（离线训练，在线推理）
joblib.dump(model, "model.pkl") 
print("AI 训练完成，已保存 model.pkl！")
