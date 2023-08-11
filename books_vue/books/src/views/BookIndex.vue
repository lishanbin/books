<template>
    <div id="BookIndex">
        <Header />
        <b-container style="margin-top: 2rem;">
            <div v-if="items.indexItems.length == 1">
                <b-row>
                    <b-col md="4">
                        <b-img thumbnail fluid class="p-3" style="width: 80%;margin-left: 10%;margin-top: 1rem;" :src="items.indexItems[0].image_urls" alt="Image 3"></b-img>
                    </b-col>
                    <b-col md="8">
                        <div>
                            <b-jumbotron header-level="4" style="padding:3rem;margin: 1rem;">
                                <template #header>{{ items.indexItems[0].book_name }}</template>
                                <div class="mb-3 mt-3">作者：{{ items.indexItems[0].book_author }}</div>
                                <div class="mb-3">最新章节：{{ items.indexItems[0].book_newest_name }}</div>
                                <div class="mb-3">最新更新时间：{{ dateFormat(items.indexItems[0].book_last_update_time) }}</div>
                                <div>本书状态：{{ items.indexItems[0].book_status }}</div>

                                <hr class="my-4">

                                <p v-html="'小说简介：' + items.indexItems[0].book_desc"></p>

                                <b-button pill variant="primary" style="float: right;" :href="'/book/'+items.indexItems[0].book_id+'/'+items.capAllItems[0].sort_id">开始阅读</b-button>
                                <b-button pill variant="success" style="float: left;" href="#">加入收藏夹</b-button>
                            </b-jumbotron>
                        </div>

                    </b-col>
                </b-row>
                <b-row class="mt-3 mb-3" style="text-align: center;font-weight: bolder;">
                    <b-col>
                        <h5>图书最近更新的20章</h5>
                    </b-col>
                </b-row>
                <b-row class="mt-3 mb-3">
                    <b-col cols="12" md="4" v-for="item in items.cap20Items" :key="item.id">
                        <a :href="'/book/'+item.book_id+'/'+item.sort_id">{{ item.detail_title }}</a>
                    </b-col>                    
                </b-row>

                <b-row class="mt-3 mb-3" style="text-align: center;font-weight: bolder;">
                    <b-col>
                        <h5>图书所有章节：</h5>
                    </b-col>
                </b-row>
                <b-row class="mt-3 mb-3">
                    <b-col cols="12" md="4" v-for="item in items.capAllItems" :key="item.id">
                       <a :href="'/book/'+item.book_id+'/'+item.sort_id">{{ item.detail_title }}</a> 
                    </b-col>
                </b-row>
            </div>
            <div v-else>
                哦哦，您要查看的图书不存在
            </div>
        </b-container>
        <Footer />
    </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import { GetInfoPost } from "@/apis/read.js";
import { reactive, ref,onMounted } from "@vue/composition-api";
import dateFormat from "@/utils/date.js"

export default {
    name: "BookIndex",
    components: {
        Header,
        Footer
    },
    setup(props, context) {
        // const now_url = ref(context.root.$route.path)
        const indexParams = reactive({
            url: context.root.$route.path,
            key: 'index'
        });

        const cap20Params = reactive({
            url: context.root.$route.path,
            key: 'cap20'
        });

        const capAllParams = reactive({
            url: context.root.$route.path,
            key: 'capAll'
        });

        const items = reactive({
            indexItems: [],
            capAllItems:[],
            cap20Items:[]
        })


        GetInfoPost(indexParams).then((resp) => {
            // console.log(resp);
            items.indexItems = resp.data.data
        });

        GetInfoPost(capAllParams).then((resp) => {
            // console.log(resp);
            items.capAllItems = resp.data.data
        });

        GetInfoPost(cap20Params).then((resp) => {
            // console.log(resp);
            items.cap20Items = resp.data.data
        });

        onMounted(() => {
            
            const titleParams = reactive({
                url:'/title',
                key:'bookindex'
                })    

            GetInfoPost(titleParams).then((resp)=>{
                console.log("In BookIndex title =",resp.data)
                document.title =items.indexItems[0].book_name + '_' +  resp.data.data[0];
                document.querySelector('meta[name="keywords"]').setAttribute('content',items.indexItems[0].book_name + '_' +  resp.data.data[1]);
                document.querySelector('meta[name="description"]').setAttribute('content',items.indexItems[0].book_name + '_' +  resp.data.data[2]);     
                })


        });

        return {
            items,
            dateFormat
        }
    }

}
</script>

<style lang="scss" scoped></style>