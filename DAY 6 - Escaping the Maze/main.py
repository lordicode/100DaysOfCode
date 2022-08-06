def my_function():
    print("This was done through the reeborg site!")
    f = open('robot_diagram.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

my_function()
