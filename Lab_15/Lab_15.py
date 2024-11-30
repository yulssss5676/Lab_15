import pandas as pd

# Створюємо словник
cars = {
    "Toyota_Camry": {"price": 12000, "age": 7},
    "Honda_Civic": {"price": 9000, "age": 5},
    "Ford_Focus": {"price": 8000, "age": 8},
    "BMW_3Series": {"price": 15000, "age": 10},
    "Mercedes_CClass": {"price": 20000, "age": 6},
    "Nissan_Altima": {"price": 11000, "age": 7},
    "Mazda_6": {"price": 10000, "age": 4},
    "Volkswagen_Passat": {"price": 9500, "age": 9},
    "Chevrolet_Malibu": {"price": 8700, "age": 3},
    "Hyundai_Elantra": {"price": 9200, "age": 6}
}

# Перетворення словника на датафрейм
df = pd.DataFrame(cars).T.reset_index()
df.columns = ['Model', 'Price', 'Age']

# Вивід датафрейму
print("Початковий датафрейм:")
print(df)

# Групування за віком автомобілів (Age) та агрегація
grouped_df = df.groupby('Age').agg(
    total_price=('Price', 'sum'),  # Сума цін автомобілів у групі
    average_price=('Price', 'mean'),  # Середня ціна автомобілів у групі
    car_count=('Model', 'count')  # Кількість автомобілів у групі
)

# Вивід результатів
print("\nАгрегація та групування:")
print(grouped_df)

# Візуалізація результатів
grouped_df['average_price'].plot(
    kind='bar', color='skyblue', title='Середня ціна автомобілів за віком',
    xlabel='Вік автомобіля (роки)', ylabel='Середня ціна ($)', figsize=(8, 5)
)
plt.grid(True)
plt.tight_layout()
plt.show()

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    3.	import pandas as pd
import matplotlib.pyplot as plt

# Завантажуємо дані з файлу
file_path = 'comptagevelo20162.csv'
df = pd.read_csv(file_path)

# Перетворюємо стовпець 'Date' у формат datetime для зручності аналізу
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Видаляємо зайві стовпці (наприклад, 'Unnamed: 1', який не несе корисної інформації)
df = df.drop(columns=['Unnamed: 1'])

# Фільтруємо дані для перших трьох днів січня 2016 року
filtered_dates = ['2016-01-01', '2016-01-02', '2016-01-03']
filtered_df = df[df['Date'].dt.strftime('%Y-%m-%d').isin(filtered_dates)]

# Перейменовуємо деякі стовпці для зручності
columns_mapping = {
    'Berri1': 'Berri 1',
    'Brébeuf': 'Brébeuf (дані недоступні)',
    'CSC (Côte Sainte-Catherine)': 'Côte Sainte-Catherine',
    'Maisonneuve_2': 'Maisonneuve 2',
    'Parc': 'Parc',
    'PierDup': 'Pierre-Dupuy',
    'Rachel / Papineau': 'Rachel/Papineau'
}
filtered_df = filtered_df.rename(columns=columns_mapping)

# Виводимо таблицю для перевірки
print(filtered_df)

# Аналіз: підраховуємо загальну кількість велосипедистів по місяцях на Berri 1
df['Month'] = df['Date'].dt.month
monthly_usage = df.groupby('Month')['Berri1'].sum()

# Знаходимо місяць з найбільшою кількістю велосипедистів
best_month = monthly_usage.idxmax()
max_cyclists = monthly_usage.max()

print(f"Найпопулярніший місяць: {best_month}, з кількістю велосипедистів: {max_cyclists}")

# Побудова графіка
plt.figure(figsize=(10, 6))
monthly_usage.plot(kind='bar', color='skyblue')
plt.title('Кількість велосипедистів на Berri 1 по місяцях (2016)')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=0)
plt.grid(True)

# Відображаємо графік
plt.tight_layout()
plt.show()

