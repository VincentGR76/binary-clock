import time

# Function to convert decimal to binary and format to specified number of bits
def decimal_to_binary(num, num_bits):
    return format(num, f'0{num_bits}b')

# Function to display the binary watch with LED-like ASCII symbols
def display_binary_watch(hour, minute, second):
    binary_hour = decimal_to_binary(hour, 4)
    binary_minute = decimal_to_binary(minute, 6)
    binary_second = decimal_to_binary(second, 6)

    # Define LED-like ASCII symbols
    LED_ON = "\033[92m██\033[0m"
    LED_OFF = "\033[91m██\033[0m"

    # Display binary watch with LED-like ASCII symbols
    print("Binary Watch with LED-like ASCII symbols (HH:MM:SS):")
    print(f"{LED_ON if binary_hour[0] == '1' else LED_OFF} {LED_ON if binary_hour[1] == '1' else LED_OFF} {LED_ON if binary_hour[2] == '1' else LED_OFF} {LED_ON if binary_hour[3] == '1' else LED_OFF}    {LED_ON if binary_minute[0] == '1' else LED_OFF} {LED_ON if binary_minute[1] == '1' else LED_OFF} {LED_ON if binary_minute[2] == '1' else LED_OFF} {LED_ON if binary_minute[3] == '1' else LED_OFF} {LED_ON if binary_minute[4] == '1' else LED_OFF} {LED_ON if binary_minute[5] == '1' else LED_OFF}    {LED_ON if binary_second[0] == '1' else LED_OFF} {LED_ON if binary_second[1] == '1' else LED_OFF} {LED_ON if binary_second[2] == '1' else LED_OFF} {LED_ON if binary_second[3] == '1' else LED_OFF} {LED_ON if binary_second[4] == '1' else LED_OFF} {LED_ON if binary_second[5] == '1' else LED_OFF}")
    print("-- -- -- --    -- -- -- -- -- --    -- -- -- -- -- --")
    print("08 04 02 01    32 16 08 04 02 01    32 16 08 04 02 01")

# Main function
def main():
    try:
        while True:
            # Get current time
            current_time = time.localtime()
            hour = current_time.tm_hour
            minute = current_time.tm_min
            second = current_time.tm_sec

            # Display binary watch with LED-like ASCII symbols
            display_binary_watch(hour, minute, second)

            # Refresh every second
            time.sleep(1)

            # Clear terminal for new display
            print("\033[H\033[J", end="")

    except KeyboardInterrupt:
        print("\nBinary watch stopped.")

if __name__ == "__main__":
    main()
