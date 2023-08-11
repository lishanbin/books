import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueCompositionApi from "@vue/composition-api";

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import { BootstrapVue,BootstrapVueIcons } from 'bootstrap-vue';

import './styles/main.scss'

import { JSEncrypt } from "jsencrypt";

//挂载全局方法
//JSEncrypt加密方法
Vue.prototype.$encryptedData = function(publicKey,data) {
  let encrypt = new JSEncrypt()
  encrypt.setPublicKey(publicKey)
  let result = encrypt.encrypt(data)
  return result
}
//JSEncrypt解密方法
Vue.prototype.$decryptData = function(privateKey,data) {
  let decrypt = new JSEncrypt()
  decrypt.setPrivateKey(privateKey)
  let result = decrypt.decrypt(data)
  return result
}

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

Vue.use(VueCompositionApi)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
