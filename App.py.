
import streamlit as st
import unicodedata

st.set_page_config(
    page_title="THE LAST COMMIT | 12А",
    page_icon="🔐",
    layout="centered"
)

# ---------- ДИЗАЙН ----------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(145deg, #100d18, #21152b, #120f19);
    color: #f7f0ff;
}
h1, h2, h3, p, label, div {
    color: #f7f0ff;
}
.hero {
    padding: 28px 20px;
    border: 1px solid #76548f;
    border-radius: 18px;
    background: rgba(35, 24, 47, .88);
    text-align: center;
    margin-bottom: 20px;
}
.eyebrow {
    color: #c9a5e8;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 700;
}
.hero h1 {
    font-size: 36px;
    color: #ead8ff;
}
.panel {
    padding: 22px;
    border: 1px solid #59406e;
    border-radius: 16px;
    background: rgba(28, 21, 38, .92);
    margin: 12px 0;
}
.level {
    color: #c9a5e8;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}
.location {
    color: #d9b8f5;
    font-weight: 700;
}
.stTextInput input {
    background: #f7f0ff;
    color: #21152b;
    border-radius: 10px;
}
.stButton button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #b58bd8;
    background: #79519b;
    color: white;
    font-weight: 700;
    min-height: 46px;
}
.stButton button:hover {
    background: #9468b8;
    color: white;
}
.success {
    padding: 16px;
    border-radius: 12px;
    background: #183528;
    border: 1px solid #3d8b65;
    color: #e0ffed;
}
</style>
""", unsafe_allow_html=True)


# ---------- МАРШРУТ И ЗАГАДКИ ----------

levels = [

    {
        "title": "Ниво 1 – Мисията започва",
        "place": "Вашето училище",
        "type": "MISSION START",

        "story": """
        Добре дошли, госпожо!

        Вашият 12А клас ви е подготвил специална мисия.
        Предстоят ви няколко загадки, малко разходки
        и вероятно въпросът: „Тези деца нормални ли са?“ 😂
        """,

        "question": """
        За да започнете мисията, трябва да откриете
        мястото, където цяла България е събрана
        в умален вид.

        Къде трябва да отидете?
        """,

        "hint": "Потърсете релефното изображение на България.",

        "answers": [
            "РЕЛЕФНАТА КАРТА",
            "КАРТАТА",
            "РЕЛЕФНА КАРТА",
            "КАРТАТА НА БЪЛГАРИЯ"
        ],

        "success": "Мисията е успешно стартирана!",

        "next": """
        Отидете до релефната карта на България.

        И не се притеснявайте, госпожо,
        засега ви разкарваме само в рамките на града! 😂
        """
    },

    {
        "title": "Ниво 2 – България в миниатюра",
        "place": "Релефната карта",
        "type": "C++ CHALLENGE",

        "story": """
        Първата спирка е достигната!
        Сега ще проверим дали програмирането
        все още е на ваша страна.
        """,

        "question": """
Какво ще изведе програмата?

```cpp
int a = 17;
int b = 78;
cout << a * 100 + b;
```""",

        "hint": "Умножете 17 по 100 и прибавете 78.",

        "answers": ["1778"],

        "success": "Правилно! Първият код е отключен!",

        "next": """
        Следващата ви спирка е Часовниковата кула!

        Времето лети, госпожо, а 12А явно
        е решило да ви организира туристическа обиколка.
        """
    },

    {
        "title": "Ниво 3 – Времето",
        "place": "Часовниковата кула",
        "type": "LOGIC CHALLENGE",

        "story": """
        Стигнахте до място, което отдавна измерва времето.
        Но нашата мисия все още не е приключила.
        """,

        "question": """
        Къде в Дряново се решават важните
        въпроси на града?

        Там работи кметът и се намира
        местната администрация.
        """,

        "hint": "Започва с буквата О.",

        "answers": [
            "ОБЩИНАТА",
            "ОБЩИНА",
            "ОБЩИНА ДРЯНОВО",
            "СГРАДАТА НА ОБЩИНАТА"
        ],

        "success": "Отговорът е правилен!",

        "next": """
        Отправете се към Община Дряново.

        Ако вече се чудите защо ви караме
        да обикаляте града, спокойно...
        И ние се чудим! 😂
        """
    },

    {
        "title": "Ниво 4 – Следващата следа",
        "place": "Община Дряново",
        "type": "HISTORY CHALLENGE",

        "story": """
        Продължавате отлично!
        Следващата следа е свързана
        с една от известните възрожденски къщи в Дряново.
        """,

        "question": """
        В Дряново има къща, известна
        с прозвището „Къщата без пирони“.

        Как се нарича тя?
        """,

        "hint": "Името ѝ започва с буквата Л.",

        "answers": [
            "ЛАФЧИЕВАТА КЪЩА",
            "ЛАФЧИЕВА КЪЩА",
            "КЪЩАТА БЕЗ ПИРОНИ"
        ],

        "success": "Точно така! Открихте следващата спирка!",

        "next": """
        Следващата ви спирка е Лафчиевата къща.

        Госпожо, вече имате сериозен километраж,
        но 12А ви уверява, че всичко е с добра цел! 💜
        """
    },

    {
        "title": "Ниво 5 – Последната загадка",
        "place": "Лафчиевата къща",
        "type": "FINAL DESTINATION",

        "story": """
        Достигнахте почти до края!
        Но последната дестинация няма да бъде
        обикновена забележителност.
        """,

        "question": """
        Не съм забележителност,
        нито място, което посещавате като турист.

        Там оставяте умората след дългия ден.
        Там ви очакват спокойствието и уютът.

        Това е мястото, което наричате свое.

        Къде трябва да отидете?
        """,

        "hint": "Там се прибирате след работа.",

        "answers": [
            "ДОМ",
            "ДОМЪТ",
            "У ДОМА",
            "ВКЪЩИ",
            "КЪЩИ"
        ],

        "success": "ПОСЛЕДНАТА ДЕСТИНАЦИЯ Е ОТКРИТА!",

        "next": """
        Госпожо, да, накарахме ви да обиколите Дряново,
        но обещаваме, че си заслужава!

        Приберете се у дома.
        Там ви очаква последната част от мисията.
        """
    },

    {
        "title": "Ниво 6 – Последният Commit",
        "place": "Финалната спирка",
        "type": "FINAL ACCESS",

        "story": """
        Госпожо, стигнахте до финала!

        След толкова загадки, кодове и разходки
        остава само един последен въпрос.
        """,

        "question": """
        Кой клас стои зад цялата тази тайна мисия?

        Въведете името на класа.
        """,

        "hint": "Две символа. Вашият любим клас!",

        "answers": ["12А", "12A", "12 А"],

        "success": "ФИНАЛНИЯТ ДОСТЪП Е ОТКЛЮЧЕН!",

        "next": "Системата е готова."
    }
]


# ---------- ПОМОЩНИ ФУНКЦИИ ----------

def normalize(value):
    value = unicodedata.normalize("NFKC", value)
    return " ".join(value.strip().upper().split())


if "unlocked" not in st.session_state:
    st.session_state.unlocked = 0

if "started" not in st.session_state:
    st.session_state.started = False

if "hints" not in st.session_state:
    st.session_state.hints = set()

if "completed_message" not in st.session_state:
    st.session_state.completed_message = None


# ---------- ЗАГЛАВИЕ ----------

st.markdown("""
<div class="hero">
    <div class="eyebrow">CLASSIFIED MISSION · 12А</div>
    <h1>THE LAST COMMIT</h1>
    <p>12А · Последният проект</p>
    <p>Някои проекти приключват. Други остават завинаги.</p>
</div>
""", unsafe_allow_html=True)

st.progress(st.session_state.unlocked / len(levels))
st.caption(
    f"Отключени нива: {st.session_state.unlocked} от {len(levels)}"
)


# ---------- НАЧАЛО ----------

if not st.session_state.started:

    st.markdown("""
    <div class="panel">
        <div class="level">ВХОДЯЩО СЪОБЩЕНИЕ</div>
        <h2>Добре дошли в мисията, госпожо!</h2>
        <p>
        Вашият 12А клас ви е избрал за специална операция.
        Предстоят ви загадки, тайни следи и няколко
        непланирани разходки из Дряново.
        </p>
        <p><b>Правило:</b> всяко ниво се отключва само след правилен отговор.</p>
        <p>Надяваме се да сте с удобни обувки! 😂</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("СТАРТИРАЙ МИСИЯТА"):
        st.session_state.started = True
        st.rerun()


# ---------- ПОСЛЕДНО ОТКЛЮЧЕНО НИВО ----------

if st.session_state.completed_message is not None:

    st.markdown(
        f"""
        <div class="success">
        <b>✓ {levels[st.session_state.completed_message]['success']}</b>
        <br><br>
        {levels[st.session_state.completed_message]['next']}
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- АКТИВНО НИВО ----------

if st.session_state.started and st.session_state.unlocked < len(levels):

    i = st.session_state.unlocked
    level = levels[i]

    st.markdown(f"""
    <div class="panel">
        <div class="level">{level['type']}</div>
        <h2>{level['title']}</h2>
        <p class="location">📍 {level['place']}</p>
        <p>{level['story']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔐 Вашата задача")
    st.markdown(level["question"])

    answer = st.text_input(
        "Въведете отговора:",
        key=f"answer_{i}",
        placeholder="Напишете отговора тук..."
    )

    if st.button("ПРОВЕРИ ОТГОВОРА", key=f"check_{i}"):

        accepted = [normalize(a) for a in level["answers"]]

        if normalize(answer) in accepted:

            st.session_state.completed_message = i
            st.session_state.unlocked += 1
            st.session_state.hints.discard(i)
            st.rerun()

        else:
            st.error(
                "Достъпът е отказан! Отговорът не е правилен. Опитайте отново."
            )

    if i not in st.session_state.hints:

        if st.button("ПОКАЖИ ПОДСКАЗКА", key=f"hint_{i}"):
            st.session_state.hints.add(i)
            st.rerun()

    else:
        st.info("Подсказка: " + level["hint"])


# ---------- ФИНАЛ ----------

if st.session_state.started and st.session_state.unlocked == len(levels):

    st.balloons()

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">ALL LEVELS COMPLETED</div>
        <h1>SYSTEM SUCCESS</h1>
        <p>Мисията е изпълнена!</p>
    </div>

    <div class="panel">
        <h2>Скъпа госпожо,</h2>

        <p>
        Успешно преминахте всички нива!
        Открихте кодовете, разгадавахте загадките
        и обиколихте почти целия град.
        </p>

        <p>
        Вероятно вече се питате защо 12А ви накара
        да извървите толкова километри.
        Е, всяка крачка имаше своя причина.
        </p>

        <p>
        През годините заедно написахме една история.
        Имаше трудни задачи, грешки, смях,
        поправки и безброй незабравими моменти.
        </p>

        <p>
        Вие бяхте човекът, който ни водеше
        през всички тях.
        </p>

        <h3 style="color:#e2c4ff; text-align:center;">
        Госпожо, ще бъдете ли наш специален гост
        на абитуриентския ни бал?
        </h3>

        <p style="text-align:center;">
        С обич, Вашият 12А клас ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### FINAL PROJECT · CLASS 12А")
    st.caption("Error 404: По-добра класна не е намерена.")


st.divider()
st.caption("THE LAST COMMIT · A special mission created by 12А")
