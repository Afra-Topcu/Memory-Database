from sys import argv

def TABLE(table): #For each table
    columnlength = []
    for i in range(len(table["tablecolumn"])):  # Iterate through the number of columns
        lmax = len(table["tablecolumn"][i]) # Get the length of the column
        for x in table["tabledata"]:  #Check all
            lmax = max(lmax, len(x[i]))  # Find the maximum length in each column
        columnlength.append(lmax)
    #Make table
    s = "-"
    for i in columnlength:
        print(f"+{s.ljust(i + 2, '-')}", end="-")
    print("+")
    for c in range(len(table["tablecolumn"])):
        print(f"| {table['tablecolumn'][c].ljust(columnlength[c] + 1, ' ')}", end=" ")
    print("|")
    for i in columnlength:
        print(f"+{s.ljust(i + 2, '-')}", end="-")
    print("+")
    for b in range(len(table["tabledata"])):
        for c in range(len(table["tablecolumn"])):
            print(f"| {table['tabledata'][b][c].ljust(columnlength[c] + 1, ' ')}", end=' ')
        print(f"|")
    for i in columnlength:
        print(f"+{s.ljust(i + 2, '-')}", end="-")
    print("+")

def CREATE_TABLE(lines,table):
    print("###################### CREATE #########################")
    table0=lines.split(" ")
    table["tablename"]=table0[1] #Get table names
    columns=table0[-1] #Get column names
    table["tablecolumn"]=columns.split(",")
    print(f"Table '{table['tablename']}' created with columns: {table['tablecolumn']}")

def INSERT(lines,table1,table2,table3,table4,table5):
    print("###################### INSERT #########################")
    line=lines.replace("INSERT ","")
    table_name = line[0:line.index(" ")] #Extract the table name
    line= line.replace(table_name, "").lstrip() #Get the data
    columns =line.split(",")
    columnstuple=tuple(columns)
    #Find which table to insert
    try:
        if table_name == table1["tablename"]:
            table=table1
        elif table_name == table2["tablename"]:
            table=table2
        elif table_name == table3["tablename"]:
            table=table3
        elif table_name == table4["tablename"]:
            table=table4
        elif table_name == table5["tablename"]:
            table=table5
        else:
            raise ValueError (f"Table {table_name} not found")
    except ValueError:
        print(f"Table {table_name} not found")
        print(f"Inserted into '{table_name}': {columnstuple}")
        return
    #Add datas to the table
    table["tabledata"].append(columns)
    print(f"Inserted into '{table_name}': {columnstuple}")
    print()
    print("Table:",table_name)
    TABLE(table) #For making a table we are calling table function

def SELECT(lines, table1, table2,table3,table4,table5):
    print("###################### SELECT #########################")
    line = lines.replace("SELECT ", "")
    left, right = line.split("WHERE")
    left = left.strip()
    table_name, columns = left.split(" ", 1) #Find the table name and column
    columns = [colum.strip() for colum in columns.split(",")]
    right = right.strip().strip("{}")
    #Find the conditions
    conditions = {}
    for a in right.split(","):
        key, value = a.split(":")
        conditions[key.strip().strip('"')] = value.strip().strip('"')
        key=key.strip().strip('"')
    #Find the table
    try:
        if table_name == table1["tablename"]:
            table = table1
        elif table_name == table2["tablename"]:
            table = table2
        elif table_name == table3["tablename"]:
            table = table3
        elif table_name == table4["tablename"]:
            table = table4
        elif table_name == table5["tablename"]:
            table = table5
        else:
            raise ValueError (f"Table '{table_name}' not found")
    except ValueError:
        print(f"Table {table_name} not found")
        print("Condition:", conditions)
        print(f"Select result from '{table_name}':", end=" ")
        print("None")
        return
    if "*" in columns: #If * select all columns
        columns=table1["tablecolumn"]
    column1=[]
    #Find the indices of the selected columns
    try:
        for column in columns:
            if column in table["tablecolumn"]:
                column1.append(table["tablecolumn"].index(column))
            else:
                raise ValueError (f"Column {column} does not exist")
    except ValueError:
            print(f"Column {column} does not exist")
            print("Condition:", conditions)
            print(f"Select result from '{table_name}':",end=" ")
            print("None")
            return
    try:
        if key not in table["tablecolumn"]:
            raise ValueError (f"Column {key} does not exist")
    except ValueError:
        print(f"Column {key} does not exist")
        print("Condition:", conditions)
        print(f"Select result from '{table_name}':",end=" ")
        print("None")
        return
    # Select data that matches conditions
    results = []
    for row in table["tabledata"]:
        rowdict = dict(zip(table["tablecolumn"], row))  #Match row to column names
        if all(rowdict.get(key) == value for key, value in conditions.items()):  #Check the conditions
            results.append(tuple(row[index] for index in column1))  #Add selected columns
    print("Condition:", conditions)
    print(f"Select result from '{table_name}': {results}")
    return results

def UPDATE(lines, table1,table2,table3,table4,table5):
    print("###################### UPDATE #########################")
    line = lines.replace("UPDATE ", "")
    left, right = line.split("WHERE")
    table_name, left2 = left.split(" ", 1) #Seperate the table name and update values
    print(f"Updated '{table_name}' with {left2}where{right}".replace('"',"'"))
    #Find the table
    try:
        if table_name ==table1["tablename"]:
            table=table1
        elif table_name ==table2["tablename"]:
            table=table2
        elif table_name ==table3["tablename"]:
            table=table3
        elif table_name ==table4["tablename"]:
            table=table4
        elif table_name ==table5["tablename"]:
            table=table5
        else:
            raise ValueError (f"Table '{table_name}' not found")
    except ValueError:
        print(f"Table {table_name} not found")
        print("0 rows updated.")
        return
    #Seperate conditions
    right=right.strip().strip("{}").strip('""')
    column2,data2 = right.split(" ", 1)
    column2=column2.strip(":").strip('""')
    data2=data2.strip('""')
    #Seperate update things
    left2=left2.strip().strip("{}").strip('""')
    column1,data1 = left2.split(" ", 1)
    data1=data1.strip('""')
    column1=column1.strip('""').strip(":")
    column1=column1.strip('""')
    a=0 #Counts the number of rows updated
    #Check if the target columns exist in the table
    try:
        if column1 in table["tablecolumn"]:
            index=table["tablecolumn"].index(column1) #Find column indices
        elif column1 not in table["tablecolumn"]:
            raise ValueError(f"Column {column1} does not exist")
    except ValueError:
            print(f"Column {column1} does not exist")
            print("0 rows updated.")
            print()
            TABLE(table) #For making a table we are calling table function
            return
    # Check if the target columns exist in the table
    try:
        # Find column indices
        if column2 in table["tablecolumn"]:
            index1 = table["tablecolumn"].index(column2)
            #Update rows
            for x in table["tabledata"]:
                if x[index1] == data2:
                    x[index] = data1
                    a += 1
            print(f"{a} rows updated.")
            print()
            TABLE(table) #For making a table we are calling table function
        if column2 not in table["tablecolumn"]:
            raise ValueError(f"Column {column2} does not exist")
    except ValueError:
        print(f"Column {column2} does not exist")
        print("0 rows updated.")
        print()
        TABLE(table) #For making a table we are calling table function
        return

def DELETE(lines,table1,table2,table3,table4,table5):
    print("###################### DELETE #########################")
    line = lines.replace("DELETE ","")
    left, right = line.split("WHERE")
    table_name=left.strip() #Extract the table name
    print(f"Deleted from '{table_name}' where{right}".replace('"',"'"))
    #Find the table
    try:
        if table_name ==table1["tablename"]:
            table=table1
        elif table_name ==table2["tablename"]:
            table=table2
        elif table_name ==table3["tablename"]:
            table=table3
        elif table_name ==table4["tablename"]:
            table=table4
        elif table_name ==table5["tablename"]:
            table=table5
        else:
            raise ValueError (f"Table '{table_name}' not found")
    except ValueError:
        print(f"Table {table_name} not found")
        print("0 rows deleted.")
        return
    a =0 # Counts the number of rows that deleted
    #If nothing is written after WHERE delete all datas
    if not right.strip():
        a = len(table["tabledata"])
        table["tabledata"].clear()  #Delete all row
        print(f"{a} rows deleted.")
        print()
        TABLE(table) #For making a table call table function
        return
    # Parse the condition
    right=right.strip().strip("{}").strip('""')
    column,data = right.split(" ", 1)
    column=column.strip(":").strip('""')
    #Check if the column exist
    try:
        if column not in table["tablecolumn"]:
            raise ValueError(f"Column {column} does not exist")
    except ValueError:
        print(f"Column {column} does not exist")
        print("0 rows deleted.")
        print()
        TABLE(table) #For making a table we are calling table function
        return
    #Find the indices
    if table_name in table["tablename"]:
        if column in table["tablecolumn"]:
            index=table["tablecolumn"].index(column)
            for x in table["tabledata"]:
                if x[index]==data:
                    x[index]=data
                    table["tabledata"].remove(x)
                    a+=1
    print(f"{a} rows deleted.")
    print()
    TABLE(table) #For making a table we are calling table function

def COUNT(lines,table1,table2,table3,table4,table5):
    print("###################### COUNT #########################")
    line = lines.replace("COUNT ", "")
    left, right = line.split("WHERE")
    table_name=left.strip() #Find the table name
    #Find the table
    try:
        if table_name ==table1["tablename"]:
            table=table1
        elif table_name ==table2["tablename"]:
            table=table2
        elif table_name ==table3["tablename"]:
            table=table3
        elif table_name ==table4["tablename"]:
            table=table4
        elif table_name ==table5["tablename"]:
            table=table5
        else:
            raise ValueError (f"Table '{table_name}' not found")
    except ValueError:
        print(f"Table {table_name} not found")
        print(f"Total number of entries in '{table_name}' is 0")
        return
    # If you saw "*" count all rows
    if "*" in right:
        a=len(table["tabledata"])
        print(f"Count: {a}")
        print(f"Total number of entries in '{table_name}' is {a}")
        return
    else:
        right = right.strip().strip("{}").strip('""')
        column, data = right.split(" ", 1)
        column = column.strip(":").strip('""')
        data = data.strip('""')
    #Check if the column exist
    try:
        if column not in table["tablecolumn"]:
            raise ValueError(f"Column {column} does not exist")
    except ValueError:
        print(f"Column {column} does not exist")
        print(f"Total number of entries in '{table_name}' is 0")
        return
    a=0 #Counts matching rows
    if table_name in table["tablename"]:
        if column in table["tablecolumn"]:
            index=table["tablecolumn"].index(column)
            for x in table["tabledata"]:
                if x[index]==data:
                    x[index]=data
                    a+=1
    print(f"Count: {a}")
    print(f"Total number of entries in '{table_name}' is {a}")

def JOIN(lines,table1,table2,table3,table4,table5):
    print("####################### JOIN ##########################")
    line = lines.replace("JOIN ", "")
    left, right = line.split("ON")
    tablex_name,tabley_name = left.split(",") #Find table names
    right=right.strip()
    tablex_name=tablex_name.strip()
    tabley_name=tabley_name.strip()
    #Find first table
    try:
        if tablex_name==table1["tablename"]:
            table1x=table1
        elif tablex_name==table2["tablename"]:
            table1x=table2
        elif tablex_name==table3["tablename"]:
            table1x=table3
        elif tablex_name==table4["tablename"]:
            table1x=table4
        elif tablex_name==table5["tablename"]:
            table1x=table5
        else:
            raise ValueError (f"Joın tables {tablex_name} and {tabley_name}")
    except ValueError:
        print(f"Joın tables {tablex_name} and {tabley_name} ")
        print(f"Table {tablex_name} does not exist")
        return
    #Find second table
    try:
        if tabley_name==table1["tablename"]:
            table2y=table1
        elif tabley_name==table2["tablename"]:
            table2y=table2
        elif tabley_name==table3["tablename"]:
            table2y=table3
        elif tabley_name==table4["tablename"]:
            table2y=table4
        elif tabley_name==table5["tablename"]:
            table2y=table5
        else:
            raise ValueError (f"Joın tables {tablex_name} and {tabley_name}")
    except ValueError:
        print(f"Joın tables {tablex_name} and {tabley_name} ")
        print(f"Table {tabley_name} does not exist")
        return
    #Make sure the join column exist in both tables
    try:
        if right not in table1x["tablecolumn"]:
            raise ValueError(f"Joın tables {tablex_name} and {tabley_name}")
    except ValueError:
        print(f"Joın tables {tablex_name} and {tabley_name}")
        print(f"Column {right} does not exist")
        return
    try:
        if right not in table2y["tablecolumn"]:
            raise ValueError(f"Joın tables {tablex_name} and {tabley_name}")
    except ValueError:
        print(f"Joın tables {tablex_name} and {tabley_name}")
        print(f"Column {right} does not exist")
        return
    #Find indices
    index_table1x=table1x["tablecolumn"].index(right)
    index_table2y=table2y["tablecolumn"].index(right)
    #Merge tables
    join=[]
    for leftrow in table1x["tabledata"]:
        for rightrow in table2y["tabledata"]:
            if leftrow[index_table1x] == rightrow[index_table2y]:
                join_row=leftrow+rightrow
                join.append(join_row)
    #Find the column indices
    joinedcolumn=table1x["tablecolumn"]+table2y["tablecolumn"]
    print(f"Joın tables {table1x['tablename']} and {table2y['tablename']}")
    print(f"Join result ({len(join)} rows):")
    print()
    #Make the join table
    columnlength = []
    for i in range(len(joinedcolumn)):
        lmax = len(joinedcolumn[i])
        for row in join:
            lmax = max(lmax, len(row[i]))
        columnlength.append(lmax)
    s = "-"
    for i in columnlength:
        print(f"+{s.ljust(i + 2, '-')}", end="-")
    print("+")
    for c in range(len(joinedcolumn)):
        print(f"| {joinedcolumn[c].ljust(columnlength[c] + 1, ' ')}", end=" ")
    print("|")
    for i in columnlength:
        print(f"+{s.ljust(i + 2, '-')}", end="-")
    print("+")
    for row in join:
        for c in range(len(joinedcolumn)):
            print(f"| {row[c].ljust(columnlength[c] + 1, ' ')}", end=" ")
        print(f"|")
    for i in columnlength:
        print(f"+{s.ljust(i + 2, '-')}", end="-")
    print("+")

def main():
    with open(argv[1],"r") as f_in:
        f_str=f_in.read()
        f_str1=f_str.split("\n")
        table1={
            "tablename": "",
            "tablecolumn": [],
            "tabledata": []
            }
        table2={
            "tablename": "",
            "tablecolumn": [],
            "tabledata": []
        }
        table3={
            "tablename": "",
            "tablecolumn": [],
            "tabledata": []
        }
        table4={
            "tablename": "",
            "tablecolumn": [],
            "tabledata": []
        }
        table5={
            "tablename": "",
            "tablecolumn": [],
            "tabledata": []
        }
        tablenumber=0
        for x in f_str1:
            if x.startswith("CREATE_TABLE") and tablenumber==0:
                CREATE_TABLE(x,table1)
                tablenumber+=1
                print("#######################################################")
                print()
            elif x.startswith("CREATE_TABLE") and  tablenumber==1:
                CREATE_TABLE(x,table2)
                tablenumber+=1
                print("#######################################################")
                print()
            elif x.startswith("CREATE_TABLE") and tablenumber==2:
                CREATE_TABLE(x,table3)
                tablenumber+=1
                print("#######################################################")
                print()
            elif x.startswith("CREATE_TABLE") and tablenumber==3:
                CREATE_TABLE(x,table4)
                tablenumber+=1
                print("#######################################################")
                print()
            elif x.startswith("CREATE_TABLE") and tablenumber==4:
                CREATE_TABLE(x,table5)
                tablenumber+=1
                print("#######################################################")
                print()
            elif x.startswith("INSERT"):
                INSERT(x,table1,table2,table3,table4,table5)
                print("#######################################################")
                print()
            elif x.startswith("SELECT"):
                SELECT(x,table1,table2,table3,table4,table5)
                print("#######################################################")
                print()
            elif x.startswith("UPDATE"):
                UPDATE(x,table1,table2,table3,table4,table5)
                print("#######################################################")
                print()
            elif x.startswith("DELETE"):
                DELETE(x,table1,table2,table3,table4,table5)
                print("#######################################################")
                print()
            elif x.startswith("COUNT"):
                COUNT(x,table1,table2,table3,table4,table5)
                print("#######################################################")
                print()
            elif x.startswith("JOIN"):
                JOIN(x,table1,table2,table3,table4,table5)
                print("#######################################################")
                print()

if __name__ == "__main__":
    main()