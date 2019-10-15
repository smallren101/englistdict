<template>
    <div class="danci">
        <el-form :inline="true">
        <el-form-item>
            <el-input v-model="query"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="search">Search</el-button>
        </el-form-item>
        </el-form>
        <section class="tables">
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="args" label="word"></el-table-column>
      <el-table-column prop="pronounce" label="pronounce"></el-table-column>
      <el-table-column prop="trans" label="trans"></el-table-column>
      <!-- <el-table-column prop="index" label="index"></el-table-column>
      <el-table-column prop="additional" label="Other"></el-table-column> -->
      <el-table-column label="button">
      <template slot-scope="scope">
          <audio ref='audio' controls :src="'http://dict.youdao.com/dictvoice?type=1&audio=' + tableData[scope.$index].args"></audio>
      </template>
    </el-table-column>
    </el-table>
    <div class="pageination-box">
     <el-pagination
      @current-change='currentChange'
      layout="prev, pager, next"
      :total='page_total'
      >
    </el-pagination>
    </div>
    </section>
    </div>
</template>


<script>
// import { METHODS } from 'http'
export default {
    name: "IndexPage",
    data(){
        return {
            
            tableData: [{
                args: '',
                pronounce: '',
                additional: '',
                trans: '',
                index: ''
                }],
            query: "",
            page_total: 0
        }
    },
    methods: {
        getAllDanci: function(){
            var that = this;
            
            this.$request({
                method: "get",
                url: "danci",
                params: { page: that.page || 1, ci: that.query}
            })
            .then(function(response){
                console.log(response.data);
                if(response.data.code==0){
                    that.tableData=response.data.data
                    that.page_total=response.data.page_total*10
                    // for(var i=0; i<response.data.data.length();i++){
                    // that.$refs.audio.src = "http://dict.youdao.com/dictvoice?type=1&audio=" + response.data.data[i]['args']
                    // }
                }
            })
        },
        currentChange (page){
      console.log(page)
      this.page=page;
      this.getAllDanci()
    },
        search(){
            this.getAllDanci()
        }
    },
    mounted(){
        this.getAllDanci()
    }
}
</script>

<style>

</style>