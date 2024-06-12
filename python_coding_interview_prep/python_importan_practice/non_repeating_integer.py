def find_first_unique(lst):
    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i],(count,order))
    counts = counts.fromkeys(lst, (0,len(lst)))
    order = 0
    for ele in lst:
        # counts[ele][0] += 1  # Incrementing for every repitition
        # counts[ele][1] = order
        counts[ele] = (counts[ele][0]+1 , order)
        order += 1 # increment order
    answer = None
    answer_key = None
    # filter non-repeating with least order
    for ele in lst:
        if (counts[ele][0] is 1) and (answer is None):
            answer = counts[ele]
            answer_key = ele
        elif answer is None:
            continue
        elif (counts[ele][0] is 1) and (counts[ele][1] < answer[1]):
            answer = counts[ele]
            answer_key = ele
    return answer_key


print(find_first_unique([1, 1, 1, 2]))