from taipy.gui import Markdown, Html
from config import *
# import * from app.config
from functions import *

text = "Welcome to the home!"
greeting = greeting_text
namevar = name
gif = "https://media.giphy.com/media/3o7aD2FQDSVdppqWIQ/giphy.gif"
typing_texts = typing_texts


# home_md = Markdown("""
# # 
# <br/>
# <|{greeting}|text|class_name=h1|>
# <|layout|columns=1 1|
# <|part|
# <|I am {namevar}.|text|class_name=h2|>
# ![](https://readme-typing-svg.demolab.com?font=Roboto&color=000000&multiline=true&random=false&width=1200&height=200&lines=Always+learning+and+exploring+the+intersections+of+technology+and+innovation.;Passionate+about+simplifying%2C+automating+and+optimizing+pipelines%2C+machine+learning+models+and+software.;Creating+unique+and+simplistic+applications+in+creative+ways.)
# |>

# <|part|
# <|{gif}|image|>
# |>
# |>

# """)
home_md = Html("""

<div class="homecontainer">
    <h1>Hey! :D</h1>
    <h2>I am <span class="homename"> Ayushri Jain</span>.</h2>

    <div class="homecontent">
        <div class="homeimage-container">
            <img class="homegif-image" src="assets/homegif.gif"></img>
        </div>
    </div>
     
    <h4 class="homeh5">Always learning and exploring the intersections of technology and innovation.</h4>
    <h4 class="homeh5">Passionate about simplifying, automating, and optimizing pipelines, machine learning models, and software.</h4>
    <h4 class="homeh5">Creating unique and simplistic applications in creative ways.</h4>

</div>

<div class="social-icons">
        <a href="https://www.linkedin.com/in/ayushrijain" target="_blank" class="social-icon"><i><img src="assets/linkedin.png"></img></i></a>
        <a href="https://github.com/AJ1904" target="_blank" class="social-icon"><img src="assets/github.png"></img></a>
        <a href="mailto:ayushrijain19@gmail.com" target="_blank" class="social-icon"><img src="assets/gmail.png"></img></a>
        <a href="https://grad.tamu.edu/aggie-life/aggie-voice/ayushri-jain" target="_blank" class="social-icon"><img src="assets/tamu_logo.png"></img></a>
        
    </div>

""")


# <div class="homecontent">
    #     <img src="https://readme-typing-svg.demolab.com?font=Roboto&color=000000&center=true&vCenter=true&multiline=true&random=false&width=1200&height=200&lines=Always+learning+and+exploring+the+intersections+of+technology+and+innovation.;Passionate+about+simplifying%2C+automating+and+optimizing+pipelines%2C+machine+learning+models+and+software.;Creating+unique+and+simplistic+applications+in+creative+ways."></img>
    # </div>   