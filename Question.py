Operator_list=[]
Character_list=[]
Logical_Operator_list=[]
Condition_list=[]
def extract_list(list_):
    for item in list_:
        if type(item) is list:
            extract_list(item)
        elif item == "OR" or item == "AND":
            Logical_Operator_list.append(item)
        elif item == "<" or item == "==" or item == "!=":
            Operator_list.append(item)
        else:
            Character_list.append(item)

def deal_with_stack():
    while len(Character_list) >= 2:
        condition_string = ""
        if len(Operator_list)>=1:
            character = Character_list.pop(0)
            operator = Operator_list.pop(0)
            character2 = Character_list.pop(0)
            condition_string += f"{character} {operator} {character2}"
            print(condition_string)
            Condition_list.append(condition_string)
        print("Out of Operators")
    print(Condition_list)
    while len(Condition_list) >= 2:
        condition_string = ""
        logical = Logical_Operator_list.pop(0)
        condition1 = Condition_list.pop(0)
        print(condition1)
        condition2 = Condition_list.pop(0)
        print(condition2)
        condition_string += f"{condition1} {logical} {condition2}"
        Condition_list.insert(0, condition_string)

    return Condition_list.pop(0)





input_list = ["OR", ["<", "a", "b"], ["AND", ["==", "c", "d"], ["!=", "e", "f"]]]
extract_list(input_list)
print(Operator_list)
print(Character_list)
print(Logical_Operator_list)
final_string=deal_with_stack()
print(final_string)
