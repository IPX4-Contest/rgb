import numpy as np
import statistics


def checkR(pixelr):
    if pixelr >= 200:
        return 1
    return 0


def checkG(pixelg):
    if pixelg <= 40:
        return 1
    return 0


def checkB(pixelb):
    if pixelb <= 40:
        return 1
    return 0


def findred(rgb):
    shape = rgb[0].shape
    row = shape[0]
    col = shape[1]
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    redDeter = np.zeros((row, col))
    # print(type(red))
    for i in range(row):
        for j in range(col):
            r = checkR(red[i][j])
            g = checkG(green[i][j])
            b = checkB(blue[i][j])
            if (r & g & b) == 1:
                redDeter[i][j] = 1
    # print(redDeter)
    return redDeter


def findCenter(matrix):
    row = len(matrix)
    col = len(matrix[0])
    arr = np.where(matrix == 1)
    mean_row = statistics.mean(arr[0])
    mean_col = statistics.mean(arr[1])
    center = [mean_row, mean_col]
    return center


if __name__ == '__main__':
    rgb = np.array([[[20, 21, 20], [210, 220, 230], [220, 230, 240], [230, 240, 250]],
                    [[20, 21, 22], [21, 22, 23], [22, 23, 24], [1, 2, 3]],
                    [[20, 21, 22], [21, 22, 23], [22, 23, 24], [2, 3, 4]]])
    matrixRed = findred(rgb)  # rgb: numpy array of
    centerRed = findCenter(matrixRed)
    # print(type(int(matrixRed[0][0])))
    print(centerRed)
    # print(matrixRed)
