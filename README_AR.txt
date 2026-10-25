CodeLearn - تجهيز للنشر على الإنترنت

محتويات الحزمة:
- app.py: كود موقع CodeLearn الأصلي.
- requirements.txt: المكتبات المطلوبة.
- Procfile: أمر تشغيل الموقع على استضافة تدعم Gunicorn.

للنشر:
1) ارفع الملفات الموجودة في هذه الحزمة إلى مستودع GitHub.
2) أنشئ Web Service جديدًا في خدمة استضافة تدعم تطبيقات Python/Flask (مثل Render).
3) اختر المستودع.
4) Build Command: pip install -r requirements.txt
5) Start Command: gunicorn app:app
6) بعد اكتمال النشر، ستعطيك الاستضافة رابط HTTPS عامًا للموقع.

ملاحظة:
هذه الحزمة تجهّز الكود للنشر لكنها لا تنشره تلقائيًا ولا تنشئ رابطًا عامًا وحدها.
