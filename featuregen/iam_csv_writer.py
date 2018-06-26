from isup_parameters import *
from isup_parameters.ForwardCallIndicatorsFlag import ForwardCallIndicatorsFlag
from featuregen.party import PartyProxy
from featuregen.number_match import NumberMatchCalc
from time import gmtime, strftime

def addNumber(cols, party):
    cols.append("\"tel:{0}\"".format(party.e164) if (party) else "NA")

def addTimestamp(cols, tmSecs, tmMilli):
    cols.append(strftime("%Y-%m-%d %H:%M:%S.{0}", gmtime(tmSecs)).format(tmMilli))

def addNumberType(cols, party):
    cols.append(party.numberType.name if party else "NA")

def addNumberFormat(cols, party):
    cols.append(party.numberFormat.name if party else "NA")

def addRestriction(cols, party):
    cols.append(party.subject.addressPresentationRestricted.name if (party) else "NA")

def addScreening(cols, party):
    cols.append(party.subject.screeningIndicator.name if (party) else "NA")

def addNumberMatch(cols, party, otherParty):
    cols.append(NumberMatchCalc.getNumberMatch(party.e164, otherParty.e164).name if (party and otherParty) else "NA")

def addTypeMatch(cols, party, otherParty):
    cols.append("NA" if not (party and otherParty) else "Equal" if party.numberType == otherParty.numberType else "NotEqual")
    
def addProtocolXlat(cols, iam):
    cols.append("Y" if ForwardCallIndicatorsFlag.InterworkingEncountered in iam.forwardCallIndicators.flags else "N")

def addOrigin(cols, iam):
    cols.append(iam.callingPartyCategory.callingPartyCategory.name)

def addSignalSignature(cols, iam):
    cols.append(iam.signalSignature)

class IamCsvWriter:
    @staticmethod
    def writeHeader(stream):
        stream.write(
            "Timestamp,"
            "N_Restriction,P_Restriction,G_Restriction,D_Restriction,"
            "N_Type,P_Type,G_Type,D_Type,"
            "N_Format,P_Format,G_Format,D_Format,"
            "N_Screening,P_Screening,G_Screening,D_Screening,"
            "UK_Specific,"
            "NP_NumMatch,NG_NumMatch,PG_NumMatch,"
            "NP_TypeMatch,NG_TypeMatch,PG_TypeMatch,"
            "Diverted,"
            "ProtXlat,"
            "OriginType,"
            "Signature,"
            "N_Telnum,P_Telnum,G_Telnum,D_Telnum"
            "\n")

    @staticmethod
    def writeRow(stream, tmSecs, tmMilli, iam):
        cols = []

        callingParty = PartyProxy.new(iam.getOptionalParam(CallingPartyNumberParameter.getTag()))
        presentationNumber = PartyProxy.new(iam.getOptionalParam(PresentationNumberParameter.getTag()))
        genericNumber = PartyProxy.new(iam.getOptionalParam(GenericNumberParameter.getTag()))
        redirectingNumber = PartyProxy.new(iam.getOptionalParam(RedirectingNumberParameter.getTag()))

        addTimestamp(cols, tmSecs, tmMilli)
        addRestriction(cols, callingParty)
        addRestriction(cols, presentationNumber)
        addRestriction(cols, genericNumber)
        addRestriction(cols, redirectingNumber)
        addNumberType(cols, callingParty)
        addNumberType(cols, presentationNumber)
        addNumberType(cols, genericNumber)
        addNumberType(cols, redirectingNumber)
        addNumberFormat(cols, callingParty)
        addNumberFormat(cols, presentationNumber)
        addNumberFormat(cols, genericNumber)
        addNumberFormat(cols, redirectingNumber)
        addScreening(cols, callingParty)
        addScreening(cols, presentationNumber)
        addScreening(cols, genericNumber)
        addScreening(cols, redirectingNumber)
        cols.append("Y" if iam.isUkSpecificParamsPresent else "N")
        addNumberMatch(cols, callingParty, presentationNumber)
        addNumberMatch(cols, callingParty, genericNumber)
        addNumberMatch(cols, presentationNumber, genericNumber)
        addTypeMatch(cols, callingParty, presentationNumber)
        addTypeMatch(cols, callingParty, genericNumber)
        addTypeMatch(cols, presentationNumber, genericNumber)
        cols.append("Y" if iam.isDiverted else "N")
        addProtocolXlat(cols, iam)
        addOrigin(cols, iam)
        addSignalSignature(cols, iam)
        addNumber(cols, callingParty)
        addNumber(cols, presentationNumber)
        addNumber(cols, genericNumber)
        addNumber(cols, redirectingNumber)

        stream.write(",".join(cols) +"\n")        
