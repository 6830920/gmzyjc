import diagrams
from diagrams import Cluster, Diagram,Edge
# from diagrams.aws.compute import *
from diagrams.aws import compute,analytics
# from diagrams.aws.analytics import *
from diagrams.aws.database import RDS
# from diagrams.aws.network import Route53
# from diagrams.onprem.logging import *

# 连接线颜色
# http://www.graphviz.org/doc/info/colors.html

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}
# 方向可以使：TB\LR
with Diagram("津液", show=False,outformat="jpg",filename="jinye", direction="TB"):
    

    with Cluster("炼油厂-腑（化物而不藏）"):
        胃 = RDS("胃-降浊")
        小肠 = RDS("小肠(泌别清浊)")
        回肠 = RDS("回肠")
        大肠 = RDS("大肠")
        大肠-RDS("大便")
        
        膀胱 = RDS("膀胱")
        膀胱-RDS("小便")

    with Cluster("内部使用-脏（藏精气而不泄）"):
        肺 = RDS("肺-水之上源-（高位水箱）")
        三焦 = RDS("三焦（水管）")
        
        肾 = RDS("肾（污水处理厂）")
        脾 = RDS("脾-升清-（水泵）")
        小肠-脾
    with Cluster("身体组织"):
        皮毛 = RDS("皮毛")
        with Cluster('内'):
            with Cluster('津'):
                肌肤 = RDS("肌肤")
            with Cluster('液'):
                骨髓 = RDS("骨髓")
                脑髓 = RDS("脑髓")
                脏腑 = RDS("脏腑")

        三焦 >>Edge(color="green2") >> 肌肤
        三焦 <<Edge(color="darkslateblue") << 肌肤
        三焦 >>Edge(color="green2") >> [骨髓,脑髓,脏腑]
        三焦 <<Edge(color="darkslateblue") << [骨髓,脑髓,脏腑]

    胃 >> 脾 >> Edge(color="green2",label="脾气散精，上归于肺") >> 肺 
    肺 >>Edge(color="green2",label="宣发清中之清") >> 皮毛
    肺 >>Edge(color="green2",label="肃降清中之浊") >> 三焦
    肺 <<Edge(color="green2",style="dotted" ,label="肾过滤后的水回归到肺") << 三焦

    胃 >>小肠 >>回肠>> 大肠
    回肠>>膀胱
    小肠 >>膀胱
    三焦 >>Edge(label="污水") >> 肾
    膀胱 >>Edge(color="green2",style="dotted" ,label="蒸化部分水") >> 肺
    肾>>Edge(color="green2",style="dotted" ,label="浊中之清")>>三焦
    肾>>Edge(label="浊中之浊",color="dark")>>膀胱

    肌肤>>RDS("汗")


with Diagram("diagrams图标", show=False,outformat="jpg",filename="diagrams", direction="TB"):

    # a = Fluentbit('test')
    # diagrams.onprem.logging.Fluentd()
    # diagrams.onprem.logging.Loki()
    # AutoScaling()
    # b =Analytics()
    # Athena()
    # CloudsearchSearchDocuments()
    
    

    with Cluster("aws.compute"):   
        # 通过dir函数获得方法名称
        # 通过getattr函数获得实际的方法，然后加个括号就可以执行了。
        mlist = [ method for method in dir(compute) if method.startswith('_') is False and callable(getattr(compute,method))]
        for method in mlist:
            getattr(compute,method)(method)
    
    with Cluster("aws.analytics"):   
        # 通过dir函数获得方法名称
        # 通过getattr函数获得实际的方法，然后加个括号就可以执行了。
        mlist = [ method for method in dir(analytics) if method.startswith('_') is False and callable(getattr(analytics,method))]
        print(mlist)
        for method in mlist:
            getattr(analytics,method)(method)
    
