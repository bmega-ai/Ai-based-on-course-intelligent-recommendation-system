from django.core.management.base import BaseCommand
from recommender.models import Domain


class Command(BaseCommand):

    help = "Load predefined AI Course Recommendation Domains"

    def handle(self, *args, **kwargs):

        # OPTIONAL → Clear old data to avoid duplicates
        Domain.objects.all().delete()

        data = [

{
"name": "Web Development",
"description": "Build responsive modern websites using HTML, CSS, and JavaScript.",
"skills": "HTML,CSS,JavaScript,React,Git",
"learning_path": "Internet Basics,HTML Basics,CSS Layouts,JavaScript Fundamentals,React Framework,Build Projects,Deployment",
"platforms": "freeCodeCamp,YouTube,Coursera,GUVI",
"youtube_link": "https://www.youtube.com/watch?v=zJSY8tJY_34",
"coursera_link": "https://www.coursera.org/professional-certificates/meta-front-end-developer",
"fcc_link": "https://www.freecodecamp.org/learn/2022/responsive-web-design/",
"guvi_link": "https://www.guvi.in/courses/full-stack-development-mern-top-quality-course-it-industry/",
"google_search_link": "https://www.google.com/search?q=Web+Development+course+english"
},

{
"name": "Frontend Development",
"description": "Design interactive and visually stunning user interfaces.",
"skills": "HTML,CSS,JavaScript,React,Redux",
"learning_path": "HTML Fundamentals,CSS Flexbox & Grid,JavaScript ES6,React Components,State Management",
"platforms": "freeCodeCamp,YouTube,Coursera,GUVI",
"youtube_link": "https://www.youtube.com/watch?v=RGKi6LSPDLU",
"coursera_link": "https://www.coursera.org/specializations/user-interface-design",
"fcc_link": "https://www.freecodecamp.org/learn/front-end-development-libraries/",
"guvi_link": "https://www.guvi.in/courses/frontend-development-course/",
"google_search_link": "https://www.google.com/search?q=Frontend+Development+course+english"
},

{
"name": "Backend Development",
"description": "Develop scalable server-side applications and databases.",
"skills": "Python,Django,REST API,SQL,Authentication",
"learning_path": "Python Basics,Object Oriented Programming,Django Framework,Database Design,API Security,Deployment",
"platforms": "GUVI,YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=jBzwzrDvZ18",
"coursera_link": "https://www.coursera.org/professional-certificates/meta-back-end-developer",
"guvi_link": "https://www.guvi.in/courses/python-programming-for-beginners/",
"google_search_link": "https://www.google.com/search?q=Backend+Development+course+english"
},

{
"name": "Full Stack Development",
"description": "Master both frontend and backend integration.",
"skills": "HTML,CSS,JavaScript,React,Django,SQL",
"learning_path": "Frontend Basics,React UI Design,Backend Django Development,Database Integration,Project Deployment",
"platforms": "freeCodeCamp,YouTube,GUVI",
"youtube_link": "https://www.youtube.com/watch?v=qwfE7fSVaZM",
"fcc_link": "https://www.freecodecamp.org/learn/full-stack-developer-certification/",
"guvi_link": "https://www.guvi.in/courses/full-stack-development-mern/",
"google_search_link": "https://www.google.com/search?q=Full+Stack+Development+course+english"
},

{
"name": "Software Engineering",
"description": "Design and build scalable, reliable software systems.",
"skills": "DSA,OOP,System Design,Testing,Git",
"learning_path": "Programming Logic,Data Structures,OOP Concepts,System Architecture,Testing Methodologies",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=zOverV47Ir0",
"coursera_link": "https://www.coursera.org/specializations/software-engineering-fundamentals",
"google_search_link": "https://www.google.com/search?q=Software+Engineering+course+english"
},

{
"name": "Machine Learning",
"description": "Build predictive models and intelligent algorithms.",
"skills": "Python,Numpy,Pandas,ScikitLearn,Model Evaluation",
"learning_path": "Mathematics Basics,Data Preprocessing,ML Algorithms,Model Optimization,Projects",
"platforms": "Coursera,YouTube,fCC",
"youtube_link": "https://www.youtube.com/watch?v=GwIo3gDZCVQ",
"coursera_link": "https://www.coursera.org/specializations/machine-learning-introduction",
"fcc_link": "https://www.freecodecamp.org/learn/machine-learning-with-python/",
"google_search_link": "https://www.google.com/search?q=Machine+Learning+course+english"
},

{
"name": "Deep Learning",
"description": "Develop advanced neural network architectures.",
"skills": "TensorFlow,Keras,CNN,RNN,Python",
"learning_path": "ML Foundations,Neural Networks,CNN Architectures,RNN Models,Real Projects",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=VyWAvY2CF9c",
"coursera_link": "https://www.coursera.org/specializations/deep-learning",
"google_search_link": "https://www.google.com/search?q=Deep+Learning+course+english"
},

{
"name": "Data Science",
"description": "Analyze, visualize, and derive insights from big data.",
"skills": "Python,Pandas,Statistics,Matplotlib,SQL",
"learning_path": "Python Analysis,Statistics Concepts,Data Cleaning,Visualization Techniques,ML Introduction",
"platforms": "freeCodeCamp,YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=ua-CiDNNj30",
"coursera_link": "https://www.coursera.org/professional-certificates/ibm-data-science",
"fcc_link": "https://www.freecodecamp.org/learn/data-analysis-with-python/",
"google_search_link": "https://www.google.com/search?q=Data+Science+course+english"
},

{
"name": "Data Analytics",
"description": "Interpret complex data sets to drive business decisions.",
"skills": "Excel,SQL,PowerBI,Python,Dashboarding",
"learning_path": "Excel Fundamentals,SQL Queries,Data Visualization,Dashboard Creation",
"platforms": "GUVI,YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=r-uOLxNrNk8",
"coursera_link": "https://www.coursera.org/professional-certificates/google-data-analytics",
"guvi_link": "https://www.guvi.in/courses/data-analytics-using-python/",
"google_search_link": "https://www.google.com/search?q=Data+Analytics+course+english"
},

{
"name": "Cloud Computing",
"description": "Deploy and manage infrastructure on major cloud platforms.",
"skills": "AWS,Linux,Docker,Kubernetes,Networking",
"learning_path": "Linux Basics,Cloud Concepts,AWS Services,Docker Containers,Kubernetes Deployment",
"platforms": "Coursera,YouTube,AWS",
"youtube_link": "https://www.youtube.com/watch?v=2LaAJq1lB1Q",
"coursera_link": "https://www.coursera.org/professional-certificates/google-cloud-digital-leader-training",
"google_search_link": "https://www.google.com/search?q=Cloud+Computing+course+english"
},

{
"name": "DevOps",
"description": "Master CI/CD and automated infrastructure management.",
"skills": "Git,Jenkins,Docker,Kubernetes,Monitoring",
"learning_path": "Version Control,CI/CD Pipelines,Dockerization,Kubernetes Orchestration,System Monitoring",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=scEDHsr3APg",
"coursera_link": "https://www.coursera.org/professional-certificates/ibm-devops-and-software-engineering",
"google_search_link": "https://www.google.com/search?q=DevOps+course+english"
},

{
"name": "Cyber Security",
"description": "Protect information and defend networks from attacks.",
"skills": "Networking,Linux,Encryption,Penetration Testing,Firewalls",
"learning_path": "Networking Basics,Linux Commands,Security Principles,Ethical Hacking Tools",
"platforms": "GUVI,YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=inWWhr5tnEA",
"coursera_link": "https://www.coursera.org/professional-certificates/google-cybersecurity",
"guvi_link": "https://www.guvi.in/courses/cyber-security-course/",
"google_search_link": "https://www.google.com/search?q=Cyber+Security+course+english"
},

{
"name": "Ethical Hacking",
"description": "Test and secure systems by identifying vulnerabilities.",
"skills": "Kali Linux,BurpSuite,Networking,Python,Scripting",
"learning_path": "Networking Deep Dive,Kali Tools Usage,Web Exploitation Techniques,Reporting",
"platforms": "YouTube,fCC",
"youtube_link": "https://www.youtube.com/watch?v=3Kq1MIfTWCE",
"fcc_link": "https://www.freecodecamp.org/news/learn-ethical-hacking-full-course/",
"google_search_link": "https://www.google.com/search?q=Ethical+Hacking+course+english"
},

{
"name": "Android Development",
"description": "Build high-quality native Android applications.",
"skills": "Java,Kotlin,XML,Firebase,REST API",
"learning_path": "Java Programming,Android UI Design,Database Integration,Firebase Services,App Publishing",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=fis26HvvDII",
"coursera_link": "https://www.coursera.org/professional-certificates/meta-android-developer",
"google_search_link": "https://www.google.com/search?q=Android+Development+course+english"
},

{
"name": "Flutter Development",
"description": "Build beautiful cross-platform apps with a single codebase.",
"skills": "Dart,Flutter,REST API,State Management,UI Design",
"learning_path": "Dart Basics,Flutter Widgets,Navigation Concepts,API Integration,Deployment",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=VPvVD8t02U8",
"coursera_link": "https://www.coursera.org/learn/flutter-app-development",
"google_search_link": "https://www.google.com/search?q=Flutter+Development+course+english"
},

{
"name": "Game Development",
"description": "Design and develop immersive video games.",
"skills": "Unity,C#,Game Physics,Animation,Level Design",
"learning_path": "Programming Logic,Unity Interface,Game Mechanics,Animation Techniques,Publishing",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=XtQMytKnuvo",
"coursera_link": "https://www.coursera.org/specializations/game-design-development",
"google_search_link": "https://www.google.com/search?q=Game+Development+course+english"
},

{
"name": "Blockchain Development",
"description": "Develop decentralized apps and smart contracts.",
"skills": "Solidity,Smart Contracts,Ethereum,Web3,Cryptography",
"learning_path": "Blockchain Fundamentals,Smart Contract Coding,DApp Development,Testing",
"platforms": "Coursera,YouTube,fCC",
"youtube_link": "https://www.youtube.com/watch?v=gyMwXuJrbJQ",
"coursera_link": "https://www.coursera.org/specializations/blockchain",
"fcc_link": "https://www.freecodecamp.org/news/learn-solidity-blockchain-and-smart-contracts-in-a-free-course/",
"google_search_link": "https://www.google.com/search?q=Blockchain+Development+course+english"
},

{
"name": "UI UX Design",
"description": "Create intuitive and user-centered digital designs.",
"skills": "Figma,Wireframing,Prototyping,User Research,Design Systems",
"learning_path": "Design Principles,Wireframe Creation,Interactive Prototypes,Usability Testing",
"platforms": "YouTube,GUVI,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=c9Wg6NX_PUk",
"coursera_link": "https://www.coursera.org/professional-certificates/google-ux-design",
"guvi_link": "https://www.guvi.in/courses/ui-ux-design-course/",
"google_search_link": "https://www.google.com/search?q=UI+UX+Design+course+english"
},

{
"name": "Digital Marketing",
"description": "Grow brands and reach audiences using digital channels.",
"skills": "SEO,Content Marketing,Analytics,Social Media,Ads",
"learning_path": "Marketing Basics,SEO Optimization,Campaign Strategy,Analytics Tools",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=nU-IIXBWlS4",
"coursera_link": "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce",
"google_search_link": "https://www.google.com/search?q=Digital+Marketing+course+english"
},

{
"name": "Automation Testing",
"description": "Ensure software quality through automated test scripts.",
"skills": "Python,Selenium,JUnit,TestNG,Framework Design",
"learning_path": "Testing Concepts,Selenium Automation Scripts,Framework Implementation",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=NidS83WosC8",
"coursera_link": "https://www.coursera.org/specializations/software-testing-automation",
"google_search_link": "https://www.google.com/search?q=Automation+Testing+course+english"
},

{
"name": "Linux System Engineering",
"description": "Administer and engineer robust Linux environments.",
"skills": "Shell Scripting,Networking,Security,System Services",
"learning_path": "Linux Fundamentals,Command Line Mastery,Scripting Automation,System Hardening",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=wBp0Rb-ZJak",
"coursera_link": "https://www.coursera.org/specializations/linux-system-administration",
"google_search_link": "https://www.google.com/search?q=Linux+System+Engineering+course+english"
},

{
"name": "Computer Vision",
"description": "Develop AI systems that can see and understand images.",
"skills": "Python,OpenCV,CNN,TensorFlow,Image Processing",
"learning_path": "Image Basics,OpenCV Projects,Deep Learning Vision Models",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=01sAkU_NvOY",
"coursera_link": "https://www.coursera.org/learn/introduction-computer-vision-watson-opencv",
"google_search_link": "https://www.google.com/search?q=Computer+Vision+course+english"
},

{
"name": "Natural Language Processing",
"description": "Build systems that understand and generate human language.",
"skills": "Python,NLTK,Transformers,Deep Learning,Tokenization",
"learning_path": "Text Preprocessing,Embeddings,Sequence Models,Transformer Architectures",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=CMrHM8a3hqw",
"coursera_link": "https://www.coursera.org/specializations/natural-language-processing",
"google_search_link": "https://www.google.com/search?q=Natural+Language+Processing+course+english"
},

{
"name": "Big Data Engineering",
"description": "Architect systems for massive scale data processing.",
"skills": "Hadoop,Spark,Scala,ETL,Distributed Systems",
"learning_path": "Big Data Concepts,Hadoop Ecosystem,Spark Processing,Pipeline Development",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=bAyrObl7TYE",
"coursera_link": "https://www.coursera.org/specializations/big-data",
"google_search_link": "https://www.google.com/search?q=Big+Data+Engineering+course+english"
},

{
"name": "Business Intelligence",
"description": "Transform data into actionable business insights.",
"skills": "PowerBI,SQL,Data Modeling,Visualization,ETL",
"learning_path": "Data Preparation,Model Design,Dashboard Creation,Insights Reporting",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=h0H6rB_A9bg",
"coursera_link": "https://www.coursera.org/specializations/business-intelligence-data-warehousing",
"google_search_link": "https://www.google.com/search?q=Business+Intelligence+course+english"
},

{
"name": "Network Engineering",
"description": "Design and manage redundant, secure network architectures.",
"skills": "Routing,Switching,TCP/IP,Firewalls,VPN",
"learning_path": "Networking Basics,Routing Protocols,Switch Configuration,Security Implementation",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=qiQR5rTSshw",
"coursera_link": "https://www.coursera.org/specializations/networking-basics",
"google_search_link": "https://www.google.com/search?q=Network+Engineering+course+english"
},

{
"name": "Embedded Systems",
"description": "Program and design microcontroller-based systems.",
"skills": "C,C++,RTOS,Electronics,Sensors",
"learning_path": "Electronics Fundamentals,C Programming,Microcontroller Interfacing,RTOS Concepts",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=W3645Pr9a1M",
"coursera_link": "https://www.coursera.org/specializations/embedded-systems",
"google_search_link": "https://www.google.com/search?q=Embedded+Systems+course+english"
},

{
"name": "Robotics Software",
"description": "Develop software for intelligent and autonomous robots.",
"skills": "Python,ROS,Computer Vision,Control Systems",
"learning_path": "Programming Basics,ROS Framework,Simulation,Hardware Integration",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=84L9770vKyo",
"coursera_link": "https://www.coursera.org/learn/robotics-specialization",
"google_search_link": "https://www.google.com/search?q=Robotics+Software+course+english"
},

{
"name": "FinTech Development",
"description": "Build innovative financial technology applications.",
"skills": "Python,APIs,Security,Blockchain,Payments",
"learning_path": "Finance Basics,Backend Development,Payment Integration,Security Compliance",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=dIAhmN8dfUU",
"coursera_link": "https://www.coursera.org/specializations/fintech",
"google_search_link": "https://www.google.com/search?q=FinTech+Development+course+english"
},

{
"name": "Product Management",
"description": "Lead cross-functional teams and product strategies.",
"skills": "Agile,Scrum,Roadmapping,User Stories,Analytics",
"learning_path": "Agile Principles,Planning Techniques,Execution Strategies,Performance Metrics",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=8YVv3mD2K0O",
"coursera_link": "https://www.coursera.org/specializations/software-product-management",
"google_search_link": "https://www.google.com/search?q=Product+Management+course+english"
},

{
"name": "Technical Writing",
"description": "Create clear and effective technical documentation.",
"skills": "Markdown,API Docs,Research,Content Structuring",
"learning_path": "Writing Basics,Documentation Tools,Publishing Workflows",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=pDLo_oOFrsY",
"coursera_link": "https://www.coursera.org/learn/technical-writing",
"google_search_link": "https://www.google.com/search?q=Technical+Writing+course+english"
},

{
"name": "Quantum Computing",
"description": "Develop algorithms for the quantum computers of the future.",
"skills": "Linear Algebra,Qiskit,Quantum Gates,Python",
"learning_path": "Math Foundations,Quantum Theory,Programming Quantum Circuits",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=QuR969uMICM",
"coursera_link": "https://www.coursera.org/learn/quantum-computing-fundamentals",
"google_search_link": "https://www.google.com/search?q=Quantum+Computing+course+english"
},

{
"name": "Bioinformatics",
"description": "Apply computational techniques to biological data.",
"skills": "Python,Genomics,Statistics,Data Analysis",
"learning_path": "Biology Basics,Python Programming,Genome Analysis Tools",
"platforms": "Coursera,YouTube",
"youtube_link": "https://www.youtube.com/watch?v=2v-pGOCpE64",
"coursera_link": "https://www.coursera.org/specializations/bioinformatics",
"google_search_link": "https://www.google.com/search?q=Bioinformatics+course+english"
},

{
"name": "Metaverse Development",
"description": "Build immersive 3D virtual world experiences.",
"skills": "Unity,3D Modeling,Blockchain,XR",
"learning_path": "3D Concepts,Unity XR Toolkit,Virtual Economy Design",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=W0y2u5-T0yE",
"coursera_link": "https://www.coursera.org/specializations/metaverse",
"google_search_link": "https://www.google.com/search?q=Metaverse+Development+course+english"
},

{
"name": "API Development",
"description": "Design and build fast, secure, and scalable APIs.",
"skills": "REST,GraphQL,Django,Authentication,Rate Limiting",
"learning_path": "HTTP Protocol,Framework Setup,Authentication Methods,Deployment",
"platforms": "YouTube,Coursera",
"youtube_link": "https://www.youtube.com/watch?v=GZvSYJDk-us",
"coursera_link": "https://www.coursera.org/specializations/api-design-fundamentals",
"google_search_link": "https://www.google.com/search?q=API+Development+course+english"
}

]
        for d in data:
            Domain.objects.create(**d)

        self.stdout.write(self.style.SUCCESS("Domains Loaded Successfully with Platform and Google Search Links"))