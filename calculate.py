import circle  # noqa: F401
import square  # noqa: F401 
import triangle  # noqa: F401 


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-triangle": 3,
    "perimeter-triangle": 3
}


def calc(fig, func, size):
    assert fig in figs, "fail"
    assert func in funcs, "fail"
    assert len(size) == sizes.get(f"{func}-{fig}", 1), "fail"
    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space,\
        1 for circle and square\n").split(' ')))

    print(calc(fig, func, size))
