class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, population_value):
        self.population_value = population_value
        self.current_value = 0
    # Допишите метод

    def create_new(self):
        self.current_value += 1
        if self.current_value > self.population_value:
            print('Нет места под новую бактерию')
        else:
            print(f'Добавлена одна бактерия. Количество бактерий в популяции: {self.current_value}')

    # Допишите метод

    def remove_one(self):
        if self.current_value <= 0:
            print('В популяции нет бактерий, удалять нечего')
        else:
            self.current_value -= 1
            print(f'Одна бактерия удалена. Количество бактерий в популяции: {self.current_value}')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
