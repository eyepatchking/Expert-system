import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


oyna = tk.Tk()
oyna.title('Tibbiyot Ma\'lumotlarini Tasniflash')
oyna.geometry('500x600')
file_label = tk.Label(oyna, text="Fayl yuklanmadi")
file_label.pack(pady=10)
aniqlik_label = tk.Label(oyna, text="Model aniqligi: Noma'lum")
aniqlik_label.pack(pady=10)

def upload_data():
    global dataframe
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        dataframe = pd.read_csv(file_path)
        file_label.config(text=f"Yuklangan fayl: {file_path.split('/')[-1]}")
        messagebox.showinfo("Ma'lumot", "Fayl muvaffaqiyatli yuklandi!")
    else:
        messagebox.showerror("Xatolik", "Faylni yuklashda xatolik yuz berdi.")


def train_model():
    global best_model, sts
    X = dataframe.drop('Target', axis=1)
    y = dataframe['Target']
    sts = StandardScaler()
    X = sts.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    param_grid = {'C': [0.01, 0.1, 1, 10, 100]}
    model = LogisticRegression()
    gridsearch = GridSearchCV(model, param_grid, cv=5)
    gridsearch.fit(X_train, y_train)
    best_model = gridsearch.best_estimator_
    y_pred = best_model.predict(X_test)
    aniqlik = accuracy_score(y_test, y_pred)
    aniqlik_label.config(text=f"Model aniqligi: {aniqlik:.2f}")
    messagebox.showinfo("Model aniqligi", f"Model aniqligi: {aniqlik:.2f}")


def expert_system():
    def submit():
        bemordata = [float(entry.get()) for entry in entries]
        tashxis = make_prediction(bemordata)
        result_label.config(text=f"Yangi bemorning tashhisi: {tashxis}")

    tashxis_oyna = tk.Toplevel(oyna)
    tashxis_oyna.title("Bemor ma'lumotlarini kiritish")
    tashxis_oyna.geometry('400x500')  # Tashxis qo'yish oynasining hajmini belgilash
    labels = dataframe.drop('Target', axis=1).columns
    entries = []
    
    for label in labels:
        tk.Label(tashxis_oyna, text=label).pack(pady=5)
        entry = tk.Entry(tashxis_oyna)
        entry.pack(pady=5)
        entries.append(entry)

    submit_button = tk.Button(tashxis_oyna, text="Tashhis qo'yish", command=submit)
    submit_button.pack(pady=10)
    result_label = tk.Label(tashxis_oyna, text="")
    result_label.pack(pady=10)

def make_prediction(patient_data):
    bemor_dataframe = pd.DataFrame([patient_data], columns=dataframe.drop('Target', axis=1).columns)
    bemor_dataframe = sts.transform(bemor_dataframe)
    result = best_model.predict(bemor_dataframe)
    return "Kasal" if result[0] == 1 else "Sog'lom"

load_button = tk.Button(oyna, text="Ma'lumotlarni yuklash", command=upload_data)
load_button.pack(pady=10)

train_button = tk.Button(oyna, text="Modelni o'qitish", command=train_model)
train_button.pack(pady=10)

diagnosis_button = tk.Button(oyna, text="Tashhis qo'yish", command=expert_system)
diagnosis_button.pack(pady=10)

oyna.mainloop()
