from myapp.models import User

def addUser(first_name,last_name,email_id):
    u = User(first_name = first_name,
            last_name = last_name,
            email_id = email_id
             )
    u.save()
