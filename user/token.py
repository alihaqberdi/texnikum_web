# from django.contrib.auth.tokens import PasswordResetTokenGenerator
#
# """
#     Ushbu funksya foydalanuvchiga parolini qayta tiklash uchun yordam beradi
# """
#
# from six import text_type
#
# """
#     1. Yadro: Ushbu modul Djangoning +asosiy funksiyalarini, jumladan so'rov/javob aylanishini, URL marshrutini, shablon mexanizmini va ma'lumotlar bazasi qatlamini ta'minlaydi.
#
# 2. Auth: Ushbu modul Django ilovalari uchun autentifikatsiya va avtorizatsiya funksiyalarini taqdim etadi.
#
# 3. Admin: Ushbu modul Django ilovalaridagi ma'lumotlarni boshqarish uchun ma'muriy interfeysni taqdim etadi.
#
# 4. Seanslar: Bu modul Django ilovalari uchun sessiyani boshqarish funksiyalarini taqdim etadi.
#
# 5. Xabarlar: Bu modul Django ilovalari uchun xabar almashish tizimini taqdim etadi.
#
# 6. Statik fayllar: Ushbu modul Django ilovalari uchun statik fayllarni (masalan, tasvirlar, CSS va JavaScript) boshqarish usulini taqdim etadi.
# """
#
#
# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
#
#     def _make_hash_value(self, user, timestamp):
#         return (
#                 text_type(user.pk) + text_type(timestamp) +
#                 text_type(user.is_active)
#         )
#
#
# account_activation_token = AccountActivationTokenGenerator()
