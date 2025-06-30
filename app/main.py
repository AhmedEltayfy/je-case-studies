# import streamlit as st
# from modules import fundamentals

# st.set_page_config(page_title="Joseph's Empire", page_icon="👑", layout="centered")

# # قائمة جانبية للتنقل
# st.sidebar.title("🚪 التنقل")
# page = st.sidebar.radio("اذهب إلى:", ["الصفحة الرئيسية", "DevOps Fundamentals"])

# # التوجيه
# if page == "الصفحة الرئيسية":
#     st.title("👑 Welcome to Joseph's Empire")
#     st.subheader("Where Code Meets Economics, and Wisdom Inspires Innovation")
#     st.markdown("""
#     **Joseph’s Empire** is an educational platform reimagining how we learn modern economics, programming, and data through the timeless wisdom of Prophet Joseph.
#     """)
#     st.markdown("---")
#     st.markdown("📄 [النسخة العربية](https://github.com/AhmedEltayfy/JE/blob/main/README.ar.md)")
#     st.markdown("📘 [English Version](https://github.com/AhmedEltayfy/JE/blob/main/README.md)")
#     st.markdown("---")
#     st.caption("Made with 💡 and purpose by Ahmed Anwar Eltayfy")

# elif page == "DevOps Fundamentals":
#     fundamentals.show()
import streamlit as st
from modules import fundamentals, ci_cd_lab  # ✅ موديولاتنا

st.set_page_config(page_title="Joseph's Empire", page_icon="👑", layout="centered")

# قائمة جانبية للتنقل
st.sidebar.title("🚪 التنقل")
titles = ["الصفحة الرئيسية", "DevOps Fundamentals", "CI/CD Lab"]

# أضف إشارات اجتياز
if "ci_cd_passed" in st.session_state and st.session_state.ci_cd_passed:
    titles[2] += " ✅"

page = st.sidebar.radio("اذهب إلى:", titles)

# التوجيه
if page == "الصفحة الرئيسية":
    st.title("👑 Welcome to Joseph's Empire")
    st.subheader("Where Code Meets Economics, and Wisdom Inspires Innovation")
    st.markdown("""
    **Joseph’s Empire** is an educational platform reimagining how we learn modern economics, programming, and data through the timeless wisdom of Prophet Joseph.
    """)
    st.markdown("---")
    st.markdown("📄 [النسخة العربية](https://github.com/AhmedEltayfy/JE/blob/main/README.ar.md)")
    st.markdown("📘 [English Version](https://github.com/AhmedEltayfy/JE/blob/main/README.md)")
    st.markdown("---")
    st.markdown("## 🌟 الآن يمكنك مشاركة تجربتك مباشرة:")
    st.markdown("[🔗 اضغط هنا لتجربة Joseph’s Empire عبر Streamlit](https://je-case-studies-haqoxuyrcesxc4u7g8ykaj.streamlit.app/)")
    st.caption("Made with 💡 and purpose by Ahmed Anwar Eltayfy")

elif page == "DevOps Fundamentals":
    fundamentals.show()

elif "CI/CD Lab" in page:
    ci_cd_lab.show()