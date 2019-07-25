
phone_no = input("Phone: ")
integers = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three', 
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
output = ""
for ch in phone_no:
    output += integers.get(ch, "!") + " "
print(output)
 