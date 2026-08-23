class Car:
    def __init__(self, color, brand, model, year, fuel_consumption, tank_volume, mileage=0):
        if fuel_consumption <= 0 or tank_volume <= 0 or mileage < 0:
            raise ValueError("Параметры не могут быть отрицательными")
        self.brand = brand  # Марка
        self.model = model  # Модель
        self.year = year  # Год выпуска
        self.fuel_consumption = fuel_consumption  # Расход топлива
        self.tank_volume = tank_volume  # Объём бака
        self.reserve = tank_volume  # Резерв топлива
        self.mileage = mileage  # Пробег
        self.engine_on = False  # Двигатель запущен
        self.color = color

    """Запуск двигателя"""
    def start_engine(self) -> str:
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return 'Двигатель запущен'
        return 'Двигатель уже был запущен'

    """Остановка двигателя"""
    def stop_engine(self) -> str:
        if self.engine_on:
            self.engine_on = False
            return 'Двигатель остановлен'
        return 'Двигатель уже был остановлен'

    """Езда автомобиля"""
    def drive(self, distance: int) -> str:
        if not self.engine_on:
            return 'Двигатель не запущен'
        if self.reserve / self.fuel_consumption * 100 < distance:
            return 'Малый запас топлива'
        self.mileage += distance
        self.reserve -= distance / 100 * self.fuel_consumption
        return (f'Проехали: {distance} км., '
                f'остаток топлива: {self.reserve:.2f} л.')

    """Запас хода автомобиля"""
    def get_range_km(self) -> str:
        range_km = self.reserve / self.fuel_consumption * 100
        return f'Запас хода составляет: {range_km:.2f} km'

    """Заправка автомобиля"""
    def refuel(self, liters=None) -> str:
        if liters is None:
            added = self.tank_volume - self.reserve
            self.reserve = self.tank_volume
            return f'Бак заправлен до полного: добавлено {added:.2f} л., теперь в баке {self.reserve:.2f} л.'
        else:
            if liters <= 0:
                return f'Нельзя залить {liters} л. (количество должно быть положительным)'
            old_reserve = self.reserve
            self.reserve = min(self.reserve + liters, self.tank_volume)
            added = self.reserve - old_reserve
            return f'Заправлено {added:.2f} л., теперь в баке {self.reserve:.2f} л.'

    """Пробег автомобиля"""
    def get_mileage(self) -> str:
        return f'Пробег автомобиля: {self.mileage} км.'

    """Остаток топлвиа в баке автомобиля"""
    def get_reserve(self) -> str:
        return f'Остаток топлива в баке: {self.reserve} л.'

    """Расход топлива автомобиля"""
    def get_fuel_consumption(self):
        return self.fuel_consumption

    """Для пользователя. Дружелюбное, читаемое описание."""
    def __str__(self) -> str:
        return (f"Марка автомобиля: {self.brand},\n"
                f"Цвет: {self.color},\n"
                f"Пробег: {self.mileage} км.,\n"
                f"Объем бака: {self.tank_volume} л.,\n"
                f"Расход: {self.fuel_consumption} л.,\n"
                f"Год выпуска: {self.year} г.")

    """Для разработчика. Техническое представление, по которому можно воссоздать объект."""
    def __repr__(self) -> str:
        return (f"Car(color='{self.color}', brand='{self.brand}', "
                f"model='{self.model}', year={self.year}, "
                f"fuel_consumption={self.fuel_consumption}, "
                f"tank_volume={self.tank_volume}, mileage={self.mileage})")


"""Создадим экземпляр класса 'Car' для теста"""
car_1 = Car('черный', 'Mercedes', 'S-class', 1997, 10, 60,)

""""" Тесты работы программы"""
print(car_1.drive(100))
print(car_1.get_range_km())
print(car_1.get_reserve())
print(car_1.get_mileage())
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.get_mileage())
print(car_1.drive(90))
print(car_1.get_mileage())
print(car_1.drive(100))
print(car_1.stop_engine())
print(car_1.refuel(30))
print(car_1.get_reserve())
print(car_1.start_engine())
print(car_1.get_range_km())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(50))
print(car_1.drive(100))
print(car_1.stop_engine())