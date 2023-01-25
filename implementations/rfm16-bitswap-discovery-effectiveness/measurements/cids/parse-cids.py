import random

"""
In file wantlist.json.2022-08-10T00_20_50+02_00, there are 22440081 CIDs requested,
including 5245888 distinct ones.
"""


def parse_cids(filename):
    f = open(filename, "r")

    lines = f.readlines()
    f.close()

    cids_set = set()

    cids_at_next_line = False
    for l in lines:
        if "cids" in l:
            cids_at_next_line = True
        elif cids_at_next_line:
            if "".join(l.split()) == "]":
                cids_at_next_line = False
            else:
                cids_set.add(l.split('"')[1])

    cids = list(cids_set)
    random.shuffle(cids)
    return cids


def write_cids(filename, cids):
    f = open(filename, "w")
    f.writelines("%s\n" % c for c in cids)
    f.close()


filename = "wantlist.json.2022-08-10T00_20_50+02_00"
# filename = "short.json"

cids = parse_cids(filename)
write_cids("cids.txt", cids)

