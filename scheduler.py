from apscheduler.schedulers.blocking import BlockingScheduler
from zakupki_parser import get_contracts_by_inn
from bot import send_contracts
from config import INNS
import json
import os

STORAGE_FILE = 'storage.json'

def load_storage():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, 'r') as f:
        return json.load(f)

def save_storage(data):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f)

def check_updates():
    storage = load_storage()
    for inn in INNS:
        contracts = get_contracts_by_inn(inn)
        new_contracts = []
        for contract in contracts:
            if contract['link'] not in storage.get(inn, []):
                new_contracts.append(contract)
                storage.setdefault(inn, []).append(contract['link'])
        if new_contracts:
            send_contracts(new_contracts)
    save_storage(storage)

scheduler = BlockingScheduler()
scheduler.add_job(check_updates, 'interval', hours=3)

print("🔁 Бот запущен. Проверка контрактов каждые 3 часа.")
check_updates()
scheduler.start()
