import pygal
import math

def ang2arc(ang):
    return ang*math.pi/180
def ang2yang(ang):
    return (math.sin(ang2arc(ang)/2))**2

year_days = 360
nliuqi = 6
nwuxig = 5

x_labels = [i+1 for i in range(year_days)]
imgdir = "./img/"

liuqi = [i+1 for i in range(year_days)]
liuqi = []
angs = int(year_days/nliuqi)
for i in range(nliuqi):
    liuqi.extend([(i+1)*angs for j in range(angs)])
print(liuqi)
liuqi = [i for i in liuqi]
# liuqi = [ang2yang(i) for i in range(year_days)]

xiantianB = pygal.Line()
xiantianB.add('六气', liuqi)
xiantianB.x_labels = x_labels
xiantianB.render_to_file(imgdir +'yunqi.svg')   