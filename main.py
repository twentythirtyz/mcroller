from modules.a import is_admin

# Give the variable a distinct name like 'has_admin' or 'admin_status'
admin_status = is_admin()

def main():
    if admin_status:
        print("Welcome admin")
    else:
        print("Welcome user")

if __name__ == "__main__":
    main()