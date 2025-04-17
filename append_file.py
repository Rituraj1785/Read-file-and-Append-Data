'''n=input("Enter text to write to the file: ")
print(n)'''


'''file3=open("my_file.txt", "r+")
writing_file=file3.write("Data successfully written in Output.txt.")
file3.close()


file3=open("Output.txt", "a")
appending_file=file3.write("Enter additional text to append: Learning file handling in Python.")
file3.close()

file3=open("Output.txt","r+")
read1_file=file3.read()
print(read1_file)
file3.close()

file3=open("Output.txt", "r+")
write_file=file3.write("Final content of Output.txt:")
print(write_file)
file3.close()'''

n=input("Enter text to write to the file: ")
with open("Output.txt", "w") as file3:
    file3.write(n + "\n")
    print("Data successfully written to output.txt.\n")
    file3.close()

append_data=input("Enter additional text to append: ")
with open("Output.txt", "a") as file3:
    file3.write(append_data + "\n")
    print("Data successfully appended.\n")
    file3.close()

print("Final content of output.txt: ")
with open("Output.txt", "r") as file3:
    print(file3.read())
    file3.close()


