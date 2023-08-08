<template>
<div id="BookDetail">
    <Header />
    <b-container v-if="items.detailsItems.length == 1">
        <b-row><b-col>
            当前路径：<a href="/">首页</a>--<a :href="'/book/'+items.detailsItems[0].book_id">{{ items.detailsItems[0].book_name }}</a>--{{ items.detailsItems[0].detail_title }}
        </b-col></b-row>
        <b-row><b-col>
            {{ items.detailsItems[0].detail_title }}
        </b-col></b-row>        
        <b-row style="text-align: center;">
            <b-col>
                <a v-if="items.detailsItems[0].prev_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].prev_sort_id">上一页</a>
            </b-col>
            <b-col><a :href="'/book/'+items.detailsItems[0].book_id">返回目录</a></b-col>
            <b-col>
                <a v-if="items.detailsItems[0].next_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].next_sort_id">下一页</a>
            </b-col>
        </b-row>
        <b-row><b-col>
            {{ items.detailsItems[0].detail_content }}
        </b-col></b-row>
        <b-row style="text-align: center;">
            <b-col>
                <a v-if="items.detailsItems[0].prev_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].prev_sort_id">上一页</a>
            </b-col>
            <b-col><a :href="'/book/'+items.detailsItems[0].book_id">返回目录</a></b-col>
            <b-col>
                <a v-if="items.detailsItems[0].next_sort_id" :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].next_sort_id">下一页</a>
            </b-col>
        </b-row>
    </b-container>
    <b-container v-else>
        您要查询的章节不存在哦！
    </b-container>
    <Footer />
</div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import { reactive,ref } from "@vue/composition-api";
import { GetInfoPost } from "@/apis/read.js";
export default{
    name:"BookDetail",
    components:{
        Header,
        Footer
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

        return {
            items
        }
    }
}
</script>

<style lang="scss" scoped>

</style>