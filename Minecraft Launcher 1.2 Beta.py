import webbrowser
print('声明：当你退出后，将销毁密码（存档不会删除）！')
password = input('为了防止你的朋友、家长、小P孩偷看你的游戏内容，请务必设置密码：')
print('设置成功！！！')
game = input('你要启动启动器吗？(y/n)')
if game == 'y':
    passwordlocked = input('请输入进入密码：')
    if passwordlocked == password:
        print('欢迎使用fangdx1014制作的简易Minecraft启动器！(网页第三方)')
        home = input('您要干什么？1=Launcher Minecraft、2=version、3=open home、4=查看服务器:')
        if home == '1':
            mcver = input('请选择版本:1=1.5.2、2=1.8.8、3=1.12.2、4=Scratch')
            if mcver == '1':
                webbrowser.open('https://eaglercraft.ir/play/1.5.2?touch=false&userscript=')
                print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/1.5.2?touch=false&userscript=')
            elif mcver == '2':
                webbrowser.open('https://eaglercraft.ir/play/1.8.8?touch=false&userscript=')
                print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/1.8.8?touch=false&userscript=')
            elif mcver == '3':
                webbrowser.open('https://eaglercraft.ir/play/1.12.2?touch=false&userscript=')
                print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/1.12.2?touch=false&userscript=')
            elif mcver == '4':
                webbrowser.open('https://eaglercraft.ir/play/scratch/?touch=false&userscript=')
                print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/scratch/?touch=false&userscript=')
            else:
                print("❌输入错误！请输入1、2或者3")
        elif home == '2':
            print('简易Minecraft启动器————by fangdx1014')
            print('版本:1.2 beta(在和同学交流)')
            print('E-mail:fangdx_369@163.com or fangdx_369@outlook.com')
            print('BiliBili:https://space.bilibili.com/3690997611498020?spm_id_from=333.1007.0.0')
            print('原网页：https://eaglercraft.ir/。在此感谢这个团队！')
            print('抵制不良游戏，拒绝正版游戏，谨防受骗上当，适度游戏益脑，沉迷游戏伤身，合理安排时间，享受健康生活。')
            print('审批文号：国新出省[2077]1145号  ISBN:114-5-14-52052-0')
            print('出版单位：fangdx1014的学“牲”团队们')
            print('著作权人：fangdx1014的学“牲”团队们')
            print('本团队积极履行《网络游戏行业不防沉迷不自律公约》')
            yuansheng = input('输入“yuansheng”即可玩原神！')
            if yuansheng == 'yuansheng':
                webbrowser.open('https://ys.mihoyo.com/cloud/#/')
            else:
                print('输入错误！')
        elif home == '3':
            webbrowser.open('https://eaglercraft.ir/')
        elif home == '4':
            print('Minecraft 服务器（仅1.12.2）')
            print('梦幻王国群组服 - join.mcmhs.org')
            print('异事簿 - ishibu.fun')
            print('凌云仙梦 - s9-4.yxsjmc.cn:20032')
            print('绘梦师DreamPainter-IV - dp4.us')
            print('神秘荒野 - mp2.i9idc.com:13035 ')
        elif home == '5':
            print('你找到了我的小彩蛋！！！！请你玩个游戏')
            stupid_miao = int(input('1.萝卜；2.米老鼠；3.纸巾，请输入序号：'))
            if stupid_miao == 1:
                print('蒸蚌！')
            elif stupid_miao == 2:
                print('蒸蚌！')
            elif stupid_miao == 3:
                print('蒸蚌！')
            else:
                print('纸巾，纸巾，纸巾！！！')
        elif home == '6':
            easter_egg = input('你还挺细心嘛！输入“mj”请你看蜘蛛侠！！！')
            if easter_egg == 'mj':
                webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7/?spm_id_from=333.1387.favlist.content.click')
        else:
            print("❌输入错误！请输入1、2或者3")
    else:
        print('密码错误，请重试，还有，这只是一个学习程序！')
elif game == 'n':
    print('好的，请手动退出，退出后将销毁所有更改（除了游戏存档）！')
    pass

# 你还是去玩PCL吧！网址：https://ltcat.lanzouv.com/b0aj6gsid，提取码：pcl2
