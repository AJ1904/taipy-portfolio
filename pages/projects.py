from taipy.gui import Markdown
from taipy.gui import Gui
text = "Welcome to the projects section!"

projects_md = Markdown("""
# Projects
<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://saajheaven.web.app/" target="_blank"><img src="assets/saaj_logo.svg" alt="SAAJ Heaven Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>SAAJ Heaven Website</h3>
                <h5>🛠️ Angular, Firebase, Software Engineering</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 SAAJ Heaven is an art & craft store which creates and sells handmade traditional decor for festivals and other occasions.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Along with the store website, I have also built admin dashboard for them to manage their store webpage.</h6></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://github.com/AJ1904/Sentiment-Analysis-Using-Transformers" target="_blank"><img src="assets/github.png" alt="git Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Sentiment Analysis Using Transformers</h3>
                <h5>🛠️ TensorFlow, PyTorch, Machine Learning, Python</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 This project is about exploring and implementing various machine learning models like CNN, RNN and Transformers for sentiment analysis based on the YELP text review and stars.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 <a href="https://www.linkedin.com/in/ayushrijain/details/projects/50879504/multiple-media-viewer?profileId=ACoAAB92TxMBv2ka7uTyeovNcno2w0r-QrjBL_0&treasuryMediaId=1635554415863&type=DOCUMENT&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_projects_details%3BycUMRUCJRimajiHbqP%2F%2FQw%3D%3D" target="_blank">Report Link</a></h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Improved legacy code, thoroughly tested using rpsec testing tool and wrote cucumber tests to have 100% code coverage</h6></li>
                </ul>
            </div>
        </div>
    </div>
</div>
|>

<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="" target="_blank"><img src="assets/github.png" alt="git Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Powerful deep learning model for machine translation</h3>
                <h5>🛠️ TensorFlow, Transfer Learning, High Performance Computing (HPC), Machine Learning, Deep Learning</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 This study focuses on machine translation for two synthetic languages: an "Input Language" and an "Output Language." </h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 The aim is to construct a model that can effectively translate texts from the "Input Language" to the "Output Language." </h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 The challenge is that model's performance will be assessed using a testing set similar to the aforementioned training set. The evaluation metric, "test accuracy," measures the fidelity of the model's translations. A translation in the Output Language generated by the model will be deemed "correct" only if it precisely matches the ground-truth text.
                     </h6></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://github.com/FashioNXT/NXTFolio" target="_blank"><img src="assets/github.png" alt="git Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Deep Learning Model on Noisy MNIST Handwritten Digits Dataset</h3>
                <h5>🛠️ TensorFlow, Transfer Learning, Deep Learning Models using Multiple GPUs, Machine Learning, Deep Learning</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 When we add noise to images in the MNIST dataset, the digits in the images become more and more difficult for human to recognize. However, interestingly, deep neural networks can still be trained to recognize them relatively well.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 As part of this project, I trained a good hand-written-digit recognition classifier for the noisy images using TensorFlow Keras. Achieved an accuracy of 69.7% on the unseen dataset.</h6></li>
                </ul>
            </div>
        </div>
    </div>
</div>
|>

<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://github.com/AJ1904/machine-learning-from-scratch" target="_blank"><img src="assets/github.png" alt="Project Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Machine Learning From Scratch</h3>
                <h5>🛠️ TensorFlow, Machine Learning</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 This study contains projects related to Machine Learning CSCE 633. </h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 It covers Linear Regression, Logistic Regression, Regularization, Decision Trees, Gradient Boosting, Feed Forward Neural Networks, Convolutional Neural Networks, Support Vector Machines, Unsupervised Learning including Clustering.</h6></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://github.com/AJ1904/Microsoft-Ignite-Azure-AI-Language" target="_blank"><img src="https://github.com/AJ1904/Microsoft-Ignite-Azure-AI-Language/assets/49027490/4438e3a4-2f84-40c9-98cf-c0b12d2928cb" alt="Microsoft Ignite Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Microsoft Ignite Azure AI Challenge</h3>
                <h5>🛠️ Artificial Intelligence, Microsoft Azure</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 I successfully completed the Microsoft Ignite module on Azure AI Language, focusing on building natural language processing (NLP) solutions using Azure AI Language services.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 This challenge covered nine modules aligned with the assessment requirement of building a natural language processing solution with Azure AI Language.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 It was a valuable learning experience, contributing to my understanding of language models and their applications in real-world scenarios.</h6></li>
                </ul>
            </div>
        </div>
    </div>
</div>
|>

<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="" target="_blank"><img src="assets/tamu_logo.png" alt="TAMU Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Autonomous Vehicle Navigation: using Carla neural networks & AI</h3>
                <h5>🛠️ Carla, Python, Neural Networks, Computer Vision</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 Created end-to-end autonomous driving solutions in Python and simulated results in Carla </h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Applied computer vision, sensor data processing & AI algorithms to enhance community mobility and quality of life</h6></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://github.com/FashioNXT/NXTFolio" target="_blank"><img src="assets/tamu_logo.png" alt="TAMU Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>NXTFolio: A Ruby on Rails Web App for Fashion industry FashionNXT</h3>
                <h5>🛠️ Ruby on Rails, HTML, CSS, Cucumber, Selenium, RSpec</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 Developed the web app's features like login, tagging, seeding using Html, CSS, S3, Ruby on Rails</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Designed and implemented the customer relation management portal, led & helped the team to implement mobile UI, github automated tests, job portal, travel, follow features</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Improved legacy code, thoroughly tested using rpsec testing tool and wrote cucumber tests to have 100% code coverage</h6></li>
                </ul>
            </div>
        </div>
    </div>
</div>
|>


<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="#" target="_blank"><img src="assets/manit_logo.png" alt="manit Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Enhancing the Capability of Analytical Hierarchy Process using Fuzzy Logic embedded with Neural Networks'</h3>
                <h5>🛠️ Python, Java, Fuzzy Logic, Neural Networks</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 Developed a multi-criteria classification model through integration of fuzzy analytical hierarchy process and NN</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Achieved 97.7% accuracy in predicting results of Swachha Bharat Abhiyan </h6></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="#" target="_blank"><img src="assets/manit_logo.png" alt="manit Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Text to Emoji</h3>
                <h5>🛠️ Python, Android, Machine Learning, Java</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 Developed android application to suggest emojis based on given text with 95% accuracy</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Implemented machine learning models Naive Bayes, Random Forest, SVM, Neural Networks using Python</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Improved legacy code, thoroughly tested using rpsec testing tool and wrote cucumber tests to have 100% code coverage</h6></li>
                </ul>
            </div>
        </div>
    </div>
</div>
|>

<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="#" target="_blank"><img src="assets/rotaract_logo.jpeg" alt="TAMU Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Rotaract App</h3>
                <h5>🛠️ Android, Java, Kotlin</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 Developed attendance tracking feature using user friendly UI designs</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 App was used by volunteers of Rotaract Club MANIT to manage attendance and information of their students</h6></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="https://github.com/AJ1904/Natural-Language-Processing" target="_blank"><img src="assets/github.png" alt="git Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Natural Language Processing</h3>
                <h5>🛠️ HuggingFace, Python, Jupyter</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 This study is about using transformers for various natural language processing tasks</h6></li>
                    
                </ul>
            </div>
        </div>
    </div>
</div>
|>

<|card|
<div class="projects">
    <div class="project">
        <div class="education">
            <div class="education-logo">
                <a href="#" target="_blank"><img src="assets/logo.png" alt="Logo"></img></a>
            </div>
            <div class="education-text">
                <h3>Personal Portfolio</h3>
                <h5>🛠️ Taipy, Python, HTML, CSS, Angular, Firebase</h5>
                <ul class="custom-list">
                    <li><h6 class="educationh6">👩🏻‍💻 (This) Personal Portfolio developed using Taipy.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Another <a href="https://aj1904.github.io/codespaces-portfolio/" target="_blank"> portfolio</a> using Github Codespaces and Github Pages.</h6></li>
                    <li><h6 class="educationh6">👩🏻‍💻 Old <a href="https://ayushrijain.web.app/" target="_blank"> portfolio</a> using Javascript and Firebase.</h6></li>
                </ul>
            </div>
        </div>
    </div>
    
</div>
|>

""")
