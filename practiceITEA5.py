
import time
import threading
import shutil
import requests
import os

start = time.time()
def download(n, url):
    print(str(n) + "tok" ("+url+"))
    dirname, filename = os.path.split(url)
    r = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
    print(str(n) + "tok end download")

    urls = [https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0005/47.png,
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0006/18.png,
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0001/67.png,
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0005/34.png,
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0006/81.png,
            https://www.winnerauto.ua/i/carstock/auto_models/image_menu/0000/88.png,
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0006/19.png
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0005/55.png
            https://www.winnerauto.ua/i/carstock/auto_colors_models_relation/image/0005/55.png]

for n ,url in enumerate(urls):
    threading.Thread(target=down, args = [n, url]).start()

fin = time.time()
t = fin - start
print(f"Time used is: {t}")
