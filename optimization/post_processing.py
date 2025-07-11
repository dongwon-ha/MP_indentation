from odbAccess import openOdb
import numpy as np
import csv

# Open the ODB file
odb = openOdb('indentation.odb')

displ = odb.steps['indentation'].historyRegions['Node TIP-1.41'].historyOutputs['U2']
force = odb.steps['indentation'].historyRegions['Node SUBSTRATE-1.33'].historyOutputs['RF2']
expansion = odb.steps['indentation'].historyRegions['Node MP-1.1'].historyOutputs['U1']

num = len(force.data)

results = np.zeros((num,3))

for i in range(num):
    results[i,0] = displ.data[i][1]
    results[i,1] = force.data[i][1]
    results[i,2] = expansion.data[i][1]

with open("odb_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)