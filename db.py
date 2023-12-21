import sqlite3 as sq
async def db_start():
    db = sq.connect('project.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS files(file_id BLOB, caption TEXT)")
    db.commit()
    return db, cur

async def save_file_id(file_id, caption):
    db, cur = await db_start()
    cur.execute("INSERT INTO files (file_id, caption) VALUES (?, ?)", (file_id, caption))
    db.commit()
    db.close()

# async def get_file_ids():
#     db, cur = await db_start()
#     cur.execute("SELECT file_id FROM files")
#     file_ids = [result[0] for result in cur.fetchall()]
#     db.close()
#     return file_ids
#
# async def get_captions():
#     db, cur = await db_start()
#     cur.execute("SELECT caption FROM files")
#     captions = [result[0] for result in cur.fetchall()]
#     db.close()
#     return captions

async def get_latest_file_ids(limit=10):
    db, cur = await db_start()
    cur.execute("SELECT file_id FROM files ORDER BY timestamp DESC LIMIT ?", (limit,))
    file_ids = [result[0] for result in cur.fetchall()]
    db.close()
    return file_ids

async def get_latest_captions(limit=10):
    db, cur = await db_start()
    cur.execute("SELECT caption FROM files ORDER BY timestamp DESC LIMIT ?", (limit,))
    captions = [result[0] for result in cur.fetchall()]
    db.close()
    return captions
