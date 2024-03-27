table_width = 79

# Print the top border of the table
print("+" + "-" * (table_width-2) + "+")

# Print the header row of the table
header = "|{:^77}|".format("Table of 79")
print(header)

# Print the middle border of the table
print("|" + "-" * (table_width-2) + "|")

# Print the content of the table
for i in range(1, 11):
    row = "|{:^77}|".format(f"{i} x 79 = {i*79}")
    print(row)

# Print the bottom border of the table
print("+" + "-" * (table_width-2) + "+")
