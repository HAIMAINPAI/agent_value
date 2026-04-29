# AI选品 + 利润测算 Agent

这是一个面向 Amazon 跨境电商场景的 FastAPI 项目，适合做毕业设计、作品集原型或后续继续扩展成运营工具。

## 功能
- 选品关键词分析
- 利润测算
- AI评分（规则引擎版，可替换为大模型）
- 推荐榜单
- SQLite 本地存储
- 示例数据初始化
- Swagger API 文档

## 技术栈
- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## 目录结构
```text
ai_product_agent/
├── app/
│   ├── api/routes/
│   ├── core/
│   ├── db/
│   ├── schemas/
│   └── services/
├── run.py
├── requirements.txt
└── README.md
```

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 初始化数据库并导入示例数据
```bash
python run.py --seed
```

### 3. 启动服务
```bash
python run.py
```

### 4. 打开文档
```text
http://127.0.0.1:8000/docs
```

## 接口说明

### 健康检查
`GET /health`

### 计算利润
`POST /analysis/profit`

### 生成选品评分
`POST /analysis/score`

### 推荐列表
`GET /analysis/recommendations`

### 产品管理
- `GET /products`
- `POST /products`
- `GET /products/{product_id}`
- `DELETE /products/{product_id}`

## 可扩展方向
- 接入 Keepa / Amazon SP-API
- 接入大模型做评论分析与竞品拆解
- 增加前端页面（uni-app / Vue）
- 增加定时任务抓取市场数据
- 增加导出 Excel 报表
