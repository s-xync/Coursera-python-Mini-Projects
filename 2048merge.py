"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result_list=zero_remover(line)
    result_list=number_merger(result_list)
    return result_list
def zero_remover(line):
    """
    Removes zeros from the line
    """
    result_list=[]
# For making a list with only non-zero numbers
    for index in range(0,len(line)):
        if line[index]!=0:
            result_list.append(line[index])
# Resizing the list created list into the size of ninput list line
    for index in range(len(list(result_list)),len(line)):
        result_list.append(0)
    return result_list
def number_merger(line):
    """
    merges numbers if any
    """
    result_list=[]
# Merging any two adjacent numbers appending them to resulting list
    index=0
    while index<len(line):
        if index==len(line)-1:
            result_list.append(line[index])
            break
        elif line[index]==line[index+1]:
            result_list.append(2*line[index])
            index+=2
        else:
            result_list.append(line[index])
            index+=1
# Resizing the list created list into the size of ninput list line
    for index in range(len(list(result_list)),len(line)):
        result_list.append(0)
    return result_list
            
