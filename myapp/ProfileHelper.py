from myapp.models import User, UserDetails

def addUser(first_name,last_name,email_id):
    u = User(first_name = first_name,
            last_name = last_name,
            email_id = email_id
             )
    u.save()

def addUserDetails(user_id, age, gender, weight, height, bmi, goal_weight):
    user = User.objects.filter(id = user_id)

    u = UserDetails(user = user[0],
        age = age,
        gender = gender,
        weight = weight,
        height = height,
        bmi = bmi,
        goal_weight = goal_weight
        )
    u.save()
