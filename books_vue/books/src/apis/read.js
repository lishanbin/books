import service from "@/utils/request.js";

export function GetCates() {
    return service({
        method:'get',
        url:"/books_cates"
    });
}

export function GetInfoPost(postParams){
    return service({
        method:'post',
        url:postParams.url,
        data:{
            key:postParams.key,
            secretKey:'大家好，我是secretKey'  //预留字段给加密用
        }
    });
}