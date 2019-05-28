import time
print('项目终于交工了，在这个周五的晚上，你是更想：')
time.sleep(2)

print('1.回家吃，外卖好料\n2.带然然下馆子吃大餐庆祝\n3.顺路买还不错的简餐，带回家\n4.回家吃，让然然做')
time.sleep(2)

answer=int(input('你的选择是：'))

if answer<=2:
      print('哇，猪猪要破费了哦')
      time.sleep(2)
      if answer==1:
            print('我有点想吃豆腐鱼汤😝')
            time.sleep(2)
      if answer==2:
            print('要不我请客？')
             
             
else:
      print('好啊，这样比较省')
      time.sleep(2)
      if answer==3:
            print('那就辛苦你去买一下啦')
      else:
            print('我也想给你做顿大餐犒劳一下你呢！')
                   
time.sleep(2)                   
print('你想吃什么呢？')