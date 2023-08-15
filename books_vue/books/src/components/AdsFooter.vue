<template>
    <b-container>
        <div>
            <a :href="rowAdsData.data.url" target="_blank">
                <img style="width: 100%;" :src="rowAdsData.data.img_path" :alt="rowAdsData.data.alt" />
            </a>
        </div>
    </b-container>
</template>

<script>
import { GetInfoPost } from "@/apis/read.js";
import { reactive } from "@vue/composition-api";
export default{
    name:"AdsFooter",
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

        return{
            rowAdsData
        }
    }
}
</script>

<style lang="scss" scoped>

</style>