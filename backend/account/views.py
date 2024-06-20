from django.shortcuts import render
from .serializers import MyUserSerializer
#get_user_model()：這個函數返回當前設置中的用戶模型，可以動態獲取用戶模型，使得代碼更具可擴展性。
from django.contrib.auth import get_user_model 
# send_mail：Django 的郵件發送函數。
from django.core.mail import send_mail
# render_to_string：將模板轉換為字符串。
from django.template.loader import render_to_string 
# urlsafe_base64_encode, urlsafe_base64_decode, force_bytes, force_str：用於處理 URL 安全的 Base64 編碼和字節串轉換。
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
# APIView, AllowAny：DRF 中的類，用於創建 API 視圖和設置許可權。
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# jwt, datetime, timedelta, settings：JWT 相關操作、日期時間處理和設置讀取。
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import LoginObtainPairSerializer,StaffTokenObtainPairSerializer

User = get_user_model()

def get_jwt_token(user,exp_time:int):
    """
    user -> django user model 模型
    exp_time -> 過期時間
    """
    expiration = datetime.utcnow() + timedelta(minutes=exp_time)  # 設置JWT過期時間為5分鐘後
    token = jwt.encode({
        'user_id': user.pk,
        'exp': expiration,
    }, settings.SECRET_KEY, algorithm='HS256') # 使用HS256算法編碼JWT
    return token

def sendVerifyMail2User(user,url,emailTemplatePath,emailTitle,request):
    """
    寄給使用者的驗證信
    user -> User模型
    url -> request 的 URL
    emailTemplatePath -> email html 模板所在的路徑
    emailTitle -> 電子郵件標題
    """
    token = get_jwt_token(user,5) # 取得 JWT token

    # 使用 urlsafe_base64_encode 將用戶的主鍵（user.pk）轉換成 URL 安全的 Base64 編碼，以便在驗證郵件中使用。
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # build_absolute_uri 創建完整的啟動帳號的連結，其中包含了用戶的編碼主鍵和 JWT token。
    activation_link = request.build_absolute_uri(
        f'/{url}{uid}/{token}/'
    )
    # 電子郵件內容樣板
    email_template = render_to_string(
        emailTemplatePath,
        {
            'username': user.username,
            'activation_link':activation_link
        }
    )

    email = EmailMessage(
        emailTitle,  # 電子郵件標題
        email_template,  # 電子郵件內容
        settings.EMAIL_HOST_USER,  # 寄件者
        [user.email]  # 收件者
    )

    email.fail_silently = False
    email.content_subtype = "html"  
    email.send()


class RegisterView(APIView):
	# 設置 permission_classes 為 [AllowAny]，表示該視圖允許任何人訪問，即未驗證的用戶也可以使用這個視圖進行註冊操作。
    permission_classes = [AllowAny]
    mail_template = 'accounts/verify_email.html'
    mail_url = 'account/activate/'
    mail_title = 'Yt2MP3_MP4註冊驗證'
    def post(self,request):
        serializer = MyUserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            sendVerifyMail2User(user,RegisterView.mail_url,RegisterView.mail_template,RegisterView.mail_title,request)    
            return Response({'is_send':'true','detail':'Verification email sent.',"email":user.email},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        email = request.data.get("email",None)
        if not email:
            return Response({"error":"無效的email"},status=HTTP_400_BAD_REQUEST)
        try :
            user = User.objects.get(pk=email)  # 根據用戶ID查詢用戶
            if user.is_active == True:
                return Response({"msg":"帳戶已開通","is_active":"true"},status=status.HTTP_201_CREATED)
            sendVerifyMail2User(user,RegisterView.mail_url,RegisterView.mail_template,RegisterView.mail_title,request)
            return Response({"is_active":"false",'is_send':'true','detail':'Verification email sent.',"email":user.email},status=status.HTTP_201_CREATED)
        except User.DoesNotExist :
            return Response({'error':"無效的帳號"},status=HTTP_400_BAD_REQUEST)

class ActivateAccountView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,uidb64,token, *args, **kwargs):
        try:
        # 使用 force_str 和 urlsafe_base64_decode 將 uidb64 解碼為實際的用戶主鍵。
            uid = force_str(urlsafe_base64_decode(uidb64))  
            user = User.objects.get(pk=uid)  # 根據用戶ID查詢用戶
            # 使用 jwt.decode 解碼 JWT token，並檢查其中的 user_id 是否與查詢到的用戶主鍵相符，確保驗證的有效性。
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])  # 解碼JWT token
            if user.pk != payload['user_id']:  # 檢查用戶ID是否與token中的ID一致
                return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True  # 將用戶設置為啟用狀態
        user.save()  # 儲存用戶狀態的變更
        # return Response({'detail': 'Account activated successfully'}, status=status.HTTP_200_OK)
        return redirect("http://localhost:5173/finish")       

# 自訂使用者jwt登入View
class LoginObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginObtainPairSerializer

# 後台使用者jwt登入View
class StaffTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = StaffTokenObtainPairSerializer
