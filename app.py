from flask import Flask, request, redirect, url_for, render_template_string
from markupsafe import escape

app = Flask(__name__)

# =====================================================
# بيانات الدورات والأسئلة
# كل سؤال: العنوان، الشرح، المثال، التوضيح،
# السؤال، الخيارات، رقم الإجابة الصحيحة
# =====================================================

COURSES = {
    "python": {
        "name": "Python",
        "icon": "🐍",
        "color": "#3776AB",
        "description": "تعلم أساسيات بايثون من الصفر.",
        "video_url": "https://www.youtube.com/results?search_query=تعلم+بايثون+من+الصفر+بالعربي",
        "lessons": [
            ("مقدمة في Python", " لغة Python هي من اللغات القوية التي يمكن قراءة تعليماتها البرمجية بسهولة ممايسهل على البرمجين من تطوير التطبيقات بسرعةويمكن استخدامها لبعض انظمة التشغيل مثل windows وتعد لغة البايثون مثالية للمنتدئين وذالك لبساطتها حيث انها تتطلب عدد اقل من الاسطر البرمجية لتنفيذ نفس المهمة مقارنة باللغات الاخرى.",
             'print("Hello, World!")',
             "تستخدم print() لعرض النصوص والقيم على الشاشة.",
             "ما وظيفة print()؟",
             ["حذف الملفات", "عرض البيانات", "إغلاق البرنامج"], 1),

            ("المتغيرات", "المتغيرات هي اسماء تعطى للبيانات التي نحتاج الى تخزينها ومعالجتها في اي برنامج .",
             'name = "Ali"\nage = 20\nprint(name)',
             "يستخدم الرمز = لإسناد قيمة إلى متغير.",
             "ما الرمز المستخدم لإسناد قيمة؟",
             ["==", "=", ">"], 1),

            ("أنواع البيانات", "تعد البيانات وانواعها في البرمجة بشكل عام وفي البايثون بشكل خاص مفهوما مهم جدا .في البايثون تنقسم انواع البيانات الى سبعة انواع منها ما هو معروف في اللغات البرمجية الاخرى مثل  str,int,float ومن جهه اخرى هناك انواع بيانات اكثر تقدما في البايثون مثلlist,tuple وفي لغة البايثون يكون كتابه نوع البيانات اختياري لان اللغة تتعرف على توع البيانات تلقائيا.",
             'age = 20\nprice = 5.5\nname = "Sara"\nmylist = ["python","c++"]',
             " age عدد صحيح، price عدد عشري، و name نص ,mylist قائمة.",
             "ما نوع القيمة 5.5؟",
             ["int", "float", "str"], 1),

            ("إدخال البيانات", "يمكن استقبال بيانات من المستخدم.",
             'name = input("Your name: ")\nprint(name)',
             "تستقبل input() ما يكتبه المستخدم وتعيده كنص.",
             "ما وظيفة input()؟",
             ["استقبال البيانات", "حذف البيانات", "رسم الصور"], 0),

            ("العمليات الحسابية", "تعرف العمليات الحسابية على انها رموز خاصة تقوم باجراء العمليات الحسابية والمنطقية .",
             "a = 3\nb = 5\nprint(a + b)",
             "الرمز + يستخدم للجمع.",
             "ما ناتج 3 + 5؟",
             ["2", "15", "8"], 2),

            ("الشروط", "تسمح الشروط باتخاذ القرارات وتعمل على السيطرة على تدفق البيانات في البرنامج .",
             'age = 20\nif age >= 18:\n    print("Adult")\nelse:\n    print("Young")',
             "تستخدم if للتحقق من الشرط وelse للحالة الأخرى.",
             "ما الكلمة المستخدمة لكتابة شرط؟",
             ["for", "if", "def"], 1),

            ("الحلقات", "تكرر الحلقات تنفيذ الأوامر اي لتكرار.",
             "for i in range(5):\n    print(i)",
             "تكرر range(5) الحلقة خمس مرات، من 0 إلى 4.",
             "كم مرة تتكرر الحلقة؟",
             ["4 مرات", "5 مرات", "6 مرات"], 1),

            ("القوائم", "تخزن القائمة عدة عناصر.",
             'fruits = ["apple", "banana"]\nprint(fruits[0])',
             "يبدأ فهرس القائمة من الصفر.",
             "ما فهرس أول عنصر؟",
             ["1", "0", "-1"], 1),

            ("الدوال", " الدوال هي مجموعة من العبارات البرمجية ذات صلة بالبرنامج وتؤدي مهمة معينة وتساعد الدوال على تنظيم الكود وإعادة استخدامه.",
             'def greet():\n    print("Welcome!")\n\ngreet()',
             "تستخدم def لتعريف الدالة.",
             "ما الكلمة المستخدمة لتعريف دالة؟",
             ["loop", "def", "input"], 1),

            ("معالجة الأخطاء", "يمكن التعامل مع الأخطاء باستخدام try وexcept.",
             'try:\n    number = int("abc")\nexcept ValueError:\n    print("Invalid number")',
             "تتعامل except مع الاستثناء المحدد عند حدوثه.",
             "ما الكلمة المستخدمة لمعالجة الاستثناء؟",
             ["except", "repeat", "import"], 0),
        ]
    },

    "javascript": {
        "name": "JavaScript",
        "icon": "🟨",
        "color": "#B69A00",
        "description": "تعلم البرمجة التفاعلية لصفحات الويب.",
        "video_url": "https://www.youtube.com/results?search_query=تعلم+JavaScript+للمبتدئين+بالعربي",
        "lessons": [
            ("مقدمة في JavaScript", "هي لغة برمجية تستخدم لاضافة الحركة و التفاعل الى مواقع الويب وتستخدم HTML لبناء هيكل الصفحة مثل العناوين والازرار والصور وتستخدم CSS لتنسيق الصفحة مثل الالوان والخطوط وتستخدم  JavaScript  لاضافة التفاعل والحسابات والشروط والحركة الى الصفحة.",
             'console.log("Hello, World!");',
             "تستخدم console.log() لعرض رسالة في وحدة التحكم.",
             "ما أمر عرض رسالة في وحدة التحكم؟",
             ["print()", "console.log()", "echo"], 1),

            ("المتغيرات", "المتغير هو اسم نستخدمه لتخزين قيمة حتى نستطيع استعمالها لاحقا في البرنامج مثلا متغير باسم name لتخزين اسم ومتغير باسم age لتخزين العمر . تستخدم ثلاث كلمات شائعة للتعامل مع المتغيرات : 1- let  تستخدم لتعريف متغير  يمكن تغيير قيمته لاحقا 2-const  تستخدم لتعريف متغير لا يمكن اعادة اسناد قيمة جديدة اليه 3- var تستخدم لتعريف متغير بطريقة العادية.",
             'let name = "Ali";\nconst age = 20;',
             "تسمح let بإعادة إسناد القيمة، أما const فلا تسمح بإعادة إسنادها.",
             "أي كلمة تسمح بتغيير قيمة المتغير لاحقًا؟",
             ["let", "const", "fixed"], 0),

            ("أنواع البيانات", "نوع البيانات يحدد طبيعة القيمة التي نتعامل معها مثل النص او رقم او قيمة منطقية . اهم انواع البيانات : 1- number لتخزين الاعداد الصحيحة والعشرية 2-String لتخزين النصوص 3-boolean لها قيمتان فقط   null- 4 True or False تستخدم للتعبير عن غياب قيمة بشكل مقصود 5-array تخزن مجموعة من القيم في متغير واحد    ",
             'let name = "Sara";\nlet age = 21;\nlet active = true;',
             "القيمة true من النوع boolean.",
             "ما نوع القيمة true؟",
             ["String", "Boolean", "Array"], 1),

            ("العمليات الحسابية", " هي العمليات التي نجريها على الارقام مثل الجمع والطرح والضرب والقسمة وغيرها من العمليات وتستخدم العمليات الحسابية لمعالجة الأعداد.",
             "let x = 5 + 3;\nconsole.log(x);",
             "العامل + يجمع العددين.",
             "ما ناتج 3 + 5؟",
             ["2", "15", "8"], 2),

            ("الشروط", " الشروط تجعل البرنامج يتخذ قرارا حسب حالة معينةاي تستخدم الشروط لاختيار الأوامر المناسبة.",
             'let age = 20;\nif (age >= 18) {\n console.log("Adult");\n} else {\n console.log("Young");\n}',
             "تنفذ if عندما يكون الشرط صحيحًا.",
             "ما الكلمة المستخدمة لكتابة شرط؟",
             ["if", "loop", "function"], 0),

            ("الحلقات", "تسمح لنا بيكرار تنفيذ مجموعة من التعليمات عدة مرات بدلا من كتابه الكود نفسه اكثر من مرة.",
             "for (let i = 0; i < 3; i++) {\n console.log(i);\n}",
             " يبدا العد من 0 ,   3 > i يستمر التكرار الى الرقم 3 ولا يطبع الرقم 3 ,++i يزيد بمقدار واحد بعد كل دورة و تطبع الحلقة القيم 0 و1 و2.",
             "كم مرة تتكرر الحلقة؟",
             ["مرتان", "3 مرات", "4 مرات"], 1),

            ("المصفوفات", "تخزن المصفوفة مجموعة من القيم بدلا من تخزين قيمة واحدة فقط وهذا يجعل التعامل مع مجموعة من القيم ابسط ولكل قيمه موقع يسمى index ويبدا العد من الصفر.",
             'let fruits = ["Apple", "Orange"];\nconsole.log(fruits[0]);',
             "يبدأ فهرس المصفوفة من الصفر.",
             "ماذا تعرض fruits[0]؟",
             ["Apple", "Orange", "0"], 0),

            ("الدوال", " الدالة هي مجموعة من التعلمات نكتبها مرة واحدة ثم نستطيع استدعاءها كلما احتجنا الى تنفيذها ",
             "function add(a, b) {\n return a + b;\n}\nconsole.log(add(2, 3));",
             "تعيد return نتيجة الجمع.",
             "ما ناتج add(2, 3)؟",
             ["23", "6", "5"], 2),
        ]
    },

    "java": {
        "name": "Java",
        "icon": "☕",
        "color": "#E76F35",
        "description": "تعلم أساسيات لغة Java والبرمجة الكائنية.",
        "video_url": "https://www.youtube.com/results?search_query=تعلم+Java+للمبتدئين+بالعربي",
        "lessons": [
            (" مقدمة عن Java ", "هي لغة برمجة بالكائنات  ويعتبر هذا الصنف من لغات البرمجة من اوسعها واكثرها استخداما .اول ما سنتعرف عليه في لغة Java   أمر الطباعة.",
             'System.out.println("Hello");',
             "يستخدم System.out.println() لعرض النص ثم الانتقال إلى سطر جديد.",
             "ما أمر الطباعة؟",
             ["print()", "System.out.println()", "echo"], 1),

            ("المتغيرات", "تخزن المتغيرات البيانات لكي يمكن استخدامها لاحقا في البرنامج .",
             'int age = 20;\nString name = "Ali";',
             "يستخدم int للأعداد الصحيحة وString للنصوص.",
             "أي نوع مناسب لعدد صحيح؟",
             ["int", "String", "boolean"], 0),

            ("العمليات الحسابية", "تتيح Java إجراء العمليات الحسابية  على الارقام مثل الجمع والقسمة والضرب والطرح .",
             "int a = 5;\nint b = 3;\nSystem.out.println(a + b);",
             "يجمع العامل + العددين.",
             "ما ناتج 5 + 3؟",
             ["15", "2", "8"], 2),

            ("الشروط", " نستخدم الشروط عندما نريد من البرنامج اتخاذ قرار مثل شرط  if و else  لاتخاذ القرارات.",
             'int age = 20;\nif (age >= 18) {\n System.out.println("Adult");\n} else {\n System.out.println("Young");\n}',
             "تستخدم if عندما يكون الشرط صحيحًا وتستخدم else اذا كان الشرط الاول غير صحيح .",
             "ما الكلمة المستخدمة للشرط؟",
             ["if", "repeat", "define"], 0),

            ("الحلقات", "الحلقات تجعل البرنامج يكرر الاوامر بدلا من كتابتها عدة مرات.",
             "for (int i = 0; i < 3; i++) {\n System.out.println(i);\n}",
             "تطبع الحلقة 0 و1 و2.",
             "كم مرة تتكرر الحلقة؟",
             ["مرتان", "3 مرات", "4 مرات"], 1),

            ("المصفوفات", "المصفوفة هي مجموعة من القيم من النوع نفسه تحت اسم واحد",
             "int[] numbers = {10, 20, 30};\nSystem.out.println(numbers[0]);",
             "يبدأ فهرس المصفوفة من الصفر.",
             "ما قيمة numbers[0]؟",
             ["30", "20", "10"], 2),

            ("الدوال Methods", " الدالة هي مجموعة من الاوامر نكتبها مرة واحدة ثم نستطيع استدعاءها عند الحاجة و تقسم الدوال البرنامج إلى أجزاء.",
             "static int add(int a, int b) {\n return a + b;\n}",
             "تعيد return القيمة التي تنتجها الدالة.",
             "ما وظيفة return؟",
             ["إرجاع قيمة", "إنشاء حلقة", "تعريف صنف"], 0),

            ("الأصناف والكائنات", " الصنف مثل مخطط نحدد فيه صفات الشيء والاوامر التي يستطيع تنفيذها  اما الكائن هو نسخة فعلية من الصنف اي (الصنف قالب لإنشاء الكائنات).",
             'class Student {\n String name;\n}\nStudent s = new Student();',
             "تستخدم new لإنشاء كائن جديد.",
             "ما الكلمة المستخدمة لإنشاء كائن؟",
             ["new", "loop", "print"], 0),
        ]
    },

    "cpp": {
        "name": "C++",
        "icon": "💠",
        "color": "#659AD2",
        "description": "تعلم أساسيات C++ مع أمثلة عملية.",
        "video_url": "https://www.youtube.com/results?search_query=تعلم+C%2B%2B+للمبتدئين+بالعربي",
        "lessons": [
            ("مقدمة عن  C++", " لغة  C++ هي لغة برمجية تستخدم لاعطاء الحاسوب اوامر لتنفيذ مهام محددة وهي لغة قوية وسريعة وتدعم البرمجة الاجرائية والبرمجة كائنية التوجه . سنتعرف اولا على طريقة او امر  عرض النصوص.",
             '#include <iostream>\nusing namespace std;\nint main() {\n cout << "Hello";\n return 0;\n}',
             "تستخدم cout لعرض النصوص على الشاشة.",
             "ما أمر الطباعة؟",
             ["cout", "print()", "echo"], 0),

            ("المتغيرات", "المتغير هو اسم نستخدمه لتخزين قيمه في الذاكرة حتى نستطيع استخدامها او تغييرها اثناء تنفيذ البرنامج",
             "int age = 20;\ndouble price = 5.5;\nchar grade = 'A';",
             "يستخدم int للأعداد الصحيحة وdouble للأعداد العشرية وchar تستخدم للحروف .",
             "أي نوع مناسب لعدد صحيح؟",
             ["int", "char", "string"], 0),

            ("العمليات الحسابية", "تدعم C++ العمليات الحسابية على الاعداد والمتغيرات .وللعمليات الحسابية اولويات مثل الرياضيات تنفذ الاقواس اولا ثم الضرب والقسمة وباقي القسمة ثم الجمع والطرح.",
             "int a = 5;\nint b = 3;\ncout << a + b;",
             "يجمع العامل + العددين.",
             "ما ناتج 5 + 3؟",
             ["15", "2", "8"], 2),

            ("الشروط", "الشروط تجعل البرنامج يتخذ قرارا بناء على قيمة او حالة معينة وفي C++ توجد عدة طرق لكتابة الشروط واهمها if  وif else  وswitch ",
             'if (age >= 18) {\n cout << "Adult";\n} else {\n cout << "Young";\n}',
             "تحدد نتيجة الشرط أي مجموعة أوامر ستنفذ.",
             "ما الكلمة المستخدمة للشرط؟",
             ["if", "for", "include"], 0),

            ("الحلقات", "تستخدم الحلقات  عند تكرار مجموعة من الاوامر دون الحاجة الى كتابتها عدة مرات  ونستخدمها غالبا عندما نعرف عدد مرات التكرار مسبقا.",
             "for (int i = 0; i < 3; i++) {\n cout << i << endl;\n}",
             "تطبع الحلقة الأعداد 0 و1 و2.",
             "كم مرة تتكرر الحلقة؟",
             ["مرتان", "3 مرات", "4 مرات"], 1),

            ("المصفوفات", " المصفوفةهي مجموعة من العناصر التي لها النوع نفسه ويستخدم اسم واحد للوصول اليها عن طريق  index",
             "int numbers[3] = {10, 20, 30};\ncout << numbers[0];",
             "أول عنصر في المصفوفة يحمل الفهرس صفر.",
             "ما قيمة numbers[0]؟",
             ["30", "20", "10"], 2),

            ("الدوال", " الدالة هي مجموعة من الاوامر نضعها تحت اسم محدد لتنفيذ مهمة معينة ونستطيع استدعاء الدالة كلما احتجنا الى المهمة بدلا من اعادة كتابة الكود ",
             "int add(int a, int b) {\n return a + b;\n}",
             "تعيد return نتيجة الجمع.",
             "ما وظيفة return؟",
             ["إرجاع قيمة", "إنشاء حلقة", "طباعة تلقائية"], 0),

            ("الأصناف", " تدعم C++ البرمجة الكائنية . الصنف هو قالب او مخطط يحدد البيانات والوظائف التي تنتمي الى نوع معين من الكائنات والكائن هو نسخه فعليه ننشئها من الصنف.",
             "class Student {\npublic:\n string name;\n};",
             "تستخدم class لتعريف صنف.",
             "ما الكلمة المستخدمة لتعريف صنف؟",
             ["class", "loop", "include"], 0),
        ]
    }
}

# تصميم الموقع

PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }} | CodeLearn</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Tahoma, Arial, sans-serif;
    background: #f3f6fc;
    color: #202b45;
}

nav {
    background: #101b36;
    color: white;
    padding: 17px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 5px 8px;
}

.logo {
    font-size: 25px;
    color: #63e6be;
    font-weight: bold;
}

.container {
    width: 92%;
    max-width: 1150px;
    margin: 30px auto;
    min-height: 65vh;
}

.hero {
    background: linear-gradient(135deg, #14213f, #3459a5);
    color: white;
    padding: 35px 28px;
    border-radius: 20px;
    margin-bottom: 25px;
}

.hero h1 { margin-top: 0; }
.hero p { line-height: 2; }

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 18px;
}

.card {
    background: white;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 5px 22px #15264b12;
    margin-bottom: 18px;
}

.icon { font-size: 42px; }

.btn, button {
    display: inline-block;
    background: #3459a5;
    color: white !important;
    border: 0;
    border-radius: 9px;
    padding: 12px 18px;
    margin: 8px 4px 0 0;
    font-size: 15px;
    cursor: pointer;
    text-decoration: none;
}

.btn:hover, button:hover { background: #223f7c; }

.btn.secondary { background: #65738b; }

.code {
    background: #101b2d;
    color: #a9f5c7;
    padding: 18px;
    border-radius: 10px;
    direction: ltr;
    text-align: left;
    white-space: pre-wrap;
    overflow-x: auto;
    line-height: 1.8;
}

.muted { color: #6d7890; }

.video-box {
    background: #eaf1ff;
    border: 1px solid #d5e1ff;
    border-radius: 12px;
    padding: 18px;
    line-height: 1.9;
}

.option {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #f2f5fa;
    border: 2px solid #dce3ef;
    border-radius: 10px;
    padding: 14px;
    margin: 10px 0;
    cursor: pointer;
}

.option input {
    width: auto;
    margin: 0;
}

.option-correct {
    background: #e4f8eb;
    border-color: #20a45a;
    color: #176b38;
}

.option-wrong {
    background: #ffe8e8;
    border-color: #d93636;
    color: #a51f1f;
}

.option:has(input:disabled) { cursor: default; }

.mark {
    font-size: 22px;
    font-weight: bold;
    margin-right: auto;
}

.green, .correct-answer { color: #16803d; }
.red { color: #d62828; }

.result-correct {
    background: #e4f8eb;
    border: 1px solid #20a45a;
    color: #176b38;
    padding: 16px;
    border-radius: 10px;
    margin-top: 18px;
}

.result-wrong {
    background: #ffe8e8;
    border: 1px solid #d93636;
    color: #a51f1f;
    padding: 16px;
    border-radius: 10px;
    margin-top: 18px;
}

.correct-answer {
    background: #e4f8eb;
    padding: 5px 9px;
    border-radius: 6px;
}

.explanation-box { border-right: 5px solid #3459a5; }

.actions {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 20px;
}

footer {
    background: #101b36;
    color: white;
    text-align: center;
    padding: 24px;
    margin-top: 40px;
}

@media (max-width: 600px) {
    .hero h1 { font-size: 26px; }
    .container { width: 94%; }
}
</style>
</head>

<body>
<nav>
    <a class="logo" href="/">CodeLearn 💻</a>
    <div><a href="/">الرئيسية</a></div>
</nav>

<div class="container">
    {{ content|safe }}
</div>

<footer> CodeLearn © 2026 — تعلم البرمجة خطوة بخطوة</footer>
<footer>  "أشراف : د/أسماء برط "    \t     " عمل : رؤى حاشد العظهي , سندس علي الحسني , نهى توفيق مخارش" </footer>
</body>
</html>
"""


def render_page(title, content):
    return render_template_string(
        PAGE,
        title=title,
        content=content
    )
# الصفحة الرئيسية

@app.route("/")
def home():
    cards = ""

    for slug, course in COURSES.items():
        cards += f"""
        <div class="card">
            <div class="icon">{course['icon']}</div>
            <h3>{escape(course['name'])}</h3>
            <p>{escape(course['description'])}</p>
            <p>عدد الدروس: {len(course['lessons'])}</p>
            <a class="btn" href="/course/{slug}">
                استكشف الدورة
            </a>
        </div>
        """

    content = f"""
    <section class="hero">
        <h1>مرحبًا بك في CodeLearn 🚀</h1>
        <p>
            منصة تعليمية لتعلم البرمجة باللغة العربية.
            اختر الدورة، واقرأ الشرح، وجرب الأمثلة،
            ثم أجب عن الأسئلة لتثبيت معلوماتك.
        </p>
        <p>
            لا تحتاج إلى حساب أو تسجيل دخول.
            الاختبارات للتعليم والتدريب فقط،
            
        </p>
        <a class="btn" href="#courses">ابدأ التعلم الآن</a>
    </section>

    <h2 id="courses">📚 الدورات التعليمية</h2>
    <div class="grid">{cards}</div>

    <div class="card">
        <h2>كيف تستخدم المنصة؟</h2>
        <p>1. اختر الدورة المناسبة.</p>
        <p>2. اقرأ الدرس وشاهد المثال البرمجي.</p>
        <p>3. أجب عن السؤال واضغط على تحقق من الإجابة.</p>
        <p>4. اقرأ التصحيح والشرح، ثم انتقل إلى السؤال التالي.</p>
        <p>5. يمكنك إعادة أي سؤال للتدرب مرة أخرى.</p>
    </div>
    """

    return render_page("الرئيسية", content)
# صفحة الدورة

@app.route("/course/<slug>")
def course(slug):
    if slug not in COURSES:
        return redirect(url_for("home"))

    item = COURSES[slug]
    cards = ""

    for i, lesson in enumerate(item["lessons"]):
        cards += f"""
        <div class="card">
            <h3>{escape(lesson[0])}</h3>
            <p>درس يتضمن شرحًا ومثالًا واختبارًا قصيرًا.</p>
            <a class="btn" href="/lesson/{slug}/{i}">
                ابدأ الدرس والاختبار
            </a>
        </div>
        """

    content = f"""
    <section class="hero">
        <div class="icon">{item['icon']}</div>
        <h1>دورة {escape(item['name'])}</h1>
        <p>{escape(item['description'])}</p>
        <p>عدد الدروس: {len(item['lessons'])}</p>
        <a class="btn"
           href="{item['video_url']}"
           target="_blank"
           rel="noopener noreferrer">
           مشاهدة فيديوهات تعليمية
        </a>
    </section>

    <h2>📚 دروس الدورة</h2>
    <div class="grid">{cards}</div>
    <a class="btn" href="/">العودة للرئيسية</a>
    """

    return render_page(item["name"], content)

# صفحة الدرس والاختبار

@app.route("/lesson/<slug>/<int:index>", methods=["GET", "POST"])
def lesson(slug, index):
    if slug not in COURSES:
        return redirect(url_for("home"))

    item = COURSES[slug]

    if index < 0 or index >= len(item["lessons"]):
        return redirect(url_for("course", slug=slug))

    (
        title,
        description,
        code_example,
        explanation,
        question,
        options,
        answer
    ) = item["lessons"][index]

    selected = None
    submitted = False
    correct = False

    if request.method == "POST":
        submitted = True
        selected = request.form.get("answer", "")

        if selected.isdigit():
            selected_index = int(selected)

            if 0 <= selected_index < len(options):
                correct = selected_index == answer
            else:
                selected = ""
        else:
            selected = ""

    options_html = ""

    for i, option in enumerate(options):
        checked = (
            "checked"
            if submitted and selected == str(i)
            else ""
        )

        option_class = "option"
        marker = ""

        if submitted:
            if i == answer:
                option_class += " option-correct"
                marker = '<span class="mark green">✓</span>'
            elif selected == str(i):
                option_class += " option-wrong"
                marker = '<span class="mark red">✗</span>'

        disabled = "disabled" if submitted else ""

        options_html += f"""
        <label class="{option_class}">
            <input
                type="radio"
                name="answer"
                value="{i}"
                {checked}
                {disabled}
                required
            >
            <span>{escape(option)}</span>
            {marker}
        </label>
        """

    result_html = ""

    if submitted:
        if selected == "":
            result_html = """
            <div class="result-wrong">
                <h3>يرجى اختيار إجابة صالحة.</h3>
            </div>
            """
        elif correct:
            result_html = """
            <div class="result-correct">
                <h3>✓ إجابة صحيحة!</h3>
                <p>أحسنت! اخترت الإجابة الصحيحة.</p>
            </div>
            """
        else:
            result_html = f"""
            <div class="result-wrong">
                <h3>✗ إجابة غير صحيحة</h3>
                <p>الإجابة الصحيحة هي:</p>
                <strong class="correct-answer">
                    {escape(options[answer])}
                </strong>
            </div>
            """

        result_html += f"""
        <div class="card explanation-box">
            <h3>💡 شرح الإجابة</h3>
            <p>{escape(explanation)}</p>
        </div>
        """

    if index + 1 < len(item["lessons"]):
        next_url = f"/lesson/{slug}/{index + 1}"
        next_label = "السؤال التالي ←"
    else:
        next_url = f"/course/{slug}"
        next_label = "إنهاء التدريب والعودة للدورة"

    if submitted and selected != "":
        answer_form = """
        <p class="muted">
            تم تصحيح الإجابة. انتقل للسؤال التالي أو أعد السؤال.
        </p>
        """
    else:
        answer_form = f"""
        <form method="post">
            {options_html}
            <button type="submit">تحقق من الإجابة</button>
        </form>
        """

    content = f"""
    <div class="card">

        <p class="muted">
            {escape(item['name'])}
            — الدرس {index + 1} من {len(item['lessons'])}
        </p>

        <h2>{escape(title)}</h2>
        <p>{escape(description)}</p>

        <h3>💻 المثال البرمجي</h3>
        <pre class="code">{escape(code_example)}</pre>

        <h3>📖 شرح مبسط</h3>
        <p>{escape(explanation)}</p>

        <section class="video-box">
            <h3>🎬 فيديوهات مساعدة</h3>
            <p>
                يمكنك مشاهدة شرح إضافي ثم العودة لمواصلة التدريب.
            </p>
            <a class="btn"
               href="{item['video_url']}"
               target="_blank"
               rel="noopener noreferrer">
                مشاهدة فيديوهات {escape(item['name'])}
            </a>
        </section>

        <hr>

        <h3>🧠 اختبر معلوماتك</h3>
        <p>{escape(question)}</p>

        {answer_form}
        {result_html}

        <div class="actions">
            <a class="btn" href="{next_url}">
                {next_label}
            </a>

            <a class="btn secondary"
               href="/lesson/{slug}/{index}">
                إعادة السؤال
            </a>

            <a class="btn secondary"
               href="/course/{slug}">
                العودة إلى الدورة
            </a>
        </div>

        <p class="muted">
            الاختبار للتعليم والتدريب فقط.
            
        </p>

    </div>
    """

    return render_page(title, content)
# صفحة الخطأ

@app.errorhandler(404)
def not_found(error):
    content = """
    <div class="card">
        <h2>الصفحة غير موجودة</h2>
        <p>عذرًا، لم نتمكن من العثور على الصفحة المطلوبة.</p>
        <a class="btn" href="/">العودة للرئيسية</a>
    </div>
    """
    return render_page("الصفحة غير موجودة", content), 404

# تشغيل الموقع

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
