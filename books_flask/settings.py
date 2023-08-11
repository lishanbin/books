MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'books'

BOOK_LIST = [
    'xuanhuan',
    'xiuzhen',
    'dushi',
    'lishi',
    'wangyou',
    'kehuan',
    'yanqing',
    'qita',
    'wanben'
    ]

RSA_1024_PRIV_KEY = b'-----BEGIN RSA PRIVATE KEY-----\n \
MIICXAIBAAKBgQDBuNS4I+PhvPw4tf4qWgvx8XrDxnoIDGXQGtywxXL7JcoLthANakGZ+rXizZTdZRZ8SWM \
Jl/5FgeowhhZ+k1ZWGF0tfziGirOIvBXbXMQC3g4KPN7aYdNIYFVpjWtN902yYSc53a1Uw6aKVo6XhMAdctz \
RqJIWyxMiEDTfOZhRHQIDAQABAoGAD7XwsnpeqdkMz4Ca+05QN6/w193J2cs/mpADI+bve0TGTQrX5G6goV8 \
+zwUDNK1VFIFTId0MxxBRMNw/CMbkMnUjxX7pPmQgbAMYHtiDr2+xUUGsZ8/9ddHuAvextyEi15zy7uMtn1X \
Bf9tKUeohgPN3e4vqRdosyWNbNQ4b8hUCQQDnP38UrCTmBTciBy2quHYr8HPqRiOBDseEo7Nsa4/FXshicgC \
CHzH0aMuU7p4+mdEQwQ17yd7T5oqG5VFu71q7AkEA1nUSOwWA1jRCsZqaNL2rEe3C4FDgSAV848tK1IcAF7u \
IkOmKLJG5QrO4pkIjKAamT02RoU2mAJV4LHePRQAiBwJAY5TmZsKSyTMpwM+SjNgOm3FamWJG28a/iJDuLRx \
Mt1PPuwUYzvAcFQIj2SjAoHignTRlWA9gk6PNt7V80eblDQJABndRLWZlFBBPUnuO2rg9SDUbAxhtKr6/nT6 \
r6uyHHDATVgs0l1Nteo1gq+KinLpWmV2FXo+wyaO4E98m+rWeUQJBAI9CjUZQ09Y65kPwzQZhKqfA8ckugDib \
oIrFwUuwhGkb9Uab/flw5Qumlzp33Fa97VJb1i8mOWt9O/gfEoIUBqA=\n-----END RSA PRIVATE KEY-----'


REQUEST_LISTS = [
    'www.weqan.com'
]
'''
表一字段：id,域名

表二字段：id,标识：修真

表三字段：id,表一的id,表二的id,title,keywords,descriptions
'''

TITLES = {
    'www.weqan.com':{
        "index":['维千网首页标题','维千网首页关键词','维千网首页描述'],
        "xuanhuan":['玄幻分类页标题','玄幻分类页关键词','玄幻分类页描述'],
        "xiuzhen":['修真分类页标题','修真分类页关键词','修真分类页描述'],
        "dushi":['都市分类页标题','都市分类页关键词','都市分类页描述'],
        "lishi":['历史分类页标题','历史分类页关键词','历史分类页描述'],
        "wangyou":['网游分类页标题','网游分类页关键词','网游分类页描述'],
        "kehuan":['科幻分类页标题','科幻分类页关键词','科幻分类页描述'],
        "yanqing":['言情分类页标题','言情分类页关键词','言情分类页描述'],
        "qita":['其他分类页标题','其他分类页关键词','其他分类页描述'],
        "wanben":['完本分类页标题','完本分类页关键词','完本分类页描述'],
        "bookindex":['小说主页标题','小说主页关键词','小说主页描述'],
        "bookdetail":['小说详情页标题','小说详情页关键词','小说详情页描述'],
    }
}