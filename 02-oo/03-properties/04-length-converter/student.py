class LengthConverter:
    FEET_PER_METER = 3.28084
    INCH_PER_METER = 39.3701

    def __init__(self):
        self.__length_in_meter = 0

    @property
    def meter(self):
        return self.__length_in_meter
    
    @meter.setter
    def meter(self, length_in_meter):
        self.__length_in_meter = length_in_meter

    @property
    def feet(self):
        return self.__length_in_meter * LengthConverter.FEET_PER_METER
    
    @feet.setter
    def feet(self, length_in_feet):
        self.__length_in_meter = length_in_feet / LengthConverter.FEET_PER_METER

    @property
    def inch(self):
        return self.__length_in_meter * LengthConverter.INCH_PER_METER
    
    @inch.setter
    def inch(self, length_in_inch):
        self.__length_in_meter = length_in_inch / LengthConverter.INCH_PER_METER