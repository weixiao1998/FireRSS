export default {
  base: {
    login: 'login',
    signUp: 'sign up',
    userName: 'user name',
    password: 'password',
  },
  validations: {
    required: '{field} is required',
    length: '{field} must be between {min} and {max} characters',
    pattern: '{field} must match the pattern {pattern}',
  },
  messages: {
    reason: 'Reason: {reason}',
    signupSuccess: 'Signup successful!',
    signupFailed: 'Signup failed. Please try again.',
  },
};
