<template>
  <div id="app">
    <el-container>
    <el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
        <el-menu-item>
          <el-image style="width: 55px; height: 55px" fix="contain" :src="require('@/assets/ee221417d8f9a4e6e03b707db09b4df2.png')"></el-image>
        </el-menu-item>
        <el-menu-item index="1">
          <el-link href="http://localhost:8000/#/" target="_blank" :underline="false">首页</el-link>
        </el-menu-item>
        <el-submenu index="2">
          <template slot="title">项目地址</template>
          <el-menu-item index="2-1">
            <el-image style="width: 20px; height: 20px" fix="contain" :src="require('@/assets/github_logo.png')"></el-image>
            <el-link href="https://github.com/haneball/gs_artifact" target="_blank" :underline="false">Github</el-link>
          </el-menu-item>
          <el-menu-item  index="2-2">
            <el-image style="width: 20px; height: 20px" fix="contain" :src="require('@/assets/gitee_logo.png')"></el-image>
            <el-link href="https://gitee.com/melon-pan/gs_artifact" target="_blank" :underline="false">Gitee</el-link>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  }
}
</script>

<style>
body {
  padding: 0;
  margin: 0;
}

.el-header {
  padding: 0;
}

.el-menu {
  z-index: 1;
}

.el-main {
  height: calc(100vh - 61px);
  overflow-y: auto;
}

.el-menu-collapse .el-menu .el-submenu, .el-menu--popup {
  min-width: 116px!important;
}
</style>
