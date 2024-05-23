# input_processing.py
# Kim_Nguyen, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:
    def __init__(self, light='green', pedestrian='no', vehicle='no'):
        # Constructor for the Sensor class with default values.
        # Attributes:
        # light (str): Represents the color of the traffic light.
        # pedestrian (str): Indicates whether a pedestrian is present ('yes' or 'no').
        # vehicle (str): Indicates whether a vehicle is present ('yes' or 'no').
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle

    def update_status(self):
        # Updates the status of the sensor based on user input.
        # Prompts the user to specify changes in the vision input. Depending on the input,
        # updates the sensor's attributes for light, pedestrian, or vehicle.
        
        print("Are changes detected in the vision input? ")

        try:
            change = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

            if change not in ["0", "1", "2", "3"]:
                raise ValueError
            else:
                if change == "1":
                    input_1 = input("What change has been identified?: ")
                    if input_1 in ["green", "yellow", "red"]:
                        self.light = input_1
                    else:
                        print("Invalid vision change \n")
                elif change == "2":
                    input_2 = input("What change has been identified?: ")
                    if input_2 in ["yes", "no"]:
                        self.pedestrian = input_2
                    else:
                        print("Invalid vision change \n")
                elif change == "3":
                    input_3 = input("What change has been identified?: ")
                    if input_3 in ["yes", "no"]:
                        self.vehicle = input_3
                    else:
                        print("Invalid vision change \n")
                elif change == "0":
                    print("\n")
        except ValueError:
            print("You must select either 0, 1, 2, 3")
            return "null"
        return change

def print_message(sensor):
    # Prints an action message based on the current sensor status.
    # If the light is red, or a pedestrian or vehicle is detected, it prints "STOP".
    # If the light is yellow and no pedestrian or vehicle is detected, it prints "Caution".
    # If the light is green and no pedestrian or vehicle is detected, it prints "Proceed".
    
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\n STOP \n")
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\n Caution \n")
    elif sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\n Proceed \n")

def main():
    # Main function to run the car vision detector processing program.
    # Initializes a Sensor object and continuously updates its status based on user input
    # until the user decides to end the program.
    
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    vehicle_sensor = Sensor()
    user_entry = " "

    while True:
        user_entry = vehicle_sensor.update_status()
        if user_entry == "0":
            break
        elif user_entry != "null":
            print_message(vehicle_sensor)
            print("Light = " + vehicle_sensor.light + ", Pedestrian = " + 
                  vehicle_sensor.pedestrian + ", Vehicle = " + vehicle_sensor.vehicle + "\n")

if __name__ == '__main__':
    main()
