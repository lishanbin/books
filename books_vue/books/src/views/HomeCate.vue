<template>
    <div id="HomeCate">
        <Header />
        <Ads />
        <b-container>           
            <div>
                <b-row>
                <b-col cols="12" md="7">
                    <h5 class="mt-3 mb-3">最新更新的小说</h5>
                    <!-- <b-table striped hover :items="nItems.newestItems.items" :fields="nItems.newestItems.fields"></b-table> -->
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">小说</th>
                                <th scope="col">最新章节</th>
                                <th scope="col">最新更新时间</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item,index in nItems.newestItems" :key="item.id">
                                <th scope="row">{{ index+1 }}</th>
                                <td><a :href="'/book/'+item.book_id">{{ item.book_name }}</a></td>
                                <td><a :href="'/book/'+item.book_id+'/'+item.book_newest_url">{{ item.book_newest_name }}</a></td>
                                <td>{{ dateFormat(item.book_last_update_time) }}</td>
                            </tr>                            
                        </tbody>
                    </table>
                </b-col>
                <b-col cols="12" md="1"></b-col>
                <b-col cols="12" md="4">
                    <h5  class="mt-3 mb-3">最多阅读的小说</h5>
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">小说</th>
                                <th scope="col">作者</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item,index in nItems.mostItems" :key="item.id">
                                <th scope="row">{{ index+1 }}</th>
                                <td><a :href="'/book/'+item.book_id">{{ item.book_name }}</a></td>
                                <td><a :href="'/book/'+item.book_id">{{ item.book_author }}</a></td>
                            </tr>                            
                        </tbody>
                    </table>
                </b-col>
            </b-row>
            </div>            
        </b-container>
        <AdsFooter />
        <Footer />
    </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import { ref, reactive, onMounted } from '@vue/composition-api';
import { GetInfoPost } from "@/apis/read.js";
import dateFormat from "@/utils/date.js";
import Ads from "@/components/Ads.vue"
import AdsFooter from "@/components/AdsFooter.vue"

export default {
    name: "HomeCate",
    props: {},
    components: {
        Header,
        Footer,
        Ads,
        AdsFooter
    },
    setup(props, context) {
        const now_url = ref(context.root.$route.path);

        const newsParams = reactive({
            url: now_url.value,
            key: 'newest'
        });

        const mostParams = reactive({
            url: now_url.value,
            key: 'most'
        });

        const nItems = reactive({
            newestItems: [],
            mostItems:[],
            resCode:0
        });

        GetInfoPost(newsParams).then((resp) => {
            console.log(resp);
            nItems.newestItems = resp.data.data
            nItems.resCode = resp.data.resCode
        }).catch(err=>{
           console.log(err)
        });

        GetInfoPost(mostParams).then((resp) => {
            console.log(resp);
            nItems.mostItems = resp.data.data
            nItems.resCode = resp.data.resCode
        });

        onMounted(() => {
            console.log("In HomeCate context = ", now_url.value)
            const titleParams = reactive({
                url:'/title',
                key:context.root.$route.path.replace(/\//g,'')
                })    

            GetInfoPost(titleParams).then((resp)=>{
                console.log("In Home title =",resp.data)
                document.title = resp.data.data[0];
                document.querySelector('meta[name="keywords"]').setAttribute('content',resp.data.data[1]);
                document.querySelector('meta[name="description"]').setAttribute('content',resp.data.data[2]);     
                })


        });

        return {
            nItems,
            dateFormat
        };
    }

}
</script>

<style lang="scss" scoped></style>