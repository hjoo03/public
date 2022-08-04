# -*- coding: utf-8 -*-
# last update: 08/04/2022 (Initial Commit)

from PIL import Image
import piexif

def set_time(time_level:int, src:str, dst:str) -> None:
    t3 = time_level // 1440
    t2 = time_level // 60
    t1 = time_level % 60
    datetime_string = f"2000:00:{t3:02} {t2:02}:{t1:02}:00"
    zeroth_ifd = {
        piexif.ImageIFD.Make: u"Python",
        piexif.ImageIFD.DateTime: datetime_string,
        piexif.ImageIFD.ImageDescription: str(time_level),
        piexif.ImageIFD.ImageID: str(time_level),
        piexif.ImageIFD.XResolution: (300, 1),
        piexif.ImageIFD.YResolution: (300, 1),
        piexif.ImageIFD.Software: u"piexif"
    }
    exif_ifd = {
        piexif.ExifIFD.DateTimeOriginal: datetime_string,
        piexif.ExifIFD.DateTimeDigitized: datetime_string,
        piexif.ExifIFD.ImageUniqueID: str(time_level),
        piexif.ExifIFD.LensMake: u"LensMake",
        piexif.ExifIFD.Sharpness: 65535,
        piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1))
    }
    gps_ifd = {
        piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
        piexif.GPSIFD.GPSAltitudeRef: 1,
        piexif.GPSIFD.GPSDateStamp: datetime_string,
    }
    first_ifd = {
        piexif.ImageIFD.Make: u"Python",
        piexif.ImageIFD.XResolution: (300, 1),
        piexif.ImageIFD.YResolution: (300, 1),
        piexif.ImageIFD.Software: u"piexif"
    }

    exif_json = {"0th":zeroth_ifd, "Exif":exif_ifd, "GPS":gps_ifd, "1st":first_ifd}
    exif_bytes = piexif.dump(exif_json)
    img = Image.open(src)
    img.save(dst, exif=exif_bytes)