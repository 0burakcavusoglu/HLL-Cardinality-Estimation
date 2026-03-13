import math
import mmh3 # MurmurHash3: Yüksek kaliteli hash fonksiyonu (Ödev gereksinimi)

class HyperLogLog:
    def __init__(self, p=10):
        """
        p: Precision (Hassasiyet) değeri. 
        m: Kova sayısı (2^p).
        """
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m
        
        # Alfa sabiti (Düzeltme Faktörü)
        if self.m == 16: self.alpha = 0.673
        elif self.m == 32: self.alpha = 0.697
        elif self.m == 64: self.alpha = 0.709
        else: self.alpha = 0.7213 / (1 + 1.079 / self.m)

    def _get_leading_zeros(self, b):
        """Binary formattaki sayının başındaki ardışık sıfır sayısını (+1) döner."""
        return (bin(b).lstrip('0b').find('1') if b > 0 else 64 - self.p) + 1

    def add(self, item):
        """Veriyi hash'ler, kovalara ayırır ve register günceller."""
        # 64-bit hash üretimi
        x = mmh3.hash64(str(item), signed=False)[0]
        
        # İlk p bit ile kova (index) belirleme (Bucketing)
        idx = x >> (64 - self.p)
        
        # Kalan bitlerdeki ardışık sıfır sayısını bulma
        w = x & ((1 << (64 - self.p)) - 1)
        rho = self._get_leading_zeros(w)
        
        # Register güncelleme (Sadece daha büyük değer gelirse)
        self.registers[idx] = max(self.registers[idx], rho)

    def count(self):
        """Harmonik ortalama kullanarak küme büyüklüğünü tahmin eder."""
        # Harmonik Ortalama Hesaplama
        res = sum(2.0**-val for val in self.registers)
        estimate = self.alpha * (self.m**2) / res
        
        # Küçük Veri Seti Düzeltmesi (Linear Counting)
        if estimate <= 2.5 * self.m:
            zeros = self.registers.count(0)
            if zeros != 0:
                estimate = self.m * math.log(self.m / zeros)
        
        return int(estimate)

    def merge(self, other):
        """İki HLL yapısını veri kaybı olmadan birleştirir (Mergeable property)."""
        if self.p != other.p:
            raise ValueError("Kova sayıları (p) aynı olmalıdır!")
        
        for i in range(self.m):
            self.registers[i] = max(self.registers[i], other.registers[i])

# --- Örnek Kullanım ---
if __name__ == "__main__":
    hll = HyperLogLog(p=10) # 1024 kova
    
    data = [f"user_{i}" for i in range(10000)]
    for d in data:
        hll.add(d)
        
    print(f"Gerçek Değer: 10000")
    print(f"HLL Tahmini: {hll.count()}")