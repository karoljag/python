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


csv.register_dialect('excel', delimiter='|', quoting=csv.QUOTE_NONE)
now = datetime.datetime.now()

myDate = now.strftime("%Y%m%d%H%M%S")
shortDate = now.strftime("%M%S")

userId = shortDate

usrPath = os.path.dirname(os.path.realpath(__file__)) + \
    '/daneTestowe/' + myDate + '/usr'

if not os.path.exists(usrPath):
    os.makedirs(usrPath, 0755)


tranPath = os.path.dirname(os.path.realpath(
    __file__)) + '/daneTestowe/' + myDate + '/trn'


if not os.path.exists(tranPath):
    os.makedirs(tranPath, 0775)


def emptyFilesMaker():

    # stworzenie pustych plików niezebdnych przy walidacji paczki .zip 
    zera = "0000000000"

    #---------------------------------------members---------------------------

    memberEmpty = open(tranPath + "/JETBLUE_MEMBERS_" + zera + ".csv", 'wt')
    ileuserow = 0
    try:
        writer = csv.writer(memberEmpty, delimiter='|')
        writer.writerow(('ROW_MARKER', 'CARD_NUMBER', 'ENROLLMENT_DATE', 'BIRTH_DATE', 'T_C_ACCEPTED_DATE', 'STATUS', 'REGION', 'COUNTRY_CODE', 'CITY', 'POSTCODE', 'SEATING_PREF1', 'SEATING_PREF2', 'BUSINES_FREQ',
                         'PLEASURE_FREQ', 'SMB_OWN', 'CC_AGREEMENT', 'EMAIL_AGREEMENT', 'POST_AGREEMENT', 'SMS_AGREEMENT', 'FAV1_AIRPORT', 'FAV2_AIRPORT', 'HOME_AIRPORT', 'GENDER', 'FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME', 'EMAIL'))
        for i in range(ileuserow):
            writer.writerow(('U', userId, '2014-06-08 09:04:13', '2016-02-13 00:00:00', '2014-06-08 00:00:00', 'A', 'BB-01', 'BRB', 'chicago', '0', 'nopref', 'nopref', 'nopref', 'nopref', 'Unknown', 'N', 'N', 'N', '', 'JFK', '', 'BGI', 'F', 'nopref', 'nopref', 'nopref',
                             'nopref@HOTMAIL.COM', '25167', '2014-05-09 00:00:00', '2015-03-01 00:00:00', '', '', '2014-03-16 00:00:00', '', 'F', 'W', 'B6', '', 'MR', '', '60 Simmons Road', 'cancun', '', '2417373', 'M', '', '', '', '', '', '', 'en-us', 'ENG', '', 'F', '', '', '', '', '', '', '', '0'))
        writer.writerow(('T', ileuserow))

    finally:
        memberEmpty.close()

    #-----------------------------------transactions--------------------------

        transaction = open(
            usrPath + "/JETBLUE_TRANSACTION_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(transaction, delimiter='|')
        writer.writerow(('ROW_MARKER', 'CODE', 'PARTNER', 'CHANNEL', 'CARD_NUMBER', 'TRANSACTION_DATE', 'PROCESSING_DATE', 'BOOKING_DATE', 'DEPARTURE_DATE', 'SOURCE_TRANSACTION_NO', 'BATCH_ID', 'USER_LOGIN', 'TRANS_TOTAL_VALUE', 'TRANSACTION_TYPE', 'TRANSACTION_STATUS', 'TARIFF', 'OND', 'BOOKING_LOCATION', 'AIRCRAFT_TYPE', 'AIRCRAFT_TAIL_NO', 'AIRLINE_MARKETING_CODE', 'ONLINE_BOOKING', 'PAX_TYPE', 'FEE_CODE', 'PARTNER_TRN_ID', 'TRANSACTION_CODE', 'TRANSACTION_FEE', 'TRANSACTION_POINTS', 'PARTNER_POINTS', 'IATA_LOCATION_CODE', 'PNR_LOCATOR', 'BASE_FARE', 'EXCISE_TAX', 'DISCOUNT_BASE', 'DISTANCE', 'COUPON_NO',
                         'AGENT_TYPE', 'IATA_LOC_NO', 'FLIGHT_NO', 'FLIGHT_NO_SUFFIX', 'OTHER_FFP_PROGRAM_CODE', 'OTHER_FFP_NO', 'TICKET_NO', 'TOUR_CODE', 'BULK_FARE_INDICATOR', 'FARE_BASIS', 'FLOWN_CLASS', 'TRANSACTION_VALUE', 'TRASNACTION_REVENUE', 'ADJUSTED_TRN_ID', 'CANCELLED_TRN_ID', 'TRN_EXT01', 'TRN_EXT02', 'TRN_EXT03', 'TRN_EXT04', 'TRN_EXT05', 'TRN_EXT06', 'TRN_EXT07', 'TRN_EXT08', 'TRN_EXT09', 'TRN_EXT10', 'TRN_EXT11', 'TRN_EXT12', 'TRN_EXT13', 'TRN_EXT14', 'TRN_EXT15', 'TRN_EXT16', 'TRN_EXT17', 'TRN_EXT18', 'TRN_EXT19', 'TRN_EXT20', 'TRN_EXT21', 'TRN_EXT22', 'TRN_EXT23', 'TRN_EXT24', 'TRN_EXT25'))
        writer.writerow(('T', "0"))
    finally:
        transaction.close()

    # # ----------------------------------member counter----------------------

    membCount = open(usrPath + "/JETBLUE_MEMBER_COUNTER_" +
                     zera + ".csv", 'awt')
    try:
        writer = csv.writer(membCount, delimiter='|')
        writer.writerow(("ROW_MARKER", "CARD_NUMBER", "COUNTER_CODE", "COUNTER_NAME",
                         "BUSINES_RULE_CODE", "COUNTER_PERIOD", "COUNTER_VALUE"))
        writer.writerow(('T', "0"))
    finally:
        membCount.close()

    membCount = open(tranPath + "/JETBLUE_MEMBER_COUNTER_" +
                     zera + ".csv", 'awt')
    try:
        writer = csv.writer(membCount, delimiter='|')
        writer.writerow(("ROW_MARKER", "CARD_NUMBER", "COUNTER_CODE", "COUNTER_NAME",
                         "BUSINES_RULE_CODE", "COUNTER_PERIOD", "COUNTER_VALUE"))
        writer.writerow(('T', "0"))
    finally:
        membCount.close()

    #  #---------------------------member fam---------------------------------

    membFam = open(usrPath + "/JETBLUE_MEMBERS_FAM_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(membFam, delimiter='|')
        writer.writerow(("ROW_MARKER", "MBF_ID", "TB#", "FAMILY_ID", "MBR_FAM_START_DATE", "MBR_FAM_HOH", "MBR_FAM_ROLE", "MBR_FAM_RELATIONSHIP", "MBR_FAM_CONTRIBUTION_ONGOING_PERCENT", "MBR_FAM_CONTRIBUTION_ONGOING_POINTS", "MBR_FAM_CONTRIBUTION_INSTANT_PERCENT",
                         "MBR_FAM_CONTRIBUTION_INSTANT_POINTS", "MBR_REGISTRATION_DATE", "MBR_UNREGISTRATION_DATE", "MBR_UNREGISTRATION_REASON", "MBR_INVITATION_EMAIL", "MBR_INTIVATION_FIRST_NAME", "MBR_INVITATION_STATUS", "MBR_REC_TYPE"))
        writer.writerow(('T', "0"))
    finally:
        membFam.close()

    membFam = open(tranPath + "/JETBLUE_MEMBERS_FAM_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(membFam, delimiter='|')
        writer.writerow(("ROW_MARKER", "MBF_ID", "TB#", "FAMILY_ID", "MBR_FAM_START_DATE", "MBR_FAM_HOH", "MBR_FAM_ROLE", "MBR_FAM_RELATIONSHIP", "MBR_FAM_CONTRIBUTION_ONGOING_PERCENT", "MBR_FAM_CONTRIBUTION_ONGOING_POINTS", "MBR_FAM_CONTRIBUTION_INSTANT_PERCENT",
                         "MBR_FAM_CONTRIBUTION_INSTANT_POINTS", "MBR_REGISTRATION_DATE", "MBR_UNREGISTRATION_DATE", "MBR_UNREGISTRATION_REASON", "MBR_INVITATION_EMAIL", "MBR_INTIVATION_FIRST_NAME", "MBR_INVITATION_STATUS", "MBR_REC_TYPE"))
        writer.writerow(('T', "0"))
    finally:
        membFam.close()

    # #-------------------------------------------MEMB RLE--------------------

    membRle = open(usrPath + "/JETBLUE_MEMBERS_RLE_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(membRle, delimiter='|')
        writer.writerow(("ROW_MARKER", "CARD_NUMBER", "REC_LEVEL_CODE", "CREATED_DATE", "START_DATE", "END_DATE",
                         "METHOD", "ARL_TRN_ID", "PRO_CODE", "ARL_CHANNEL", "ARL_MODIFICATION_REASON_CODE", "ID"))
        writer.writerow(('T', "0"))
    finally:
        membRle.close()

    membRle = open(tranPath + "/JETBLUE_MEMBERS_RLE_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(membRle, delimiter='|')
        writer.writerow(("ROW_MARKER", "CARD_NUMBER", "REC_LEVEL_CODE", "CREATED_DATE", "START_DATE", "END_DATE",
                         "METHOD", "ARL_TRN_ID", "PRO_CODE", "ARL_CHANNEL", "ARL_MODIFICATION_REASON_CODE", "ID"))
        writer.writerow(('T', "0"))
    finally:
        membRle.close()

    # # ----------------------------------------Redemptions-------------------
    redemptions = open(usrPath + "/JETBLUE_REDEMPTIONS_" +
                       zera + ".csv", 'awt')
    try:
        writer = csv.writer(redemptions, delimiter='|')
        writer.writerow(("ROW_MARKER", "REDEMPTION_CODE", "TRANSACTION_CODE", "REDEMPTION_TYPE", "DEPARTURE_DATE", "BOOKING_DATE", "CANCEL_DATE", "ORIGIN", "DESTINATION", "BOOKING_CLASS", "CONSUMPTION_DATE", "AWARD_CODE", "ORDER_CHANNEL", "ORDER_STATUS", "PARTNER", "PNR_LOCATOR", "FIRST_NAME", "LAST_NAME", "OLD_NEW_REDEMPTION", "POINTS_PAID", "MONEY_PAID", "NUM_OF_PASSENGERS", "CARD_NUMBER",
                         "ARD_PARTNER_TRANSACTION_ID", "ARD_MIDDLE_NAME", "ARD_FLIGHT_NO", "ARD_ARRIVAL_DATE", "ARD_OPERATING_AIRLINE", "ARD_CUSTOMER_ID", "ARD_GENDER", "ARD_PRICE_IN_POINTS", "ARD_PRICE_IN_CASH", "ARD_QUANTITY", "ARD_CANCEL_TRN_ID", "ARD_KIND", "ARD_EXT01", "ARD_EXT02", "ARD_EXT03", "ARD_EXT04", "ARD_EXT05", "ARD_EXT06", "ARD_EXT07", "ARD_EXT08", "ARD_EXT09", "ARD_EXT10"))
        writer.writerow(('T', "0"))
    finally:
        redemptions.close()

    redemptions = open(tranPath + "/JETBLUE_REDEMPTIONS_" +
                       zera + ".csv", 'awt')
    try:
        writer = csv.writer(redemptions, delimiter='|')
        writer.writerow(("ROW_MARKER", "REDEMPTION_CODE", "TRANSACTION_CODE", "REDEMPTION_TYPE", "DEPARTURE_DATE", "BOOKING_DATE", "CANCEL_DATE", "ORIGIN", "DESTINATION", "BOOKING_CLASS", "CONSUMPTION_DATE", "AWARD_CODE", "ORDER_CHANNEL", "ORDER_STATUS", "PARTNER", "PNR_LOCATOR", "FIRST_NAME", "LAST_NAME", "OLD_NEW_REDEMPTION", "POINTS_PAID", "MONEY_PAID", "NUM_OF_PASSENGERS", "CARD_NUMBER",
                         "ARD_PARTNER_TRANSACTION_ID", "ARD_MIDDLE_NAME", "ARD_FLIGHT_NO", "ARD_ARRIVAL_DATE", "ARD_OPERATING_AIRLINE", "ARD_CUSTOMER_ID", "ARD_GENDER", "ARD_PRICE_IN_POINTS", "ARD_PRICE_IN_CASH", "ARD_QUANTITY", "ARD_CANCEL_TRN_ID", "ARD_KIND", "ARD_EXT01", "ARD_EXT02", "ARD_EXT03", "ARD_EXT04", "ARD_EXT05", "ARD_EXT06", "ARD_EXT07", "ARD_EXT08", "ARD_EXT09", "ARD_EXT10"))
        writer.writerow(('T', "0"))
    finally:
        redemptions.close()

    # #-----------------------------------------TRN POINT TYPE----------------
    trnpointtype = open(
        usrPath + "/JETBLUE_TRN_POINT_TYPE_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(trnpointtype, delimiter='|')
        writer.writerow(("ROW_MARKER", "TRANS_POINT_TYPE_CODE", "TRANS_CODE", "POINT_TYPE_CODE", "POINTS_VALUE",
                         "EXPIRATION_DATE", "CARD_NUMBER", "TRUEPASS_NO", "SRC_TP_ACCRUAL_TRN_ID", "SRC_PTS_ACCRUAL_TRN_ID"))
        writer.writerow(('T', "0"))
    finally:
        trnpointtype.close()

    trnpointtype = open(
        tranPath + "/JETBLUE_TRN_POINT_TYPE_" + zera + ".csv", 'awt')
    try:
        writer = csv.writer(trnpointtype, delimiter='|')
        writer.writerow(("ROW_MARKER", "TRANS_POINT_TYPE_CODE", "TRANS_CODE", "POINT_TYPE_CODE", "POINTS_VALUE",
                         "EXPIRATION_DATE", "CARD_NUMBER", "TRUEPASS_NO", "SRC_TP_ACCRUAL_TRN_ID", "SRC_PTS_ACCRUAL_TRN_ID"))
        writer.writerow(('T', "0"))
    finally:
        trnpointtype.close()
