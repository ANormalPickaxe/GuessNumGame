#include <bits/stdc++.h>
#include <conio.h>
#include <cstdlib>
using namespace std;

int main(){
    cout<<"猜数字\n作者:A Normal Pickaxe\nB站:https://space.bilibili.com/2036075820 | 一个普通的Pickaxe\n按下任意键开始\n";
    system("pause");
    system("cls");
    srand(time(0));
    int n=rand()%100+1,g=0,s=0;
    cout<<"我现在想一个1~100的数字,你猜一猜他是几,我告诉你他大了还是小了\n";
    while(g!=n){
        s++;
        cout<<"猜:";
        cin>>g;
        if(g!=n)cout<<(g>n?"大了\n":"小了\n");
        else{
            cout<<"正好，猜了"<<s<<"次";
            break;
        }
    }
    system("pause");
    return 0;
}
