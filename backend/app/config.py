"""全局配置。"""
from pathlib import Path

# backend/ 目录
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
DB_PATH = BASE_DIR / "ids.db"
UPLOAD_DIR = BASE_DIR / "uploads"

for _d in (DATA_DIR, MODEL_DIR, UPLOAD_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# 认证
SECRET_KEY = "industrial-ids-demo-secret-key"
TOKEN_EXPIRE_MINUTES = 60 * 24

# 默认管理员（首次启动时播种）
DEFAULT_ADMIN = {"username": "admin", "password": "admin123", "display_name": "系统管理员", "role": "admin"}

# 检测类别（与合成数据/训练脚本保持一致）
LABELS = [
    "BENIGN", "DDoS", "DoS Hulk", "DoS GoldenEye", "DoS Slowloris",
    "DoS Slowhttptest", "PortScan", "Bot", "Web Attack", "Heartbleed", "Patator",
]
