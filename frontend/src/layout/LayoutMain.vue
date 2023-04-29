<template>
  <div class="layout-container">
    <el-container>
      <LayoutAside></LayoutAside>
      <el-container>
        <LayoutHeader></LayoutHeader>
        <el-main><RouterView></RouterView></el-main>
        <el-footer><LayoutFooter></LayoutFooter></el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import LayoutAside from './LayoutAside.vue';
import LayoutHeader from './LayoutHeader.vue';
import LayoutFooter from './LayoutFooter.vue';
</script>
