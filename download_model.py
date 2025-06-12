import os
import requests

# رابط الموديل من GitHub (خام مباشر)
url = "https://github.com/amira900928/gaze-api/raw/main/code/exps/2025-05-23-14-56/ckpts/model_best.pth.tar"
save_path = "model/model_best.pth.tar"

# اتأكد إن الفولدر موجود
os.makedirs("model", exist_ok=True)

# نزّل الملف لو مش موجود
if not os.path.exists(save_path):
    print("Downloading model...")
    response = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("Model already exists.")
