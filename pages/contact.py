from taipy.gui import Markdown

text = "Welcome to the contact section!"

contact_md = Markdown("""
# Contact
#### <center>Please feel free to reach out to me via email or LinkedIn. </center>
#### <center> I am generally open to new opportunities and collaborations.</center>
<div class="social-icons">
        <a href="https://www.linkedin.com/in/ayushrijain" target="_blank" class="social-icon"><i><img src="assets/linkedin.png"></img></i></a>
        <a href="https://github.com/AJ1904" target="_blank" class="social-icon"><img src="assets/github.png"></img></a>
        <a href="mailto:ayushrijain19@gmail.com" target="_blank" class="social-icon"><img src="assets/gmail.png"></img></a>
        <a href="https://grad.tamu.edu/aggie-life/aggie-voice/ayushri-jain" target="_blank" class="social-icon"><img src="assets/tamu_logo.png"></img></a>
        <a href="https://ayushrijain.hashnode.dev/" target="_blank" class="social-icon"><img src="assets/hashnode_logo.png"></img></a>
    </div>
""")