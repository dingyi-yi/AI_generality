'''
Created on 2020年10月24日
启发式搜素——全局优先搜索解决8数码问题
@author: dingxinlong
'''
import  GlobalOptimal  as GO
if __name__=='__main__':
    glo=GO.globalOptimal()
    #list=[1,3,2,4,0,5,6,7,8 ]
    print("输入起始状态")
    for i in range(9):
        a=input("第"+str(i)+"个数")
        list.append(int(a))

    glo.start(S0=list)