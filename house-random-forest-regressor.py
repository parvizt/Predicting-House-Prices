import pandas as pd
import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

# Read data from the file
df = pd.read_csv('housebroker.csv')

# Convert yes/no values to 1 and 0
df['Elevator'] = df['Elevator'].apply(lambda x: 1 if x == 'TRUE' else 0)
df['Parking'] = df['Parking'].apply(lambda x: 1 if x == 'TRUE' else 0)
df['Warehouse'] = df['Warehouse'].apply(lambda x: 1 if x == 'TRUE' else 0)

# Replace NaN values with column mean
imputer = SimpleImputer(strategy='mean')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

def predict_price():
    # Extract features from user inputs
    elevator = elevator_var.get()
    floor = int(floor_var.get())
    area = int(area_var.get())
    parking = parking_var.get()
    room = int(room_var.get())
    warehouse = warehouse_var.get()
    year_of_construction = int(year_var.get())

    # Convert yes/no values to 1 and 0
    elevator = 1 if elevator == 'TRUE' else 0
    parking = 1 if parking == 'TRUE' else 0
    warehouse = 1 if warehouse == 'TRUE' else 0

    # Create a new DataFrame based on user inputs
    input_data = pd.DataFrame({
        'Elevator': [elevator],
        'Floor': [floor],
        'Area': [area],
        'Parking': [parking],
        'Room': [room],
        'Warehouse': [warehouse],
        'YearOfConstruction': [year_of_construction]
    })

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Price', axis=1), df['Price'], test_size=0.2, random_state=42)

    # Use a Random Forest model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Predict the price
    predicted_price = model.predict(input_data)

    # Display the result to the user
    result_label.config(text=f"Predicted Price: {predicted_price[0]:,.0f} Toman")

    # Calculate the error
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    error_percentage = (mae / df['Price'].mean()) * 100
    error_label.config(text=f"Mean Absolute Error: {error_percentage:.2f}%")

# Create a user interface
root = tk.Tk()
root.title("Random Forest Regressor Model: House Price Estimation")

# Create widgets and labels
elevator_label = ttk.Label(root, text="Elevator:")
elevator_var = ttk.Combobox(root, values=['TRUE', 'FALSE'])
elevator_var.set('TRUE')

floor_label = ttk.Label(root, text="Floor:")
floor_var = ttk.Combobox(root, values=['-1', '0', '1', '2', '3', '4', '5',
                                              '6', '7', '8', '9', '10',
                                              '11', '12', '13', '14', '15',
                                              '16', '`17', '18', '19', '20',
                                               '21', '22', '23', '24', '25',
                                               '26', '27', '28', '29', '30'])
floor_var.set('0')

area_label = ttk.Label(root, text="Area:")
area_var = ttk.Combobox(root, values=[str(i) for i in range(3, 355)])
area_var.set('100')

parking_label = ttk.Label(root, text="Parking:")
parking_var = ttk.Combobox(root, values=['TRUE', 'FALSE'])
parking_var.set('TRUE')

room_label = ttk.Label(root, text="Number of Rooms:")
room_var = ttk.Combobox(root, values=['1', '2', '3', '4'])
room_var.set('2')

warehouse_label = ttk.Label(root, text="Warehouse:")
warehouse_var = ttk.Combobox(root, values=['TRUE', 'FALSE'])
warehouse_var.set('TRUE')

year_label = ttk.Label(root, text="Year of Construction:")
year_var = ttk.Combobox(root, values=['1375','1376','1377','1378','1379','1380','1381',
                                      '1382','1383','1384','1385','1386','1387','1388',
                                       '1389','1390','1391','1392','1393','1394','1395',
                                      '1396', '1397', '1398', '1399', '1400', '1401'])
year_var.set('1375')

predict_button = ttk.Button(root, text="Predict Price", command=predict_price)

result_label = ttk.Label(root, text="Predicted Price: -")
error_label = ttk.Label(root, text="Mean Absolute Error: -")

# Display widgets in a grid
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

# Run mainloop
root.mainloop()
