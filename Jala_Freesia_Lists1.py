array = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
print("--- 1. Original Array ---")
print(f"Original array: {array}\n")

try:
    print("--- Update Section ---")
    idx = int(input("Enter index to update (0-4): "))
    new_value = input("Enter the replacement value: ")
    
    old_value = array[idx]
    array[idx] = new_value

    print(f"\n-> Updated index {idx} from '{old_value}' to '{new_value}'\n")

    print("--- Slicing Section ---")
    start = int(input("Enter slice start index: "))
    end = int(input("Enter slice end index: "))
    
    sliced_array = array[start:end]
    
    print(f"Sliced portion [{start}:{end}]: {sliced_array}\n")

    print("--- Search Section ---")
    search_item = input("Enter an item to search for inside the sliced portion: ")
    
    if search_item in sliced_array:
        sliced_idx = sliced_array.index(search_item)
        print(f"-> Search Result: '{search_item}' FOUND in the sliced array at slice-index {sliced_idx}.\n")
    else:
        print(f"-> Search Result: '{search_item}' NOT FOUND inside the sliced portion.\n")

    print("--- Final Result ---")
    print(f"Updated array: {array}")

except IndexError:
    print("\nError: Index is out of bounds for the array.")
except ValueError:
    print("\nError: Please enter a valid integer for indices.")
