import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_random_neko():
    
    try:
        
        api_response = requests.get("https://nekos.best/api/v2/neko")
        api_response.raise_for_status()
        data = api_response.json()
        image_url = data['results'][0]['url']

        
        img_response = requests.get(image_url, stream=True)
        img_response.raise_for_status()

        
        pil_image = Image.open(BytesIO(img_response.content))
        pil_image = pil_image.resize((400, 400), Image.Resampling.LANCZOS)

        return ImageTk.PhotoImage(pil_image)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")
        return None
    except KeyError:
        messagebox.showerror("Ошибка", "Неожиданный формат ответа от сервера.")
        return None
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка обработки: {e}")
        return None

def update_image():
    
    new_img = get_random_neko()
    if new_img:
        label.config(image=new_img)
        label.image = new_img

root = tk.Tk()
root.title("Генератор случайных аниме")
root.geometry("500x500")

label = tk.Label(root)
label.pack(pady=10, expand=True)

button = tk.Button(root, text="Меняй!", command=update_image, font=("Arial", 14))
button.pack(pady=10)

update_image()

root.mainloop()