from flask import Flask,jsonify,request,json
from books import Book
from settings import BOOK_LIST

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
    if request.method == 'POST':
        print("捕获到了post请求 book_cate:",book_cate)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        print(key,secretKey)

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
            pass
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



if __name__ == '__main__':
    app.run()