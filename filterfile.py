from PIL import Image

file=open("wider_face_train_bbx_gt.txt","r")
details=''
files=0
for rline in file:
  line = rline.strip()
  if line.endswith('.jpg') and (line.startswith('8') or line.startswith('49') or line.startswith('56')):
     print line
     skip = False
  elif line.endswith('.jpg') and not (line.startswith('8') or line.startswith('49') or line.startswith('56')):
     skip = True
  else:
   if skip:
     continue
   else:
     print line

