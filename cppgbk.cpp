#include <bits/stdc++.h>
#include <conio.h>
#include <cstdlib>
using namespace std;

int main(){
    cout<<"������\n����:A Normal Pickaxe\nBվ:https://space.bilibili.com/2036075820 | һ����ͨ��Pickaxe\n�����������ʼ\n";
    system("pause");
    system("cls");
    srand(time(0));
    int n=rand()%100+1,g=0,s=0;
    cout<<"��������һ��1~100������,���һ�����Ǽ�,�Ҹ����������˻���С��\n";
    while(g!=n){
        s++;
        cout<<"��:";
        cin>>g;
        if(g!=n)cout<<(g>n?"����\n":"С��\n");
        else{
            cout<<"���ã�����"<<s<<"��";
            break;
        }
    }
    system("pause");
    return 0;
}
