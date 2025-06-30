# import streamlit as st

# def show():
#     st.title("📘 DevOps Fundamentals")
#     st.markdown("---")

#     st.write("""
#     هذه الوحدة تعرّفك على المفاهيم الأساسية في DevOps:  
#     كيف بدأ؟ ما الفرق بينه وبين الطرق التقليدية؟ ولماذا يُعد فلسفة وليست أداة فقط؟

#     سنتناول سويًا:
#     - الفرق بين Agile وDevOps
#     - أساسيات التعاون بين الفرق
#     - أهمية الأتمتة والبنية التحتية ككود (IaC)
#     - كيف نقيس الأداء ونحسّنه (DORA metrics)
#     """)

#     st.markdown("## 🕰️ DevOps Timeline")

#     timeline = {
#         "2001": "🔹 **ظهور Agile Manifesto**: بداية التفكير في التعاون والمرونة في تطوير البرمجيات.",
#         "2007": "🔸 **ولادة مفهوم DevOps**: بدأ يتشكل من النقاشات حول صراع التطوير والتشغيل.",
#         "2009": "🔹 **أول مؤتمر DevOpsDays** في بلجيكا: النقلة الرسمية نحو حركة DevOps.",
#         "2011": "🔸 **نمو أدوات CI/CD**: ظهور Jenkins وGitLab وغيرها.",
#         "2016": "🔹 **Infrastructure as Code**: تفشي استخدام أدوات مثل Terraform وAnsible.",
#         "2020+": "🔸 **DevOps Cloud-Native**: انتشار Kubernetes وMicroservices والفلسفة السحابية."
#     }

#     for year, event in timeline.items():
#         st.markdown(f"**{year}** — {event}")

#     st.markdown("---")
#     st.info("⬅️ استخدم القائمة الجانبية للعودة إلى الصفحة الرئيسية")
#     st.markdown("## 🧩 مفاهيم أساسية في DevOps")

# with st.expander("🔄 Agile vs DevOps"):
#     st.write("""
#     - **Agile**: إطار عمل لتطوير البرمجيات بسرعة ومرونة من خلال دورات قصيرة وتعاون مستمر.
#     - **DevOps**: ثقافة وممارسات تجمع بين التطوير (Dev) والتشغيل (Ops) لتحقيق تسليم مستمر وتشغيل موثوق.
#     - **الفرق؟** Agile يهتم بتطوير البرمجيات، DevOps يهتم بتوصيلها وتشغيلها بكفاءة.

#     ✅ المثال: Agile يبني السيارة... DevOps يضمن أنها تشتغل بكفاءة وتسافر بأمان.
#     """)

# with st.expander("🚀 CI/CD"):
#     st.write("""
#     - **CI** (التكامل المستمر): دمج تغييرات الكود تلقائيًا واختبارها بشكل متكرر.
#     - **CD** (التسليم/النشر المستمر): توصيل التحديثات تلقائيًا إلى بيئة الإنتاج بسرعة وثقة.
#     - يقللان من الأخطاء، ويسرّعان التحديثات، ويحسّنان تجربة المستخدم.

#     🛠 أدوات شائعة: GitHub Actions, GitLab CI, Jenkins.
#     """)

# with st.expander("💻 IaC – Infrastructure as Code"):
#     st.write("""
#     - **تعريف**: إدارة البنية التحتية (سيرفرات، قواعد بيانات...) باستخدام كود، بدلًا من الإعداد اليدوي.
#     - يساعد في الاتساق، القابلية للتكرار، والنسخ الاحتياطي السريع.
    
#     🧩 أدوات شائعة: Terraform, Ansible, Pulumi.
#     """)

# with st.expander("📊 DORA Metrics"):
#     st.write("""
#     - **DORA** هو اختصار لـ DevOps Research and Assessment.
#     - 4 مؤشرات رئيسية تقيس فاعلية الفرق:
#         - Lead Time for Changes
#         - Deployment Frequency
#         - Mean Time to Restore
#         - Change Failure Rate

#     📈 الفرق ذات الأداء العالي تحقق استقرارًا وتحسّنًا مستمرًا.
#     """)
#     st.markdown("## 🧪 اختبار سريع: DevOps vs Agile")

# question = "ما هو الفرق الجوهري بين Agile و DevOps؟"
# options = [
#     "Agile تهتم بالتشغيل، وDevOps تهتم بالتطوير",
#     "Agile هي لغة برمجة، وDevOps نظام تشغيل",
#     "Agile تركز على تطوير البرمجيات، وDevOps على تشغيلها وتسليمها",
#     "Agile تعتمد على الحوسبة السحابية، وDevOps لا تدعم ذلك"
# ]

# answer = st.radio(question, options)

# if answer:
#     if answer == options[2]:
#         st.success("🎉 إجابة صحيحة! بالفعل، Agile تركز على التطوير وDevOps على التشغيل والتسليم المستمر.")
#     else:
#         st.error("❌ للأسف، ليست الإجابة الصحيحة. راجع بطاقة Agile vs DevOps أعلاه ✨")
#         st.markdown("## 🔁 دورة DevOps (DevOps Loop)")

# st.graphviz_chart("""
#   digraph devops_infinity {
#     rankdir=LR;
#     node [shape=circle, style=filled, color=lightblue];

#     Plan -> Develop -> Build -> Test -> Release -> Deploy -> Operate -> Monitor -> Plan;
#   }
# """)
import streamlit as st

def show():
    st.title("📘 DevOps Fundamentals")
    st.markdown("---")

    # 👋 مقدّمة الوحدة
    st.write("""
    هذه الوحدة تعرّفك على المفاهيم الأساسية في DevOps:  
    كيف بدأ؟ ما الفرق بينه وبين الطرق التقليدية؟ ولماذا يُعد فلسفة وليست أداة فقط؟

    سنتناول سويًا:
    - الفرق بين Agile وDevOps
    - أساسيات التعاون بين الفرق
    - أهمية الأتمتة والبنية التحتية ككود (IaC)
    - كيف نقيس الأداء ونحسّنه (DORA metrics)
    """)

    # 🕰️ الجدول الزمني لتاريخ DevOps
    st.markdown("## 🕰️ DevOps Timeline")

    timeline = {
        "2001": "🔹 **ظهور Agile Manifesto**: بداية التفكير في التعاون والمرونة في تطوير البرمجيات.",
        "2007": "🔸 **ولادة مفهوم DevOps**: بدأ يتشكل من النقاشات حول صراع التطوير والتشغيل.",
        "2009": "🔹 **أول مؤتمر DevOpsDays** في بلجيكا: النقلة الرسمية نحو حركة DevOps.",
        "2011": "🔸 **نمو أدوات CI/CD**: ظهور Jenkins وGitLab وغيرها.",
        "2016": "🔹 **Infrastructure as Code**: تفشي استخدام أدوات مثل Terraform وAnsible.",
        "2020+": "🔸 **DevOps Cloud-Native**: انتشار Kubernetes وMicroservices والفلسفة السحابية."
    }

    for year, event in timeline.items():
        st.markdown(f"**{year}** — {event}")

    st.markdown("---")
    st.info("⬅️ استخدم القائمة الجانبية للعودة إلى الصفحة الرئيسية")

    # 🧩 مفاهيم أساسية
    st.markdown("## 🧩 مفاهيم أساسية في DevOps")

    with st.expander("🔄 Agile vs DevOps"):
        st.write("""
        - **Agile**: إطار عمل لتطوير البرمجيات بسرعة ومرونة من خلال دورات قصيرة وتعاون مستمر.
        - **DevOps**: ثقافة وممارسات تجمع بين التطوير (Dev) والتشغيل (Ops) لتحقيق تسليم مستمر وتشغيل موثوق.
        - **الفرق؟** Agile يهتم بتطوير البرمجيات، DevOps يهتم بتوصيلها وتشغيلها بكفاءة.

        ✅ المثال: Agile يبني السيارة... DevOps يضمن أنها تشتغل بكفاءة وتسافر بأمان.
        """)

    with st.expander("🚀 CI/CD"):
        st.write("""
        - **CI** (التكامل المستمر): دمج تغييرات الكود تلقائيًا واختبارها بشكل متكرر.
        - **CD** (التسليم/النشر المستمر): توصيل التحديثات تلقائيًا إلى بيئة الإنتاج بسرعة وثقة.
        - يقللان من الأخطاء، ويسرّعان التحديثات، ويحسّنان تجربة المستخدم.

        🛠 أدوات شائعة: GitHub Actions, GitLab CI, Jenkins.
        """)

    with st.expander("💻 IaC – Infrastructure as Code"):
        st.write("""
        - **تعريف**: إدارة البنية التحتية (سيرفرات، قواعد بيانات...) باستخدام كود، بدلًا من الإعداد اليدوي.
        - يساعد في الاتساق، القابلية للتكرار، والنسخ الاحتياطي السريع.
        
        🧩 أدوات شائعة: Terraform, Ansible, Pulumi.
        """)

    with st.expander("📊 DORA Metrics"):
        st.write("""
        - **DORA** هو اختصار لـ DevOps Research and Assessment.
        - 4 مؤشرات رئيسية تقيس فاعلية الفرق:
            - Lead Time for Changes
            - Deployment Frequency
            - Mean Time to Restore
            - Change Failure Rate

        📈 الفرق ذات الأداء العالي تحقق استقرارًا وتحسّنًا مستمرًا.
        """)

    # 🧪 اختبار تفاعلي
    st.markdown("## 🧪 اختبار سريع: DevOps vs Agile")

    question = "ما هو الفرق الجوهري بين Agile و DevOps؟"
    options = [
        "Agile تهتم بالتشغيل، وDevOps تهتم بالتطوير",
        "Agile هي لغة برمجة، وDevOps نظام تشغيل",
        "Agile تركز على تطوير البرمجيات، وDevOps على تشغيلها وتسليمها",
        "Agile تعتمد على الحوسبة السحابية، وDevOps لا تدعم ذلك"
    ]

    selected = st.radio(question, options, index=None, key="quiz1")

    if st.button("✅ تحقق من إجابتك"):
        if selected:
            if selected == options[2]:
                st.success("🎉 إجابة صحيحة! بالفعل، Agile تركز على التطوير وDevOps على التشغيل والتسليم المستمر.")
            else:
                st.error("❌ ليست الإجابة الصحيحة. راجع بطاقة Agile vs DevOps أعلاه ✨")
        else:
            st.warning("⚠️ الرجاء اختيار إجابة أولًا.")

    # 🔁 رسم DevOps Loop
    st.markdown("## 🔄 دورة DevOps (DevOps Loop)")

    st.graphviz_chart("""
      digraph devops_infinity {
        rankdir=LR;
        node [shape=circle, style=filled, color=lightblue];

        Plan -> Develop -> Build -> Test -> Release -> Deploy -> Operate -> Monitor -> Plan;
      }
    """)