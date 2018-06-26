#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.RedirectionIndicator import *
from isup_parameters.OriginalRedirectionReason import *

from isup_parameters.RedirectingReason import *
class RedirectionInformationParameter:
    def __init__(self, 
        redirectionIndicator,
        originalRedirectionReason,
        redirectionCounter,
        redirectingReason):
        self._redirectionIndicator = redirectionIndicator
        self._originalRedirectionReason = originalRedirectionReason
        self._redirectionCounter = redirectionCounter
        self._redirectingReason = redirectingReason

    def __str__(self):
        return ("RedirectionInformationParameter["

        + str(self.redirectionIndicator)      + ","
        + str(self.originalRedirectionReason)      + ","
        + str(self.redirectionCounter)      + ","
        + str(self.redirectingReason)      + "]")


    @staticmethod
    def getTag():
        return 0x013



    @property
    def redirectionIndicator(self):
        return self._redirectionIndicator



    @property
    def originalRedirectionReason(self):
        return self._originalRedirectionReason



    @property
    def redirectionCounter(self):
        return self._redirectionCounter



    @property
    def redirectingReason(self):
        return self._redirectingReason
