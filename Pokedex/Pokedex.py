try:
    import pandas as pd
except ImportError as e:
    print(f'pogram failed beacuse of {e} plz install pandas')
    raise SystemExit(0)
try:
    import matplotlib.pyplot as mat
except ImportError as e:
    print(f'pogram failed beacuse of {e} plz install matplotlib')
    raise SystemExit(0)
data = pd.read_json('data.json').set_index(['No','Name'],drop=False)
mat.style.use('ggplot')
def rarity():
    mat.pie([((data['Legendary']==False) & (data['Mythical']==False)).sum(),data['Legendary'].sum(),data['Mythical'].sum()],labels = ['Common','Legendary','Mythical'])
    mat.show()
def look():
    user_input=int(input())
    global data
    match user_input:
        case 1:
            user_input=str(input('enter name:- ')).title()
            try:
                print(data.loc[(slice(None),user_input),:])
                mat.barh(data.columns[7:13],data.loc[(slice(None),user_input),data.columns[7:13]].values.flatten())
                mat.gca().invert_yaxis()
                mat.show()
            except KeyError as e:
                print(f"{e}\nplease enter a valid name\n")
                return
        case 2:
            try:
                user_input=int(input('enter number:- '))
            except ValueError as e:
                print(f"{e}\nplease insert a number\n")
                return
            print(data.loc[user_input])
            mat.barh(data.columns[7:13],data.loc[user_input,data.columns[7:13]].values.flatten())
            mat.gca().invert_yaxis()
            mat.show()
        case _:
            print('please follow the instructions\n')
def filter_():
    global data
    for i in data.keys():
        print(f'{i} {data[i].dtype}')
    user_input= str(input()).title()
    if user_input not in data.keys():
        print("enter a valid criteria")
        return
    match data[user_input].dtype:
        case 'str':
            value=str(input("enter the value:- ")).title()
            if user_input == 'Type1' or user_input=='Type2':
                print(data[(data['Type1']==value) | (data['Type2']==value)].to_string())
            elif user_input in data.columns[13:20]:
                print(data[(data[data.columns[13:20]]=='Water').any(axis=1)].to_string())
        case 'float64':
            max_value=float(input("enter the max value:- "))
            min_value=float(input("enter the min value:- "))
            print(data[(data[user_input]>=min_value) & (data[user_input]<=max_value)])
        case 'int64':
            max_value=float(input("enter the max value:- "))
            min_value=float(input("enter the min value:- "))
            print(data[(data[user_input]>=min_value) & (data[user_input]<=max_value)].to_string(index=False))
        case 'bool':
            print(f"to show only {user_input} type true\nto show except {user_input} press enter")
            value=bool(input())
            print(data[data[user_input]==value])
        case _:
            print(data[user_input].dtype)
print(data.to_string(index=False))
