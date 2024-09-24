def count_texts(L):
    result = []
    
    for element in L:
        if isinstance(element, (list, tuple, set)):
            result.append(count_texts(list(element)))  
        elif isinstance(element, str):
            
            if not any(vowel in element for vowel in 'aeiou'):
                result.append(element)  
            else:
               
                vowel_count = {vowel: element.count(vowel) for vowel in 'aeiou'}
               
                if len(set(vowel_count.values())) == 1 and list(vowel_count.values())[0] > 0:
                    result.append(element)
    
    return len(result)

print(count_texts(["abcde", 123, ("sas", {}), {"bcdei", "aeiouu"}]))  
