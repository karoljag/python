#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
import datetime
import os
import shutil
from sys import argv
import random
import time
from emptyFiles import emptyFilesMaker

csv.register_dialect('excel', delimiter='|', quoting=csv.QUOTE_NONE)
now = datetime.datetime.now()

myDate = now.strftime("%Y%m%d%H%M%S")
shortDate = now.strftime("%M%S")

userId = shortDate

# destynacje w jestblue
dest = ["ANC", "ABQ", "ACK", "ALB", "ANU", "AUA", "AUS", "AZS", "BDA", "BDL", "BGI", "BOG", "BOS", "BQN", "BTV", "BUF", "BUR", "BWI", "CHS", "CLE", "CLT", "CTG", "CUN", "CUR", "DCA", "DEN", "DFW", "DTW", "EWR", "FLL", "GCM", "GND", "HOU", "HPN", "HYA", "IAD", "JAX", "JFK", "KIN", "LAS", "LAX", "LGA", "LGB", "LIM", "LIR", "LRM", "MBJ",
        "MCO", "MDE", "MEX", "MSY", "MVY", "NAS", "OAK", "ORD", "ORH", "PAP", "PBI", "PDX", "PHL", "PHX", "PIT", "PLS", "POP", "POS", "PSE", "PSP", "PUJ", "PVD", "PWM", "RDU", "RIC", "RNO", "ROC", "RSW", "SAN", "SAV", "SDQ", "SEA", "SFO", "SJC", "SJO", "SJU", "SLC", "SMF", "SRQ", "STI", "STT", "STX", "SWF", "SXM", "SYR", "TPA", "UVF"]  # 94
# kody partnerskie
partnerCode = ["SQ", "flowers", "ha", "ax", "np", "av", "ft", "bu", "pc1", "nca", "CLUBW", "gt", "ngl",
               "ek", "he", "hh", "ihg", "my", "ner", "ep", "nrm", "fbs", "pcshm", "3m", "sa", "ssi", "ndw", "zc"]  # 26

T = 0  # ilosc wierszy w pliku csv - suma kontrolna

usrPath = os.path.dirname(os.path.realpath(__file__)) + \
    '/daneTestowe/' + myDate + '/usr'

if not os.path.exists(usrPath):
    os.makedirs(usrPath, 0755)


tranPath = os.path.dirname(os.path.realpath(
    __file__)) + '/daneTestowe/' + myDate + '/trn'


if not os.path.exists(tranPath):
    os.makedirs(tranPath, 0775)


def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)


bDay = randomDate("1902-01-01", "2010-12-31", random.random())
userRandBirthDay = bDay + " 10:00:00"


# ------------------------------------------transakcjaLotnicza----------------------------------------------------------
def transakcjaLotnicza():
    T = 0  # ilosc wierszy
    ileLotow = input("Ile kopii lotów : ")
    if int(ileLotow) < 1:
        print "Zbyt mala liczba"

    ileDestynacji = input("Ile destynacji : ")
    if int(ileDestynacji) < 1:
        print "Zbyt mala liczba"
        print ileDestynacji

    if int(ileDestynacji) == 1:
        kodLotn = raw_input("Kod lotniska docelowego : ")
        kodStr = str(kodLotn)
        kod = str(kodLotn)

        transaction = open(
            tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")

        try:
            writer = csv.writer(transaction, delimiter='|')
            writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                             'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
            for ie in range(ileuserow):
                for ee in range(0, ileLotow):
                    writer.writerow(('I', '842166164', 'B6', '12', userId + str(ie), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', '2015-02-03 10:00:00', '', '17470', 'System', '0', 'I', '1', 'Y', dest[0] + str(
                        kod), 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center', 'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', '',))
                    T += 1
            writer.writerow(('T', T))
        finally:
            transaction.close()

    if int(ileDestynacji) > 1:
        ileKierunow = raw_input("(J)ednokierunkowo, (D)wukierunkowo :  ")
        kierunki = str(ileKierunow)
        if kierunki == 'D':
            print "Dwukierunkwo"
    # dwukierunkowo ----------------------------------------------------------
            transactionall = open(
                tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")
            try:
                writer = csv.writer(transactionall, delimiter='|')
                writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                                 'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
                for de in range(0, ileDestynacji):
                    for ie in range(0, ileDestynacji):
                        for ile in range(0, ileuserow):
                            for ilosc in range(ileLotow):
                                writer.writerow(('I', '842166164', 'B6', '12', userId + str(ile), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', '2015-02-03 10:00:00', '', '17470', 'System', '0', 'I', '1', 'Y', dest[de] + dest[
                                                ie], 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center', 'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', ''))
                                T += 1
                writer.writerow(('T', T))
            finally:
                transactionall.close()
        if kierunki == 'J':
            print "Jednokierunkowo"

    # jednokierunkowo--------------------------------------------------------------
        # if int(ileDestynacji) > 1:
            transactionall = open(
                tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")

            try:
                writer = csv.writer(transactionall, delimiter='|')
                writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                                 'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
                # for de in range (0, ileDestynacji):
                for ie in range(0, ileDestynacji):
                    for ile in range(0, ileuserow):
                        for ilosc in range(ileLotow):
                            writer.writerow(('I', '842166164', 'B6', '12', userId + str(ile), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', '2015-02-03 10:00:00', '', '17470', 'System', '0', 'I', '1', 'Y', dest[1] + dest[
                                            ie], 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center', 'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', ''))
                            T += 1
                writer.writerow(('T', T))
            finally:
                transactionall.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def transakcjaPartnerska():
    T = 0  # ilosc wierszy

    ilePartnerow = input("Ile partnerow  : ")  # ile kodów uzyje
    if int(ilePartnerow) < 1:
        print "Zbyt mala liczba"
        print ilePartnerow

    # ile transakcji partnerskich w obrebie konkretnego partnera
    ileTransakcjiDlaKodu = input(
        "Ile transakcji w obrebie jednego  partnera : ")
    if int(ileTransakcjiDlaKodu) < 1:
        print "Zbyt mala liczba"

    if int(ilePartnerow) == 1:
        kodPartnera = raw_input("Kod partnera : ")

        transaction = open(
            tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")

        try:
            writer = csv.writer(transaction, delimiter='|')
            writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                             'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
            for ie in range(ileuserow):
                for ee in range(ileTransakcjiDlaKodu):
                    writer.writerow(('I', '842166164', kodPartnera, '12', userId + str(ie), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', '2015-02-03 10:00:00', '', '17470', 'System', '0', 'I', '1', 'Y', 'KRKWAW', 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center',
                                     'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', '',))
                    T = T + 1
            writer.writerow(('T', T))
        finally:
            transaction.close()

    elif int(ilePartnerow) > 1:
        transactionall = open(
            tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")
        T = 0  # ilosc wierszy
        try:
            writer = csv.writer(transactionall, delimiter='|')
            writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                             'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
            for de in range(0, ilePartnerow):
              # for ie in range (0, ilePartnerow):
                for ile in range(ileuserow):
                    for ilosc in range(ileTransakcjiDlaKodu):
                        writer.writerow(('I', '842166164', partnerCode[de], '12', userId + str(ile), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', '2015-02-03 10:00:00', '', '17470', 'System', '0', 'I', '1', 'Y', 'KRKKRK', 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center',
                                         'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', '',))
                        T = T + 1
            writer.writerow(('T', T))
        finally:
            transactionall.close()


# -----------------------------------------------transakcja zwiazana z dat
def transakcjaData():
    T = 0  # ilosc wierszy
    ileLotow = input("Ile lotow : ")
    if int(ileLotow) < 1:
        print "Zbyt mala liczba"

    deptDate = raw_input("Departure date (YYYY-MM-DD): ")

    ileDestynacji = input("Ile destynacji : ")
    if int(ileDestynacji) < 1:
        print "Zbyt mala liczba"
        print ileDestynacji

    if int(ileDestynacji) == 1:
        kodLotn = raw_input("Kod Lotniska docelowego : ")
        kodStr = str(kodLotn)
        kod = str(kodLotn)

        transaction = open(
            tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")

        try:
            writer = csv.writer(transaction, delimiter='|')
            writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                             'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
            for ie in range(ileuserow):
                for ee in range(ileLotow):
                    writer.writerow(('I', '842166164', 'B6', '12', userId + str(ie), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', deptDate + " 10:00:00", '', '17470', 'System', '0', 'I', '1', 'Y', dest[0] + str(
                        kod), 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center', 'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', '',))
                    T += 1
            writer.writerow(('T', T))
        finally:
            transaction.close()

    elif int(ileDestynacji) > 1:
        transactionall = open(
            tranPath + "/JETBLUE_TRANSACTION_" + myDate + ".csv", "awt")

        try:
            writer = csv.writer(transactionall, delimiter='|')
            writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                             'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
            for ie in range(0, ileDestynacji):
                for ile in range(0, ileuserow):
                    for ilosc in range(ileLotow):
                        writer.writerow(('I', '842166164', 'B6', '12', userId + str(ile), '2015-02-03 10:00:00', '2015-03-07 01:03:51', '2015-02-02 10:00:00', deptDate + " 10:00:00", '', '17470', 'System', '0', 'I', '1', 'Y', dest[0] + dest[
                                        ie], 'seattle', '32F', '32F658', 'B6', 'F', 'A', '', '', '', '', '1922', '', 'Salt Lake Support Center', 'ONGBGB', '298.05', '22.35', '298.05', '1000', '1', 'A', '4100003', '8072', '', '', '', '2125457278', '', 'N', 'QH00AE5U', 'Y', '', '', '', '', '', '', 'B6', '8072', 'SLC', 'ORL', '9010001', 'WEB - B2C / GUEST - USA', '2015-01-08 10:00:00', '279', 'QHIP', '', '', '', '', '7664', 'L', 'P', '', '', '', '', '', ''))
                        T += 1
            writer.writerow(('T', T))
        finally:
            transactionall.close()



def membCreate():
    # --------------------------------------------------  tworzenie pliku MEMB
    f = open(usrPath + "/JETBLUE_MEMBERS_" + myDate + ".csv", "a")
    member = open(usrPath + "/JETBLUE_MEMBERS_" + myDate + ".csv", 'wt')

    try:
        writer = csv.writer(member, delimiter='|')
        writer.writerow(('ROW_MARKER', 'CARD_NUMBER', 'ENROLLMENT_DATE', 'BIRTH_DATE', 'T_C_ACCEPTED_DATE', 'STATUS', 'REGION', 'COUNTRY_CODE', 'CITY', 'POSTCODE', 'SEATING_PREF1', 'SEATING_PREF2', 'BUSINES_FREQ',
                         'PLEASURE_FREQ', 'SMB_OWN', 'CC_AGREEMENT', 'EMAIL_AGREEMENT', 'POST_AGREEMENT', 'SMS_AGREEMENT', 'FAV1_AIRPORT', 'FAV2_AIRPORT', 'HOME_AIRPORT', 'GENDER', 'FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME', 'EMAIL'))
        for i in range(ileuserow):
            writer.writerow(('U', userId + str(i), '2014-06-08 09:04:13', BirthDay, '2014-06-08 10:00:00', 'A', 'BB-01', 'BRB', 'Cracov', '0', 'nopref', 'nopref', 'nopref', 'nopref', 'Unknown', 'N', 'N', 'N', '', 'JFK', '', 'BGI', 'F', 'nopref', 'nopref', 'nopref', userId + str(
                i) + '@HOTMAIL.COM', '25167', '2014-05-09 10:00:00', '2015-03-01 10:00:00', '', '', '2014-03-16 10:00:00', '', 'F', 'W', 'B6', '', 'MR', '', '60 Simmons Road', 'cancun', '', '2417373', 'M', '', '', '', '', '', '', 'en-us', 'ENG', '', 'F', '', '', '', '', '', '', '', '0'))
        writer.writerow(('T', ileuserow))

    finally:
        member.close()

#  -----------------------------------------------------------------
print 60 * '*'
ileuserow = input("Ile uzytkownikow : ")
if int(ileuserow) < 1:
    print "Zbyt mala liczba"
elif int(ileuserow) == 1:

    specifID = raw_input(
        "Podaj ID użytkownika (w przeciwnym wypadku zostanie nadane losowe  ID) : ")
    str(specifID)
    if len(specifID) > 0:
        userId = specifID
    else:
        userId = shortDate


birDate = raw_input(
    "Podaj date urodzenia użytkownika YYYY-MM-DD (w przeciwnym wypadku zostanie nadane losowa) : ")
str(birDate)
if len(birDate) > 0:
    BirthDay = birDate + " 01:00:00"
else:
    BirthDay = userRandBirthDay


typTransakcji = raw_input(
    "Typ Transakcji (L)otnicza , (P)artnerska, (T)erminowa  : ")
if typTransakcji == 'L':    
    transakcjaLotnicza()
if typTransakcji == 'P': 
    transakcjaPartnerska()
if typTransakcji == 'T': 
    transakcjaData()


# tworzenie pliku z użytkownikiem który dokonal transakcji
membCreate()
# wywołanie funkcji z pliku "emptyFiles.py"tworzaca puste pliki niezbedne
# przy walidacji importu.
emptyFilesMaker()
# -----------------------------------------------------------------------------------------------

usrPathToZIP = os.path.dirname(os.path.realpath(
    __file__)) + '/daneTestowe/' + myDate + '/usr'
tranPathToZIP = os.path.dirname(os.path.realpath(
    __file__)) + '/daneTestowe/' + myDate + '/trn'

u1 = os.path.dirname(os.path.realpath(__file__)) + \
    '/daneTestowe/' + myDate + '/'
t1 = os.path.dirname(os.path.realpath(__file__)) + \
    '/daneTestowe/' + myDate + '/'


shutil.make_archive(u1 + shortDate + "us", 'zip', usrPathToZIP)
shutil.make_archive(t1 + shortDate + "tr", 'zip', tranPathToZIP)
print 60 * '-'
print "Nazwa paczki: " + myDate + " w lokalizacji:" + os.path.dirname(os.path.realpath(__file__)) + '/daneTestowe/' + myDate
print "User ID: " + userId
print 60 * '*'
