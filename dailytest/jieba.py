import jieba
from wordcloud import WordCloud

s = '''
????
python
Python
PyCharm
Translation 
snake
today is clo
???
translation plugins
'''

cut_list = jieba.lcut(s)  # 分词
new_str = ' '.join(cut_list)  # 用空格从拼接成一个字符串
word_cloud = WordCloud(font_path='msyh.ttc').generate(new_str)  # 生成词云对象
word_cloud.to_file('test.png')  # 保存到图片
