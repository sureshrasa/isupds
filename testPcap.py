from decoders import Pcap
from decoders.stream_decoder import StreamDecoder
from decoders.mtp import *
from decoders.isup_message import *
from decoders.initial_address_message import InitialAddressMessage
from featuregen.iam_csv_writer import IamCsvWriter
from io import BytesIO

from pathlib import Path, PurePath

def processFile(outputStream, filename):
    print("Processing file:", filename)
    with open(str(filename), "rb") as inputFile:
        inputStream = StreamDecoder(inputFile)
        return dumpPcapFile(inputStream, outputStream)
        
def dumpPcapFile(stream, outputStream):
    iamGoodCount = 0
    iamBadCount = 0
    
    maxPktLen = 0

    #badIams = []

    lloyds_point_codes = [13471, 13472, 13469, 13473, 13471, 13462, 13466, 13912]

    pcapHdr = Pcap.Header(stream)
    print(pcapHdr)

    try:
        while stream.hasMore():
            pkt = Pcap.Packet(stream)
            #print(pkt)
            if (pkt.length > 5):
                mtpStream = StreamDecoder(BytesIO(pkt.payload))
                mtp2 = Mtp2(mtpStream)
                #print(mtp2) 
                if (mtp2.length > 2):
                    mtp3 = Mtp3(mtpStream)
                    #print(mtp3)
                    if mtp3.dpc in lloyds_point_codes:
                        isup = IsupMessage(mtpStream)
                        #print(isup)
                        if (isup.code == 1):
                            #print("payload:", bytearray.hex(pkt.payload))
                            #break;
                            if (pkt.length > maxPktLen):
                                maxPktLen = pkt.length
                                
                            try:
                                iam = InitialAddressMessage(mtpStream) 
                                iamGoodCount += 1
                                #print(iam)
                                IamCsvWriter.writeRow(outputStream, pkt.tmStampSecs, pkt.tmStampMillisecs, iam)
                            except Exception as e:
                                #print("Bad IAM; reason:{0}, calling:{1}".format(e, iam.getOptionalParam(10)))
                                iamBadCount += 1
                                #badIams.append(pkt.payload)

    except Exception as e:
        print("Error while reading pcap file; reason:", e)

    print("Total IAM good:{0}; bad:{1}".format(iamGoodCount, iamBadCount))
    return maxPktLen
    #for d in badIams:
    #    print("payload:", ",".join(map(str,d)))

    #print("Unknown parameter tags: ", ",".join(map(str, IsupParameterDecoder.unknownParameterTags)))                   
 
filename = "/EDIN_TAS1_2018-02-08.pcap"

p = Path("/media/psf/Home/Downloads/PCAP Trace Files")
grandMax = 0

with open(str(p/"all_files.csv"), "w") as outputStream:
    IamCsvWriter.writeHeader(outputStream)

    for entry in p.iterdir():
        if not entry.is_dir():
            filename = PurePath(entry)
            if filename.suffix == ".pcap":
                maxPktLen = processFile(outputStream, filename)
                if (maxPktLen > grandMax):
                    grandMax = maxPktLen
                    
print("Grand max packet length = ", grandMax)
