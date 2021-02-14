import cv2
import dropbox
import random
import time

startTime = time.time()

def take_Pic():


    num = random.randint(0, 100000000000000000000000000000000)

    VideoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):
        snp = "SnapshotForCamera" + str(num) + ".png"

        ret, frame = VideoCaptureObject.read()

        cv2.imwrite(snp, frame)

        global startTime

        startTime = time.time()

        result = False

    return(snp)
    VideoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(snp):
    access_token = 'E-x9-dSNM-0AAAAAAAAAAa8YDt0gjJEAla-4LblpgHoEsEWi8PxVmI4G8vIcEfju'

    dbx = dropbox.Dropbox(access_token)
    
    file_from = snp

    file_to = '/snapshotforwebcam/'+(snp)


    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("Files uploaded...")

def main():
    while(True):
        if(time.time()-startTime >= 300.0):
            name = take_Pic()
            upload_file(name)

if __name__ == '__main__':
    main()
