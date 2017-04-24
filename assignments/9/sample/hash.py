
from werkzeug.security import generate_password_hash, check_password_hash

t2 = generate_password_hash("dat310A9")

print(t2)

print(check_password_hash(t2, "Hans123"))
