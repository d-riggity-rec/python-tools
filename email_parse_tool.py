import win32com.client
import os
import os.path

############# Email Attachment Checking Tool ###############
'''
This script showcases a function that can be called to check
the most recent emails in an assigned Outlook inbox for attachments,
then saves them according to parameters set inside of the function.

Be sure to fill specified areas with appropriate email addresses and file
names for function to work.
'''

def email_attach_chk():

    try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        namespace = outlook.GetNamespace('MAPI')
        inbox = namespace.GetDefaultFolder(6)   #6 refers to the Inbox folder for Outlook app

        #########################################################################
        ###### Begin filtering through newest emails in the 'Inbox' folder ######
        #########################################################################

        inbox_itm = inbox.Items
        inbox_itm.sort('[ReceivedTime]', True)
        num_cnt = 0
        for email in inbox_itm:
            sub = email.Subject
            atch = email.Attachments
            atch_cnt = len(atch)  # no errors even no attachements! will be 0 for emails with no attachments..
            sndr = email.SenderEmailAddress

            #####################################################################
            #### Set Conditions for Specific Senders in this loop here ##########
            #####################################################################

            if sndr == 'insert sender email address' and sub == 'insert attachment file name':   # this is an EXACT match to whole subject name in email
                xl_path = 'insert file path attachment is to be saved in'
                print(sndr,'; ',sub,'; ', atch_cnt)
            for af in atch:
                xlnme = os.path.splitext(af.FileName)[0]
                xlext = os.path.splitext(af.FileName)[1]
                if '.xls' in xlext:
                    xl_save = xl_path + xlnme + xlext
                    af.SaveASFile(xl_save)


            if sndr == 'insert other sender email address' and 'insert other attachment file name' in sub:  # this checks subject for partial match
                xl_path = 'insert other file path attachment is to be saved in'
                print(sndr,'; ',sub,'; ', atch_cnt)     
                for af in atch:
                    # print(af)
                    xlnme = os.path.splitext(af.FileName)[0]
                    xlext = os.path.splitext(af.FileName)[1]
                    # print(xlnme,xlext)
                    if '.xls' in xlext:
                        xl_save = xl_path + xlnme + xlext
                        # print(xl_save)
                        af.SaveASFile(xl_save)

            #############################################################
            ### Variable below sets limit on how many emails to check ###
            #############################################################

            num_cnt = num_cnt + 1

            if num_cnt == 15:
                break

    except:
        print('')
