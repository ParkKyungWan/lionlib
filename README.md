# 디자인만 된 상태 다운받기
  [lionlib.zip](https://github.com/ParkKyungWan/lionlib/files/9921374/lionlib.zip)

# mysql 서버 따로 켜야 함
  ![image](https://user-images.githubusercontent.com/48673195/199519020-b61a29aa-7707-4571-9a42-a6886d806f7e.png)
  
# 유저 테이블 ( AuthUser )
  | username | email | password |
  | ---------| ------| ---------|
  | CharField(150) | charField(150) | charfield(128) |

# 유저 모델 ( models.py )
    class AuthUser(models.Model):
      password = models.CharField(max_length=128)
      last_login = models.DateTimeField(blank=True, null=True)
      is_superuser = models.IntegerField()
      username = models.CharField(unique=True, max_length=150)
      first_name = models.CharField(max_length=150)
      last_name = models.CharField(max_length=150)
      email = models.CharField(max_length=254)
      is_staff = models.IntegerField()
      is_active = models.IntegerField()
      date_joined = models.DateTimeField()

      class Meta:
          managed = False
          db_table = 'auth_user'

# 디자인 시안
  https://www.figma.com/file/TNGEwrW4vURmllRZXfgtQF/%EC%82%AC%EC%9E%90%EC%9D%98-%EC%84%9C%EC%9E%AC-prototype?node-id=0%3A1

# 진행 상황
  디자인 + 로그인/로그아웃
 
# 작동 예시
  ## /
  ![image](https://user-images.githubusercontent.com/48673195/198835538-60d2bf47-45cf-4ea7-9af2-a49b5e05583a.png)
  ## /login
  ![image](https://user-images.githubusercontent.com/48673195/198835550-95323699-9307-44ef-830b-09d79bf49afc.png)
  ## /trend
  ![image](https://user-images.githubusercontent.com/48673195/198835565-77fd10bd-ce27-4748-b737-b8285b1ec165.png)
  ## /my
  ![image](https://user-images.githubusercontent.com/48673195/198835575-b9962914-e60d-4e2e-8f14-ce4b9e164e87.png)
  ## /new
  ![image](https://user-images.githubusercontent.com/48673195/198835586-49a019af-a6f6-4f29-8946-23135f2d4561.png)
  ## /show
  ![image](https://user-images.githubusercontent.com/48673195/198835605-abdcdcda-e3a1-4a96-8ed6-c47e40aafb25.png)


