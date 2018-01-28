import os
import shutil
import getPhotoEXIF
photo_dir=input("dir of photo folder:")
pic_spare_root = (r"D:\\pic_spare")

def winDirTrans(win_dir):
	abs_dir = win_dir.replace('\\','/')
	return abs_dir

photo_dir = winDirTrans(photo_dir)
print(photo_dir)
files = os.listdir(photo_dir)
print(files)
#os.makedirs(r“c：\python\test”)
pic_suffix_list = ['.jpg', '.png', '.JPG', '.PNG']
vid_suffix_list = ['.MOV', '.MOV','.mp4' ,'.MP4']
emoji_suffix_list = ['.gif', '.GIF']
for file in files:
	pic_full_path = os.path.join(photo_dir,file)
	suffix = os.path.splitext(file)[1]
	print('suffix:')
	print(suffix)
	if suffix in pic_suffix_list:
		print("find a pic")
		print(pic_full_path)
		#pic_addr = getPhotoEXIF.getPhotoAddr(pic_full_path)
		#print(pic_addr)
		pic_date = getPhotoEXIF.getPhotoDate(pic_full_path)
		print(pic_date)
		if pic_date == 'NA':
			print('no date info in this pic')
			folderName = 'no_date'
			dest_path = os.path.join(pic_spare_root,folderName)
		else:
			#copy the pictures to corresponding folder according to the date.
			pic_date_str = str(pic_date)
			yyyy = pic_date_str[:7].split(':')[0]
			mm = pic_date_str[:7].split(':')[1]
			folderName = yyyy+mm+'XX'
			print('generate folder:')
			dest_path = os.path.join(pic_spare_root,folderName)
			print(dest_path)
		if os.path.isdir(dest_path):
			print("folder already there, now copy pic")
		else:
			print("folder not exist, generate folder", dest_path)
			os.makedirs(dest_path)
		#copy pic file into date folder
		try:
			shutil.move(pic_full_path, dest_path)
		except:
			print('moving failed')
			print(pic_full_path)
	elif suffix in vid_suffix_list:
		dest_path = os.path.join(pic_spare_root,'VIDEO')
		shutil.move(pic_full_path, dest_path)
	elif suffix in emoji_suffix_list:
		dest_path = os.path.join(pic_spare_root,'emoji')
		shutil.move(pic_full_path, dest_path)
