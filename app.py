from flask import Flask, request
import joblib
import logging
from datetime import datetime

# 【监控核心1】配置标准日志（替换掉所有 print）
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return "AI 预测服务运行中！路由：/predict?hours=时长"

# 【监控核心2】健康检查接口（供外部系统探活）
@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}, 200

@app.route('/predict')
def predict():
    # 🚨 你的踩坑史：曾把 request 拼成 reqest。
    hours_str = request.args.get('hours', '0')
    try:
        hours = float(hours_str)
        prediction = model.predict([[hours]])[0]
        final_score = min(round(prediction, 1), 100)
        
        # 记录业务日志（用于后续排查数据漂移）
        logging.info(f"预测成功 - 输入时长:{hours}, 输出分数:{final_score}")
        
        return f"你计划学习 {hours} 小时，预测分数为：{final_score} 分！"
    except Exception as e:
        logging.error(f"预测失败 - 输入:{hours_str}, 错误:{e}")
        return f"格式错误：{e}", 400

if __name__ == '__main__':
    # 🚨 你的踩坑史：漏掉英文冒号、拼错 __name__。
    app.run(host='0.0.0.0', port=5000)
