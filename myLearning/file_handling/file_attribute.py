note_file = open("notes.txt","w")

print("name",note_file.name)
print("mode",note_file.mode)
print("readable",note_file.readable())
print("writable",note_file.writable())
print("is closed",note_file.closed)

note_file.close()
print("is closed",note_file.closed)