from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi('Hummer', 200, 4)
print(hummer)

silver_service_taxi = SilverServiceTaxi('Taxi', 100, 2)
silver_service_taxi.drive(18)
print(silver_service_taxi)
print(f"Fare for taxi is ${silver_service_taxi.get_fare()}")
