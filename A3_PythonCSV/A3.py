import csv

#Converting selected dict fields
print('Reading as dicts with type conversion')

field_types = [ ('X1', float),
                ('X2', float)]
rows = []
X1 = []
X2 = []

with open('e:\pcsv.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) 
                   for key, conversion in field_types)
        print(row)
        rows.append(row)
        X1.append(row['X1'])
        X2.append(row['X2'])
        
print('***************************************\n')
print(rows)
print('\nX1')
print(X1)
print('\nX2')
print(X2)

X3 = [x + y for x, y in zip(X1, X2)]
X4 = [y - x for x, y in zip(X1, X2)]
print('\nX3 = X1 + X2')
print(X3)
print('\nX4 = X2 - X1')
print(X4)

w_rows = [X1, X2, X3, X4]
headers = ['X1', 'X2', 'X1_add_X2', 'X2_sub_X1']
#print(w_rows)

with open('e:\pcsv2.csv','w') as f2:
    f_csv = csv.writer(f2)
    f_csv.writerow(headers)
    
    for i in range(len(X1)):
        tem_row = []
        tem_row.append(X1[i])
        tem_row.append(X2[i])
        tem_row.append(X3[i])
        tem_row.append(X4[i])
        f_csv.writerow(tem_row)
        #print(tem_row)
        
