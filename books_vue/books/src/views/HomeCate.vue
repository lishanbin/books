<template>
    <div id="HomeCate">
        <Header />
        <b-container>
            <b-row>
                <b-col cols="12" md="7">
                    <h6>最新更新的小说</h6>
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
                            <tr v-for="item in nItems.newestItems">
                                <th scope="row">{{ item.id }}</th>
                                <td><a :href="'/book/'+item.book_id">{{ item.book_name }}</a></td>
                                <td><a :href="'/book/'+item.book_id+'/'+item.book_newest_url">{{ item.book_newest_name }}</a></td>
                                <td>{{ dateFormat(item.book_last_update_time) }}</td>
                            </tr>                            
                        </tbody>
                    </table>
                </b-col>
                <b-col cols="12" md="1"></b-col>
                <b-col cols="12" md="4">
                    <h6>最多阅读的小说</h6>
                </b-col>
            </b-row>
        </b-container>
        <Footer />
    </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import { ref, reactive, onMounted } from '@vue/composition-api';
import { GetInfoPost } from "@/apis/read.js";
import dateFormat from "@/utils/date.js";

export default {
    name: "HomeCate",
    props: {},
    components: {
        Header,
        Footer
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
            newestItems: []
        });

        GetInfoPost(newsParams).then((resp) => {
            console.log(resp);
            nItems.newestItems = resp.data.data
        });

        onMounted(() => {
            console.log("In HomeCate context = ", now_url.value)
        });

        return {
            nItems,
            dateFormat
        };
    }

}
</script>

<style lang="scss" scoped></style>