from src.v1.layout import DOCUMENT

payload = "PRINT\nGUIA 5\nPARA Churute\n* texto 5\n* text 22\n* text 1"

data = DOCUMENT.message_to_print(payload)
print(data)