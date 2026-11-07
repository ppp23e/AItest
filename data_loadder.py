import json

# 模拟原始数据（工业界可能是数据库或数据湖）
raw_data = {
    "samples": [
        {"hours": 1, "score": 20}, {"hours": 2, "score": 40},
        {"hours": 3, "score": 60}, {"hours": 4, "score": 80},
        {"hours": 5, "score": 100}
    ]
}

def prepare_data():
    # 1. 数据落盘（模拟数据采集）
    with open("raw_data.json", "w") as f:
        json.dump(raw_data, f)
    
    # 2. 数据清洗与读取
    with open("raw_data.json", "r") as f:
        data = json.load(f)
    
    # 3. 转换为模型需要的二维数组
    X = [[item["hours"]] for item in data["samples"]]
    y = [item["score"] for item in data["samples"]]
    return X, y

if __name__ == "__main__":
    X, y = prepare_data()
    print(f"数据清洗完成，样本数：{len(X)}")
