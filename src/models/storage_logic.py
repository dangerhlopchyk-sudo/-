import json
import os
from datetime import datetime

STORAGE_DIR = "storage"
SHLAH = os.path.join(STORAGE_DIR, "contacts.json")

def load_contacts():
    if os.path.exists(SHLAH):
        with open(SHLAH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_contact(name, phone):
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    data = load_contacts()
    data.append({"name": name,
                 "phone": phone,
                 "data_add":datetime.now().isoformat()
                 })
    with open(SHLAH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def delete_contact(index):
    data = load_contacts()
    data.pop(index)
    with open(SHLAH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def edit_contact(index, name, phone):
    data = load_contacts()
    staryy_chas = data[index].get("data_add", "")  # ← спочатку зберігаємо
    data[index] = {"name": name, "phone": phone, "data_add": staryy_chas}  # ← потім вставляємо
    with open(SHLAH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)