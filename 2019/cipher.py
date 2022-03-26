def main(sa):
    sb = ""
    # pairs = set()

    for i in range(len(sa)):
        # pairs.add((sa[i], sb[i], ord(sa[i]) - ord(sb[i])))
        if sa[i] == " ":
            sb += sa[i]
        elif ord(sa[i]) <= ord("m"):
            sb += chr(ord(sa[i])+12)
        else:
            sb += chr(ord(sa[i])-14)

    # pairs = list(pairs)
    # pairs.sort(key = lambda t: t[0])
    # for p in pairs:
    #     print(p)

    return sb


if __name__ == "__main__":
    print(main(input()))
