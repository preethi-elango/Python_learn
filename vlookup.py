#!/usr/bin/python

user_input=input("Enter the PMIDs:")
PMID_list=user_input.split(",")

output=open("outfile.csv","w")
output.write("PMID,Link\n")

for pmid in PMID_list:
    ID="PMID: " + pmid
    with open("DataFile.csv","r") as DF:
        count=0
        for line in DF:
            line=line.rstrip()
            temp_arr=line.split(",")
            if ID == temp_arr[0]:
                out=ID+","+temp_arr[2]+"\n"
                output.write(out)
            temp_arr.clear()
            count+=1
    DF.close()
output.close()

