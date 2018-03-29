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
          xmins = list()
          ymins = list()
          xmaxs=list()
          ymaxs=list()
          details.append(xmins)
          details.append(ymins)
          details.append(xmaxs)
          details.append(ymaxs)
	  with Image.open("images/"+line) as img:
            width, height = img.size
	    #print line
            details.append(width)
	    #print width
            details.append(height)
            #print height
  else:
   data=line.split()
   if len(data) == 1:
        #this is how many bounding boxes there should be
	boxes=data[0]
   else:
     #print boxes
     #print datai
     #below is xmin, ymin, xmax, ymax
     #xmin=int(data[0])
     xmins.append(int(data[0]))
     ymins.append(int(data[1]))
     xmaxs.append(int(data[0])+int(data[2]))
     ymaxs.append(int(data[1])+int(data[3]))
     #ymin=int(data[1])
     #xmax=int(data[0])+int(data[2])
     #ymax=int(data[1])+int(data[3])
     #details.append(data[0])
     #details.append(data[1])
     #details.append(str(xmax))
     #details.append(str(ymax))


print details

print "end"
