import s_taper
from s_taper.consts import *

s = {
    "user_id": INT + KEY,
    "rep": TEXT
}

users = s_taper.Taper("users", "datads.db").create_table(s)
