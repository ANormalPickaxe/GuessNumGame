from random import randint
print('猜数字\n作者:A Normal Pickaxe\nB站:https://space.bilibili.com/2036075820 | 一个普通的Pickaxe\n按下任意键开始')
input()
print('我现在想一个1~100的数字,你猜一猜他是几,我告诉你他大了还是小了\n')
n,g,s = randint(1, 100),0,0
while n!=g:
    g = int(input('猜:'))
    s+=1
    if g!=n:
        print('大了' if g>n else '小了')
    else:
        print(f'正好，猜了{s}次')
        break
input()
