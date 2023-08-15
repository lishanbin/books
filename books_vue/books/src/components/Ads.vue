<template>
    <b-container>
        <div id="main-top-ad">
            <a :href="rowAdsData.data.url" target="_blank">
                <img id="top-img" :src="rowAdsData.data.img_path" :alt="rowAdsData.data.alt" />
            </a>
        </div>
        <div id="main-left-ad">
            <a :href="colAdsData.data[0].url" target="_blank">
                <img id="left-img" :src="colAdsData.data[0].img_path" :alt="colAdsData.data[0].alt" />
            </a>
        </div>
        <div id="main-right-ad">
            <a :href="colAdsData.data[1].url" target="_blank">
                <img id="left-img" :src="colAdsData.data[1].img_path" :alt="colAdsData.data[1].alt" />
            </a>
        </div>
    </b-container>
</template>

<script>
import { GetInfoPost } from "@/apis/read.js";
import { reactive } from "@vue/composition-api";
export default{
    name:"Ads",
    setup(props,context){

        const is_PC = ()=>{
            if (document.body.clientWidth<400) {
                return 'phone'
            }else{
                return 'pc'
            }
        }

        const adsParams = reactive({
            url:'/ads',
            key:is_PC()
        });

        const rowAdsData = reactive({
            data:{}
        })

        GetInfoPost(adsParams).then((resp)=>{
            console.log("AAAAAAAAAA resp.data=",resp.data);
            rowAdsData.data = resp.data.data;

        });

        const colParams = reactive({
            url:'/colads',
            key:''
        });

        const colAdsData = reactive({
            data:{}
        })

        GetInfoPost(colParams).then((resp)=>{
            console.log("BBBBBBBBBBB resp.data=",resp.data);
            colAdsData.data = resp.data.data;
        });

        return{
            rowAdsData,
            colAdsData
        }
    }
}
</script>

<style lang="scss" scoped>
@media (max-width:500px) {
    #main-left-ad,#main-right-ad{
        display: none;
    }
    #main-top-ad{
        position: fixed;
        top: 0;
        bottom: auto;
        left: 0;
        z-index: 9999;
        right: 0;
    }
}
#top-img{
    width: 100%;
}
#main-left-ad{
    position: fixed;
    bottom: auto;
    top: 0;
    width: 150px;
    height: 600px;
    z-index: 9999;
    margin-top: 158px;
    left: 0;
}
#main-right-ad{
    position: fixed;
    bottom: auto;
    top: 0;
    width: 150px;
    height: 600px;
    z-index: 9999;
    margin-top: 158px;
    right: 0;
}
</style>