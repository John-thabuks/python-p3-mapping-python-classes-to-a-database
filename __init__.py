# from config import CONN, CURSOR
import sqlite3

CONN = sqlite3.connect("db/music.db")
CURSOR = CONN.cursor()