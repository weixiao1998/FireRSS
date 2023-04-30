<template>
  <el-container class="layout-container">
    <el-aside class="aside-container">
      <LayoutAside></LayoutAside>
    </el-aside>
    <el-container class="right-container">
      <el-header class="header-container">
        <LayoutHeader></LayoutHeader>
      </el-header>
      <el-main class="main-container">
        <RouterView></RouterView>
      </el-main>
      <el-footer class="footer-container">
        <LayoutFooter></LayoutFooter>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import LayoutAside from './MainLayoutAside.vue';
import LayoutHeader from './MainLayoutHeader.vue';
import LayoutFooter from './MainLayoutFooter.vue';
</script>

<style lang="scss" scoped>
.header-container {
  padding: 1rem;
}

.aside-container {
  height: 100vh;
  width: auto;
}
</style>
