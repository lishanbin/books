<template>
  <div class="home">
    <div>
      <Header />

      <b-container>
        <div style="height: 1000px;background-color: red;">
          body部分
        </div>
      </b-container>

      <Footer />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import { GetInfoPost } from "@/apis/read.js";
import { ref,reactive,onMounted } from "@vue/composition-api";

export default {
  name: "HomeView",
  components: {
    Header,
    Footer
  },
  setup(props,context){

    const titleParams = reactive({
      url:'/title',
      key:'index'
    })    

    GetInfoPost(titleParams).then((resp)=>{
      console.log("In Home title =",resp.data)
      document.title = resp.data.data[0];
      document.querySelector('meta[name="keywords"]').setAttribute('content',resp.data.data[1]);
      document.querySelector('meta[name="description"]').setAttribute('content',resp.data.data[2]);     
    })

    // document.title = "金牌小说网";
    // document.querySelector('meta[name="keywords"]').setAttribute('content','金牌小说网keywords');
    // document.querySelector('meta[name="description"]').setAttribute('content','金牌小说网description');

   
    return {
      
    }
  }
};
</script>
