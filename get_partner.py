from env import user, password, host
import pandas as pd

def ask_for_name():

    return input('\n  \nWhat Last Name would yout like to look up?\n')


def ask_for_module():
    print("\nwhich module are you needing partner for?")
    print('(Python: Module4, Linear Reg: Module5, Classification: Module6)')
    print('type "all" for all modules')
    return input()


url = f'mysql+pymysql://{user}:{password}@{host}'

db_url = url + '/ada_students'

def main():
    print("let's check partner groups!")
    #student name
    sname = ask_for_name()
    module = ask_for_module()
    all_modules = False
    if module.isdigit():
        module = int(module)
    else:
        all_modules =  (module.lower().strip() == 'all')


    df = pd.read_sql('SELECT * FROM student_groups JOIN students USING(student_id) \
        JOIN modules USING(module_id)', db_url)


    ### Module is int
    if all_modules:
        sdf = df[df['last_name']==sname]
        module_ids = list(sdf['module_id'])
        module_names = list(sdf['module_name'])
        for i in (module_ids):
            sdf = df[df['last_name']==sname]
            gdf = sdf[sdf['module_id']== i]
            group_id = int(gdf.group_id)
            group = df[df['group_id'] == group_id]
            module_name = str(gdf.module_name)
            module_n = df[df['module_name'] == module_name]
            partners = group[group['module_id'] == i]
            print(partners[['student_id','module_id','module_name', 'first_name','last_name']])
    else:
        sdf = df[df['last_name']==sname]
        gdf = sdf[sdf['module_id']== module]
        group_id = int(gdf.group_id)
        group = df[df['group_id'] == group_id]
        module_name = str(gdf.module_name)
        module_n = df[df['module_name'] == module_name]
        partners = group[group['module_id'] == module]
        print(partners[['student_id','module_id','module_name', 'first_name','last_name']])



if __name__ == '__main__':
    main()