# Model Deployment
6 haber kategorisinde haber metinlerini sınıflandıran modeldir. MNaiev Bayes algoritması ve vektörel dönüşüm işlemleri ile basit anlamda geliştirilmiş bir modeldir. Model Flask ile Heroku'ya deploy edilecek duruma getirilmiştir. Aşağıdaki adresten modeli test edebilirsiniz. https://flask-news-class.herokuapp.com/

Haber Kategorileri:
0: 'magazin', 1: 'dunya', 2: 'spor', 3: 'siyaset', 4: 'kultur-sanat', 5: 'teknoloji'



# Heroku deployment:

1- Heroku'da üye olmalısınız.
2- Yeni app oluşturmalısınız.
3- Lokaldeki dosyaları deploy etme. (İki seçenekle bu işlemi yapabilirsiniz. Birincisi terminalden modeli Heroku'ya deploy edebilirsiniz. İkincisi GitHub'a yüklediğiniz respostory Heroku'da oluşturduğunuz uygulamaya bağlayabilirsiniz.)

## Terminalden yüklemek için:

Heroku'da login olmalısınız:
$ heroku login 

Projenizin olduğu dizine gelin ve yeni bir git deposu oluşturun: 

$ cd my-project/
$ git init
$ heroku git:remote -a your-app-name

Modelinizi deploy edin: 

$ git add . 
$ git commit -am "make it better" 
$ git push heroku master


Modelin eğitiminde "Kişisel Gazete”, Oğuz Yıldırım, Fatih Atık, Yıldız Teknik Üniversitesi, Bilgisayar Mühendisliği Bölümü, Bitirme Projesi, 2013. çalışmasında kullanılan haber metinlerinden yukarıda belirtilen kategoriler ve yaklaşık 5600 haber metni kullanılmıştır.
