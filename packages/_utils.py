from datetime import datetime

from ._cvtColor import COLORIZE
from ._imgConverter import IMG_CONVERTER


class UTILS(IMG_CONVERTER):
    
    __DATETIME = datetime.now()    
    __COLORIZE = COLORIZE()

    def __init__(self) -> None:
        self.MONTH = self.__DATETIME.strftime('%m')
        self.DATE = self.__DATETIME.strftime('%d')
        self.YEAR = self.__DATETIME.strftime('%Y')
        
        self.DAY = self.__DATETIME.strftime('%a')

        self.HOUR = self.__DATETIME.strftime('%H')
        self.MINUTE = self.__DATETIME.strftime('%M')
        self.SECOND = self.__DATETIME.strftime('%S')

    
    def startColor(self, buff) -> tuple:
        return self.__COLORIZE.start_process(image_data=self.buffToImg(buff))
    
    def getFilenameExtension(self, bwImageData) -> list:
        return [bwImageData.filename, 
                bwImageData.filename.split('.')[-2], 
                bwImageData.filename.split('.')[-1]]
        
    
