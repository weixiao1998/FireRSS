import api from './baseRequest';

// User registration API
export const apiUserSignUp = (userData: { name: string, password: string }) => {
  return api.post('/v1/users/sign_up', {
    name: userData.name,
    password: userData.password
  });
};
