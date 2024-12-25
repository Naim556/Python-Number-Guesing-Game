# Code Explanation in English
Function user_get_input

This function handles user input.
If the input must be within a specific range or among predefined options (e.g., [Y, N]), it validates the input and handles any errors.
If the input is invalid, a proper message is displayed, and the function prompts the user again.
Function play

This function implements the main logic of the game.
The user is asked to select a number between 1 and 6. Then, the program generates a random number within the same range.
If the selected number matches the random number, the user wins; otherwise, they lose.
At the end of each round, the user is asked whether they want to continue playing or exit.
Function main

This is the starting point of the program.
It displays a welcome message to the user and asks if they want to play the game.
If the response is positive, the play function is executed; otherwise, the program exits with a goodbye message.
Program Execution

If the file is run directly (__name__ == "__main__"), the main function is called.
This structure ensures that the code does not execute unintentionally if used as a module.

# Key Points:
Modularity: The code is split into different functions for specific tasks, making it easier to read and maintain.
Error Handling: The use of try-except in the input function ensures that invalid inputs are properly handled.
User Experience: The prompts and messages are clear and user-friendly, avoiding unnecessary repetitions.

# Kod Açıklamaları Türkçe
user_get_input Fonksiyonu

Bu fonksiyon, kullanıcıdan giriş almayı sağlar.
Eğer giriş belirli bir aralıkta veya önceden tanımlanmış seçenekler arasında olmalıysa (örneğin [Y, N]), bu fonksiyon hataları kontrol eder.
Geçersiz giriş durumunda kullanıcıya bir mesaj gösterilir ve tekrar giriş yapması istenir.
play Fonksiyonu

Bu fonksiyon, oyunun ana mantığını uygular.
Kullanıcıdan 1 ile 6 arasında bir sayı seçmesi istenir. Program da aynı aralıkta rastgele bir sayı üretir.
Eğer kullanıcının seçtiği sayı ile rastgele sayı eşleşirse, kullanıcı kazanır; aksi takdirde kaybeder.
Her tur sonunda, kullanıcıya oyuna devam etmek isteyip istemediği sorulur.
main Fonksiyonu

Bu fonksiyon, programın başlangıç noktasıdır.
Kullanıcıya hoş geldiniz mesajı gösterilir ve oyuna başlamak isteyip istemediği sorulur.
Eğer cevap olumluysa, play fonksiyonu çalıştırılır; aksi takdirde program çıkış yapar.
Programın Çalıştırılması

Eğer dosya doğrudan çalıştırılırsa (__name__ == \"__main__\"), main fonksiyonu çağrılır.
Bu yapı, kodun bir modül olarak kullanılması durumunda istem dışı çalıştırılmasını engeller.

# Önemli Noktalar:
Modülerlik: Kod, belirli görevler için farklı fonksiyonlara bölünmüştür; bu da okunabilirliği ve bakım kolaylığını artırır.
Hata Yönetimi: Giriş fonksiyonunda kullanılan try-except, geçersiz girişlerin doğru şekilde ele alınmasını sağlar.
Kullanıcı Deneyimi: Kullanıcıya sunulan mesajlar açık ve kullanıcı dostudur; gereksiz tekrarlar önlenmiştir.

# توضیحات کلی کد:
تابع user_get_input

وظیفه این تابع دریافت ورودی از کاربر است.
اگر ورودی باید در یک محدوده خاص یا از میان گزینه‌های مشخص باشد (مثلاً [Y, N])، این تابع خطاهای احتمالی را مدیریت می‌کند.
اگر ورودی نامعتبر باشد، پیام مناسبی به کاربر نمایش داده می‌شود و دوباره درخواست ورودی می‌کند.
تابع play

این تابع منطق اصلی بازی را پیاده‌سازی می‌کند.
کاربر باید یک عدد بین 1 تا 6 را انتخاب کند. سپس برنامه یک عدد تصادفی در همان محدوده تولید می‌کند.
اگر عدد انتخابی کاربر با عدد تصادفی یکسان باشد، کاربر برنده می‌شود؛ در غیر این صورت، بازنده است.
در پایان هر دور، از کاربر پرسیده می‌شود که آیا می‌خواهد بازی را ادامه دهد یا خیر.
تابع main

این تابع نقطه شروع برنامه است.
پیام خوش‌آمدگویی به کاربر نشان داده می‌شود و از او پرسیده می‌شود که آیا می‌خواهد بازی را شروع کند یا خیر.
اگر پاسخ مثبت باشد، تابع play اجرا می‌شود؛ در غیر این صورت، برنامه با یک پیام خداحافظی خاتمه می‌یابد.
نحوه اجرای برنامه

در صورت اجرای مستقیم فایل (__name__ == "__main__")، تابع main فراخوانی می‌شود.
این ساختار تضمین می‌کند که اگر کد در قالب یک ماژول استفاده شود، اجرای ناخواسته‌ای رخ ندهد.

# نکات مهم:
ماژولار بودن کد: توابع مختلف برای وظایف خاصی تعریف شده‌اند تا کد خواناتر و قابل نگهداری‌تر باشد.
مدیریت خطاها: استفاده از try-except در تابع ورودی تضمین می‌کند که خطاهای ناشی از ورود مقادیر نامعتبر به درستی مدیریت شوند.
تجربه کاربری بهتر: پیام‌ها برای کاربر واضح و قابل فهم هستند و از تکرار پرسش‌های غیرضروری جلوگیری می‌شود.
