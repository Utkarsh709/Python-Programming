def count1(string, sub_string, boolean):
    if sub_string == "" and boolean:
        return len(string)
    elif sub_string == "" and not boolean:
        return len(string) + 1
    elif sub_string == " ":
        return 0
    elif sub_string != " " and not boolean:
        count_f = 0
        sub_len = len(sub_string)
        i = 0
        while i <= len(string) - sub_len:
            if string[i:i + sub_len] == sub_string:
                count_f += 1
                i += sub_len  # Move past the current match
            else:
                i += 1
        return count_f
    elif sub_string != " " and boolean:
        return len(sub_string) + 1

# Test the function
print(count1("sggs", "gg", False))



















