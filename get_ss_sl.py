def get_ss_sl(L):
    result = []
    
    for ele in L:
        if isinstance(ele, (tuple, set, list)):
            
            result.extend(get_ss_sl(ele))
        elif isinstance(ele, dict):
            
            result.extend(get_ss_sl(ele.keys()))
            result.extend(get_ss_sl(ele.values()))
        elif isinstance(ele, str) and ele.isnumeric():
            
            result.append(int(ele))  
        elif isinstance(ele, (int, float)):
            
            result.append(ele)
    
    result = list(set(result))
    sorted_result = sorted(result)
    
    if len(sorted_result) == 0:
        return "no numeric object"
    elif len(sorted_result) == 1:
        return "one numeric object", sorted_result
    else:
        return sorted_result[1], sorted_result[-2]

# Test the function with a mixed input
print(get_ss_sl([1, 2, {3, "utkarsh"}, {1: '1', 2: '2'}, [8, -8, 7.4], 0.02]))
