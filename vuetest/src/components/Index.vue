<template>
  <el-aside width="0px">
    
    <el-menu
      router
      background-color="#262E47"
      text-color="#9199A4"
      active-text-color="#0090ED"
      :default-active="$route.path"
    >
      <el-menu-item index="/danci">Dashboard</el-menu-item>
      
    </el-menu>
  </el-aside>
</template>

<style lang="scss" scoped>
.el-aside{
  height: 100%;
}
.el-menu {
  border:none;
  height: 100%;
}
.side-head{
  width: 100%;
  height: 100px;
  background: #606266;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
.side-head img{
  width: 70px;
  height: 70px;
}
.el-menu-item{
  text-align: left;
  vertical-align: middle;
  display: flex;
  align-items: center;
}
.el-menu-item /deep/ i{
  display: inline-block;
  margin-right: 10px
}
</style>