<template>
  <div class="signup-container">
    <div class="form-title">{{ $t("base.signUp") }} Fire RSS</div>
    <el-form :model="form">
      <el-form-item>
        <el-input v-model="form.userName" :placeholder="$t('base.userName')">
          <template #prefix><el-icon>
              <User />
            </el-icon></template>
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-input v-model="form.password" type="password" show-password :placeholder="$t('base.password')">
          <template #prefix><el-icon>
              <Key />
            </el-icon></template>
        </el-input>
      </el-form-item>
    </el-form>
    <el-button type="primary" class="submit-btn">{{ $t("base.signUp") }}</el-button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { User, Key } from '@element-plus/icons-vue'

const form = ref({
  userName: null,
  password: null,
})
</script>

<style lang="scss">
@import '@/styles/variables.module.scss';

$bg-color: #2d3a4b;

.signup-container {
  background-color: $bg-color;
  height: 100vh;
  min-height: 100vh;
  padding: 0 35% 0 35%;

  .form-title {
    padding: 10rem 0 3rem 0;
    text-align: center;
    font-size: $base-font-size-max;
    font-weight: 600;
    color: $color-white;
  }

  .el-input {
    height: 3rem;

    .el-input__wrapper {
      background-color: $bg-color;

      .el-input__inner {
        color: $color-white;
      }
    }
  }

  .submit-btn {
    width: 100%;
  }
}</style>
