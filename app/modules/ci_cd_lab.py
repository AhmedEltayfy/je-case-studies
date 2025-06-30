# import streamlit as st
# import base64

# def show():
#     st.title("🚀 CI/CD Lab")
#     st.markdown("---")

#     st.write("""
#     في هذا الموديول، سنقوم بإنشاء أول **Pipeline CI/CD** باستخدام GitHub Actions.  
#     الهدف هو بناء تطبيق Streamlit تلقائيًا وتشغيله بعد كل تعديل.

#     📦 ستتعلّم:
#     - إنشاء ملف Workflow داخل `.github/workflows/`
#     - تفعيل `build → test → deploy` تلقائيًا
#     - عرض الحالة مباشرة داخل GitHub
#     """)

#     with st.expander("📁 مثال على ملف GitHub Actions"):
#         st.code("""
# name: CI/CD

# on:
#   push:
#     branches: [ main ]

# jobs:
#   build:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       - name: Setup Python
#         uses: actions/setup-python@v4
#         with:
#           python-version: '3.10'
#       - name: Install dependencies
#         run: pip install -r requirements.txt
#       - name: Run Streamlit test
#         run: streamlit run app/main.py --headless
#         """, language="yaml")

#     st.info("⏭️ في المرحلة القادمة، ستقوم برفع الملف إلى GitHub وتجربة أول Build حقيقي.")

#     # زر تحميل ملف YAML
#     st.markdown("### ⬇️ تحميل ملف CI/CD")

#     yml_content = """
# name: CI/CD

# on:
#   push:
#     branches: [ main ]

# jobs:
#   build:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       - name: Setup Python
#         uses: actions/setup-python@v4
#         with:
#           python-version: '3.10'
#       - name: Install dependencies
#         run: pip install -r requirements.txt
#       - name: Run Streamlit
#         run: streamlit run app/main.py --headless
# """

#     b64 = base64.b64encode(yml_content.encode()).decode()
#     href = f'<a href="data:file/text;base64,{b64}" download="ci-cd.yml">📥 اضغط هنا لتحميل الملف</a>'
#     st.markdown(href, unsafe_allow_html=True)

#     # 🧪 التحدي التطبيقي
#     st.markdown("## 🧪 التحدي التطبيقي")

#     st.write("""
# 📌 **المطلوب:**

# 1. أنشئ مستودع جديد على GitHub (أو استخدم الموجود).
# 2. أنشئ مجلد `.github/workflows/` داخل مشروعك.
# 3. حمّل ملف `ci-cd.yml` من هذا الموديول وضعه داخل المجلد.
# 4. عدّل على الكود، ثم ادفع التغييرات إلى الفرع `main`.
# 5. راقب صفحة **Actions** على GitHub للتحقق من نجاح Pipeline.

# 🎯 التحدي يمنحك أول تجربة CI/CD حقيقية داخل مشروعك التعليمي!
# """)

#     # ✅ زر اجتياز التحدي + وسام
#     if st.button("🎉 اجتزت هذا التحدي"):
#         st.success("🥳 مبروك يا أحمد! اجتزت تحدي CI/CD بنجاح — خطوة عظيمة نحو التمكّن من DevOps الحقيقي 👑")
#         st.balloons()
#         st.markdown("### 🏅 وسام التحدي:")
#         st.markdown("#### ✅ CI/CD Challenger: [Github + Actions + Streamlit]")
import streamlit as st
import base64

def show():
    st.title("🚀 CI/CD Lab")
    st.markdown("---")

    # ✅ تهيئة حالة الجلسة
    if "ci_cd_passed" not in st.session_state:
        st.session_state.ci_cd_passed = False

    st.write("""
    في هذا الموديول، سنقوم بإنشاء أول **Pipeline CI/CD** باستخدام GitHub Actions.  
    الهدف هو بناء تطبيق Streamlit تلقائيًا وتشغيله بعد كل تعديل.

    📦 ستتعلّم:
    - إنشاء ملف Workflow داخل `.github/workflows/`
    - تفعيل `build → test → deploy` تلقائيًا
    - عرض الحالة مباشرة داخل GitHub
    """)

    with st.expander("📁 مثال على ملف GitHub Actions"):
        st.code("""
name: CI/CD

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Streamlit test
        run: streamlit run app/main.py --headless
        """, language="yaml")

    st.info("⏭️ في المرحلة القادمة، ستقوم برفع الملف إلى GitHub وتجربة أول Build حقيقي.")

    # ⬇️ تحميل ملف YAML
    st.markdown("### ⬇️ تحميل ملف CI/CD")

    yml_content = """
name: CI/CD

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Streamlit
        run: streamlit run app/main.py --headless
"""

    b64 = base64.b64encode(yml_content.encode()).decode()
    href = f'<a href="data:file/text;base64,{b64}" download="ci-cd.yml">📥 اضغط هنا لتحميل الملف</a>'
    st.markdown(href, unsafe_allow_html=True)

    # 🧪 التحدي التطبيقي
    st.markdown("## 🧪 التحدي التطبيقي")

    st.write("""
📌 **المطلوب:**

1. أنشئ مستودع جديد على GitHub (أو استخدم الموجود).
2. أنشئ مجلد `.github/workflows/` داخل مشروعك.
3. حمّل ملف `ci-cd.yml` من هذا الموديول وضعه داخل المجلد.
4. عدّل على الكود، ثم ادفع التغييرات إلى الفرع `main`.
5. راقب صفحة **Actions** على GitHub للتحقق من نجاح Pipeline.

🎯 التحدي يمنحك أول تجربة CI/CD حقيقية داخل مشروعك التعليمي!
""")

    # ✅ زر اجتياز التحدي
    if st.button("🎉 اجتزت هذا التحدي"):
        st.session_state.ci_cd_passed = True
        st.success("🥳 مبروك يا أحمد! اجتزت تحدي CI/CD بنجاح — خطوة عظيمة نحو التمكّن من DevOps الحقيقي 👑")
        st.balloons()

    # 🏅 عرض الوسام لو تم الاجتياز
    if st.session_state.ci_cd_passed:
        st.markdown("### 🏅 وسام التحدي:")
        st.markdown("#### ✅ CI/CD Challenger: [Github + Actions + Streamlit]")