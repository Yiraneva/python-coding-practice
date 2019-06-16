# 作者：python教程
# 链接：https://www.zhihu.com/question/27699413/answer/327777872
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Animal(object):
    '''
    猪和鸭子的基类（基因图纸表）
    '''
    def __init__(self, name): # 实例化的时候传入要制作的东西名字，如猪、鸭子
        self.name = name 
    def makeMoth(self):
        #这里可以放其他制作细节  
        print(self.name+'的嘴巴 制作完毕') #这里的self.name就是获取我们传入的name

    def makeEar(self):
        #这里可以放其他制作细节  
        print(self.name+'的耳朵 制作完毕') 

    def makeEye(self):
        #这里可以放其他制作细节  
        print(self.name+'的眼睛 制作完毕') 

    def makeHead(self):
        #这里可以放其他制作细节  
        print(self.name+'的头 制作完毕') 

    def makeBody(self):
        #这里可以放其他制作细节  
        print(self.name+'的身体 制作完毕') 

    def makeFoot(self):
        #这里可以放其他制作细节  
        print(self.name+'的脚 制作完毕') 

    def makeMerge(self):
        #这里可以放其他制作细节  
        print(self.name+'合并完毕') 

    def makeAll(self): 
        # 一条龙。直接跑完整个流水线
        self.makeMoth()
        self.makeEar()
        self.makeEye()
        self.makeHead()
        self.makeBody()
        self.makeFoot()
        self.makeMerge()
    
    def whoamI(self):
      print(self)

pig = Animal('Pig')
# pig.makeAll()
pig.whoamI()

duck = Animal('Duck')
# duck.makeAll()
duck.whoamI()