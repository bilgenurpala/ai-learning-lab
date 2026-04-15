# Devlog — AI Learning Lab

A day-by-day record of what I learned, built, and figured out.  
Her günün öğrendiklerini, inşa ettiklerimi ve çözdüklerimi günü gününe kaydeden bir log.

---

## Phase 1 — Python Fundamentals

---

### Day 1 — Variables
**Date:** 2026-03-01

**EN**
First day of the journey. Covered the absolute basics: how Python handles variables, how dynamic typing works (Python figures out the type at runtime, no declarations needed), and the `snake_case` naming convention. Practiced `print()`, `input()`, f-strings, and type conversion with `int()`. The key insight today was that f-strings are cleaner than concatenation — they make the intent readable at a glance.

**TR**
Yolculuğun ilk günü. Python'ın değişkenleri nasıl yönettiğini, dinamik tip sistemini (Python türü çalışma zamanında kendisi belirliyor, önceden tanımlama gerekmiyor) ve `snake_case` isimlendirme kuralını ele aldım. `print()`, `input()`, f-string ve `int()` ile tip dönüşümü pratik yaptım. Bugünün temel çıkarımı: f-string'ler string birleştirmesinden çok daha okunabilir ve temiz.

```python
# Key examples / Temel örnekler
name = "Bilge"
age = 25
print(f"Hello {name}, you are {age} years old.")
user_age = int(input("Enter your age: "))
```

---

### Day 2 — Data Types & String Manipulation
**Date:** 2026-03-02

**EN**
Went deeper into Python's type system. Learned the four primitive types (`int`, `float`, `str`, `bool`), how to check types with `type()`, and how to cast between them. Arithmetic operators felt familiar, but `//` (floor division) and `%` (modulus) are ones to remember — they come up constantly. String methods like `.upper()`, `.lower()`, `.strip()` were also covered.

**TR**
Python'ın tip sistemine daha derinlemesine girdim. Dört temel tipi (`int`, `float`, `str`, `bool`) öğrendim, `type()` ile tip kontrolü ve tipler arası dönüşüm yaptım. Aritmetik operatörler tanıdıktı ama `//` (tam bölme) ve `%` (mod) — bunlar sürekli karşıma çıkacak, iyi ezberlemek gerekiyor. `.upper()`, `.lower()`, `.strip()` gibi string metodlarını da gördüm.

```python
print(10 // 3)   # 3  — floor division / tam bölme
print(10 % 3)    # 1  — modulus / kalan
print(2 ** 8)    # 256 — exponent / üs
```

---

### Day 3 — Control Flow & Operators
**Date:** 2026-03-03

**EN**
Conditionals today. `if / elif / else` with comparison and logical operators. Nested conditions are where it gets interesting — the indentation-based structure forces you to think clearly about the logic tree. Built the Treasure Island text game, which was a good exercise in branching: every wrong path ends differently.

**TR**
Bugün koşullu ifadeler. Karşılaştırma ve mantıksal operatörlerle birlikte `if / elif / else`. İç içe koşullar işin ilginçleştiği yer — girintiye dayalı yapı, mantık ağacını net düşünmeni zorunda bırakıyor. Treasure Island metin oyununu yaptım; her yanlış seçim farklı bir sonuçla bitiyor, güzel bir dallanma egzersiziydi.

```python
age = 20
if age >= 18 and age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("Minor")
```

**Project / Proje:** Treasure Island — text-based adventure, nested conditionals, `.lower()` for input normalization.

---

### Day 4 — Lists & Randomisation
**Date:** 2026-03-04

**EN**
Lists are Python's workhorse. Covered creation, indexing (including negative), slicing, and the key methods: `append()`, `remove()`, `len()`. The `random` module — `random.choice()` and `random.shuffle()` — opens up a lot of possibilities. Built a Rock Paper Scissors game where the computer picks randomly. The logic for all three outcomes (win, lose, tie) was a good conditional exercise.

**TR**
Listeler Python'ın iş atı. Oluşturma, indeksleme (negatif dahil), dilimleme ve temel metodları ele aldım: `append()`, `remove()`, `len()`. `random` modülü — `random.choice()` ve `random.shuffle()` — çok fazla kapı açıyor. Bilgisayarın rastgele seçim yaptığı bir Taş Kağıt Makas oyunu yaptım. Üç sonucun (kazan, kaybet, beraberlik) tümünü ele almak güzel bir koşullu mantık egzersiziydi.

```python
import random
choices = ["Rock", "Paper", "Scissors"]
cpu = random.choice(choices)
random.shuffle(choices)
```

**Project / Proje:** Rock Paper Scissors — `random.choice()`, `.capitalize()` for input normalization, all outcomes covered.

---

### Bonus — Rock Paper Scissors Lizard Spock
**Date:** 2026-03-04 (same day / aynı gün)

**EN**
Extended the RPS project with two new choices: Lizard and Spock. This meant going from 3 choices and 3 win conditions to 5 choices and 10 win conditions. Used emoji for the choices and handled all outcomes with nested `if/elif`. A good exercise in scaling conditional logic.

**TR**
RPS projesini iki yeni seçimle genişlettim: Kertenkele ve Spock. Bu, 3 seçim ve 3 kazanma koşulundan, 5 seçim ve 10 kazanma koşuluna geçmek demekti. Seçimler için emoji kullandım ve tüm sonuçları iç içe `if/elif` ile yönettim. Koşullu mantığı ölçeklendirme üzerine iyi bir egzersiz.

---

### Day 5 — Loops
**Date:** 2026-03-05

**EN**
Loops are the backbone of most programs. Covered `for` with `range(start, stop, step)`, looping through lists and strings, and `while`. The control flow keywords `break`, `continue`, `pass` add real power. `enumerate()` is a clean way to get both index and value without maintaining a counter manually. The password generator project put all of this together: pick characters from lists with loops, shuffle the result.

**TR**
Döngüler çoğu programın omurgasıdır. `range(start, stop, step)` ile `for`, listeler ve stringler üzerinde döngü ve `while`'ı ele aldım. Kontrol akışı anahtar kelimeleri `break`, `continue`, `pass` gerçek güç katıyor. `enumerate()` — manuel bir sayaç tutmadan hem indeks hem değer almanın temiz yolu. Şifre üreteci projesi hepsini bir araya getirdi: döngülerle listelerden karakter seç, sonucu karıştır.

```python
for i in range(1, 10, 2):     # 1, 3, 5, 7, 9
    print(i)

for index, char in enumerate("Python"):
    print(index, char)
```

**Project / Proje:** Password Generator — loops over letter/symbol/number sets, `random.shuffle()` for final randomization.

---

### Day 6 — Functions
**Date:** 2026-03-06

**EN**
Functions are the foundation of reusable code. Learned `def`, parameters, return values, default parameter values, and keyword arguments. The main takeaway: a function should do one thing and do it well. Default values and keyword arguments make functions flexible without overcomplicating the call site.

**TR**
Fonksiyonlar yeniden kullanılabilir kodun temelidir. `def`, parametreler, dönüş değerleri, varsayılan parametre değerleri ve anahtar kelime argümanlarını öğrendim. Ana çıkarım: bir fonksiyon tek bir şey yapmalı ve onu iyi yapmalı. Varsayılan değerler ve anahtar kelime argümanları, çağrı noktasını karmaşıklaştırmadan fonksiyonları esnek kılar.

```python
def greet(name="stranger"):
    return f"Hello {name}!"

print(greet())              # Hello stranger!
print(greet(name="Bilge"))  # Hello Bilge!
```

---

### Day 7 — Hangman Project
**Date:** 2026-03-07

**EN**
First major project that combines everything learned so far. The key technique: start with a list of underscores `['_'] * len(word)`, then use `enumerate()` to replace at the correct index when a letter is guessed correctly. Tracking already-guessed letters in a list prevents duplicate guesses. This project made loops, lists, and functions feel like a cohesive toolkit rather than separate topics.

**TR**
Şimdiye kadar öğrenilen her şeyi bir araya getiren ilk büyük proje. Temel teknik: `['_'] * len(word)` ile alt çizgi listesi oluştur, ardından harf doğru tahmin edildiğinde doğru indekste değiştirmek için `enumerate()` kullan. Zaten tahmin edilmiş harfleri bir listede takip etmek mükerrer tahminleri önlüyor. Bu proje, döngüleri, listeleri ve fonksiyonları ayrı konular yerine uyumlu bir araç seti gibi hissettirdi.

```python
display = ['_'] * len(chosen_word)
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess
```

**Project / Proje:** Hangman — random word selection, lives system, already-guessed tracking, ASCII art stages.

---

### Day 8 — Function Parameters & Caesar Cipher
**Date:** 2026-03-08

**EN**
Went deeper into how Python handles function arguments. `*args` lets a function accept any number of positional arguments as a tuple; `**kwargs` does the same for keyword arguments as a dict. These are used everywhere in Python's standard library and frameworks — understanding them is essential. The Caesar Cipher project is a classic encoding exercise that loops forever until the user quits.

**TR**
Python'ın fonksiyon argümanlarını nasıl ele aldığına daha derinlemesine girdim. `*args` bir fonksiyonun istediği sayıda konumsal argümanı tuple olarak almasını sağlar; `**kwargs` aynısını anahtar kelime argümanları için dict olarak yapar. Python'ın standart kütüphanesinde ve framework'lerde her yerde kullanılıyor — anlamak şart. Caesar Cipher projesi, kullanıcı çıkana kadar döngüde çalışan klasik bir şifreleme egzersizi.

```python
def total(*numbers):
    return sum(numbers)

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
```

**Project / Proje:** Caesar Cipher — letter shifting encoder/decoder, handles upper/lowercase, runs in loop until quit.

---

### Day 9 — Dictionaries & Silent Auction
**Date:** 2026-03-09

**EN**
Dictionaries are the most important data structure in Python after lists. Covered full CRUD (create, read, update, delete), the three iteration methods (`.keys()`, `.values()`, `.items()`), and nested dictionaries. The `max()` function with `key=dict.get` is a pattern worth memorising — it's clean and Pythonic. The Silent Auction project is a good real-world use case: collect multiple bidders, find the highest bid in one line.

**TR**
Sözlükler, listelerden sonra Python'daki en önemli veri yapısı. Tam CRUD (oluştur, oku, güncelle, sil), üç iterasyon metodu (`.keys()`, `.values()`, `.items()`) ve iç içe sözlükleri ele aldım. `key=dict.get` ile `max()` fonksiyonu ezberlenmeye değer bir kalıp — temiz ve Pythonic. Sessiz Açık Artırma projesi güzel bir gerçek dünya kullanımı: birden fazla teklif veren kişiyi topla, en yüksek teklifi tek satırda bul.

```python
winner = max(bids, key=bids.get)
```

**Project / Proje:** Silent Auction — bids stored in a dict, highest bidder found with `max(key=bids.get)`.

---

### Day 10 — Functions as Outputs & Calculator
**Date:** 2026-03-10

**EN**
Functions in Python are first-class objects — they can be stored in variables, passed as arguments, and returned from other functions. Storing operations in a dictionary and calling them dynamically is a key pattern. Recursive functions feel natural once you understand that each call has its own stack frame. The Calculator project uses both: a dict of operations called dynamically, with optional recursion for chaining.

**TR**
Python'da fonksiyonlar birinci sınıf nesnelerdir — değişkenlerde saklanabilir, argüman olarak geçilebilir ve başka fonksiyonlardan döndürülebilir. İşlemleri sözlükte saklayıp dinamik olarak çağırmak önemli bir kalıp. Özyinelemeli fonksiyonlar, her çağrının kendi yığın çerçevesine sahip olduğunu anladıktan sonra doğal hissettiriyor. Hesap Makinesi projesi ikisini de kullanıyor: dinamik olarak çağrılan işlemler sözlüğü ve zincirleme için isteğe bağlı özyineleme.

```python
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
result = operations[operator](n1, n2)
```

**Project / Proje:** Calculator — operations in a dict, dynamic calls, chained calculations, division-by-zero guard.

---

### Day 11 — Blackjack Project
**Date:** 2026-03-11

**EN**
The most complex project so far. The Ace rule (11 or 1 depending on the total score) is the trickiest part — if the score exceeds 21 and there's an Ace counted as 11, swap it to 1. The game needed multiple functions working together: dealing, scoring, the dealer's turn, and outcome checking. Good exercise in thinking about how to split a large problem into small, focused functions.

**TR**
Şimdiye kadarki en karmaşık proje. As kuralı (toplam puana göre 11 ya da 1) en zorlu kısım — puan 21'i aşarsa ve 11 olarak sayılan bir As varsa, 1'e çevir. Oyun birlikte çalışan birden fazla fonksiyon gerektirdi: kart dağıtma, puanlama, krupiye turu ve sonuç kontrolü. Büyük bir problemi küçük, odaklı fonksiyonlara nasıl böleceğimi düşünmek için iyi bir egzersiz.

```python
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0   # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
```

**Project / Proje:** Blackjack — dealer logic, dynamic Ace handling, all game outcomes covered.

---

### Day 12 — Scope & Number Guessing Game
**Date:** 2026-03-12

**EN**
Scope is one of those concepts that seems simple but causes real bugs if misunderstood. Python's rule: a function can read a global variable but cannot reassign it without the `global` keyword. The real lesson though is to avoid needing `global` at all — pass values through parameters and return them. Clean scope = fewer bugs. The Number Guessing Game is a good exercise in keeping state inside a function.

**TR**
Kapsam, yanlış anlaşılırsa gerçek hatalara yol açan ama basit görünen kavramlardan biri. Python'ın kuralı: bir fonksiyon global bir değişkeni okuyabilir ama `global` anahtar kelimesi olmadan yeniden atayamaz. Asıl ders ise `global`'e hiç ihtiyaç duymamak — değerleri parametreler aracılığıyla geç ve döndür. Temiz kapsam = daha az hata. Sayı Tahmin Oyunu, durumu bir fonksiyonun içinde tutmak için iyi bir egzersiz.

```python
x = 10  # global

def my_func():
    y = 5   # local
    print(x)  # can read global ✅

# print(y)  # ❌ NameError outside function
```

**Project / Proje:** Number Guessing Game — difficulty levels (easy: 10 lives, hard: 5), hints, clean scope throughout.

---

### Day 13 — Debugging
**Date:** 2026-03-13

**EN**
Debugging is a skill, not just a reflex. The three error types each require a different mindset: Syntax errors are caught before the program runs, Runtime errors happen during execution (often due to bad input or wrong types), and Logic errors are the hardest — the program runs fine but produces the wrong answer. The most useful debugging technique so far: isolate the bug by adding `print()` statements at each step to trace the actual values. `try/except` makes programs more resilient at boundaries where bad input is expected.

**TR**
Hata ayıklama bir refleks değil, bir beceridir. Üç hata türü her biri farklı bir zihniyeti gerektirir: Sözdizimi hataları program çalışmadan önce yakalanır, Çalışma zamanı hataları yürütme sırasında olur (genellikle kötü girdi veya yanlış türden), ve Mantık hataları en zordur — program sorunsuz çalışır ama yanlış sonuç üretir. Şimdiye kadarki en kullanışlı hata ayıklama tekniği: gerçek değerleri izlemek için her adıma `print()` ifadeleri ekleyerek hatayı izole et. `try/except` programları kötü girdinin beklendiği sınırlarda daha dayanıklı kılar.

```python
# Logic bug — the +1 makes every average wrong
# Mantık hatası — +1 her ortalamayı yanlış yapıyor
def find_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # ✅ fixed / düzeltildi
```

**Project / Proje:** Debugging Challenge — three buggy functions (FizzBuzz, Celsius converter, average calculator), each bug identified and fixed.

---

*Last updated: 2026-04-15*
