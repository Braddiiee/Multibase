
def adjust(original, result):

    length = len(original)

    if len(result) < length:
        additional = length - len(result)
        zeros = "0" * additional

        result_binary = zeros + result

        return result_binary