<template>
  <div class="home">
    <el-container class="container">     
      <el-container>
        <index></index>
        <el-main> 
         <keep-alive>
          <router-view v-if="$route.meta.keepAlive"></router-view>
         </keep-alive>
         <router-view v-if="!$route.meta.keepAlive"></router-view>
    
        <!-- <router-view > </router-view> -->
        
        </el-main>
       
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Index from "@/components/Index.vue";

export default {
  name: 'home',
  components: {
    Index
  }
}
</script>
