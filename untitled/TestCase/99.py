
# -*- coding: utf-8 -*-

# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print ("%d*%d=%d"%(i,j,i*j),end=' ')
# #     print ('')
# #
# for ii in range(1,10):
#     for jj in range (1,ii+1):
#         print('%d * %d=%d' %(ii,jj,ii*jj),end=' ')
#     print('')
# list1=[5,6,1,2,3,4,5,1,2]
# aa=list(set(list1))
# print(aa)
# bb=sorted(aa,key=list1.index)
# print(bb)
# dic={}
# text='h h h a a a a  b b c d e'
# ll=text.split( )
# for i in ll:
#     dic[i]=ll.count(i)
# print(list(dic.items()))
# a=list(dic.values())
# b=sorted(list(dic.items()),key=lambda x:x[1],reverse=True)
# # print(b[:3])
# class Test:
#     a=1
#     b=2
#     c=3
#     def test1(self):
#         return self.a+self.b
#     def test2(self):
#         return self.a+self.c
#     @property
#     def test3(self):
#         return self.b+self.c

class Student:
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,nu):
        if not isinstance(nu,int):
            raise Exception('score must be an integer!')
        #elif nu<0 or nu >100:
            raise Exception
        self._score=nu
if __name__ == '__main__':
    s = Student()
   # tt=s.socre1((60))
    s.score = '123'
    print(s.score)



