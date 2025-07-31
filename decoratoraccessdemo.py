def require_admin(func):
    def wrapper(user_role,*agrs, **kwargs):
        if user_role != 'admin':
            print("❌ Access denied.")
            return
        return func(user_role,*agrs, **kwargs)
    return wrapper

@require_admin
def delete_user(user_role,user_id):
    print(f"User {user_id} deleted.")

delete_user("guest",101)
delete_user("admin",101)