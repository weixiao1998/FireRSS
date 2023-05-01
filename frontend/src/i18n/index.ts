import { createI18n } from 'vue-i18n';
import zh from './lang/zh';
import en from './lang/en';

const FALLBACK_LANG = 'en'
const LANG = (navigator.language || FALLBACK_LANG).toLocaleLowerCase().split('-')[0];

const i18n = createI18n({
  locale: localStorage.getItem('lang') || LANG || FALLBACK_LANG,
  fallbackLocale: 'en',
  messages: {
    en,
    zh,
  },
});

export default i18n;
