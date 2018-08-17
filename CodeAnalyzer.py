import UtilFunctions as uf

# open a file and read it
file_path = input("Enter destination file name\n")  # D:\Programming\Python\CSSourceCodeAnalyzer\Sample.cs
target_file = open(file_path, "r")
file_contents = target_file.read()
target_file.close()

operands, operators = uf.getMetrics(file_contents)

print(operands)
print(operators)
