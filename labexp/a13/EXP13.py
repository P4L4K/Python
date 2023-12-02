def extract_text(input_file_path):
    try:
        input_file=open(input_file_path)
        text=input_file.read()
        input_file.close()
        text=list(set(text.split()))
        text.sort()
        print(text)
        text="\n".join(text)
        return text
    except:
        print("file not found")
        return ""
def writing_text(output_file_words,words):
    output_file=open(output_file_words,"w")
    output_file.write(words)
    output_file.close()

#calling function
input_file_path=input("Enter input file path: ")
output_file_path=input("ENTER OUTPUT FILE PATH:")
writing_text(output_file_path,extract_text(input_file_path))


"""text.sort()
for i in text:
    if text.count(i)>1:
        while(text.count(i)!=1):
            text.remove(i)
"""

