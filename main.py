from taipy.gui import Gui
from pages.home import home_md
from pages.projects import projects_md
from pages.certifications import certifications_md
from pages.contact import contact_md
from pages.education import education_md
from pages.experience import experience_md
from pages.recognition import recognition_md
from pages.skills import skills_md
from pages.volunteer import volunteer_md
from taipy.gui import Gui, navigate
from taipy.gui import Markdown

logo = "assets/logo.png"

root_md = Markdown("""
<|layout|columns=auto auto auto|class_name=container align_columns_center|
<|part|class_name=text_left|
<|{logo}|image|width=100px|>
|>
<center><|navbar|></center>
<|part|class_name=text_right|
<|toggle|theme|class_name=nolabel|>
|>
|>
<|content|>

""")
pages = {
    "/": root_md,
    "Home": home_md,
    "Education": education_md,
    "Experience": experience_md,
    "Skills": skills_md,
    "Certifications": certifications_md,
    "Projects": projects_md,
    "Recognition": recognition_md,
    "Volunteer": volunteer_md,
    "Contact": contact_md,
    
}

page_names = [page for page in pages.keys() if page not in ["/"]]


gui = Gui(pages=pages, css_file="styles/styles.css")
gui.run(run_browser=True, use_reloader=True, title="Ayushri Jain", favicon="assets/logo.png")
