from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)

"""
To download a pack, go to file >> settings >> project >> interpreter and then search and download the pack you want and you will
get access to all its functions and libraries. Dont forget to import it in the code
"""
