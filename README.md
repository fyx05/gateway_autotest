# 基于Pytest网关接口自动化测试项目
## 项目简介
针对模拟网关服务开展接口自动化回归测试，通过真实HTTP调用接口。覆盖正常业务、异常参数、边界值场景，YAML维护测试数据，pytest实现用例管理与日志输出。

### 技术栈
- Python3、pytest
- requests
- pyyaml

### 运行步骤
1. 安装依赖：
`pip install -r requirements.txt`

2. 终端A启动模拟网关后端服务：
`python mock_gateway.py`

3. 终端B执行自动化测试用例：
`pytest test_gateway.py -v -s`
