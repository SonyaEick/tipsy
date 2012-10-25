"""
seed.py
"""
import model
db = model.connect_db()

# a=model.call_users(db, None)
# print a 

# rem= model.remove_task(db, 3)
# rem= model.remove_task(db, 4)
# rem= model.remove_task(db, 6)
# rem= model.remove_task(db, 8)
# rem= model.remove_task(db, 10)
# rem= model.remove_user(db, 6)
# print rem 

# rem= model.remove_user(db, 5)
# rem= model.remove_user(db, 6)
# rem= model.remove_user(db, 7)
# rem= model.remove_user(db, 8)
# rem= model.remove_user(db, 9)
# rem= model.remove_user(db, 10)
# rem= model.remove_user(db, 11)
# rem= model.remove_user(db, 2)
# rem= model.remove_user(db, 3)
# print rem 

# user_id = model.new_user(db, "when@issonyabusy.com", 
#                             "Pineapple", "SonyaEick")
# task = model.new_task(db, "Use the BART", user_id)

# dict1= dict() 
# dict1= model.get_user(db, 5) 
# print dict1

# a= model.complete_task(db, 1)
# print a

# a=model.get_tasks(db, None)
# print a

# a=model.get_task( db, 7)
# print a