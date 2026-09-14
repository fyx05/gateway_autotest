
from flask import Flask, jsonify, request

app = Flask(__name__)

device_state = {"status": "online", "version": "1.0.0", "config": {}}

@app.route('/api/device/status', methods=['GET'])
def get_status():
    return jsonify(device_state)

@app.route('/api/device/reboot', methods=['POST'])
def reboot():
    return jsonify({"code": 0, "message": "reboot command received"}), 200

@app.route('/api/device/config', methods=['POST'])
def set_config():
    data = request.json
    if not data or "network" not in data:
        return jsonify({"code": 400, "message": "missing network config"}), 400
    device_state["config"] = data
    return jsonify({"code": 0, "message": "config updated"}), 200

# 模拟设备心跳（网关常见功能）
@app.route('/api/device/heartbeat', methods=['POST'])
def heartbeat():
    # 实际网关会返回时间戳
    return jsonify({"code": 0, "timestamp": "2026-09-14 12:00:00"}), 200

# 模拟生产测试：批量设备状态检查
import concurrent.futures
@app.route('/api/device/batch_status', methods=['GET'])
def batch_status():
    # 模拟并发查询10个设备
    def get_one(i):
        return {"device_id": i, "status": "online"}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(get_one, range(1, 11)))
    return jsonify({"code": 0, "data": results}), 200

if __name__ == '__main__':
    app.run(port=5000)

