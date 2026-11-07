FROM python:3.11-slim
WORKDIR /app
# 把依赖拷进去
COPY requirements.txt .
# 安装依赖（加清华源防超时）
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# 把代码全拷进去
COPY . .
# 启动
CMD ["python", "app.py"]
