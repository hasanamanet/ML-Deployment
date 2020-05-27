# Model Deployment
Haber metinlerini 6 kategoride sınıflandıran modeldir. MNaiev Bayes algoritması ve vektörel dönüşüm işlemleri ile basit anlamda geliştirilmiş bir modeldir. Model Flask ile Heroku'ya deploy edilecek duruma getirilmiştir. Aşağıdaki adresten modeli test edebilirsiniz. https://flask-news-class.herokuapp.com/
</br>
Haber Kategorileri:
0: 'magazin', 1: 'dunya', 2: 'spor', 3: 'siyaset', 4: 'kultur-sanat', 5: 'teknoloji'



# Heroku deployment:
- Heroku'ya üye olmalısınız.
- Yeni app oluşturmalısınız.
- Lokaldeki dosyaları deploy etme. (İki seçenekle bu işlemi yapabilirsiniz. Birincisi terminalden modeli Heroku'ya deploy edebilirsiniz. İkincisi GitHub'a yüklediğiniz respostory Heroku'da oluşturduğunuz uygulamaya bağlayabilirsiniz.)

## Terminalden yüklemek için:

- Heroku'da login olmalısınız:
$ heroku login

- Projenizin olduğu dizine gelin ve yeni bir git deposu oluşturun: </br>
$ cd my-project/</br>
$ git init</br>
$ heroku git:remote -a your-name-app</br>

- Modelinizi deploy edin: </br>
$ git add .</br>
$ git commit -am "make it better"</br>
$ git push heroku master

## GitHub bağlantısıyla yüklemek için:

- Heroku'da app oluşturduktan sonra "Deploy" seçeneklerinde GitHub seçerek GitHub hesabınızı Heroku'ya bağlamalısınız. İlgili respositroyi seçtikten sonra "Deploy Branch" tıklayarak deploy işlemini tamamlayabilirsiniz.

- Modelin eğitiminde "Kişisel Gazete”, Oğuz Yıldırım, Fatih Atık, Yıldız Teknik Üniversitesi, Bilgisayar Mühendisliği Bölümü, Bitirme Projesi, 2013. çalışmasında kullanılan haber metinlerinden yukarıda belirtilen kategoriler ve yaklaşık 5600 haber metni kullanılmıştır.
