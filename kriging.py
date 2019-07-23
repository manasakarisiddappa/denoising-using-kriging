import numpy as np
import cv2

def inter(im):
	m = 3
	for i,x in zip(range(0,im.shape[0]-m),range(1,im.shape[0]-1)):
		for j,y in zip(range(0,im.shape[1]-m),range(1, im.shape[1]-1)):
			grid = im[i:i+m,j:j+m]
			pure = []; rowid = []; colid = []
			for k in range(m):
				for h in range(m):
					if(grid[k,h] > 0 and grid[k,h] < 255):
						pure.append(grid[k,h])
						rowid.append(k)
						colid.append(h)
			if len(pure) == 0 or len(pure) == 1 or len(pure) == 2:
				continue
			wtmat = np.zeros((len(pure),len(pure)))
			for a in range(len(pure)):
				for b in range(len(pure)):
					wtmat[a,b] = np.square(rowid[a] - rowid[b]) + np.square(colid[a] - colid[b])

			wt = np.sum(wtmat,axis = 0)/(2*len(pure))
			wtsum = np.sum(wt) ; numerator = 0
			for s in range(len(pure)):
				numerator += pure[s]*wt[s]

			im[x,y] = numerator/wtsum;

	return im





im = cv2.imread('n3.jfif')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
copying = im.copy()
print(im.shape)
gr = inter(im)
stacked = np.hstack((copying,gr))
cv2.imshow('image',stacked)
cv2.waitKey(0)