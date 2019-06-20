from myapp.models import User, UserDetails, FoodInfo

def addUser(first_name,last_name,email_id):
    u = User(first_name = first_name,
            last_name = last_name,
            email_id = email_id
             )
    u.save()

def addUserDetails(user, age, gender, weight, height, bmi, goal_weight):
    print('adding user details')
    print("user = ",user)
    print("age = ",age)
    print("weight = ",weight)
    print("height = ",height)
    print("bmi = ",bmi)
    print("goal_weight = ",goal_weight)
    u = UserDetails(user = user,
        age = age,
        gender = gender,
        weight = weight,
        height = height,
        bmi = bmi,
        goal_weight = goal_weight
        )
    u.save()
