def convert_temperature():
    """Handles temperature conversions between Celsius, Fahrenheit, and Kelvin."""
    print("\n--- Temperature Converter ---")
    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Enter the starting unit (C, F, K): ").upper()
        to_unit = input("Enter the unit to convert to (C, F, K): ").upper()

        if from_unit == to_unit:
            result = value
        # Celsius conversions
        elif from_unit == 'C':
            if to_unit == 'F':
                result = (value * 9 / 5) + 32
            elif to_unit == 'K':
                result = value + 273.15
            else:
                print("Invalid target unit!")
                return
        # Fahrenheit conversions
        elif from_unit == 'F':
            if to_unit == 'C':
                result = (value - 32) * 5 / 9
            elif to_unit == 'K':
                result = (value - 32) * 5 / 9 + 273.15
            else:
                print("Invalid target unit!")
                return
        # Kelvin conversions
        elif from_unit == 'K':
            if to_unit == 'C':
                result = value - 273.15
            elif to_unit == 'F':
                result = (value - 273.15) * 9 / 5 + 32
            else:
                print("Invalid target unit!")
                return
        else:
            print("Invalid starting unit!")
            return

        print(f"\nResult: {value:.2f} {from_unit} is equal to {result:.2f} {to_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")
    except Exception as e:
        print(f"An error occurred: {e}")


def convert_length():
    """Handles length conversions using a dictionary of factors relative to meters."""
    print("\n--- Length Converter ---")
    # Conversion factors to meters
    factors = {
        'M': 1.0,
        'KM': 1000.0,
        'CM': 0.01,
        'MM': 0.001,
        'MI': 1609.34,
        'YD': 0.9144,
        'FT': 0.3048,
        'IN': 0.0254,
    }

    print("Available units: M (Meters), KM (Kilometers), CM (Centimeters), MM (Millimeters)")
    print("                 MI (Miles), YD (Yards), FT (Feet), IN (Inches)")

    try:
        value = float(input("Enter the length value: "))
        from_unit = input("Enter the starting unit: ").upper()
        to_unit = input("Enter the unit to convert to: ").upper()

        if from_unit not in factors or to_unit not in factors:
            print("Invalid unit specified. Please use one of the available units.")
            return

        # Convert the initial value to meters
        value_in_meters = value * factors[from_unit]

        # Convert from meters to the target unit
        result = value_in_meters / factors[to_unit]

        print(f"\nResult: {value:.4f} {from_unit} is equal to {result:.4f} {to_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")
    except Exception as e:
        print(f"An error occurred: {e}")


def convert_weight():
    """Handles weight conversions using a dictionary of factors relative to kilograms."""
    print("\n--- Weight Converter ---")
    # Conversion factors to kilograms
    factors = {
        'KG': 1.0,
        'G': 0.001,
        'MG': 0.000001,
        'LB': 0.453592,
        'OZ': 0.0283495,
    }

    print("Available units: KG (Kilograms), G (Grams), MG (Milligrams), LB (Pounds), OZ (Ounces)")

    try:
        value = float(input("Enter the weight value: "))
        from_unit = input("Enter the starting unit: ").upper()
        to_unit = input("Enter the unit to convert to: ").upper()

        if from_unit not in factors or to_unit not in factors:
            print("Invalid unit specified. Please use one of the available units.")
            return

        # Convert the initial value to kilograms
        value_in_kg = value * factors[from_unit]

        # Convert from kilograms to the target unit
        result = value_in_kg / factors[to_unit]

        print(f"\nResult: {value:.4f} {from_unit} is equal to {result:.4f} {to_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the weight.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main function to run the unit converter application."""
    print("Welcome to the Python Unit Converter!")

    while True:
        print("\nPlease choose a category:")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            convert_temperature()
        elif choice == '2':
            convert_length()
        elif choice == '3':
            convert_weight()
        elif choice == '4':
            print("Thank you for using the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
