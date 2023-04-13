

def check_two_files(a, b):
    with open(a) as file_a:
        lines_a = file_a.readlines()
    with open(b) as file_b:
        lines_b = file_b.readlines()

   
    print(lines_a[0] == lines_b[0])

    for i in range(len(lines_a)):
        if lines_a[i] == lines_b[i]:
            continue
        
        else:
            print("sth wrong")

check_two_files("./compress_test2.tsv", "./compress_test2_back.tsv")
