class Car:
    def __init__(self, company_name, model, color, manufacturing_year, price):
        self.company_name = company_name
        self.model = model
        self.color = color
        self.manufacturing_year = manufacturing_year
        self.price = price

    def display(self):
        print(f"Company: {self.company_name}, Model: {self.model}, Color: {self.color}, "
              f"Year: {self.manufacturing_year}, Price: ₹{self.price}")
        
def get_car_details():
    car_list = []
    num = int(input("Enter number of cars to input: "))
    for i in range(num):
        print(f"\nEnter details for Car {i + 1}:")
        company = input("Company Name: ")
        model = input("Model: ")
        color = input("Color: ")
        year = input("Manufacturing Year: ")
        price = float(input("Price (in ₹): "))
        car = Car(company, model, color, year, price)
        car_list.append(car)
    return car_list
def display_filtered_cars(car_list, company_filter, model_filter, price_filter):
    print(f"\nCars matching -> Company: {company_filter}, Model: {model_filter}, Price: ₹{price_filter}")
    found = False
    for car in car_list:
        if (car.company_name.lower() == company_filter.lower() and
            car.model.lower() == model_filter.lower() and
            car.price == price_filter):
            car.display()
            found = True
    if not found:
        print("No matching car found")

cars = get_car_details()

# Sample filter (you can also take input from user for this)
print("\nEnter filter criteria to search car details:")
search_company = input("Enter Company Name to Search: ")
search_model = input("Enter Model to Search: ")
search_price = float(input("Enter Price to Search: "))

display_filtered_cars(cars, search_company, search_model, search_price)
              

