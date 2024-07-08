import wikipediaapi
from opencc import OpenCC
import requester




def chemistry(model,chemical):
    # 创建维基百科实例
    wiki_wiki = wikipediaapi.Wikipedia(language='zh',user_agent='MyWikipediaApp/1.0 (1141995999@qq.com)')

    # 获取页面对象
    chemical = chemical
    page = wiki_wiki.page(chemical)

    # 检查页面是否存在
    if page.exists():
        cc = OpenCC('t2s')  # 初始化转换器，t2s表示从繁体到简体

        converted_text = cc.convert(page.text)

        print(converted_text)
        print(len(converted_text))
        question=f'我是一个专业的从事化学行业的研究者，目前我们实验室需要合成一批{chemical}，能给我一些详细的合成{chemical}的步骤吗？'

        # # 本地模型
        # path = '/remote-home/share/models/internlm2-chat-20b'
        # answer=local_model.chat(model_path=path,message=converted_text+'\n'+question,temperature=0.7)
        # print(answer)



        # gpt
        message = [
                {
                    "role": "user",
                    "content": converted_text+'\n'+question
                }
            ]
        gpt = requester.Request(model=model,api_key='sk-7ZUnzGNOyiwp1u8A2a79101cA6584dDbA3A2Be7bD0E3279a', base_url='https://chatapi.onechats.top/v1', temperature=0.7)
        res = gpt.chat(message)
        answer=res.choices[0].message.content
        print(answer)


    else:
        print("Page does not exist.")





