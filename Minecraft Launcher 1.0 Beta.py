import webbrowser
print('欢迎使用fangdx1014制作的简易Minecraft启动器！(网页第三方)')
home = input('您要干什么？1=Launcher Minecraft、2=version、3=open home:')
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
    print('版本:1.0 beta(在和同学交流)')
    bilibili = input('bilibili账号：https://space.bilibili.com/3690997611498020?spm_id_from=333.1007.0.0 ，输入隐藏代码：lemon访问。')
    print('E-mail:fangdx_369@163.com or fangdx_369@outlook.com')
    print('原网页：https://eaglercraft.ir/。在此感谢这个团队！')
    if bilibili == 'lemon':
        webbrowser.open('https://space.bilibili.com/3690997611498020?spm_id_from=333.1007.0.0')
    else:
        print('输入错误！')
elif home == '3':
    webbrowser.open('https://eaglercraft.ir/')
elif home == '4':
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
elif home == '5':
    easter_egg = input('你还挺细心嘛！输入“mj”请你看蜘蛛侠！！！')
    if easter_egg == 'mj':
        webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7/?spm_id_from=333.1387.favlist.content.click')
else:
    print("❌输入错误！请输入1、2或者3")
    
# 你还是去玩PCL吧！网址：https://ltcat.lanzouv.com/b0aj6gsid，提取码：pcl2
