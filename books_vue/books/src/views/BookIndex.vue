<template>
    <div id="BookIndex">
        <Header />
        <b-container style="margin-top: 2rem;">
            <div v-if="items.indexItems.length == 1">
                <b-row>
                    <b-col md="4">
                        <b-img thumbnail fluid src="https://picsum.photos/250/250/?image=59" alt="Image 3"></b-img>
                    </b-col>
                    <b-col md="8">
                        <div>
                            <b-jumbotron header-level="4">
                                <template #header>{{ items.indexItems[0].book_name }}</template>
                                <div>作者：{{ items.indexItems[0].book_author }}</div>
                                <div>最新章节：{{ items.indexItems[0].book_newest_name }}</div>
                                <div>最新更新时间：{{ dateFormat(items.indexItems[0].book_last_update_time) }}</div>
                                <div>本书状态：{{ items.indexItems[0].book_status }}</div>

                                <hr class="my-4">

                                <p v-html="'小说简介：' + items.indexItems[0].book_desc"></p>

                                <b-button pill variant="primary" style="float: right;" href="#">开始阅读</b-button>
                                <b-button pill variant="success" style="float: left;" href="#">加入收藏夹</b-button>
                            </b-jumbotron>
                        </div>

                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <h5>图书最近更新的20章</h5>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="12" md="4" v-for="item in items.cap20Items" :key="item.id">
                        <a :href="'/book/'+item.book_id+'/'+item.sort_id">{{ item.detail_title }}</a>
                    </b-col>                    
                </b-row>

                <b-row>
                    <b-col>
                        <h5>图书所有章节：</h5>
                    </b-col>
                </b-row>
                <b-row>
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
import { reactive, ref } from "@vue/composition-api";
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

        return {
            items,
            dateFormat
        }
    }

}
</script>

<style lang="scss" scoped></style>