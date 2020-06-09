from skimage import io
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu as otsu
from skimage.measure import label, regionprops
import os, shutil, string

def leavesClass(a):
    if a>=1001 and a<=1059:
        return 'pubescent bamboo'
    elif a>=1060 and a<=1122:
        return 'Chinese horse chestnut'
    elif a>=1123 and a<=1194:
        return 'Chinese redbud'
    elif a>=1195 and a<=1267:
        return 'true indigo'
    elif a>=1268 and a<=1323:
        return 'Japanese maple'
    elif a>=1324 and a<=1385:
        return 'Nanmu'
    elif a>=1386 and a<=1437:
        return 'castor aralia'
    elif a>=1438 and a<=1496:
        return 'goldenrain tree'
    elif a>=1497 and a<=1551:
        return 'Chinese cinnamon'
    elif a>=1552 and a<=1616:
        return 'Anhui Barberry'
    elif a>=2001 and a<=2050:
        return 'Big-fruited Holly'
    elif a>=2051 and a<=2113:
        return 'Japanese cheesewood'
    elif a>=2114 and a<=2165:
        return 'wintersweet'
    elif a>=2166 and a<=2230:
        return 'camphortree'
    elif a>=2231 and a<=2290:
        return 'Japan Arrowwood'
    elif a>=2291 and a<=2346:
        return 'sweet osmanthus'
    elif a>=2347 and a<=2423:
        return 'deodar'
    elif a>=2424 and a<=2485:
        return 'maidenhair tree' 
    elif a>=2486 and a<=2546:
        return 'Crepe myrtle'
    elif a>=2547 and a<=2612:
        return 'oleander'
    elif a>=2616 and a<=2675:
        return 'yew plum pine'
    elif a>=3001 and a<=3055:
        return 'Japanese Flowering Cherry'
    elif a>=3056 and a<=3110:
        return 'Glossy Privet'
    elif a>=3111 and a<=3175:
        return 'Chinese Toon'
    elif a>=3176 and a<=3229:
        return 'peach'
    elif a>=3230 and a<=3281:
        return 'Ford Woodlotus'
    elif a>=3282 and a<=3334:
        return 'trident maple'
    elif a>=3335 and a<=3389:
        return 'Beale\'s barberry'
    elif a>=3390 and a<=3446:
        return 'southern magnolia'
    elif a>=3447 and a<=3510:
        return 'Canadian poplar'
    elif a>=3511 and a<=3563:
        return 'Chinese tulip tree'
    elif a>=3566 and a<=3621:
        return 'tangerine'
    else:
        return 'unknown'

f=open('feature.csv','w')
f.write('area,bbox_area,centroidX,centroidY,convex_area,eccentricity,equivalent_diameter,euler_number,extent,filled_area,major_axis_length,.minor_axis_length,orientation,perimeter,solidity,kelas\n')
for i in os.listdir('.'):
    if i.endswith('.jpg'):
        temp=i.split('.')
        kelas=leavesClass(int(temp[0]))
        img=io.imread(i)
        imgGray=rgb2gray(img)
        threshold=otsu(imgGray,256)
        x,y=imgGray.shape
        for k in range(x):
            for l in range(y):
                if imgGray[k][l]>threshold:
                    imgGray[k][l]=0
                else:
                    imgGray[k][l]=1

        imgLabel=label(imgGray)
        props=regionprops(imgLabel)
        centroid=props[0].centroid
        f.write(str(props[0].area)+','+str(props[0].bbox_area)+','+str(centroid[0])+','+str(centroid[1])+','+str(props[0].convex_area)+','+str(props[0].eccentricity)+','+str(props[0].equivalent_diameter)+','+str(props[0].euler_number)+','+str(props[0].extent)+','+str(props[0].filled_area)+','+str(props[0].major_axis_length)+','+str(props[0].minor_axis_length)+','+str(props[0].orientation)+','+str(props[0].perimeter)+','+str(props[0].solidity)+','+kelas+'\n')

f.close()
