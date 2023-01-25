from random import shuffle

filename = "out.txt"
parsed = "gateway-cids.txt"

def parse_cids(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    cids = set()
    for l in lines:
        uri = l.split('"')[7]
        if uri[:6] == '/ipfs/':
            cid = uri.split('/')[2].split('?')[0].split('.')[0]

            if len(cid) >= len('QmenQRE3FGP6MXfbu8F59Dz7qEYHZWRCQ8xUFfiCziWCm') and \
                cid[:2] in ['Qm', 'ba']:
                cids.add(cid)

    cids = list(cids)
    shuffle(cids)
    return cids

def write_cids(filename, cids):
    f = open(filename, "w")
    f.writelines("%s\n" % c for c in cids)
    f.close()

cids = parse_cids(filename)
print(len(cids))
write_cids(parsed, cids)
