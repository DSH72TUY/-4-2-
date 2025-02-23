class Aircraft:
    """ Базовый класс для самолётов. """

    def __init__(self, brand: str, model: str, capacity: int):
        """
        Инициализация самолёта.

        :param brand: Марка самолёта.
        :param model: Модель самолёта.
        :param capacity: Вместимость самолёта (количество пассажиров).
        """
        self._brand = brand  # Защищенный атрибут, чтобы предотвратить его изменение.
        self._model = model
        self._capacity = capacity

    @property
    def brand(self) -> str:
        """ Возвращает марку самолёта. """
        return self._brand

    @property
    def model(self) -> str:
        """ Возвращает модель самолёта. """
        return self._model

    @property
    def capacity(self) -> int:
        """ Возвращает вместимость самолёта. """
        return self._capacity

    def take_off(self) -> str:
        """ Запускает процесс взлёта самолёта.

        :return: Сообщение о взлёте самолёта.
        """
        return f"{self.brand} {self.model} is taking off."

    def __str__(self) -> str:
        """ Возвращает строковое представление самолёта. """
        return f"{self.brand} {self.model} with capacity of {self.capacity} passengers"

    def __repr__(self) -> str:
        """ Возвращает формальное строковое представление самолёта. """
        return f"Aircraft(brand={self.brand!r}, model={self.model!r}, capacity={self.capacity})"


class CivilianAircraft(Aircraft):
    """ Класс для гражданских самолётов. """

    def __init__(self, brand: str, model: str, capacity: int, airline: str):
        """
        Инициализация гражданского самолёта.

        :param brand: Марка самолёта.
        :param model: Модель самолёта.
        :param capacity: Вместимость самолёта (количество пассажиров).
        :param airline: Авиакомпания, которой принадлежит самолёт.
        """
        super().__init__(brand, model, capacity)
        self._airline = airline  # Защищенный атрибут, чтобы предотвратить его изменение.

    @property
    def airline(self) -> str:
        """ Возвращает авиакомпанию самолёта. """
        return self._airline

    def take_off(self) -> str:
        """ Запускает процесс взлёта гражданского самолёта.

        Переопределяем метод для добавления информации об авиакомпании.

        :return: Сообщение о взлёте самолёта с указанием авиакомпании.
        """
        return f"{super().take_off()} Airline: {self.airline}."

    def __str__(self) -> str:
        """ Возвращает строковое представление гражданского самолёта. """
        return f"{super().__str__()} operated by {self.airline}"

    def __repr__(self) -> str:
        """ Возвращает формальное строковое представление гражданского самолёта. """
        return f"CivilianAircraft(brand={self.brand!r}, model={self.model!r}, capacity={self.capacity}, airline={self.airline!r})"


class MilitaryAircraft(Aircraft):
    """ Класс для военных самолётов. """

    def __init__(self, brand: str, model: str, capacity: int, armament: str):
        """
        Инициализация военного самолёта.

        :param brand: Марка самолёта.
        :param model: Модель самолёта.
        :param capacity: Вместимость самолёта (количество пассажиров).
        :param armament: Тип вооружения самолёта.
        """
        super().__init__(brand, model, capacity)
        self._armament = armament  # Защищенный атрибут, чтобы предотвратить его изменение.

    @property
    def armament(self) -> str:
        """ Возвращает тип вооружения самолёта. """
        return self._armament

    def take_off(self) -> str:
        """ Запускает процесс идентификации военного самолёта.

        Переопределяем метод для добавления информации о классе-типе самолёта.

        :return: Сообщение самолёта с указанием функционального класса.
        """
        return f"{super().take_off()} Armament: {self.armament}."

    def __str__(self) -> str:
        """ Возвращает строковое представление военного самолёта. """
        return f"{super().__str__()} armed with {self.armament}"

    def __repr__(self) -> str:
        """ Возвращает формальное строковое представление военного самолёта. """
        return f"MilitaryAircraft(brand={self.brand!r}, model={self.model!r}, capacity={self.capacity}, armament={self.armament!r})"


if __name__ == '__main__':
    civilian_plane = CivilianAircraft("Boeing", "737", 160, "S7 Airlines")
    military_plane = MilitaryAircraft("ОКБ П.О.Сухого ", "СУ-57", 1, "многоцелевой истребитель")

if __name__ == '__main__':
    civilian_plane = CivilianAircraft("Boeing", "737", 160, "S7 Airlines")
    military_plane = MilitaryAircraft("ОКБ П.О.Сухого ", "СУ-57", 1, "многоцелевой истребитель")
    print(civilian_plane)  # вывод информации о гражданском самолёте
    print(repr(civilian_plane))  # вывод параметров(?) о самолёте
    print(civilian_plane.take_off())  # общая инф-я
    print(military_plane)  # вывод информации о военном самолёте
    print(repr(military_plane))  # Вывод параметров(?) военного самолёта
    print(military_plane.take_off())  # # общая инф-я
