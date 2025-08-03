import axios from 'axios';
import type { AxiosInstance, AxiosRequestConfig, AxiosError } from 'axios';
import { ElMessage } from 'element-plus';

// Define a custom Axios instance type that matches our response interceptor behavior
declare module 'axios' {
  interface AxiosInstance {
    <T = any>(config: AxiosRequestConfig): Promise<T>;
    request<T = any>(config: AxiosRequestConfig): Promise<T>;
    get<T = any>(url: string, config?: AxiosRequestConfig): Promise<T>;
    delete<T = any>(url: string, config?: AxiosRequestConfig): Promise<T>;
    head<T = any>(url: string, config?: AxiosRequestConfig): Promise<T>;
    options<T = any>(url: string, config?: AxiosRequestConfig): Promise<T>;
    post<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T>;
    put<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T>;
    patch<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T>;
  }
}

// ApiError
interface ApiErrorInterface {
  code: number;
  msg: string;
  data: any;
}

export class ApiError implements ApiErrorInterface {
  code: number;
  msg: string;
  data: any;
  error: ApiError;

  constructor(code: number, msg: string, data: any = null, error: any) {
    this.code = code;
    this.msg = msg;
    this.data = data;
    this.error = error;
  }
}

function createApiError(error: AxiosError): ApiError {
  if (!error.response) {
    return new ApiError(90002, 'network error', null, error);
  }

  const data = error.response.data as { msg: string, code: number };
  return new ApiError(data?.code, data?.msg || "unknown error", data, error);
}

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 5000, // Request timeout time
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // You can add authentication token here
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    return Promise.reject(createApiError(error));
  }
);

export default api;
