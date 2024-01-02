import json
import os
import pandas as pd

class DatasetManager:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
        self.data = pd.DataFrame()

    def save_prompt(self, content, role, version):
        versioned_filename = f"{self.dataset_path}/prompt_{role}_v{version}.json"
        with open(versioned_filename, "w", encoding='utf-8') as file:
            json.dump({"role": role, "content": content}, file, ensure_ascii=False)

    def load_dataset(self):
        for filename in os.listdir(self.dataset_path):
            if filename.endswith('.json'):
                file_path = os.path.join(self.dataset_path, filename)
                if os.path.getsize(file_path) > 0:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            # استفاده از pd.concat به جای append برای اضافه کردن داده‌ها به DataFrame
                            self.data = pd.concat([self.data, pd.DataFrame([data])], ignore_index=True)
                        except json.JSONDecodeError:
                            print(f"Error decoding JSON from file {filename}")
                else:
                    print(f"Warning: The file {filename} is empty and will be skipped.")
