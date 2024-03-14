def all_cap_if_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(all_cap_if_long('nug'))