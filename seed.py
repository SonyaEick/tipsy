"""
seed.py
"""
import model
db = model.connect_db()

# user_id = model.new_user(db, "onceuponatimeforever@gmail.com", 
#                             "Chocolates", "SusanTan")
# task = model.new_task(db, "Use the BART", user_id)

# dict1= dict() 
# dict1= model.get_user(db, 5) 
# print dict1

a= model.complete_task(db, 1)
a= model.complete_task(db, 2)
a= model.complete_task(db, 3)
a= model.complete_task(db, 4)
a= model.complete_task(db, 5)
a= model.complete_task(db, 6)
a= model.complete_task(db, 7)

a=model.get_tasks(db, None)
print a

# a=model.get_task( db, 7)
# print a