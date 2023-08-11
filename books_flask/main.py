from flask import Flask,jsonify,request,json,abort
from books import Book
from settings import BOOK_LIST,RSA_1024_PRIV_KEY,REQUEST_LISTS,TITLES
import re
import rsa
import base64
import time

"""
接口说明：
1、返回的是json数据
2、结构如下：
{
    resCode:0,  # 非0即错误 1
    data:  # 数据位置，一般为数组
    message: '对本次请求的说明'
}
"""

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# 检查是否有特殊字符
def is_string_validate(str):
    sub_str = re.sub(u"([^\u4E00-\u9FA5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str) == len(sub_str):
        return False
    else:
        return True
# 解密
def get_secret_key(cryptdata):
    with open('rsa_private_key.pem','rb+') as privatefile:
        p = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)
    msg = rsa.decrypt(base64.b64decode(cryptdata),privkey)
    try:        
        result={
            "timespan":msg.decode().split(':')[0],
            "url":msg.decode().split(':')[1],
            "infos":msg.decode().split(':')[2]
        }
    except:
        result={
            "timespan":'',
            "url":'',
            "infos":''
        }
    return result

# 获得当前的13位时间戳
def get_now_time_13():
    return int(time.time() * 1000)

# 判断能不能访问数据
def is_allow_domain_time(timespan,url):
    if(int(time.time()*1000)-int(timespan)>300000):
        return True          
        
    if(url not in REQUEST_LISTS):
        return True
    
    return False

    
@app.errorhandler(404)
def handler_404_error(err):
    resData = {
            'resCode':404,
            'data':[],
            'message':'404'
            }
    return jsonify(resData)


@app.route('/')
def hello_world():
    book = Book()
    data = book.get_books_infos_limit()
    return jsonify(data)

@app.route('/books_cates')
def get_books_cates():
    resData = {
        'resCode':0,
        'data':[
            {"id":0,"text":'首页',"url":'/'},
            {"id":1,"text":'玄幻',"url":'/xuanhuan'},
            {"id":2,"text":'修真',"url":'/xiuzhen'},
            {"id":3,"text":'都市',"url":'/dushi'},
            {"id":4,"text":'历史',"url":'/lishi'},
            {"id":5,"text":'网游',"url":'/wangyou'},
            {"id":6,"text":'科幻',"url":'/kehuan'},
            {"id":7,"text":'言情',"url":'/yanqing'},
            {"id":8,"text":'其他',"url":'/qita'},
            {"id":9,"text":'完本',"url":'/wanben'}
        ],
        'message':'请求成功'
    }
    return jsonify(resData)


@app.route('/<string:book_cate>',methods=['POST'])
def get_cates_infos(book_cate):
    if is_string_validate(book_cate):
        # resData = {
        #     'resCode':404,
        #     'data':[],
        #     'message':'输入数据有误！'
        #     }
        # return jsonify(resData)
        abort(404)
        

    if request.method == 'POST':
        print("捕获到了post请求 book_cate:",book_cate)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']        
        # print(key,secretKey)
        secret_result = get_secret_key(secretKey)
        if secret_result['timespan'] == '':
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)
        # print(key,secretKey)
        if is_allow_domain_time(secret_result['timespan'],secret_result['url']):
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)

        # if(int(time.time()*1000)-int(secret_result['timespan'])>300000):
        #     resData = {
        #     'resCode':1,
        #     'data':[],
        #     'message':'你猜，你使劲猜！'
        #     }
        #     return jsonify(resData) 

        if book_cate not in BOOK_LIST:
            resData = {
            'resCode':404,
            'data':[],
            'message':'图书类别有误！'
            }
            return jsonify(resData) 

        if key == 'newest':
            # select * from book_infos where book_cate='xiuzhen' order by book_last_update_time desc limit 10
            book = Book()
            sql_data = book.get_cates_newest_books_30(book_cate)
            resData = {
            'resCode':0,
            'data':sql_data,
            'message':'最新的30本图书！'
            }
            return jsonify(resData)
        elif key == 'most':
            book = Book()
            sql_data = book.get_cates_most_books_30(book_cate)
            resData = {
            'resCode':0,
            'data':sql_data,
            'message':'阅读最多的30本图书！'
            }
            return jsonify(resData)
        else:
            resData = {
            'resCode':2,
            'data':[],
            'message':'参数有误！'
            }
            return jsonify(resData)


        return
    else:
        resData = {
        'resCode':1,
        'data':[],
        'message':'请求方法错误！'
        }
        return jsonify(resData)

# 图书首页信息
@app.route('/book/<int:book_id>',methods=['POST'])
def get_book_infos_by_id(book_id):
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)

        if secret_result['timespan'] == '':
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)


        if is_allow_domain_time(secret_result['timespan'],secret_result['url']):
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)


        book = Book()
        sql_data = book.get_book_infos_by_book_id(book_id)
        if key == 'index':            
            resData = {
            'resCode':0,
            'data':sql_data,
            'message':'图书信息！'
            }
            return jsonify(resData)
        elif key == 'cap20':
            if len(sql_data) == 0:
                resData = {
                    'resCode':5,
                    'data':[],
                    'message':'图书不存在！'
                    }
                return jsonify(resData)
            cap20_data = book.get_book_details_newest_20_by_book_id(book_id)
            resData = {
            'resCode':0,
            'data':cap20_data,
            'message':'最新20章图书信息！'
            }
            return jsonify(resData)
        elif key == 'capAll':
            if len(sql_data) == 0:
                resData = {
                    'resCode':5,
                    'data':[],
                    'message':'图书不存在！'
                    }
                return jsonify(resData)
            capAll_data = book.get_book_details_by_book_id(book_id)
            resData = {
            'resCode':0,
            'data':capAll_data,
            'message':'图书所有章节的信息！'
            }
            return jsonify(resData)
        else:
            resData = {
            'resCode':1,
            'data':[],
            'message':'请求参数错误'
            }
            return jsonify(resData) 
    else:
        resData = {
            'resCode':1,
            'data':[],
            'message':'请求方法错误'
            }
        return jsonify(resData) 

# 获取图书详情页接口
@app.route('/book/<int:book_id>/<int:sort_id>',methods=['POST'])
def get_book_detail_infos(book_id,sort_id):
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)

        if secret_result['timespan'] == '':
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)

        if is_allow_domain_time(secret_result['timespan'],secret_result['url']):
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)


        if is_string_validate(key):
            resData = {
            'resCode':1,
            'data':[],
            'message':'请求参数错误'
            }
            return jsonify(resData) 

        book = Book()
        sql_data = book.get_book_infos_by_book_id(book_id)
        if len(sql_data) == 0:
            # 不存在该图书
            resData = {
            'resCode':1,
            'data':[],
            'message':'不存在该图书信息'
            }
            return jsonify(resData) 
        # 该图书存在        
        sql_detail_data = book.get_book_detail_by_book_id_sort_id(book_id,sort_id)
        prev_data = book.get_prev_cap_id(book_id,sort_id)
        next_data = book.get_next_cap_id(book_id,sort_id)

        sql_detail_data[0]['book_name'] = sql_data[0]['book_name']
        print('prev_data=====',prev_data)
        if prev_data != None:
            sql_detail_data[0]['prev_sort_id'] = prev_data['sort_id']
        if next_data != None:
            sql_detail_data[0]['next_sort_id'] = next_data['sort_id']

        resData = {
            'resCode':0,
            'data':sql_detail_data,
            'message':'图书详情信息！'
            }
        return jsonify(resData)

    else:
        resData = {
            'resCode':1,
            'data':[],
            'message':'请求方法错误'
            }
        return jsonify(resData) 

# 搜索接口
@app.route('/search',methods=['POST'])
def search_infos():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        # print(is_string_validate(key))

        if secret_result['timespan'] == '':
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)

        if is_string_validate(key):
            resData = {
            'resCode':1,
            'data':[],
            'message':'请求参数错误'
            }
            return jsonify(resData) 
        if is_allow_domain_time(secret_result['timespan'],secret_result['url']):
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)

        book = Book()
        sql_data = book.search_infos_by_key(key)
        resData = {
            'resCode':0,
            'data':sql_data,
            'message':'图书搜索信息！'
            }
        return jsonify(resData)

    else:
        resData = {
            'resCode':1,
            'data':[],
            'message':'请求方法错误'
            }
        return jsonify(resData) 

# 获取关键词的接口
@app.route('/title',methods=['POST'])
def get_titles_infos():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey =get_data['secretKey']
        secret_result = get_secret_key(secretKey)


        if secret_result['timespan'] == '':
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)

        if is_allow_domain_time(secret_result['timespan'],secret_result['url']):
            resData = {
                'resCode':1,
                'data':[],
                'message':'你猜，你使劲猜'
                }
            return jsonify(resData)

        # if(int(time.time()*1000)-int(secret_result['timespan'])>300000):
        #     resData = {
        #         'resCode':1,
        #         'data':[],
        #         'message':'你猜，你使劲猜'
        #         }
        #     return jsonify(resData)
        
        # if(secret_result['url'] not in REQUEST_LISTS):
        #     resData = {
        #         'resCode':1,
        #         'data':[],
        #         'message':'你猜，你使劲猜'
        #         }
        #     return jsonify(resData)
        
        resData = {
                'resCode':0,
                'data':TITLES[secret_result['url']][key],
                'message':'首页的关键词'
                }
        return jsonify(resData)
        
    else:
        resData = {
            'resCode':1,
            'data':[],
            'message':'请求方法错误'
            }
        return jsonify(resData)  



if __name__ == '__main__':
    app.run()