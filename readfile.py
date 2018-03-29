from PIL import Image

file=open("wider_face_train_bbx_gt.txt","r")
details=''
for rline in file:
  line = rline.strip()
  if line.endswith('.jpg'):
	  #print "images/" + line
          if len(details) > 0:
	   print details
          details = [line]
	  with Image.open("images/"+line) as img:
            width, height = img.size
            details.append(width)
            details.append(height)

          xmins = list()
          ymins = list()
          xmaxs=list()
          ymaxs=list()
          details.append(xmins)
          details.append(ymins)
          details.append(xmaxs)
          details.append(ymaxs)
  else:
   data=line.split()
   if len(data) == 1:
        #this is how many bounding boxes there should be
	boxes=data[0]
   else:
     xmins.append(int(data[0]))
     ymins.append(int(data[1]))
     xmaxs.append(int(data[0])+int(data[2]))
     ymaxs.append(int(data[1])+int(data[3]))


print details

print "end"
