# Read input from input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Process lines
output = []
for line in lines:
    if line.strip():  # Check if line is not empty
        parts = line.strip().split(' = { ')
        if len(parts) == 2:
            item_name = parts[0].strip()
            attributes = parts[1].strip().strip('},')

            # Initialize attributes
            label = weight = shouldClose = None

            # Extracting attributes
            attribute_pairs = [pair.strip() for pair in attributes.split(',')]
            for pair in attribute_pairs:
                key_value = pair.split(' = ')
                if len(key_value) == 2:
                    key = key_value[0].strip()
                    value = key_value[1].strip().strip('"')
                    if key == 'label':
                        label = value
                    elif key == 'weight':
                        weight = value
                    elif key == 'shouldClose':
                        shouldClose = value

            # Constructing the output
            if label is not None and weight is not None and shouldClose is not None:
                output.append(f"['{item_name}'] = {{\n"
                              f"    label = '{label}',\n"
                              f"    weight = {weight},\n"
                              f"    stack = false,\n"
                              f"    close = {shouldClose}\n"
                              f"}},\n")

# Write output to output.lua
with open('output.lua', 'w') as file:
    file.writelines(output)
