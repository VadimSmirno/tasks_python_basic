def sort(cortege):
    for i in list(cortege):
        if isinstance(i, float) == True:  # TODO, лучше "if isinstance(i, float)". Но возможно, стоит проверять int?
            return cortege

    lst = sorted(list(cortege))
    return tuple(lst)


cortege = (1,3,4,5,7,4,3,5.2,64,3,4)
print (sort(cortege))