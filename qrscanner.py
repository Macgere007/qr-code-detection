import cv2
from pyzbar import pyzbar

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        x, y , w, h = qrcode.rect
      
        qrcode_info = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (116, 0, 179), 2)
      
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, qrcode_info, (x, y - 10 ), font, 0.6,(255, 159, 243), 2)
     
        with open("QRCode_result.txt", mode ='w') as file:
            file.write("Recognized QRCode:" + qrcode_info)
    return frame

def main():
    
    camera = cv2.VideoCapture('http://0.0.0.0:4747/video')
    ret, frame = camera.read()
    
    while ret:
        ret, frame = camera.read()
        frame = read_qrcodes(frame)
        cv2.imshow('QRCode Scanner by RJS', frame)
        if cv2.waitKey(1) & 0xFF == 27:
           break
    
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
