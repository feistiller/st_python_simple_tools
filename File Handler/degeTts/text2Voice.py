import edge_tts
import os
import asyncio


async def init_function():
    f = open(os.path.dirname(__file__) + "\\word.txt", "r+", encoding="utf-8")
    text = f.read()
    print("需要转化文字" + text)
    if len(text) < 1:
        print("文件内容信息为空")
    else:
        v = input("输入音频增强（数字 default 0）")
        if v == "":
            v = "0"
        os.system("edge-tts --list-voices")
        voice = input("选择voice类型，输入全称")
        if len(voice) < 1:
            voice = 'zh-CN-YunxiNeural'
        tts = edge_tts.Communicate(text=text, voice=voice, volume="+"+v+"%")
        await tts.save(os.path.dirname(__file__) + "\\trans.mp3")


if __name__ == '__main__':
    asyncio.run(init_function())
