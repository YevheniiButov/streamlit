# modules/big_info.py

import streamlit as st

texts = {
    "en": {
        "title": "📄 BIG Registration Information",
        "markdown_content": """
As a foreign-trained dentist in the Netherlands, you must register in the BIG register (Individual Healthcare Professions).

### Steps of the registration process:
1.  **Have your diploma recognized** via DUO or Nuffic
2.  **Proof of language proficiency** (Dutch B2 or C1)
3.  **Knowledge and skills assessment** (BI-toets)
4.  **Complete the application form** with CIBG
5.  **Assessment and registration**

👉 On this website, you can practice for the BI-toets and prepare for Dutch dental practice.
""",
        "link_text": "More information? Visit [bigregister.nl](https://www.bigregister.nl)"
    },
    "ru": {
        "title": "📄 Информация о BIG-регистрации",
        "markdown_content": """
Как стоматолог с иностранным образованием, вы должны зарегистрироваться в реестре BIG (Beroepen in de Individuele Gezondheidszorg) в Нидерландах.

### Этапы процесса регистрации:
1.  **Признание диплома** через DUO или Nuffic
2.  **Подтверждение уровня владения языком** (Нидерландский B2 или C1)
3.  **Тест знаний и навыков** (BI-toets)
4.  **Заполнение заявки** в CIBG
5.  **Рассмотрение и регистрация**

👉 На этом сайте вы можете попрактиковаться для BI-toets и подготовиться к работе в нидерландской стоматологической практике.
""",
        "link_text": "Больше информации? Посетите [bigregister.nl](https://www.bigregister.nl)"
    },
    "nl": {
        "title": "📄 BIG-registratie informatie",
        "markdown_content": """
Als buitenlandse tandarts in Nederland moet je je registreren in het BIG-register (Beroepen in de Individuele Gezondheidszorg).

### Stappen van het registratieproces:
1.  **Diploma laten erkennen** via DUO of Nuffic
2.  **Bewijs van taalvaardigheid** (Nederlands B2 of C1)
3.  **Kennis- en vaardighedentoets** (BI-toets)
4.  **Aanvraagformulier invullen** bij CIBG
5.  **Beoordeling en registratie**

👉 Op deze website kun je oefenen voor de BI-toets en je voorbereiden op de Nederlandse tandartspraktijk.
""",
        "link_text": "Meer informatie? Bezoek [bigregister.nl](https://www.bigregister.nl)"
    },
    "uk": {
        "title": "📄 Інформація про BIG-реєстрацію",
        "markdown_content": """
Як стоматолог з іноземною освітою, ви повинні зареєструватися в реєстрі BIG (Beroepen in de Individuele Gezondheidszorg) у Нідерландах.

### Етапи процесу реєстрації:
1.  **Визнання диплома** через DUO або Nuffic
2.  **Підтвердження рівня володіння мовою** (Нідерландська B2 або C1)
3.  **Тест знань та навичок** (BI-toets)
4.  **Заповнення заявки** в CIBG
5.  **Розгляд та реєстрація**

👉 На цьому сайті ви можете потренуватися для BI-toets та підготуватися до роботи в нідерландській стоматологічній практиці.
""",
        "link_text": "Більше інформації? Відвідайте [bigregister.nl](https://www.bigregister.nl)"
    },
    "es": {
        "title": "📄 Información sobre el registro BIG",
        "markdown_content": """
Como dentista formado en el extranjero en los Países Bajos, debe registrarse en el registro BIG (Profesiones Sanitarias Individuales).

### Pasos del proceso de registro:
1.  **Reconocimiento del diploma** a través de DUO o Nuffic
2.  **Prueba de competencia lingüística** (Neerlandés B2 o C1)
3.  **Evaluación de conocimientos y habilidades** (BI-toets)
4.  **Completar el formulario de solicitud** con CIBG
5.  **Evaluación y registro**

👉 En este sitio web, puede practicar para el BI-toets y prepararse para la práctica dental neerlandesa.
""",
        "link_text": "¿Más información? Visite [bigregister.nl](https://www.bigregister.nl)"
    },
    "tr": {
        "title": "📄 BIG Kayıt Bilgileri",
        "markdown_content": """
Hollanda'da yabancı eğitimli bir diş hekimi olarak BIG siciline (Bireysel Sağlık Meslekleri) kaydolmanız gerekmektedir.

### Kayıt sürecinin adımları:
1.  **Diploma denkliği** DUO veya Nuffic aracılığıyla
2.  **Dil yeterliliği kanıtı** (Hollandaca B2 veya C1)
3.  **Bilgi ve beceri değerlendirmesi** (BI-toets)
4.  **Başvuru formunun doldurulması** CIBG ile
5.  **Değerlendirme ve kayıt**

👉 Bu web sitesinde, BI-toets için pratik yapabilir ve Hollanda diş hekimliği pratiğine hazırlanabilirsiniz.
""",
        "link_text": "Daha fazla bilgi? [bigregister.nl](https://www.bigregister.nl) adresini ziyaret edin"
    },
    "fa": {
        "title": "📄 اطلاعات ثبت نام BIG",
        "markdown_content": """
به عنوان یک دندانپزشک آموزش دیده در خارج از کشور در هلند، باید در رجیستر BIG (مشاغل مراقبت های بهداشتی فردی) ثبت نام کنید.

### مراحل فرآیند ثبت نام:
۱. **ارزشیابی مدرک تحصیلی** از طریق DUO یا Nuffic
۲. **اثبات تسلط بر زبان** (هلندی B2 یا C1)
۳. **ارزیابی دانش و مهارت** (آزمون BI)
۴. **تکمیل فرم درخواست** با CIBG
۵. **ارزیابی و ثبت نام**

👈 در این وب سایت، می توانید برای آزمون BI تمرین کرده و برای کار دندانپزشکی در هلند آماده شوید.
""",
        "link_text": "اطلاعات بیشتر؟ از [bigregister.nl](https://www.bigregister.nl) دیدن کنید"
    },
    "pt": {
        "title": "📄 Informações sobre o registo BIG",
        "markdown_content": """
Como dentista formado no estrangeiro nos Países Baixos, deve registar-se no registo BIG (Profissões Individuais de Saúde).

### Etapas do processo de registo:
1.  **Reconhecimento do diploma** via DUO ou Nuffic
2.  **Prova de proficiência linguística** (Neerlandês B2 ou C1)
3.  **Avaliação de conhecimentos e competências** (BI-toets)
4.  **Preencher o formulário de candidatura** junto do CIBG
5.  **Avaliação e registo**

👉 Neste website, pode praticar para o BI-toets e preparar-se para a prática dentária neerlandesa.
""",
        "link_text": "Mais informações? Visite [bigregister.nl](https://www.bigregister.nl)"
    }
}

def render(lang="nl"):
    t = texts.get(lang, texts["nl"])

    st.title(t["title"])

    st.markdown(t["markdown_content"])

    st.success(t["link_text"])