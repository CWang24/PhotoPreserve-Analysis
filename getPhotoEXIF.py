# -*- coding:utf-8 -*-
import exifread
from geopy.geocoders import Nominatim

#Note that the dictionary keys are the IFD name followed by the tag name. For example:
#'EXIF DateTimeOriginal', 'Image Orientation', 'MakerNote FocusMode'

def HHMMSS2degree(x):
  #transform the format of longitude and latitude from hr, min, sec to degree.
	x[0]=int(x[0])
	x[1]=int(x[1])
	x[2] = int(x[2].split('/')[0])/int(x[2].split('/')[1])
	y = x[0]+x[1]/60+x[2]/3600
	return y

def getPhotoAddr(path):
	pic_content = open(path, 'rb')
	exif_data = exifread.process_file(pic_content)
	try:
		la = exif_data['GPS GPSLatitude'].printable[1:-1].split(', ')
		lo = exif_data['GPS GPSLongitude'].printable[1:-1].split(', ')
		lat = HHMMSS2degree(la)
		lon = HHMMSS2degree(lo)
		#to make xx look like: "121.629371, 31.220263"
		xy = str(lat),str(lon)
		geolocator = Nominatim()
		print(xy)
		try:
			location = geolocator.reverse(xy)
			return location.address
		except:
			print("geo reverse failed")
			return "failed"
	except:
		print('this pic does not contain GPS info in its EXIF')
		return('NA')

def getPhotoDate(path):
	f = open(path, 'rb')
	data = exifread.process_file( f )
	try:
		return data['EXIF DateTimeOriginal']
	except:
		print('this pic does not have date info in its EXIF')
		return('NA')
#import io
#import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  
#location = geolocator.reverse("121.629371, 31.220263")
if __name__ == "__main__":
	main()
