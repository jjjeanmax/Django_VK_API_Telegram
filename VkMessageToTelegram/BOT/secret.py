from pathlib import Path
import json

# Получение данных из конфиг файла configs.json

secrets_path = Path(__file__).resolve(strict=True).parent / 'configs.json'

with open(secrets_path) as f:
    secrets = json.loads(f.read())


def get_secret(setting, section=None, secrets=secrets):
    if section:
        return secrets[section][setting]
    return secrets[setting]
