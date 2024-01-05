def sum(s1,m1,s2,m2):

    s=s1*m2 + m1*s2
    m=m1*m2

    return s,m


def mul(s1,m1,s2,m2):

    s=s1*s2
    m=m1*m2

    return s,m


def fraction_to_number(s1,m1):
    res=s1/m1
    return res



res_mul=mul(2,5,6,8)
print(res_mul)

res_sum=sum(7,2,3,5)
print(res_sum)