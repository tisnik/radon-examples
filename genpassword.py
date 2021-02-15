# taken from http://hovnokod.cz/1429 and slightly updated


def genpassword(wlc, maxchar, txt, List, verbose):
    word = ""
    i1 = i2 = i3 = i4 = i5 = i6 = i6 = i7 = i8 = i9 = i10 = i11 = i12 = i13 = i14 = i15 = 0
    txtfile = open(txt, 'w')

    i = 0
    mc = int(maxchar) - 1
    lword = [0]
    for i in range(mc):
        lword += [0]

    for i1 in range(len(wlc)):
        for i2 in range(len(wlc)):
            for i3 in range(len(wlc)):
                for i4 in range(len(wlc)):
                    for i5 in range(len(wlc)):
                        for i6 in range(len(wlc)):
                            for i7 in range(len(wlc)):
                                for i8 in range(len(wlc)):
                                    for i9 in range(len(wlc)):
                                        for i10 in range(len(wlc)):
                                            for i11 in range(len(wlc)):
                                                for i12 in range(len(wlc)):
                                                    for i13 in range(len(wlc)):
                                                        for i14 in range(len(wlc)):
                                                            for i15 in range(len(wlc)):
                                                                if int(maxchar) == 1:
                                                                    word = wlc[i15]
                                                                if int(maxchar) == 2:
                                                                    word = wlc[i14] + wlc[i15]
                                                                if int(maxchar) == 3:
                                                                    word = wlc[i13] + wlc[i14] + wlc[i15]  # noqa: E501

                                                                if int(maxchar) == 14:
                                                                    word = wlc[i1] + wlc[i2] \
                                                                        + wlc[i3] + wlc[i4] \
                                                                        + wlc[i5] + wlc[i6] \
                                                                        + wlc[i7] + wlc[i8] \
                                                                        + wlc[i9] + wlc[i10] \
                                                                        + wlc[i11] + wlc[i12] \
                                                                        + wlc[i13] + wlc[i14] \
                                                                        + wlc[i15]

                                                                if int(maxchar) == 15:
                                                                    word = wlc[i1] + wlc[i2] + wlc[i3] + wlc[i4] \
                                                                       + wlc[i5] + wlc[i6] + wlc[i7] + wlc[i8] + wlc[i9] \
                                                                       + wlc[i10] + wlc[i11] + wlc[i12] + wlc[i13] \
                                                                       + wlc[i14] + wlc[i15]

                                                                if int(verbose) == 1:
                                                                    print(word)

                                                                txtfile.writelines(word + "\n")

                                                                i = 0
                                                                end = 0
                                                                if int(List) == 1:
                                                                    for i in range(len(word)):
                                                                        lword[i] = "9"
                                                                    if str(lword) == str(list(word)):
                                                                        end = 1
                                                                 
                                                                if end == 1: break
                                                            if end == 1: break
                                                        if end == 1: break
                                                    if end == 1: break
                                                if end == 1: break
                                            if end == 1: break
                                        if end == 1: break
                                    if end == 1: break
                                if end == 1: break
                            if end == 1: break
                        if end == 1: break
                    if end == 1: break
                if end == 1: break
            if end == 1: break
        if end == 1 : break

    txtfile.close()
