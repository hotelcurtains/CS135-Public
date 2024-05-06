def alternating_sum(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    
    # Initialize the sum to 0
    result = 0
    
    # Iterate through the digits
    for i in range(len(num_str)):
        # Check if the current index is even or odd
        if i % 2 == 0:
            # Add the digit to the sum if the index is even
            result += int(num_str[i])
        else:
            # Subtract the digit from the sum if the index is odd
            result -= int(num_str[i])
    
    # Return the alternating sum
    return result


hi = list(range(-99999,99999))
for i in range(len(hi)):
    hi[i] = i*11
for i in hi:
    if alternating_sum(i) % 11 != 0:
        print(i)