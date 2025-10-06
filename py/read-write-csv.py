import csv

def writeFile(filename, data, headers):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)     # write column names first
        writer.writerows(data)       # write rows of data


def readFile(filename):
    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def convert(value, from_base, to_base):

    num = int(value, from_base)

    def to_bin(v): return bin(num)

    # switch = {
    #     "bin": to_bin,
    #     "oct": to_oct,
    #     "hex": to_hex,
    #     "chr": to_chr,
    #     "ord": to_ord,
    #     "int": int
    # }

    # try:
        # return switch[to_type](value)
    # except Exception as e:
    #     return f"Error: {e}"

