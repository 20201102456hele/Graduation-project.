import SparkApi

# 以下密钥信息从控制台获取
appid = "9f4c599b"
api_secret = "ODA0YTUyYjAyMmYxZjUwZTA2OTE4Mzlh"
api_key = "7efb829af861f183c67375e0ace1771d"

domain = "generalv3"

Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"  # v1.5环境的地址

text = []


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text




if __name__ == '__main__':
    text.clear
    while (1):
        Input = input("\n" + "我:")
        content = "帮我识别评论信息是好评还是差评， 只需要回复我是好评还是差评就行。以下是评论信息：" + Input
        question = checklen(getText("user", content))

        SparkApi.answer = ""
        print("星火:", end="")
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        getText("assistant", SparkApi.answer)
        # print(str(text))
