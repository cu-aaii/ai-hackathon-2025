


#import streamlit as st
# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import altair as alt

# # Sample JSON Data (Competency Mapping)
# sample_json = """
# {
#   "course_id": "COURSE001",
#   "course_name": "Attacks and Defenses",
#   "competency_mapping": [
#     {
#       "competency": "Medical Knowledge",
#       "sub_competencies": [
#         {
#           "name": "Basic Sciences Application",
#           "coverage": "85%",
#           "missing_sessions": ["SESSION045"],
#           "ready_for_AAMC": false
#         },
#         {
#           "name": "Clinical Reasoning",
#           "coverage": "70%",
#           "missing_sessions": [],
#           "ready_for_AAMC": false
#         }
#       ]
#     },
#     {
#       "competency": "Patient Care",
#       "sub_competencies": [
#         {
#           "name": "History Taking",
#           "coverage": "95%",
#           "missing_sessions": [],
#           "ready_for_AAMC": true
#         }
#       ]
#     }
#   ],
#   "overall_AAMC_compliance": false,
#   "missing_courses": ["SESSION045"],
#   "recommendations": [
#     "Improve coverage for 'Basic Sciences Application' by adding missing sessions.",
#     "Enhance 'Clinical Reasoning' with additional mapped objectives.",
#     "Ensure all required competencies meet at least 90% coverage before submission."
#   ]
# }
# """

# # Load JSON Data
# data = json.loads(sample_json)

# # Streamlit UI
# st.title("📊 AAMC Competency Mapping Dashboard")
# st.subheader(f"Course: {data['course_name']} ({data['course_id']})")

# # AAMC Compliance Check
# if data["overall_AAMC_compliance"]:
#     st.success("✅ This course is **READY** for AAMC submission!")
# else:
#     st.warning("⚠️ This course is **NOT READY** for AAMC submission. Review missing competencies below.")

# # Prepare Data for Charts
# competency_names = []
# sub_competencies = []
# coverages = []
# ready_status = []

# for comp in data["competency_mapping"]:
#     for sub_comp in comp["sub_competencies"]:
#         competency_names.append(comp["competency"])
#         sub_competencies.append(sub_comp["name"])
#         coverages.append(int(sub_comp["coverage"].strip("%")))
#         ready_status.append("Ready" if sub_comp["ready_for_AAMC"] else "Not Ready")

# # Convert to Pandas DataFrame
# df = pd.DataFrame({
#     "Competency": competency_names,
#     "Sub-Competency": sub_competencies,
#     "Coverage (%)": coverages,
#     "Status": ready_status
# })

# # ------------------ 📊 Competency Coverage Progress Bars ------------------
# st.subheader("🧑‍🎓 Competency Coverage Breakdown")
# for comp in data["competency_mapping"]:
#     st.write(f"### **{comp['competency']}**")
#     for sub_comp in comp["sub_competencies"]:
#         coverage = int(sub_comp["coverage"].strip("%"))
#         st.write(f"📌 **{sub_comp['name']}**")
#         st.progress(coverage / 100)
#         if sub_comp["ready_for_AAMC"]:
#             st.success("✅ Meets AAMC requirements")
#         else:
#             st.warning(f"⚠️ Needs improvement (Current Coverage: {coverage}%)")

# # ------------------ 📊 Competency Coverage Pie Chart ------------------
# st.subheader("📊 Competency Coverage Overview")

# fig, ax = plt.subplots()
# ax.pie(df["Coverage (%)"], labels=df["Sub-Competency"], autopct='%1.1f%%', startangle=140, colors=["#66b3ff", "#ff9999", "#99ff99"])
# ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
# st.pyplot(fig)

# # ------------------ 📊 Competency Coverage Bar Chart ------------------
# st.subheader("📊 Competency Coverage by Sub-Competency")

# bar_chart = alt.Chart(df).mark_bar().encode(
#     x=alt.X("Sub-Competency", sort="-y"),
#     y="Coverage (%)",
#     color="Status"
# ).properties(width=700, height=400)

# st.altair_chart(bar_chart)

# # ------------------ 📝 Missing Sessions ------------------
# st.subheader("⚠️ Missing Sessions")
# if data["missing_courses"]:
#     missing_sessions_df = pd.DataFrame({"Missing Sessions": data["missing_courses"]})
#     st.table(missing_sessions_df)
# else:
#     st.success("✅ No missing sessions detected!")

# # ------------------ 📌 AI Recommendations ------------------
# st.subheader("📌 AI Recommendations for AAMC Compliance")
# for rec in data["recommendations"]:
#     st.write(f"🔹 {rec}")

# st.info("Make the suggested updates before resubmitting to AAMC for compliance approval.")
