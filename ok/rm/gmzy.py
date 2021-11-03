import pygal

x_labels = [0,8,16,'24',32,"40",48,"56",64]
imgdir = "./img/"

xiantian = [100, 95, 90, 80, 70, 50, 40, 30, 20]
xiantianB = pygal.Line()
xiantianB.add('先天之精', xiantian)
xiantianB.x_labels = x_labels
xiantianB.render_to_file(imgdir +'xiantian.svg')                          # Save the svg to a file

houtian = [10, 30, 80, 80, 70, 50,  40, 30,20]
huoutianB = pygal.Line()
huoutianB.add('后天之精', houtian)
huoutianB.x_labels = x_labels
huoutianB.render_to_file(imgdir +'houtian.svg')                          # Save the svg to a file

shenjing = [x+y for x,y in zip(xiantian,houtian)]

shenjingB = pygal.Line()
shenjingB.add('先天之精', xiantian)
shenjingB.add('后天之精', houtian)

shenjingB.add('肾精=先天+后天', shenjing)
x_labels = [1,'8岁肾气实','16肾气盛','24肾气平均',32,"40岁肾气衰",48,"56岁肾脏衰",64]
shenjingB.x_labels = x_labels

# bar_chart.render()
shenjingB.render_to_file(imgdir +'shenjing.svg')                          # Save the svg to a file
