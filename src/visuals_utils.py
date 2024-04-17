# Color Map Options (directly from MatPlotLib)
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
COLOR_MAPS = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'binary', 
            'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']

COLOR_MODES_NAMES = ['random', 'diagonal gradient', 'x gradient', 'y gradient', 'z gradient']
COLOR_MODES = range(1, len(COLOR_MODES_NAMES) + 1)

# display color mode options
def printColorModeOptions():
    print("\nColor Modes -- Select From:")
    for i in COLOR_MODES:
        print("\t" + str(i) + ": " + COLOR_MODES_NAMES[i-1])
    print()

# validates color mode option int from standard input
def getColorMode():
    printColorModeOptions()
    colorMode = getIntFromInput("Color Mode: ")
    while (colorMode not in COLOR_MODES):
        colorMode = getIntFromInput("Invalid Input -- Select From:\n\t1: random\n\t2: diagonal gradient\n\t3: x gradient\n\t4: y gradient\n\t5: z gradient\n\nColor Mode: ")
    return colorMode

# validates int from standard input
def getIntFromInput(message):
    while True: 
        try:
            x = int(input(message))
            if (x >= 1):
                return x
            else:
                print("Invalid Input -- Must be >= 1")
        except ValueError:
            print("Invalid Input -- Must be Integer")

# display color map options
def printColorMapOptions():
    print("\nColor Map Options -- Select From:")
    for cmap in COLOR_MAPS:
        print("\t" + cmap)
    print()

# validates color map string from standard input
def getColorMap():
    printColorMapOptions()
    cmap = input("Color Map: ")
    while (cmap not in COLOR_MAPS):
        print("\nInvalid Color Map -- Select From:")
        for cmap in COLOR_MAPS:
            print("\t" + cmap)
        print()
        cmap = input("Color Map: ")
    return cmap

# validates yes/no (boolean) input from standard input
def getBoolFromInput(message):
    while True:
        answer = input(message).lower()
        if (answer == 'y' or answer == 'yes'):
            return True
        elif (answer == 'n' or answer == 'no'):
            return False
        else:
            print("Invalid Input -- Must be Yes/No or Y/N")

# validates positive float input from standard input
def getPosFloatFromInput(message):
    while True: 
        try:
            x = float(input(message))
            if (x > 0.0):
                return x
            else:
                print("Invalid Input -- Must be > 0.0")
        except ValueError:
            print("Invalid Input -- Must be Integer")
