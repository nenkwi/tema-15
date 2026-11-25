from typing import Generic, TypeVar

T = TypeVar("T", int, float, str)
T1 = TypeVar("T1", int, float)
T2 = TypeVar("T2", int, float)



class Building:
    def __init__(self, address: str, floors: int, area: float) -> None:
        if not address.strip():
            raise ValueError("Адреса будинку не може бути порожньою.")
        if floors <= 0:
            raise ValueError("Кількість поверхів має бути більшою за 0.")
        if area <= 0:
            raise ValueError("Площа має бути більшою за 0.")
        self.address = address.strip()
        self.floors = floors
        self.area = area

    def get_info(self) -> str:
        return (
            f"[Будинок] Адреса: {self.address}, "
            f"Поверхів: {self.floors}, Площа: {self.area:.2f} м²"
        )


class AcademicBuilding(Building):
    def __init__(
        self, address: str, floors: int, area: float, lecture_halls: int, faculty: str
    ) -> None:
        super().__init__(address, floors, area)
        if lecture_halls < 0:
            raise ValueError("Кількість аудиторій не може бути від'ємною.")
        if not faculty.strip():
            raise ValueError("Назва факультету/установи не може бути порожньою.")
        self.lecture_halls = lecture_halls
        self.faculty = faculty.strip()

    def get_info(self) -> str:
        return (
            f"[Навчальний корпус] Адреса: {self.address}, "
            f"Поверхів: {self.floors}, Площа: {self.area:.2f} м², "
            f"Аудиторій: {self.lecture_halls}, Профіль: {self.faculty}"
        )



class DigitalDevice:
    def __init__(self, brand: str, model: str, price: float) -> None:
        if not brand.strip() or not model.strip():
            raise ValueError("Виробник і модель пристрою не можуть бути порожніми.")
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self.brand = brand.strip()
        self.model = model.strip()
        self.price = price

    def get_info(self) -> str:
        return (
            f"[Цифровий пристрій] {self.brand} {self.model}, "
            f"Ціна: {self.price:.2f} грн"
        )


class MobilePhone(DigitalDevice):
    def __init__(
        self, brand: str, model: str, price: float, os_name: str, sim_count: int
    ) -> None:
        super().__init__(brand, model, price)
        if not os_name.strip():
            raise ValueError("Назва ОС не може бути порожньою.")
        if sim_count <= 0:
            raise ValueError("Кількість SIM-карт має бути більшою за 0.")
        self.os_name = os_name.strip()
        self.sim_count = sim_count

    def get_info(self) -> str:
        return (
            f"[Мобільний телефон] {self.brand} {self.model}, "
            f"Ціна: {self.price:.2f} грн, ОС: {self.os_name}, SIM: {self.sim_count}"
        )



def find_in_range(items: list[T], min_val: T, max_val: T) -> list[T]:

    if min_val > max_val:
        raise ValueError(
            f"Помилка діапазону: нижня межа ({min_val}) більша за верхню ({max_val})."
        )
    return [item for item in items if min_val <= item <= max_val]



class NumberPair(Generic[T1, T2]):
    def __init__(self, first: T1, second: T2) -> None:
        if isinstance(first, bool) or isinstance(second, bool):
            raise ValueError("Логічні значення (bool) не допускаються як числа.")
        self.first: T1 = first
        self.second: T2 = second

    def __str__(self) -> str:
        return (
            f"Пара чисел: ({self.first} [{type(self.first).__name__}], "
            f"{self.second} [{type(self.second).__name__}])"
        )



def input_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print(f"Помилка вводу: '{raw}' не є цілим числом. Спробуйте ще раз.")


def input_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            val = float(raw)
            if val != val:
                raise ValueError("NaN")
            return val
        except ValueError:
            print(f"Помилка вводу: '{raw}' не є коректним числом. Спробуйте ще раз.")


def input_non_empty_str(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Помилка вводу: рядок не може бути порожнім. Спробуйте ще раз.")


def input_choice(prompt: str, valid_choices: set[str]) -> str:
    while True:
        val = input(prompt).strip()
        if val in valid_choices:
            return val
        print(
            f"Помилка вводу: оберіть один із варіантів {sorted(valid_choices)}."
        )



def run_buildings_demo() -> None:
    print("\n--- 1. Будинки та навчальні корпуси ---")
    count = input_int("Скільки об'єктів додати в масив? ")
    if count <= 0:
        print("Помилка: кількість об'єктів має бути більшою за 0.")
        return

    buildings: list[Building] = []
    for i in range(1, count + 1):
        print(f"\nОб'єкт #{i}:")
        kind = input_choice("Тип (1 - Будинок, 2 - Навчальний корпус): ", {"1", "2"})
        while True:
            try:
                address = input_non_empty_str("Адреса: ")
                floors = input_int("Кількість поверхів: ")
                area = input_float("Площа (м²): ")
                if kind == "1":
                    obj: Building = Building(address, floors, area)
                else:
                    halls = input_int("Кількість аудиторій: ")
                    faculty = input_non_empty_str("Факультет / профіль: ")
                    obj = AcademicBuilding(address, floors, area, halls, faculty)
                buildings.append(obj)
                break
            except ValueError as err:
                print(f"Помилка створення об'єкта: {err}. Введіть дані для цього об'єкта ще раз.")

    print("\nВивід масиву об'єктів у циклі:")
    for item in buildings:
        print(" ", item.get_info())


def run_devices_demo() -> None:
    print("\n--- 2. Цифрові пристрої та мобільні телефони ---")
    count = input_int("Скільки пристроїв додати в масив? ")
    if count <= 0:
        print("Помилка: кількість пристроїв має бути більшою за 0.")
        return

    devices: list[DigitalDevice] = []
    for i in range(1, count + 1):
        print(f"\nПристрій #{i}:")
        kind = input_choice(
            "Тип (1 - Цифровий пристрій, 2 - Мобільний телефон): ", {"1", "2"}
        )
        while True:
            try:
                brand = input_non_empty_str("Виробник: ")
                model = input_non_empty_str("Модель: ")
                price = input_float("Ціна (грн): ")
                if kind == "1":
                    dev: DigitalDevice = DigitalDevice(brand, model, price)
                else:
                    os_name = input_non_empty_str("Операційна система: ")
                    sims = input_int("Кількість SIM-карт: ")
                    dev = MobilePhone(brand, model, price, os_name, sims)
                devices.append(dev)
                break
            except ValueError as err:
                print(f"Помилка створення пристрою: {err}. Введіть дані ще раз.")

    print("\nВивід масиву пристроїв у циклі:")
    for dev in devices:
        print(" ", dev.get_info())


def run_range_search_demo() -> None:
    print("\n--- 3. Шаблонна функція пошуку в діапазоні ---")
    data_type = input_choice(
        "Оберіть тип елементів масиву (1 - цілі числа int, 2 - дробові float, 3 - рядки str): ",
        {"1", "2", "3"},
    )
    n = input_int("Скільки елементів ввести в масив? ")
    if n <= 0:
        print("Помилка: розмір масиву має бути більшим за 0.")
        return

    arr: list = []
    for i in range(1, n + 1):
        if data_type == "1":
            arr.append(input_int(f"Елемент [{i}]: "))
        elif data_type == "2":
            arr.append(input_float(f"Елемент [{i}]: "))
        else:
            arr.append(input_non_empty_str(f"Елемент [{i}]: "))

    while True:
        try:
            if data_type == "1":
                low = input_int("Нижня межа діапазону: ")
                high = input_int("Верхня межа діапазону: ")
            elif data_type == "2":
                low = input_float("Нижня межа діапазону: ")
                high = input_float("Верхня межа діапазону: ")
            else:
                low = input_non_empty_str("Нижня межа діапазону (рядок): ")
                high = input_non_empty_str("Верхня межа діапазону (рядок): ")

            found = find_in_range(arr, low, high)
            print(f"Вхідний масив: {arr}")
            print(f"Елементи в діапазоні [{low}; {high}]: {found}")
            break
        except ValueError as err:
            print(f"Помилка: {err}. Спробуйте ввести межі ще раз.")


def run_number_pair_demo() -> None:
    print("\n--- 4. Шаблон класу для пари чисел різних типів ---")
    type1 = input_choice("Тип першого числа (1 - int, 2 - float): ", {"1", "2"})
    type2 = input_choice("Тип другого числа (1 - int, 2 - float): ", {"1", "2"})

    try:
        first = input_int("Введіть перше число (int): ") if type1 == "1" else input_float("Введіть перше число (float): ")
        second = input_int("Введіть друге число (int): ") if type2 == "1" else input_float("Введіть друге число (float): ")
        pair = NumberPair(first, second)
        print("Результат:", pair)
    except ValueError as err:
        print(f"Помилка: {err}")


def main() -> None:
    while True:
        print("\n================ МЕНЮ ЗАВДАНЬ ================")
        print("1 - Ієрархія 'Будинок – Навчальний корпус'")
        print("2 - Ієрархія 'Цифровий пристрій – Мобільний телефон'")
        print("3 - Шаблонна функція пошуку в діапазоні")
        print("4 - Шаблон класу 'Пара чисел різних типів'")
        print("0 - Вихід")

        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            run_buildings_demo()
        elif choice == "2":
            run_devices_demo()
        elif choice == "3":
            run_range_search_demo()
        elif choice == "4":
            run_number_pair_demo()
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print(f"Помилка: невідомий пункт меню '{choice}'. Оберіть число від 0 до 4.")


if __name__ == "__main__":
    main()
