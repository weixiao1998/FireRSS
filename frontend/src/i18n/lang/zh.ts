export default {
  base: {
    login: '登录',
    signUp: '注册',
    userName: '用户名',
    password: '密码',
  },
  validations: {
    required: '{field}不能为空',
    length: '{field}长度必须在{min}到{max}个字符之间',
    pattern: '{field}必须匹配正则{pattern}',
  },
  messages: {
    reason: '原因：{reason}',
    signupSuccess: '注册成功！',
    signupFailed: '注册失败，请重试。'
  },
};
