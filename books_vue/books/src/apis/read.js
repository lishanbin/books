import service from "@/utils/request.js";
import { rsaEncrypt } from "@/utils/rsa.js";

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
            secretKey:rsaEncrypt(new Date().getTime()+':'+'www.weqan.com'+':'+'otherinfos')  //预留字段给加密用
        }
    });
}