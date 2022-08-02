import cv2,os
import numpy as np
import pydicom as PDCM
from tqdm import tqdm
import pandas as pd
import argparse
from glob import glob
from pathlib import Path

def dcm2png(dicom_dosya_yolu):
    # dicom resim çekilmiş ct görüntüsü hastaya ait bütün bilgileri içermektedir.
    # hastaya ait bilgilerede ulaşmak için (yaş,isim vb.) kodu düzenleyebilirsiniz
    dicom_resim= PDCM.read_file(dicom_dosya_yolu)
    #print(dicom_resim)
    satirlar=dicom_resim.get(0x00280010).value
    sutunlar=dicom_resim.get(0x00280011).value

    try:
        pencere_merezi = int((dicom_resim.get(0x00281050).value)[0])
        pencere_genişlik = int((dicom_resim.get(0x00281051).value)[0])
    except:
        pencere_merezi = int(dicom_resim.get(0x00281050).value)
        pencere_genişlik = int(dicom_resim.get(0x00281051).value)

    max=int((pencere_merezi+pencere_genişlik)/2)
    min=int((pencere_merezi-pencere_genişlik)/2)

    if (dicom_resim.get(0x00281052) is None):
        kesisimi_yeniden_olceklendirme = 0

    else:
        kesisimi_yeniden_olceklendirme = int(dicom_resim.get(0x00281052).value)
    
    if (dicom_resim.get(0x00281053) is None):
        eğimi_yeniden_olceklendirme = 1
    
    else:
        eğimi_yeniden_olceklendirme = int(dicom_resim.get(0x00281053).value)

    
    yeni_gorsel=np.zeros((satirlar,sutunlar), np.uint8)
    pikseller=dicom_resim.pixel_array

    for i in range(satirlar):
        for j in range(sutunlar):
            piksel_degeri = pikseller[i,j]
            yeni_piksel_degeri=piksel_degeri*eğimi_yeniden_olceklendirme + kesisimi_yeniden_olceklendirme

            if (yeni_piksel_degeri > max):
                yeni_gorsel[i][j]=255
            elif (yeni_piksel_degeri < min):
                yeni_gorsel[i][j]=0
            else:
                yeni_gorsel[i][j]=int(((yeni_piksel_degeri-min)/(max-min))*255)
    
    return yeni_gorsel


def main(args):
    path= glob(args["input"]+"/*.dcm")
    if not os.path.exists(args["output"]):
        filepath = Path(args["output"])
        filepath.mkdir(parents=True, exist_ok=True)
        
    for dcm_path in tqdm(path):
        dcm_path = dcm_path.replace("\\","/")
        img_name = dcm_path.split("/")[-1].split(".dcm")[0]
        png_formatindaki_hali = dcm2png(dcm_path)
        cv2.imwrite(f"{args['output']}/{img_name}.png",png_formatindaki_hali)
    
        
    
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,help="path to input directory of DICOM images")
    ap.add_argument("-o", "--output", required=True,help="path to output directory of PNG images")
    args = vars(ap.parse_args())
    main(args)
    print("Bitti")

