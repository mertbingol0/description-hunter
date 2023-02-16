## Description of the script

[EN]


This code that I have written here, retrieves all the links found in the description of videos on a given YouTube channel, based on the channel ID provided, and presents it to you.

Charmquell, a YouTuber, conducted an OSINT by attempting to examine the channel of a narcissist who denies the facts presented in the video. I also wrote this script to be useful in such situations.

In short, by using this script, you can access all the links in the description of videos on a YouTube channel.


[TR]


### Neden?
Geçenlerde canım sıkıldı ve YouTube'da takılıyım dedim. YouTube'a girdiğimde ana sayfamda CharmQuell'in bir yayını düştü. Yayın da "SiyahGiyenGenc" adlı bir YouTuber'in gerçek kişiliğini ortaya çıkarıyordu. Bunu yaparken tüm kaynaklarıyla, kanıtlayarak yapıyordu. Velashil, bu Siyah diye hitap edeceğim arkadaş kanıtli bir şekilde söylenen gerçekleri inkar etmeye devam ederken, CharmQuell ve ekibi Siyah'ın YouTube kanalında bir OSINT gerçekleştirdi. Bu OSINT sonucunda Siyah'ın bir videonun açıklama kısmında, Charm'in içerisinde kötü paylaşımlarla dolu bir Facebook hesabının Siyah'a ait olduğu iddası doğrulandı çünkü videonun açıklama kısmında o Facebook hesabının linki vardı. İşin komik kısmı bunlara rağmen Siyah bu iddaları reddediyordu ki artık bir idda değil, bir gerçekti.

### Teknik Kısımlar
Bu yazdığım script sayesinde verilen bir YouTube kanalı üzerinde tüm videoların açıklamalarında bulunan linkleri topluyor ve sizlere sunuyor. Bunu yaparken YouTube API'ini kullanıyorum. Bu API sayesinde, YouTube'da bulunan verilere JSON türünde erişebiliyorum. İçerisinden "description" bölümünü çekiyor ve Python'da bulunan regex kütüphanesini kullanarak "description" bölümündeki tüm linkleri arıyor ve ekrana bastırıyourum. Bunu da her bir JSON verisi için döngüye sokuyorum.

Aşağıya, bu tool'un kullanımına dair örnek bir video bıraktım.

https://user-images.githubusercontent.com/92278684/214796536-7b1ae6a1-75a1-4418-99db-7ec32e64e663.mp4

