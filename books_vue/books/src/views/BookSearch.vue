<template>
    <div id="Search">
        <Header />
        <b-container>
            <b-row class="my-3">
                <b-col><h5><strong>查询结果：</strong></h5></b-col>
            </b-row>
            <b-row>               
                <b-col v-if="searchResult.items.length!=0">
                    <table class="table table-hover table-striped">
                        <thead>
                            <tr>
                                <th scope="col">编号</th>
                                <th scope="col">图书名</th>
                                <th scope="col">作者</th>
                                <th scope="col">最新章节</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item,index in searchResult.items" :key="item.id">
                                <th scope="row">{{ index+1 }}</th>
                                <td><a :href="'/book/'+item.book_id">{{ item.book_name }}</a></td>
                                <td><a :href="'/book/'+item.book_id">{{ item.book_author }}</a></td>
                                <td><a :href="'/book/'+item.book_id+'/'+item.book_newest_url">{{ item.book_newest_name }}</a></td>
                            </tr>                            
                        </tbody>
                    </table>
                </b-col>
                <b-col v-else>
                    <div class="alert alert-danger" role="alert">
                        您搜索的信息不存在！！
                    </div>
                </b-col>
            </b-row>
        </b-container>
        <Footer />
    </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import {  reactive } from "@vue/composition-api";
import { watch } from "vue";
import { GetInfoPost } from "@/apis/read";
export default {
    name: "Search",
    components: {
        Header,
        Footer
    },
    setup(props, context) {
        const searchParam = reactive({
            url:"/search",
            key:context.root.$route.query.q
        });        

        const searchResult = reactive({
            items:[]
        })
        GetInfoPost(searchParam).then((resp)=>{
            searchResult.items = resp.data.data
        });
        
              
        return {
            searchResult
        }
    },    
    watch:{
        $route(to,from){
            console.log('to===',to,'from====',from)
            if (to.path == from.path) {
                location.reload();
            }
        }
    }




}
</script>

<style lang="scss" scoped></style>