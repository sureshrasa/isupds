import unittest
from decoders.stream_decoder import StreamDecoder

from featuregen.iam_csv_writer import IamCsvWriter
from decoders.initial_address_message import InitialAddressMessage

from io import StringIO, BytesIO

class TestIamCsvWriter(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        
    def testIamHeader(self):
        stream = StringIO()
        IamCsvWriter.writeHeader(stream)
        self.assertEqual(stream.getvalue(),
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

    def testIamRow(self):
        stream = StringIO()
        sampleBytes = "1020010a00020a08839092221313830f0a07031377039084181d038090a3fd0703937703908418fe020300c0080603107703908418f401823908f4d1c0c0fec0fdc000"
        iam = InitialAddressMessage(StreamDecoder(BytesIO(bytearray.fromhex(sampleBytes))))
        IamCsvWriter.writeRow(stream, 1529080919, 234, iam)
        self.assertEqual(stream.getvalue(),
            "2018-06-15 16:41:59.234,Allowed,Allowed,Allowed,NA,UkMobile,UkMobile,UkMobile,NA,Valid,Valid,Valid,NA,NetworkProvided,NetworkProvided,UserProvidedNotVerified,NA,Y,Equal,Equal,Equal,Equal,Equal,Equal,N,N,OrdinarySubscriber,a.1d.fd.fe.c0.f4.39,\"tel:+447730094881\",\"tel:+447730094881\",\"tel:+447730094881\",NA\n")

if __name__ == '__main__':
    unittest.main()

