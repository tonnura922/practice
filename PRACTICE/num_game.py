print("数字ゲームをしましょう")
print("15言ったら負けです。最大の数字を三つまで言えます")
print("数字は次のように入力してください例5,6,7と入力したい場合→: 5 6 7 ")
print("私が先行です\n")
print("1 2\n")
x=2


while x<15:
    print("あなたの番です。数字を入力してください")
    a=list(map(int,input().split()))
#ルール違反
    if len(a)>3:
        print("ルール違反です、あなたの負けです。")

        break
    if a[0]!=x+1:
        print("ルール違反です、あなたの負けです。")

        break
    
    if a[0]>=15:
        print("あなたは15を言いました。")
        break
#判定
    if len(a)==1:
        print(a[0]+1,"",end="")
        print(a[0]+2,"",end="")
        print(a[0]+3,end="")
        x=a[0]+3
        
    if len(a)==2:
        print(a[1]+1,"",end="")
        print(a[1]+2,end="")
        x=a[1]+2
        
    if len(a)==3:
        print(a[2]+1)
        x=a[2]+1


print("私の勝利です。＾＾")