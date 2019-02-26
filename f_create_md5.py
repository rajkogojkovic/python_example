from hashlib import md5
'''
function takes one input parameter and returns hexdigest value
'''
def create_md5(in_string):
    v_md5=md5()
    v_md5.update(in_string.encode())
    return v_md5.hexdigest()



