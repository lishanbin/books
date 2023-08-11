<template>
    <b-container id="Header">

        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">嗨小说</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>

                    <b-nav-item  v-for="item in headData.headers" :key="item.id" :class="item.url==now_url?'active':''" :href="item.url">{{ item.text
                    }}</b-nav-item>

                </b-navbar-nav>

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-form>
                        <b-form-input v-model="search.key" size="sm" class="mr-sm-2" placeholder="请输入图书名或作者名"></b-form-input>
                        <b-button @click="onSearch" size="sm" class="my-2 my-sm-0" type="button">开始查询</b-button>
                    </b-nav-form>

                </b-navbar-nav>
            </b-collapse>
        </b-navbar>

    </b-container>
</template>

<script>
import { GetCates } from "@/apis/read.js";
import { reactive, ref } from "@vue/composition-api";
import { stripscript } from "@/utils/validate";

export default {
    name: "Header",
    setup(props, context) {

        const now_url = ref(context.root.$route.path)

        const headData = reactive({
            headers: []
        });
        GetCates().then(response => {
            console.log(response);
            headData.headers = response.data.data;
        });

        const search = reactive({
            key:''
        })

        const onSearch=()=>{
            if (search.key == '') {
                alert('搜索信息不能为空！')
                return false
            }

            if (!stripscript(search.key)) {
                alert('搜索信息包含不合法字符！')
                return false
            } 

            context.root.$router.push({
                path:'/search', 
                query:{
                    q:search.key
                }
            });
        }

        return {
            headData,
            now_url,
            search,
            onSearch
        };
    }
}
</script>

<style lang="scss" scoped>
@media (max-width: 500px) {
    #Header{
        margin-top: 90px;
    }
}
</style>