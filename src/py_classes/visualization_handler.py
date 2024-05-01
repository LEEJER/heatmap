from src.py_classes.imports import *
from src.py_classes.vis_imports import *

class VisualizationHandler:

    is_single_command = False
    visualization : VisualizationInterface = None
    optionInfo : OptionInfo = None

    def __init__(self, accessor: Accessor, is_single_command):
        self.accessor = accessor
        self.is_single_command = is_single_command
        self.verbose = not is_single_command
        self.optionInfo = self.accessor['optionInfo']

    def validateOption(self, option, value):
        result = True
        opt = self.optionInfo.OPTIONS[option]
        if (callable(opt)):
            if ((not opt(value)) and self.verbose):
                print("Invalid " + option)
                result = False
        else:
            if (not (value in self.optionInfo.OPTIONS[option]) and self.verbose):
                print("Invalid " + option + " -- Select From: ")
                print("----------------------------------")
                self.optionInfo.getOptionsString(option, "\n"),
                result = False
        return result
    
    def setup(self, params):
        vis = params['visualization']
        # create visualization object
        self.visualization = self.optionInfo.visualizations[vis](self.accessor, params)

        # get list of requirements
        req = self.visualization.getParamList()

        # get values for every requirement
        if self.is_single_command:
            pass
        else:
            for item in req:
                self.visualization.params[item] = self.getOptionInput(item)

    def run(self):
        self.visualization.generate()

    def open(self):
        self.visualization.open()

    def getOptionInput(self, option):
        match option:
            case 'rows':
                return InputHandler.getIntFromInput("Number of Rows: ")

            case 'columns':
                return InputHandler.getIntFromInput("Number of Columns: ")

            case 'colorMap':
                print("\nColor Map Options -- Select From:")
                print("\t" + self.accessor['optionInfo'].getOptionsString('color_maps', "\n\t"))
                
                return InputHandler.getItemFromListFromInput("Color Map: ", self.accessor['optionInfo'].OPTIONS['color_maps'])

            case '':
                pass

            case _:
                pass
        return ''


