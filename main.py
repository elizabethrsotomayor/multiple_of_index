def multiple_of_index(arr: list) -> list:
    """
    Return a new array consisting of elements which are multiple of
    their own index in input array (length > 1).
    :param arr: list to determine values
    :return:
    """
    final = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            final.append(arr[i])

    return final
