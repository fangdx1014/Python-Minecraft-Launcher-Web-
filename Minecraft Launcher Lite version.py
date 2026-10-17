import webbrowser
home = input('您要干什么？1=Launcher Minecraft、2=version、3=open home:')
if home == '1':
    mcver = input('请选择版本:1=1.5.2、2=1.8.8、3=1.12.2')
    if mcver == '1':
        webbrowser.open('https://eaglercraft.ir/play/1.5.2?touch=false&userscript=')
        print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/1.5.2?touch=false&userscript=')
    elif mcver == '2':
        webbrowser.open('https://eaglercraft.ir/play/1.8.8?touch=false&userscript=')
        print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/1.8.8?touch=false&userscript=')
    elif mcver == '3':
        webbrowser.open('https://eaglercraft.ir/play/1.12.2?touch=false&userscript=')
        print('启动完成！若无显示，请打开以下链接:https://eaglercraft.ir/play/1.12.2?touch=false&userscript=')
elif home == '2':
    print('简易Minecraft启动器————by fangdx1014')
    print('版本:Lite version(在和同学交流)')
    print('bilibili账号：https://space.bilibili.com/3690997611498020?spm_id_from=333.1007.0.0')
    print('E-mail:fangdx_369@163.com or fangdx_369@outlook.com')
    print('原网页：https://eaglercraft.ir/。在此感谢这个团队！')
elif home == '3':
    webbrowser.open('https://eaglercraft.ir/')
