# HLL-Cardinality-Estimation
# Büyük Veri Analitiğinde Olasılıksal Veri Yapıları: HyperLogLog Tasarımı

Bu proje, Kırklareli Üniversitesi Yazılım Mühendisliği bölümü kapsamında, Büyük Veri Analitiği dersi ödevi olarak geliştirilmiştir. Projenin amacı, devasa veri setlerinde "Unique Count" (Eşsiz Eleman Sayısı) tahminini minimum bellek kullanımı ile gerçekleştiren **HyperLogLog (HLL)** algoritmasını sıfırdan tasarlamaktır.

## 🚀 Proje Özellikleri
- **Dil:** Python
- **Hash Fonksiyonu:** MurmurHash3 (Yüksek kaliteli dağılım için)
- **Hata Düzeltme:** Küçük veri setleri için *Linear Counting* entegrasyonu.
- **Birleştirilebilirlik:** İki farklı HLL yapısını veri kaybı olmadan birleştirme (`merge`) desteği.
- **Metodoloji:** Agentic Coding yaklaşımı (Gemini/Copilot desteğiyle mimari tasarım).

## 🛠️ Teknik Bileşenler
Algoritma şu üç temel sütun üzerine inşa edilmiştir:
1. **Bucketing (Kovalama):** Hash değerinin ilk $p$ biti kullanılarak veriler kovalara ayrılır.
2. **Leading Zeros:** Geri kalan bitlerdeki ardışık sıfırların sayısı (`rho`) kaydedilir.
3. **Harmonik Ortalama:** Uç değerlerin (outliers) tahmini bozmaması için aritmetik yerine harmonik ortalama formülü kullanılmıştır.

## 📊 Teorik Analiz ve Hata Sınırları
HLL algoritmasında hata payı ($\sigma$), kova sayısı ($m$) ile ters orantılıdır:
$$\sigma \approx \frac{1.04}{\sqrt{m}}$$
Bu projede varsayılan olarak $p=10$ ($m=1024$) kullanılmış olup, teorik hata payı yaklaşık **%3.25** civarındadır.

## 💻 Kurulum ve Çalıştırma
Projeyi yerelinizde çalıştırmak için:
1. Depoyu klonlayın: `git clone [REPO_LINKINIZ]`
2. Gereksinimleri yükleyin: `pip install mmh3`
3. Çalıştırın: `python hll.py`

## 👤 Hazırlayan
- **Ad Soyad:** Burak Çavuşoğlu
- **Okul/Bölüm:** Kırklareli Üniversitesi - Yazılım Mühendisliği
