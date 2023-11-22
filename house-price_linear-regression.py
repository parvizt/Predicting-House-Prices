import pandas as pd
import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

# خواندن داده‌ها از فایل
df = pd.read_csv('housebroker.csv')

# تبدیل مقادیر بله و خیر به ۱ و ۰
df['Elevator'] = df['Elevator'].apply(lambda x: 1 if x == 'TRUE' else 0)
df['Parking'] = df['Parking'].apply(lambda x: 1 if x == 'TRUE' else 0)
df['Warehouse'] = df['Warehouse'].apply(lambda x: 1 if x == 'TRUE' else 0)

# جایگزینی مقادیر NaN با میانگین ستون
imputer = SimpleImputer(strategy='mean')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

def predict_price():
    # استخراج ویژگی‌ها از ورودی‌های کاربر
    elevator = elevator_var.get()
    floor = int(floor_var.get())
    area = int(area_var.get())
    parking = parking_var.get()
    room = int(room_var.get())
    warehouse = warehouse_var.get()
    year_of_construction = int(year_var.get())

    # تبدیل مقادیر بله و خیر به ۱ و ۰
    elevator = 1 if elevator == 'TRUE' else 0
    parking = 1 if parking == 'TRUE' else 0
    warehouse = 1 if warehouse == 'TRUE' else 0

    # ایجاد یک داده‌فریم جدید بر اساس ورودی‌های کاربر
    input_data = pd.DataFrame({
        'Elevator': [elevator],
        'Floor': [floor],
        'Area': [area],
        'Parking': [parking],
        'Room': [room],
        'Warehouse': [warehouse],
        'YearOfConstruction': [year_of_construction]
    })

    # تقسیم داده به داده آموزشی و تست
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Price', axis=1), df['Price'], test_size=0.2, random_state=42)

    # استفاده از یک مدل خطی
    model = LinearRegression()
    model.fit(X_train, y_train)

    # پیش‌بینی قیمت
    predicted_price = model.predict(input_data)

    # نمایش نتیجه به کاربر
    result_label.config(text=f"پیش‌بینی قیمت: {predicted_price[0]:,.0f} تومان")

    # محاسبه خطا
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    error_percentage = (mae / df['Price'].mean()) * 100
    error_label.config(text=f"میانگین خطا: {error_percentage:.2f}%")


# ساخت رابط کاربری
root = tk.Tk()
root.title("Regression model:House Price Estimation")

# ایجاد ویدجت‌ها و لیبل‌ها
elevator_label = ttk.Label(root, text="آسانسور:")
elevator_var = ttk.Combobox(root, values=['TRUE', 'FALSE'])
elevator_var.set('TRUE')

floor_label = ttk.Label(root, text="طبقه:")
floor_var = ttk.Combobox(root, values=['-1', '0', '1', '2', '3', '4', '5',
                                              '6', '7', '8', '9', '10',
                                              '11', '12', '13', '14', '15',
                                              '16', '`17', '18', '19', '20',
                                               '21', '22', '23', '24', '25',
                                               '26', '27', '28', '29', '30'])

floor_var.set('1')

area_label = ttk.Label(root, text="مساحت:")
area_var = ttk.Combobox(root, values=[str(i) for i in range(3, 355)])
area_var.set('100')

parking_label = ttk.Label(root, text="پارکینگ:")
parking_var = ttk.Combobox(root, values=['TRUE', 'FALSE'])
parking_var.set('TRUE')

room_label = ttk.Label(root, text="تعداد اتاق:")
room_var = ttk.Combobox(root, values=['1', '2', '3', '4'])
room_var.set('2')

warehouse_label = ttk.Label(root, text="انبار:")
warehouse_var = ttk.Combobox(root, values=['TRUE', 'FALSE'])
warehouse_var.set('TRUE')

year_label = ttk.Label(root, text="سال ساخت:")
year_var = ttk.Combobox(root, values=['1375','1376','1377','1378','1379','1380','1381',
                                      '1382','1383','1384','1385','1386','1387','1388',
                                       '1389','1390','1391','1392','1393','1394','1395',
                                      '1396', '1397', '1398', '1399', '1400', '1401'])

year_var.set('1398')

predict_button = ttk.Button(root, text="پیش‌بینی قیمت", command=predict_price)

result_label = ttk.Label(root, text="پیش‌بینی قیمت: -")
error_label = ttk.Label(root, text="میانگین خطا: -")

# نمایش ویدجت‌ها در یک grid
elevator_label.grid(row=0, column=0, padx=10, pady=5)
elevator_var.grid(row=0, column=1, padx=10, pady=5)

floor_label.grid(row=1, column=0, padx=10, pady=5)
floor_var.grid(row=1, column=1, padx=10, pady=5)

area_label.grid(row=2, column=0, padx=10, pady=5)
area_var.grid(row=2, column=1, padx=10, pady=5)

parking_label.grid(row=3, column=0, padx=10, pady=5)
parking_var.grid(row=3, column=1, padx=10, pady=5)

room_label.grid(row=4, column=0, padx=10, pady=5)
room_var.grid(row=4, column=1, padx=10, pady=5)

warehouse_label.grid(row=5, column=0, padx=10, pady=5)
warehouse_var.grid(row=5, column=1, padx=10, pady=5)

year_label.grid(row=6, column=0, padx=10, pady=5)
year_var.grid(row=6, column=1, padx=10, pady=5)

predict_button.grid(row=7, column=0, columnspan=2, pady=10)

result_label.grid(row=8, column=0, columnspan=2, pady=5)
error_label.grid(row=9, column=0, columnspan=2, pady=5)


# اجرای mainloop
root.mainloop()
