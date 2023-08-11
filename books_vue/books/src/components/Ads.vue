<template>
    <b-container>
        <div id="main-top-ad">
            <a href="#" target="_blank">
                <img id="top-img" src="https://i.loli.net/2020/06/11/MLPaI12eFsyRXck.jpg" alt="对于该图片的描述" />
            </a>
        </div>
        <div id="main-left-ad">
            <a href="#" target="_blank">
                <img id="left-img" src="https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg" alt="对于该图片的描述" />
            </a>
        </div>
        <div id="main-right-ad">
            <a href="#" target="_blank">
                <img id="right-img" src="https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg" alt="对于该图片的描述" />
            </a>
        </div>
    </b-container>
</template>

<script>
export default{
    name:"Ads",
    setup(props,context){

        return{

        }
    }
}
</script>

<style lang="scss" scoped>
@media (max-width:500px) {
    #main-left-ad,#main-right-ad{
        display: none;
    }
    #main-top-ad{
        position: fixed;
        top: 0;
        bottom: auto;
        left: 0;
        z-index: 9999;
        right: 0;
    }
}
#top-img{
    width: 100%;
}
#main-left-ad{
    position: fixed;
    bottom: auto;
    top: 0;
    width: 150px;
    height: 600px;
    z-index: 9999;
    margin-top: 158px;
    left: 0;
}
#main-right-ad{
    position: fixed;
    bottom: auto;
    top: 0;
    width: 150px;
    height: 600px;
    z-index: 9999;
    margin-top: 158px;
    right: 0;
}
</style>