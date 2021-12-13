individuals = {'Pluto': 'active', 'Goofy': 'inactive', 'Sofie': 'active'}

for individual, status in individuals.copy().items():
    if status == 'inactive':
        del individuals[individual]

        
active_individuals = {}
for individual, status in individuals.items():
    if status == 'active':
        active_individuals[individual] = status

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


for i in range(100):
    print(i)

list(range(68, 150))




file = open("sample.bin", "wb")
file. write(b"This binary string will be written to sample.bin")
file