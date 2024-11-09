import random
import csv

data = {
    'Yosh': [25, 45, 35, 50, 40, 60, 30, 55, 42, 38],
    'Vazn': [70, 80, 60, 90, 75, 85, 65, 82, 68, 74],
    'Qon_Bosim': [120, 130, 125, 140, 135, 150, 115, 145, 125, 130],
    'Diastolik_Qon_Bosim': [80, 85, 82, 90, 88, 95, 78, 92, 80, 83],
    'Xolesterin': [180, 210, 190, 220, 200, 240, 170, 230, 180, 200],
    'Glukoza': [90, 110, 100, 120, 105, 130, 85, 125, 95, 100],
    'Target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
}


for _ in range(90000):
    yosh = random.randint(20, 70)
    vazn = random.randint(50, 120)
    qon_bosim = random.randint(110, 180)
    diastolik_qon_bosim = random.randint(70, 100)
    xolesterin = random.randint(150, 250)
    glukoza = random.randint(80, 150)

    
    if yosh > 50 and qon_bosim > 140:  
        target = 1
    elif xolesterin > 240 or glukoza > 120: 
        target = 1
    else:
        target = 0  

    data['Yosh'].append(yosh)
    data['Vazn'].append(vazn)
    data['Qon_Bosim'].append(qon_bosim)
    data['Diastolik_Qon_Bosim'].append(diastolik_qon_bosim)
    data['Xolesterin'].append(xolesterin)
    data['Glukoza'].append(glukoza)
    data['Target'].append(target)


with open('data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()

   
    for i in range(len(data['Yosh'])):
        row = {key: data[key][i] for key in data}
        writer.writerow(row)

print("Ma'lumotlar faylga saqlandi.")
