#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.BackwardCallIndicatorsFlag import *
from isup_parameters.ChargeIndicator import *
from isup_parameters.CalledPartysStatusIndicator import *
from isup_parameters.CalledPartysCategoryIndicator import *
from isup_parameters.EndToEndMethodIndicator import *
from isup_parameters.SccpMethodIndicator import *
class BackwardCallIndicatorsParameter:
    def __init__(self, flags, 
        chargeIndicator,
        calledPartysStatusIndicator,
        calledPartysCategoryIndicator,
        endToEndMethodIndicator,
        sccpMethodIndicator):
        self._chargeIndicator = chargeIndicator
        self._calledPartysStatusIndicator = calledPartysStatusIndicator
        self._calledPartysCategoryIndicator = calledPartysCategoryIndicator
        self._endToEndMethodIndicator = endToEndMethodIndicator
        self._sccpMethodIndicator = sccpMethodIndicator
        self._flags = flags

    def __str__(self):
        return ("BackwardCallIndicatorsParameter["
        + str(self.flags)+ ","
        + str(self.chargeIndicator)      + ","
        + str(self.calledPartysStatusIndicator)      + ","
        + str(self.calledPartysCategoryIndicator)      + ","
        + str(self.endToEndMethodIndicator)      + ","
        + str(self.sccpMethodIndicator)      + "]")


    @staticmethod
    def getTag():
        return 0x011

    @property
    def flags(self):
        return self._flags


    @property
    def chargeIndicator(self):
        return self._chargeIndicator



    @property
    def calledPartysStatusIndicator(self):
        return self._calledPartysStatusIndicator



    @property
    def calledPartysCategoryIndicator(self):
        return self._calledPartysCategoryIndicator



    @property
    def endToEndMethodIndicator(self):
        return self._endToEndMethodIndicator



    @property
    def sccpMethodIndicator(self):
        return self._sccpMethodIndicator
