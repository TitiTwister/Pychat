import csv, getpass
from email import _name

class User():
    
    def __init__(self):
        name =''
        login=''
        
    def _get_last_id(self,users_csv):
        res = 0
        for row in users_csv :
            if int(row['id']) > res :
                res = int(row['id'])
        return res
            
    def _check_login_unique(self,users_csv,login):
        for row in users_csv :
            if row['login'] == login :
                return False
        return True
             
    def _user_input(self):
        name = raw_input('Enter a name, this is not your login, people wont see it : ')
        login = raw_input('Enter your login, remember people will see this one =) : ')
        password = getpass.getpass('Enter you password : ')
        return name, login, password
       
    def _write_user(self,new_id, name, login, password):
        with open('users.csv', 'a') as csv_writer:
            fieldnames = ['id','name', 'login', 'password']
            writer = csv.DictWriter(csv_writer, fieldnames=fieldnames)
            writer.writerow({'id':new_id, 'name':name, 'login':login, 'password':password})
    
    def user_sign_up(self):
        
        users_csv = csv.DictReader(open('users.csv', 'r'))
        login_uniq = False
        while (login_uniq == False) :
            name, login, password = self._user_input()
            flag = self._check_login_unique(users_csv,login) 
            if login_uniq == False :
                print("Sorry your someone already use this login ... try again !")
            
        new_id = self._get_last_id(users_csv)+1
        self._write_user(new_id, name, login, password)
    
    
    def check_login(self, login):
        
        users_csv = csv.DictReader(open('users.csv', 'r'))
        exist = False
        for row in users_csv:
            if row['login']==login :
                self.login = login
                exist=True
        return exist
    
    def check_password(self, password):
        
        users_csv = csv.DictReader(open('users.csv', 'r'))
        for row in users_csv:
            if row['login'] == self.login and row['password'] == password :
                
                self.name = row['name']
                return True
        return False
        
        
        
        
