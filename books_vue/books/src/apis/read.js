import service from "@/utils/request.js";

export function GetCates() {
    return service({
        method:'get',
        url:"/books_cates"
    });
}