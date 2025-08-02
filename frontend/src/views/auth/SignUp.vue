<template>
  <el-container class="signup-container">
    <el-main>
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
    </el-main>
    <el-footer class="footer-container"><span>© 2025 FireRSS</span></el-footer>
  </el-container>
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
@use '@/styles/var.module.scss';


.signup-container {
  background-color: var.$main-color;
  height: 100vh;
  min-height: 100vh;
  padding: 0 35% 0 35%;

  .form-title {
    padding: 10rem 0 3rem 0;
    text-align: center;
    font-size: var.$base-font-size-max;
    font-weight: 600;
    color: var.$color-white;
  }

  .el-input {
    height: 3rem;

    .el-input__wrapper {
      background-color: var.$main-color;

      .el-input__inner {
        color: var.$color-white;
      }
    }
  }

  .submit-btn {
    width: 100%;
  }

  .footer-container {
    text-align: center;
  }
}
</style>
