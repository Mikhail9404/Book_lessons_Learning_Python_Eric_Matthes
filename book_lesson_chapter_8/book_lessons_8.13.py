def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile_1 = build_profile('mikhail', 'kuznetsov', country='Russia', city='St.Petersburg', programm_lang='Python')
print(user_profile_1)