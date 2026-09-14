import pytest
import requests
import yaml
import logging
from config import BASE_URL

# 读取 YAML 测试数据
with open("test_data.yaml", "r", encoding="utf-8") as f:
    test_data = yaml.safe_load(f)

def test_get_status():
    logging.info("开始测试获取设备状态")
    r = requests.get(f"{BASE_URL}/status")
    assert r.status_code == 200
    assert r.json()["status"] == "online"
    # 性能断言：响应时间小于0.5秒
    assert r.elapsed.total_seconds() < 0.5

def test_reboot():
    logging.info("开始测试重启指令")
    r = requests.post(f"{BASE_URL}/reboot")
    assert r.status_code == 200
    assert r.json()["code"] == 0

# 数据驱动 + 失败重试（比如网络抖动重试2次）
@pytest.mark.parametrize("case", test_data["config_test_cases"])
def test_set_config(case):
    logging.info(f"执行用例：{case['name']}，参数：{case['payload']}")
    r = requests.post(f"{BASE_URL}/config", json=case["payload"])
    assert r.status_code == (200 if case["expected_code"] == 0 else 400)
    assert r.json()["code"] == case["expected_code"]

def test_heartbeat():
    r = requests.post(f"{BASE_URL}/heartbeat")
    assert r.status_code == 200
    assert r.json()["code"] == 0

def test_batch_status():
    r = requests.get(f"{BASE_URL}/batch_status")
    assert r.status_code == 200
    assert len(r.json()["data"]) == 10