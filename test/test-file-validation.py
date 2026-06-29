from app.utils.file_validator import (
    is_valid_image,
    is_valid_document
)

print(is_valid_image(r"C:\Users\admin\OneDrive\Desktop\editable image of me.jpeg"))
print(is_valid_image(r"C:\Users\Public\Desktop\Grand Theft Auto V.lnk"))

# print(is_valid_document("resume.pdf"))
# print(is_valid_document("notes.txt"))