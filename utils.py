from select import select
from database.sqlitedbmain import qry


# qry.run("""
# CREATE TABLE user(
#     userid text,
#     fullname text,
#     email text,
#     phone text, 
#     address text,
#     city text,
#     username text,
#     password text  
# )
# """)

# qry.commit()

qry.run("""
        INSERT into user values(
            'userid', 'Adam', 'admin@site.com', '123456', 'aderess', 'city', 'username', 'pasw123'
        )
""")


qry.commit()

print(qry.run("SELECT * from user").getDict())