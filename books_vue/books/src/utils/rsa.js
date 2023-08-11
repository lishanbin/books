import { JSEncrypt } from "jsencrypt";

export function rsaEncrypt(data) {
    console.log("in RSA data = ",data);
    const publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBuNS4I+PhvPw4tf4qWgvx8XrDxnoIDGXQGtywxXL7JcoLthANakGZ+rXizZTdZRZ8SWMJl/5FgeowhhZ+k1ZWGF0tfziGirOIvBXbXMQC3g4KPN7aYdNIYFVpjWtN902yYSc53a1Uw6aKVo6XhMAdctzRqJIWyxMiEDTfOZhRHQIDAQAB";
    const jse = new JSEncrypt();
    jse.setPublicKey(publicKey);
    const result = jse.encrypt(data);
    console.log("in RSA result = ",result);
    return result
}