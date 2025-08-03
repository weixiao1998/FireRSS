<template>
  <el-container class="signup-container">
    <el-main>
      <div class="form-title">{{ $t("base.signUp") }} Fire RSS</div>
      <el-form :model="form" :rules="rules" ref="signupForm">
        <el-form-item prop="name">
          <el-input v-model="form.name" :placeholder="$t('base.userName')">
            <template #prefix><el-icon>
                <User />
              </el-icon></template>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="form.password" type="password" show-password :placeholder="$t('base.password')">
            <template #prefix><el-icon>
                <Key />
              </el-icon></template>
          </el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" class="submit-btn" @click="handleSignup">{{ $t("base.signUp") }}</el-button>
    </el-main>
    <el-footer class="footer-container"><span>© 2025 FireRSS</span></el-footer>
  </el-container>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { User, Key } from '@element-plus/icons-vue'
import { ElMessage, ElForm, type FormInstance } from 'element-plus';
import { ApiError } from '@/api/baseRequest';
import { apiUserSignUp } from '@/api/user';
import { useUserStore } from '@/stores/user';
const { t } = useI18n();

const form = ref({
  name: '',
  password: '',
})

const router = useRouter();
const userStore = useUserStore();

const signupForm = ref<FormInstance>();
const USER_NAME_REGEX = /^[a-zA-Z0-9_]{3,32}$/;
const PASSWORD_REGEX = /^[a-zA-Z0-9_!@#$%^&*()_+\-=\[\]{}|;:\'",.<>?/]{8,16}$/;

const rules = {
  name: [
    { required: true, message: t('validations.required', { field: t('base.userName') }), trigger: 'blur' },
    { min: 3, max: 32, message: t('validations.length', { field: t('base.userName'), min: 3, max: 32 }), trigger: 'blur' },
    { pattern: USER_NAME_REGEX, message: t('validations.pattern', { field: t('base.userName'), pattern: USER_NAME_REGEX }), trigger: 'blur' }
  ],
  password: [
    { required: true, message: t('validations.required', { field: t('base.password') }), trigger: 'blur' },
    { min: 8, max: 16, message: t('validations.length', { field: t('base.password'), min: 8, max: 16 }), trigger: 'blur' },
    { pattern: PASSWORD_REGEX, message: t('validations.pattern', { field: t('base.password'), pattern: PASSWORD_REGEX }), trigger: 'blur' }
  ]
};

const handleSignup = async () => {
  if (!signupForm.value) return;

  signupForm.value.validate(async (valid: boolean) => {
    if (!valid) {
      return;
    }

    try {
      const response = await apiUserSignUp(form.value);

      // Store user state
      userStore.setUserInfo({
        id: response.id,
        username: response.name,
      });

      // Show success message
      ElMessage.success(t('messages.signupSuccess'));

      // Redirect to home page
      router.push('/');
    } catch (error) {
      if (error instanceof ApiError) {
        ElMessage.error(t('messages.signupFailed') + t('messages.reason', { reason: error.msg }));
      } else {
        ElMessage.error(t('messages.signupFailed'));
        console.error('Signup failed:', error);
      }
    }
  });

}
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

  .el-form-item {
    margin-bottom: 2rem;
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
