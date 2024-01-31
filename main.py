# calculate age part 1
# def calculate_age(birth_year, current_year):
#     age = current_year - birth_year
#     return age
#
# # assigning var to func
# def test_age():
#     test_1 = calculate_age(2001, 2024)
#     print("Hello, your age is", str(test_1))
# # test_age()
#
# #
# def make_location(city, country):
#     loction = city , country
#     return loction
#
# # pick_location()
# def pick_location():
#     location_1 = make_location('Tokyo', 'Japan')
#     print(location_1)


#part 2

# Add the functions for the assignment below here and above the main function.

def calculate_gas_vehicle_trip_cost (MILES, MPG, gas_price):
    # Calculate gallons needed for trip
    gallons_needed_for_trip = MILES/MPG
    # Calculate trip cost
    trip_cost = gallons_needed_for_trip * gas_price
    return trip_cost

def calculate_electric_vehicle_trip_cost (MILES, WHPM, eletric_price):
    # Calculate kwh needed for trip
    kwh_needed_for_trip = (WHPM/1000) * MILES
    # Calculate trip cost if in e-car
    trip_cost_for_ecar = kwh_needed_for_trip * eletric_price
    return trip_cost_for_ecar


# Keep this main function
def main():
    # Ask for gas and elertric prices
    gas_price = float(input(" Enter gas price: "))
    eletricity_price = float(input(" Enter eletricity prices in dollars per kilowatt-hour: "))

    # car mph variables
    gas_car_mpg = 25.1
    truck_mpg = 14.2
    eletric_car_mpg = 230.7


    # loop miles of trip by 50
    for distance in range(50, 501, 50):
        gas_car_cost = calculate_gas_vehicle_trip_cost(distance, gas_car_mpg, gas_price)
        truck_car_cost = calculate_gas_vehicle_trip_cost(distance,truck_mpg, gas_price)
        eletric_car_cost = calculate_electric_vehicle_trip_cost(distance, eletric_car_mpg, eletricity_price)

    print(" For a trip of "+ str(distance)+ "miles", "the costs for a gas car is", str(gas_car_cost)+ ", the costs for a truck is: "+ str(truck_car_cost)+ " the costs for a eletric car is: " + str(eletric_car_cost))
# Keep these lines. It helps Python run the program correctly by calling main when the program is run.
if __name__ == "__main__":
    main()