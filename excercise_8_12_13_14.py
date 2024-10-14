# excercise 8_12_13_14

def make_sandwich(*sadwich):
    """print a summary about the sandwich ordered"""
    print("making sandwich:")
    print(f"{sadwich}")

make_sandwich('beef', 'chicken','cheese')

def user_profile(first, last, **user_info):
    """build a profile of yourself"""
    user_info['first']= first
    user_info['last']= last
    return user_info

ahmed_user = user_profile('ahmed','helmy',age=35, height= 180, nationality= 'Egyptian')
print(ahmed_user)

def make_car(model_name,manufacturer_name,**kwargs):
    """store information about a car in a dictionary"""
    kwargs['model']= model_name
    kwargs['Manufacturer']= manufacturer_name
    return  kwargs

car = make_car('c300','mercedes',color= 'blue',optional_feature= True)
print(car)
