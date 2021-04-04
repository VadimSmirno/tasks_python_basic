def sort(cortege):
    for i in list(cortege):
        if isinstance(i, int) == False:  # лучше "if not isinstance(i, int)"
            return cortege
    return tuple(sorted(list(cortege)))


cortege = (1, 3, 4, 5, 7, 4, 3, 56, 64, 3, 4)
print(sort(cortege))

# зачёт!
