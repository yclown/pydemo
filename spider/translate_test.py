from urllib import request
from urllib import parse
import json
#blog http://blog.csdn.net/c406495762/article/details/59095864
#有道翻译爬虫
if __name__ == "__main__":
    # 对应上图的Request URL  
    request_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 创建Form Data字典，存储上图中的Form Data  
    Form_Data = {}
    Form_Data['i'] = 'Jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'
    # 使用urlencode方法转换标准格式  
    data = parse.urlencode(Form_Data).encode('utf-8')
    # 传递Request对象和转换完格式的数据  
    response = request.urlopen(request_url, data)
    #print(data)
    # 读取信息并解码  
    html = response.read().decode('utf-8')
    # 使用json  
    translate_results = json.loads(html)
    # 找到翻译结果
    print(translate_results)
    translate_result = translate_results["translateResult"][0][0]['tgt']
    # 打印翻译结果  
    print("翻译的结果是 %s" % translate_result)