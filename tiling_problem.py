## given  a 4*n board and a tile of size
## 4*1 count the number of ways to tile the given board
## a tile can be placed both horizontaly and vertically

def tilingway(n):
    if n<4:
        return 1

    else:
        no_ofway = tilingway(n-1) + tilingway(n-4)

        return no_ofway