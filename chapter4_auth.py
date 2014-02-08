import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        hash_string = (self.username + password).encode("utf8")
        #hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        return self.password ==  self._encrypt_pw(password)

class AuthException(Exception):
    def __init__(self, username, user=None): #user = user class
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

class PermissionError(Exception):
    pass

class Authenticator:
    def __init__(self):
        self.users = {} #empty dictionary

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False # if not found 

    def logout(self, username):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        user.is_logged_in = False
        return None

class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set() #στο dict το value είναι τύπου set
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exists")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username) #if username already in set then is not doubled
            
    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exists")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True
        
class Editor:
  def __init__(self):
    self.username = None
    self.menu_map = {"l": self.login,
                     "t": self.test,
                     "c": self.change,
                     "q": self.quit
                     }

  def login(self):
    logged_in = False
    while not logged_in:
        username = input("username: ")
        password = input("password: ")
        try:
            logged_in = authenticator.login(username, password)
        except InvalidUsername:
            print("Sorry, that username does not exist")
        except InvalidPassword:
            print("Sorry, incorrect password")
        else:
            self.username = username

  def is_permitted(self, permission):
        try:
            authorizor.check_permission(permission, self.username)
        except NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

  def test(self):
        perm = input('permission:')
        if self.is_permitted(perm):
            print("Joe can", perm)

  def change(self):
        perm = input('permission:')
        if not self.is_permitted(perm):
            authorizor.permit_user(perm, "joe")            

  def quit(self):
        raise SystemExit()        

  def menu(self):
        try:
            answer = ""
            while True:
                print("""Please enter a command: \nl\tLogin\nt\tTest the program \nc\tChange the program \nq\tQuit""")
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")
        return None

if __name__=="__main__":
  authenticator = Authenticator()
  authorizor = Authorizor(authenticator)

  authenticator.add_user("joe", "joepassword")
  authorizor.add_permission('paint')#create permission
  authorizor.add_permission('dance')#create permission
  authorizor.permit_user('paint', "joe")#add joe in permission
  Editor().menu()
