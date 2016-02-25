import csv, getpass

def get_last_id(users_csv):
    res = 0
    for row in users_csv :
        if int(row['id']) > res :
            res = int(row['id'])
    return res
        
def check_login(users_csv,login):
    print(users_csv)
    for row in users_csv :
        print(row)
        if row['login'] == login : return False
        else : return True
    
        
def user_input():
    name = raw_input('Enter a name, this is not your login, people wont see it ')
    login = raw_input('Enter your login, remember people will see that =) ')
    password = getpass.getpass('Enter you password : ')
    
    return name, login, password
   
def save_user(new_id, name, login, password):
    with open('users.csv', 'a') as csv_writer:
        fieldnames = ['id','name', 'login', 'password']
        writer = csv.DictWriter(csv_writer, fieldnames=fieldnames)
        writer.writerow({'id':new_id, 'name':name, 'login':login, 'password':password})
    
def main():
    
    users_csv = csv.DictReader(open('users.csv'))
    flag = False
    while (flag == False) :
        name, login, password = user_input()
        flag = check_login(users_csv,login) 
        if flag == False :
            print("Sorry your someone already use this login ... try again !")
        
    new_id = get_last_id(users_csv)+1
    save_user(new_id, name, login, password)
    
main()

