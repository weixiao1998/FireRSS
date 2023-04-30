<template>
  <div class="header-container-inner">
    <el-row type="flex" justify="space-between">
      <el-col :span="18">
        <el-breadcrumb :separator-icon="ArrowRight">
          <el-breadcrumb-item v-for="item in breadcrumbList" :to="item.path">{{ item.title }}</el-breadcrumb-item>
        </el-breadcrumb>
      </el-col>
      <el-col :span="6">
        <div style="float: right;">
          <!-- TODO: account -->
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
import { ArrowRight } from '@element-plus/icons-vue';
import { reactive, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const route = useRoute();
const router = useRouter();

// breadcrumb
let breadcrumbList: { title: string, path: string }[] = reactive(getBreadcrumbList());

watch(
  () => router.currentRoute.value,
  () => { breadcrumbList = reactive(getBreadcrumbList()) }
)

function getBreadcrumbList() {
  let list = [];
  for (const match of route.matched) {
    if (match.meta.title) {
      list.push({
        title: `${match.meta.title}`,
        path: match.path,
      });
    }
  }
  return list;
}
</script>
