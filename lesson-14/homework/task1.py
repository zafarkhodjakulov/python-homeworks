from bs4 import BeautifulSoup
from pathlib import Path

current_dir = Path(__file__).resolve().parent
weather_dict = {}
number = []
temperature = []
with open(current_dir / 'weather.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

def read_th():
    th = soup.find_all('th')
    th_items = [i.text for i in th]
    return th_items

def read_td():
    td = soup.find_all('td')
    td_items = [i.text for i in td]
    return td_items

def identify():
    a = read_td()
    day = [a[i] for i in range(0, len(a), 3)]
    temp = [a[i+1] for i in range(0, len(a), 3)]
    cond = [a[i+2] for i in range(0, len(a), 3)]  
    return day, temp, cond

def print_data():
    data = identify()
    day = data[0]
    temp = data[1]
    cond = data[2]
    return [print(f'Day: {day[i]}, Temperature: {temp[i]}, Contion: {cond[i]}') for i in range(len(day))]

def identify_max():
    number = []
    temperature = []
    data = identify()
    for i in data[1]:
        temperature.append(int(i[:2]))
    max_index = temperature.index(max(temperature))
    for i in range(len(data[2])):
        if data[2][i] == 'Sunny':
            number.append(i)
    return number, max_index, temperature

def print_max_temp():
    n = identify_max()
    data = identify()
    return print(f'Maximal temperatura day:\nDay: {data[0][n[1]]}, Temperature: {data[1][n[1]]}, Contion: {data[2][n[1]]}')
    

def print_sunny():
    n = identify_max()
    data = identify()
    for i in n[0]:
        print(f'Sunny days:\nDay: {data[1][i]}, Temperature: {data[1][i]}, Condition: {data[2][i]}\n')

def week_mean():
    n = identify_max()
    temp = n[2]
    mean_temp = sum(temp) / len(temp)
    return print(f'Hafta davomida ortacha harorat - {mean_temp}')
  
print_data()
print('-'*50)
print_max_temp()
print('-'*50)
print_sunny()
print('-'*50)
week_mean()
    






