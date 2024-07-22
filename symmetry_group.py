def parity(permutation):
    """
    The input permutation is 1 row reprentation ,
    means that 1 is permuate to permutaiton[1] , 2 to permutaiton [2], tec.
    """
    orbitals=generate_orbital(permutation)
    n_orbital=len(orbitals)
    group_order=len(permutation)
    sign=group_order-n_orbital
    return sign
def orbital(permutation,element):
    """
    The define of the orbital is x \phi x , \phi^2 x ,\cdots ,\phi^N x 
    """
    orbital=[element]
    permute_result=permutation[element-1]
    while permute_result!=element:
        orbital.append(permute_result)
        permute_result=permutation[permute_result-1]
    return orbital
def generate_orbital(permutation):
    """ 
    Given permutation ,generate all its orbital
    """
    elements=set(permutation)
    orbitals=[]
    while len(elements)!=0:
        element=next(iter(elements)) ## get a member of set need better grammer.
        orbit=orbital(permutation,element)
        orbitals.append(orbit)
        elements-=set(orbit)
    return orbitals


