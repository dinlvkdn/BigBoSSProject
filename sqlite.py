import sqlite3 as sq

async def db_start():
    global db, cur
    #
    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, role TEXT)")

    db.commit()

async def create_profile(user_id, role=None):
    user = cur.execute("SELECT 1 FROM users WHERE user_id == ?", (user_id,)).fetchone()
    if not user:
        cur.execute("INSERT INTO users (user_id, role) VALUES (?, ?)", (user_id, role))
        db.commit()
    else:
        cur.execute("UPDATE users SET role = ? WHERE user_id = ?", (role, user_id))
        db.commit()




async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE users SET role = '{}' WHERE user_id = '{}'".format(data['role'], user_id))
        db.commit()



async def get_role_and_id(user_id):
    user_data = cur.execute("SELECT role FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if user_data:
        role = user_data[0]
        return role
    else:
        return None, None



async def get_user_id_by_role(role):
    user_data = cur.execute("SELECT user_id FROM users WHERE role = ?", (role,)).fetchone()
    if user_data:
        user_id = user_data[0]
        return user_id
    else:
        return None



async def send_document_to_role(role, file_id):
    team_members = cur.execute("SELECT user_id FROM users WHERE role = ?", (role,)).fetchall()
    for member_id in team_members:
        try:
            await dp.bot.send_document(member_id[0], file_id)
        except Exception as e:
            print(f"Error sending document to {member_id[0]}: {e}")