"""
Django settings for yt_backend project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import configparser
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

"""
configparser 模組在解析包含百分號 (%) 的字串時會認為這是一個佔位符，
所以當字串中包含 % 字元時，需要使用 configparser 的 RawConfigParser 
類別來避免這個問題。
"""
# 建立設定檔解析器物件
secret = configparser.RawConfigParser()
secret.read(BASE_DIR / 'secret.ini')

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = secret['django']['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'basic',
    'account',
    'rest_framework_simplejwt',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
# settings.py
CORS_EXPOSE_HEADERS = (
'Content-Disposition',
)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vue.js 默認的開發伺服器地址,這只是範例，實際要參照你Vue的伺服器位置
]

ROOT_URLCONF = 'yt_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yt_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



# 讀取資料庫設定檔
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'database.ini'))

DATABASES = {
    'default': {
        'ENGINE': config['mysql']['ENGINE'],
        'NAME': config['mysql']['NAME'],
        'USER': config['mysql']['USER'],
        'PASSWORD': config['mysql']['PASSWORD'],
        'HOST': config['mysql']['HOST'],
        'PORT': config['mysql']['PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


AUTH_USER_MODEL = 'account.MyUser'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  #SMTP伺服器
EMAIL_PORT = 587  #TLS通訊埠號
EMAIL_USE_TLS = True  #開啟TLS(傳輸層安全性)
EMAIL_HOST_USER = 'eddiewang880215@gmail.com'  #寄件者電子郵件
EMAIL_HOST_PASSWORD = 'mqmhlsszworiiafn'  #Gmail應用程式的密碼


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), # 設置存取令牌（access token）的有效期限為5分鐘
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1), # 設置刷新令牌（refresh token）的有效期限為1天後過期。
    'ROTATE_REFRESH_TOKENS': False, # 是否在每次使用刷新令牌時發放新的刷新令牌。
    'BLACKLIST_AFTER_ROTATION': True, # 是否在發放新刷新令牌後將舊的刷新令牌列入黑名單。
    'ALGORITHM': 'HS256', # 用於簽名和驗證 JWT 的加密演算法，使用 HMAC-SHA256 演算法。
    'SIGNING_KEY': SECRET_KEY, # 於簽名 JWT 的密鑰。這是一個非常重要的安全參數，應該使用強密鑰並保密。
    'VERIFYING_KEY': None, # 用於驗證 JWT 的密鑰。如果使用非對稱加密（如 RS256），需要設置此參數。
    'AUTH_HEADER_TYPES': ('Bearer',), # 指定 HTTP 認證頭的類型。
    'USER_ID_FIELD': 'email', #  指定用戶模型中用於標識用戶的欄位。
    'USER_ID_CLAIM': 'email', # 指定 JWT 中用於保存用戶 ID 的聲明。
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), # 指定使用的 JWT 類型。
    'TOKEN_TYPE_CLAIM': 'token_type',  # 指定 JWT 中用於保存令牌類型的聲明。
}