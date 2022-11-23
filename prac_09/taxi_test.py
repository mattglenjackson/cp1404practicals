from taxi import Taxi

my_taxi = Taxi('Prius 1', 100)
my_taxi.drive(40)
print(my_taxi)
print(f"${my_taxi.get_fare()}")
my_taxi.add_fuel(40)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(f"${my_taxi.get_fare()}")

