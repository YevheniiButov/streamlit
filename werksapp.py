import streamlit as st
import json
from pathlib import Path
import importlib

st.set_page_config(page_title="Become a Tandarts", layout="wide")

DATA_DIR = Path("data")
MODULES_DIR = Path("modules")
DEFAULT_LANG = "en"

def load_module_definitions():
    path = DATA_DIR / "modules.json"
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            st.error(f"❌ Error loading module definitions ({path}): {e}")
            return []
    else:
        st.warning(f"⚠️ Module definition file not found: {path}")
        return []

languages = {
    "en": "English", "nl": "Nederlands", "ru": "Русский",
    "uk": "Українська", "es": "Español", "tr": "Türkçe",
    "fa": "فارسی", "pt": "Português"
}

if "lang" not in st.session_state:
    st.session_state.lang = DEFAULT_LANG

selected_lang_key = st.sidebar.selectbox(
    "🌐 Language / Taal / Язык",
    options=list(languages.keys()),
    format_func=lambda k: languages[k],
    key="lang",
    index=list(languages.keys()).index(st.session_state.lang)
)

menu_keys = [
    "home",
    "bi_toets",
    "flashcards",
    "dutch_phrases",
    "big_info",
    "syllabus"
]

menu_options_translations = {
    "home": {
        "en": "🏠 Home", "ru": "🏠 Главная", "nl": "🏠 Thuis", "uk": "🏠 Головна",
        "es": "🏠 Inicio", "tr": "🏠 Ana Sayfa", "fa": "🏠 خانه", "pt": "🏠 Início"
    },
    "bi_toets": {
        "en": "🧪 BI-Toets", "ru": "🧪 BI-Toets", "nl": "🧪 BI-Toets", "uk": "🧪 BI-Toets",
        "es": "🧪 BI-Toets", "tr": "🧪 BI-Toets", "fa": "🧪 آزمون BI", "pt": "🧪 BI-Toets"
    },
    "flashcards": {
        "en": "🧠 Flashcards (soon)", "ru": "🧠 Карточки (скоро)", "nl": "🧠 Flashcards (binnenkort)",
        "uk": "🧠 Картки (незабаром)", "es": "🧠 Tarjetas (pronto)", "tr": "🧠 Bilgi Kartları (yakında)",
        "fa": "🧠 فلش کارت (به زودی)", "pt": "🧠 Flashcards (em breve)"
    },
    "dutch_phrases": {
        "en": "💬 Dutch Phrases (soon)", "ru": "💬 Голландские фразы (скоро)", "nl": "💬 Nederlandse Zinnen (binnenkort)",
        "uk": "💬 Голландські фрази (незабаром)", "es": "💬 Frases en neerlandés (pronto)", "tr": "💬 Hollandaca İfadeler (yakında)",
        "fa": "💬 عبارات هلندی (به زودی)", "pt": "💬 Frases em holandês (em breve)"
    },
    "big_info": {
        "en": "📄 BIG Info", "ru": "📄 Информация BIG", "nl": "📄 BIG Info", "uk": "📄 Інформація BIG",
        "es": "📄 Información BIG", "tr": "📄 BIG Bilgisi", "fa": "📄 اطلاعات BIG", "pt": "📄 Informação BIG"
    },
    "syllabus": {
        "en": "📖 Syllabus (Example)", "ru": "📖 Учебный план (Пример)", "nl": "📖 Syllabus (Voorbeeld)",
        "uk": "📖 Навчальний план (Приклад)", "es": "📖 Programa (Ejemplo)", "tr": "📖 Müfredat (Örnek)",
        "fa": "📖 سرفصل دروس (مثال)", "pt": "📖 Programa (Exemplo)"
    }
}

menu_labels = {
    "en": "📚 Section:", "ru": "📚 Раздел:", "nl": "📚 Sectie:",
    "uk": "📚 Розділ:", "es": "📚 Sección:", "tr": "📚 Bölüm:",
    "fa": "📚 بخش:", "pt": "📚 Seção:"
}

if "menu_select" not in st.session_state:
    st.session_state.menu_select = "home"

current_lang = st.session_state.lang

def get_translated_menu_name(key):
    return menu_options_translations.get(key, {}).get(current_lang, key.replace("_", " ").title())

selected_menu_key = st.sidebar.selectbox(
    menu_labels.get(current_lang, "📚 Section:"),
    options=menu_keys,
    format_func=get_translated_menu_name,
    key="menu_select"
)

st.markdown("---")

try:
    if selected_menu_key == "home":
        st.title(get_translated_menu_name("home"))
        home_text = {
        "en": "Welcome! This platform is designed specifically for foreign-trained dentists preparing for the BIG registration process in the Netherlands. Here you will find resources to help you improve your Dutch language skills for professional practice, prepare effectively for the BI-toets (knowledge and skills assessment), and navigate the necessary steps towards your registration.",
        "ru": "Добро пожаловать! Эта платформа создана специально для стоматологов c иностранным образованием, готовящихся к процессу BIG-регистрации в Нидерландах. Здесь вы найдете ресурсы, которые помогут вам улучшить знание нидерландского языка для профессиональной практики, эффективно подготовиться к BI-toets (тест знаний и навыков) и разобраться в необходимых шагах для получения регистрации.",
        "nl": "Welkom! Dit platform is speciaal ontworpen voor tandartsen met een buitenlands diploma die zich voorbereiden op het BIG-registratieproces in Nederland. Hier vindt u hulpmiddelen om uw Nederlandse taalvaardigheid voor de beroepspraktijk te verbeteren, u effectief voor te bereiden op de BI-toets (kennis- en vaardighedentoets) en de noodzakelijke stappen naar uw registratie te doorlopen.",
        "uk": "Ласкаво просимо! Ця платформа розроблена спеціально для стоматологів з іноземною освітою, які готуються до процесу BIG-реєстрації в Нідерландах. Тут ви знайдете ресурси, що допоможуть вам покращити знання нідерландської мови для професійної практики, ефективно підготуватися до BI-toets (тест знань та навичок) та розібратися y необхідних кроках для отримання реєстрації.",
        "es": "¡Bienvenido/a! Esta plataforma está diseñada específicamente para dentistas formados en el extranjero que se preparan para el proceso de registro BIG en los Países Bajos. Aquí encontrará recursos para ayudarle a mejorar sus habilidades en el idioma neerlandés para la práctica profesional, prepararse eficazmente para el BI-toets (evaluación de conocimientos y habilidades) y navegar por los pasos necesarios hacia su registro.",
        "tr": "Hoş geldiniz! Bu platform, Hollanda'daki BIG kayit sürecine hazirlanan yabanci eğitimli diş hekimleri için özel olarak tasarlanmiştir. Burada, mesleki pratik için Hollandaca dil becerilerinizi geliştirmenize, BI-toets'e (bilgi ve beceri değerlendirmesi) etkili bir şekilde hazirlanmaniza ve kaydiniz için gerekli adimlarda yolunuzu bulmaniza yardimci olacak kaynaklar bulacaksiniz.",
        "fa": "خوش آمدید! این پلتفرم به طور خاص برای دندانپزشکان آموزش دیده در خارج از کشور که برای فرآیند ثبت نام BIG در هلند آماده می شوند، طراحی شده است. در اینجا منابعی برای کمک به بهبود مهارت های زبان هلندی شما برای فعالیت حرفه ای، آمادگی مؤثر برای آزمون BI (ارزیابی دانش و مهارت) و پیمایش مراحل لازم برای ثبت نام خود خواهید یافت.",
        "pt": "Bem-vindo(a)! Esta plataforma foi projetada especificamente para dentistas formados no estrangeiro que se preparam para o processo de registo BIG nos Países Baixos. Aqui encontrará recursos para ajudar a melhorar as suas competências na língua neerlandesa para a prática profissional, preparar-se eficazmente para o BI-toets (avaliação de conhecimentos e competências) e navegar pelos passos necessários para o seu registo."
}
        
        st.markdown(f"<p style='font-size:18px; color:#555;'>{home_text.get(current_lang, home_text[DEFAULT_LANG])}</p>", unsafe_allow_html=True)
        st.markdown("---")

    else:
        module_file_name = selected_menu_key
        try:
            module_path = f"modules.{module_file_name}"
            module_to_render = importlib.import_module(module_path)

            if hasattr(module_to_render, "render"):
                module_to_render.render(current_lang)
            elif hasattr(module_to_render, "show"):
                 module_to_render.show(current_lang)
            else:
                st.warning(f"Module '{module_file_name}' does not have a 'render' or 'show' function.")

        except ModuleNotFoundError:
            st.error(f"❌ Error: Could not find module file 'modules/{module_file_name}.py'")
            st.info(f"Please make sure the file exists and the key in 'menu_keys' matches the filename (without .py). File requested: {module_file_name}.py")
        except Exception as e_render:
            st.error(f"❌ Error rendering module '{selected_menu_key}': {e_render}")
            st.exception(e_render)

except Exception as e:
    st.error(f"❌ An unexpected error occurred: {e}")
    st.exception(e)