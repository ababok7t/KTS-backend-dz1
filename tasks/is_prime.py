__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    k = 2
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            if i*i == number:
                k+=1
            else:
                k+=2
    if number > 1 and k == 2:
        return True
    return False
    raise NotImplementedError
