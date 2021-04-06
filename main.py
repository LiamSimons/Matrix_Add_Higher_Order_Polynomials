indexes = []
extra_col = []


def make_pol(orde, depth):
    extra = orde - 1
    i = 1
    while i < orde:
        add = (orde - i) * depth
        extra = extra + add
        i = i + 1

    extra_col.append(extra)
    # print("Extra: " + str(extra))

    p = 1
    while p < orde:
        indexes.append(2+p)
        p = p + 1

    f = 2
    add = 0
    while f <= orde: #f=1
        j = 1
        while j <= (f-1)*depth: #j<=3
            new_index = 2 + orde + add
            indexes.append(new_index)
            add = add + 1
            j = j + 1
        f = f + 1


def check():
    if len(indexes) == extra_col[0]:
        print("Test 1 'PASSED': right amount of extra columns added.")
    else:
        print("Test 1 'FAILED': wrong amount of columns added, got: "
              + str(len(indexes)) + " - but expected: " + str(extra_col))

    test_2 = True
    for i in indexes:
        if i != indexes.index(i) + 3:
            test_2 = False
            print("At index: " + str(i))
    if test_2:
        print("Test 2 'PASSED': indexes are correct.")
    else:
        print("Test 2 'FAILED': indexes are not correct see index before.")


make_pol(27, 5)
check()