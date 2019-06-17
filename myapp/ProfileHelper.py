from myapp.models import User

def addUser(first_name,last_name,email):
    u = User(first_name = first_name,
            last_name = last_name,
            email = email
             )
    u.save()
