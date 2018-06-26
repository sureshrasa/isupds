from isup_parameters.NatureOfAddress import NatureOfAddress
from featuregen.number_traits import NumberTypeCalc

class PartyProxy:
    @staticmethod
    def new(subject):
        return PartyProxy(subject) if subject else None

    def __init__(self, subject):
        self._subject = subject
        self._digits = "".join(map(lambda x:str(x.digit.value), self._subject.addressSignals))
        self._e164 = PartyProxy._getE164(subject.natureOfAddress, self._digits)
        self._numType = NumberTypeCalc.getType(self._e164)
        self._numberFormat = NumberTypeCalc.getFormat(self._numType, self._e164)

    @property
    def subject(self):
        return self._subject

    @property
    def digits(self):
        return self._digits

    @property
    def e164(self):
        return self._e164
    
    @property
    def numberType(self):
        return self._numType

    @property
    def numberFormat(self):
        return self._numberFormat

    @staticmethod
    def _getE164(noa, digits):
        if noa == NatureOfAddress.National:
            return "+44" + digits    
        elif noa == NatureOfAddress.International:
            return "+" + digits
        elif noa == NatureOfAddress.UkSpecific:
            return "uk:" + digits
        else:
            return "-" + digits