from . import db
import json


def logMessage(request):
    msg = json.loads(request)
    print(msg)
    chat = msg['topic']
    print(chat)
    print(msg)
    if 'username' not in msg.keys() or 'message' not in msg.keys() or 'deviceID' not in msg.keys():
        raise json.decoder.JSONDecodeError(msg="invalid input", doc="", pos=0)
    database = db.get_db()
    updateUser(database, msg)

    auth = database.execute(
        'SELECT id FROM users WHERE clientID = ?', (msg['deviceID'],)
    ).fetchone()[0]
    message = msg['message']
    database.execute(
        'INSERT INTO messages (author_id, content, chatName) VALUES (?, ?, ?)',
        (auth, message, chat),
    )
    database.commit()
    return msg


def getMessages(chat):
    msg = json.loads(chat)
    print("huhuuuuuu")
    if 'chat' not in msg.keys():
        raise json.decoder.JSONDecodeError(msg="invalid input", doc="", pos=0)

    d = db.get_db()
    print("huuhu")
    messages = d.execute(
        'SELECT * FROM messages WHERE chatName = ?', (msg['chat'],)
    ).fetchall()
    result = []
    for message in messages:
        user = d.execute(
            'SELECT username FROM users WHERE id = ?', (message[1],)
        ).fetchone()

        result.append(
            {"username": user[0], "received": message[2].strftime("%Y-%m-%d %H:%M:%S"), "message": message[3]})
    return result


def updateUser(database, msg):
    clientID = msg['deviceID']
    user = database.execute(
        'SELECT username, clientID FROM users WHERE clientID = ?', (clientID,)
    ).fetchone()
    if user is None:
        database.execute(
            'INSERT INTO users (username, clientID) VALUES (?,?)',
            (msg['username'], clientID),
        )
        database.commit()
    elif user != msg['username']:
        database.execute(
            'UPDATE users SET username = ? WHERE clientID = ?',
            (msg['username'], clientID),
        )
        database.commit()
