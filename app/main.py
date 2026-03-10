class Car:
    def __init__(self: "Car", comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self: "CarWashStation",
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self: "CarWashStation", car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self: "CarWashStation", car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self: "CarWashStation", cars: list) -> float:
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self: "CarWashStation", rate: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


# Приклади
bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([bmw, audi, mercedes])

print("Income:", income)  # 41.7
print("Clearity:")
print(f"Brand {bmw.brand}:", bmw.clean_mark)  # 8
print(f"Brand {audi.brand}:", audi.clean_mark)  # 9
print(f"Brand {mercedes.brand}:", mercedes.clean_mark)  # 8
# audi wasn't washed
# all other cars are washed to '8'

ford = Car(2, 1, "Ford")
wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
print(f"Brand {ford.brand}. Washing_price:", wash_cost)  # 9.1
print(f"Brand {ford.brand}. Clearity", ford.clean_mark)  # 1

ws.rate_service(5)

print("Count of ratings", ws.count_of_ratings)  # 12
print("Average rating:", ws.average_rating)  # 4.0
