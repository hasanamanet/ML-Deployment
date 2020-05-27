# Model Deployment
6 haber kategorisinde haber metinlerini sınıflandıran modeldir. MNaiev Bayes algoritması ve vektörel dönüşüm işlemleri ile basit anlamda geliştirilmiş bir modeldir. Model Flask ile Heroku'ya deploy edilecek duruma getirilmiştir. Aşağıdaki adresten modeli test edebilirsiniz. https://flask-news-class.herokuapp.com/

Haber Kategorileri:

0: 'magazin', 1: 'dunya', 2: 'spor', 3: 'siyaset', 4: 'kultur-sanat', 5: 'teknoloji'

Modelin eğitiminde "Kişisel Gazete”, Oğuz Yıldırım, Fatih Atık, Yıldız Teknik Üniversitesi, Bilgisayar Mühendisliği Bölümü, Bitirme Projesi, 2013. çalışmasında kullanılan haber metinlerinden yukarıda belirtilen kategoriler ve yaklaşık 5600 haber metni kullanılmıştır.
