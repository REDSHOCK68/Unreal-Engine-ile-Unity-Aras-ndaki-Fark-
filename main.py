fark = {
            "UNITY": "Unity genellikle mobil oyunlar yapmak için kullanılan arayüzü basit ve düşük prodüksüyonlu oyunlar için kullanılır genellikle düşük sistemli pc'lerde daha iyi performans gösterir.",
            "Unreal Engine": "Yüksek prodüksüyonlu ve gerçekçi oyunlar yapmak için kullanılır ve ayrıca yüksek sistem bir pc gerekir.",
            }

word = input("Farkları görmek için (UNITY veya Unreal Engine): ")

if word in fark.keys():
    print(fark[word])
else:
   print("Bilinmeyen Komut")
