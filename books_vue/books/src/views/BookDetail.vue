<template>
<div id="BookDetail">
    <Header />
    <Ads />
    <b-container v-if="items.detailsItems.length == 1">
        <b-row class="mt-3"><b-col>
            当前路径：<a href="/">首页</a>--<a :href="'/book/'+items.detailsItems[0].book_id">{{ items.detailsItems[0].book_name }}</a>--{{ items.detailsItems[0].detail_title }}
        </b-col></b-row>
        <b-row>
            <b-col id="book-detail-title" class="mt-3 mb-3">
                {{ items.detailsItems[0].detail_title }}
            </b-col>
        </b-row>        
        <b-row style="text-align: center;" class="mb-3">
            <b-col cols="4" md="4">
                <a v-if="items.detailsItems[0].prev_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].prev_sort_id">上一页</a>
            </b-col>
            <b-col cols="4" md="4"><a :href="'/book/'+items.detailsItems[0].book_id">返回目录</a></b-col>
            <b-col cols="4" md="4">
                <a v-if="items.detailsItems[0].next_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].next_sort_id">下一页</a>
            </b-col>
        </b-row>
        <b-row class="mb-3">
            <b-col id="content-text" v-html="replaceBr(items.detailsItems[0].detail_content)"></b-col>
        </b-row>
        <b-row style="text-align: center;" class="mb-3">
            <b-col cols="4" md="4">
                <a v-if="items.detailsItems[0].prev_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].prev_sort_id">上一页</a>
            </b-col>
            <b-col cols="4" md="4"><a :href="'/book/'+items.detailsItems[0].book_id">返回目录</a></b-col>
            <b-col cols="4" md="4">
                <a v-if="items.detailsItems[0].next_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].next_sort_id">下一页</a>
            </b-col>
        </b-row>
    </b-container>
    <b-container v-else>
        您要查询的章节不存在哦！
    </b-container>
    <AdsFooter />
    <Footer />
</div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import { reactive,ref,onMounted } from "@vue/composition-api";
import { GetInfoPost } from "@/apis/read.js";
import { replaceBr } from "@/utils/replaceBr.js";
import Ads from "@/components/Ads.vue"
import AdsFooter from "@/components/AdsFooter.vue"


export default{
    name:"BookDetail",
    components:{
        Header,
        Footer,
        Ads,
        AdsFooter
    },
    setup(props,context){
        const detailParams = reactive({
            url:context.root.$route.path,
            key:''
        });

        const items = reactive({
            detailsItems:[]
        })

        GetInfoPost(detailParams).then((resp)=>{
            console.log(resp.data)
            items.detailsItems = resp.data.data
        });

        onMounted(() => {
            
            const titleParams = reactive({
                url:'/title',
                key:'bookdetail'
                })    

            GetInfoPost(titleParams).then((resp)=>{
                console.log("In BookDetail title =",resp.data)
                document.title =items.detailsItems[0].detail_title + '_' + resp.data.data[0];
                document.querySelector('meta[name="keywords"]').setAttribute('content',items.detailsItems[0].detail_title + '_' + items.detailsItems[0].book_name +'_'+ resp.data.data[1]);
                document.querySelector('meta[name="description"]').setAttribute('content',items.detailsItems[0].detail_title + '_'  + items.detailsItems[0].book_name +'_'+ resp.data.data[2]);     
                })
        });


        return {
            items,
            replaceBr
        }
    }
}
</script>

<style lang="scss" scoped>
    #book-detail-title{ 
        text-align: center;
        font-size: 24px;     
    }
    #content-text{
        line-height: 30px;
    }
</style>