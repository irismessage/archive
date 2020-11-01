#import periodictable

elements_list = ["H", "He"]
elements = {"Hydrogen": "H", "Helium": "He"}

def write_from(target, parts, progress=""):
    for arg in [target, parts, progress]:
        arg = arg.lower()
        
    if progress == target:
        return True
    
    needed = target - progress
    for part in parts:
        if needed[:len(part)] == part:
            progress += part
            return write_from(target, parts, progress)
        
#test
print(write_from("hehe", elements_list)