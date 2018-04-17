#method 1, n square
def find_length(input_string, char_set):
    output = len(input_string)
    k = len(char_set)
    for start in range(len(input_string)):
        for end in range(start+1,len(input_string)):
            sub_string = input_string[start,end+1]
            c = 0
            for char in char_set:
                if char in sub_string:
                    c += 1
            if c == k:
                if len(sub_string) < output:
                   output = len(sub_string)
    return(output+1)

#method 2, linear
def find_length(input_string, char_set):
    #get the length of the input_string
    n = len(input_string)
    #store the first position of each char in char set as the first matching substring on the left to start
    p = {}
    for char in char_set:
        first_position = input_string.find(char)
        #if there is no match, it will return -1 and means we cannot find any matching substring
        if first_position < 0:
            return("Not Found")
        p[char] = first_position
    #store length of the first matching substring and then moving the window to the right
    output = max(p.values()) - min(p.values()) + 1
    #we find the left side of the substring and move it to the right
    left_char = min(p, key=p.get)
    left_position = p[left_char]
    next_position = input_string[left_position+1:].find(left_char)
    #shift the current left positon to the actual input_string position of the char we are going to move
    new_left_position =  next_position + left_position + 1
    #we continue moving it until there is no more match on the right hand side
    while next_position > 0:
        #recalculate the left char and left position and move until there no match on the right hand side
        p[left_char] = new_left_position
        #compare the length against current smallest value
        if output > max(p.values()) - min(p.values()) + 1:
            output = max(p.values()) - min(p.values()) + 1
        #repeat, same thing as line 15 - 19
        left_char = min(p, key=p.get)
        left_position = p[left_char]
        next_position = input_string[left_position+1:].find(left_char)
        new_left_position =  next_position + left_position + 1
    print(output)
    return(output)

find_length('facbserwrtruhndfhfgjtdfasascdgfdyh', set(['c','d','s']))
