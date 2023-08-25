import csv

def save_crimes(crimes):
    with open('crime_costs.csv', 'w', newline='') as csvfile:
        fieldnames = ['role', 'cost', 'succeed', 'escape', 'caught', 'expected_value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for crime in crimes:
            for role in crime.roles:
                row = {'role': f'{crime.name} - {role.name}', **role.__describe__()} 
                writer.writerow(row)