from .database import SessionLocal, engine
from .models import Base, FAQ

Base.metadata.create_all(bind=engine)

db = SessionLocal()
    
career_faqs = [

("what is career guidance","Career guidance helps individuals choose the right career path based on skills, interests and market demand.","Career"),

("how to choose a career","Choose a career based on your interests, strengths, education and future opportunities.","Career"),

("which career is best in IT","Popular IT careers include Software Development, DevOps, Cloud Computing, Data Science and Cybersecurity.","Career"),

("what skills are required for IT jobs","Programming, problem solving, communication and teamwork are essential skills for IT jobs.","Career"),

("how can i switch my career to IT","Start with foundational skills, complete projects and build a portfolio before applying for jobs.","Career"),

("what is a career roadmap","A career roadmap is a structured plan that outlines skills, projects and milestones required to achieve career goals.","Career"),

("how to become a software engineer","Learn programming, data structures, databases and build projects to become a software engineer.","Career"),

("how to become a devops engineer","Learn Linux, Git, Docker, Jenkins, Kubernetes and cloud platforms.","Career"),

("how to become a data scientist","Learn Python, statistics, machine learning and complete data science projects.","Career"),

("what is cloud computing career","Cloud professionals manage cloud infrastructure, deployment and security.","Career"),

("which IT field has highest salary","Cloud Computing, AI, Data Science and Cybersecurity are among the highest-paying IT fields.","Career"),

("how to improve communication skills","Practice public speaking, presentations and active listening regularly.","Career"),

("how to build professional network","Connect with professionals through LinkedIn, events and industry communities.","Career"),

("what is business analyst role","Business Analysts bridge business requirements and technical solutions.","Career"),

("what is project manager role","Project Managers plan, execute and monitor projects successfully.","Career"),

("what is product manager role","Product Managers define product vision and coordinate development.","Career"),

("what is career growth","Career growth refers to progressing in responsibilities, skills and salary over time.","Career"),

("how to prepare for career change","Identify skill gaps, learn required skills and gain practical experience.","Career"),

("what are future career trends","AI, Cloud Computing, DevOps, Cybersecurity and Data Science are growing rapidly.","Career"),

("what is remote job","A remote job allows employees to work from locations outside a traditional office.","Career"),

("how to create career goals","Set specific, measurable and realistic goals with timelines.","Career"),

("what is freelancing","Freelancing involves working independently on projects for multiple clients.","Career"),

("what is entrepreneurship","Entrepreneurship is creating and managing your own business.","Career"),

("how to build confidence for interviews","Practice mock interviews and improve communication skills.","Career"),

("how to write career objective","A career objective should clearly describe your goals and value to employers.","Career")
]

internship_faqs = [

("what is internship","An internship provides practical industry experience for students and freshers.","Internship"),

("how to get internship","Build projects, create a resume and apply through job portals and company websites.","Internship"),

("what is paid internship","A paid internship offers financial compensation during the internship period.","Internship"),

("what is unpaid internship","An unpaid internship provides experience without monetary compensation.","Internship"),

("where can i find internships","Internships can be found on LinkedIn, Internshala, Naukri and company career pages.","Internship"),

("how to apply for internship","Submit your resume, portfolio and application through official channels.","Internship"),

("what skills are required for internship","Technical skills, communication and problem-solving abilities are important.","Internship"),

("how to prepare for internship interview","Practice technical questions and review your projects thoroughly.","Internship"),

("how long is internship","Internships usually last between one and six months.","Internship"),

("what is virtual internship","A virtual internship is completed remotely through online collaboration.","Internship"),

("what is software internship","A software internship focuses on software development projects.","Internship"),

("what is python internship","A Python internship involves working on Python-based development projects.","Internship"),

("what is devops internship","A DevOps internship focuses on automation, deployment and cloud technologies.","Internship"),

("what is cloud internship","Cloud internships provide experience with AWS, Azure or Google Cloud.","Internship"),

("what is data science internship","Data science internships involve data analysis and machine learning projects.","Internship"),

("how to create internship resume","Highlight projects, skills, education and achievements.","Internship"),

("what projects should i add in resume","Include practical projects relevant to your target role.","Internship"),

("can freshers get internship","Yes, internships are designed for students and freshers.","Internship"),

("what is internship certificate","An internship certificate validates your internship experience.","Internship"),

("how to get internship without experience","Build projects and demonstrate practical skills.","Internship"),

("how many internships should i do","One to three quality internships are generally sufficient.","Internship"),

("what are internship benefits","Internships provide experience, networking and career opportunities.","Internship"),

("how to impress internship recruiter","Show enthusiasm, projects and willingness to learn.","Internship"),

("what is internship stipend","A stipend is the financial compensation provided during an internship.","Internship"),

("how to convert internship into job","Perform well, communicate effectively and contribute consistently.","Internship")
]

technology_faqs = [

("what is python","Python is a popular programming language used in web development, automation and AI.","Technology"),

("what is java","Java is an object-oriented programming language widely used in enterprise applications.","Technology"),

("what is devops","DevOps combines software development and IT operations to improve delivery speed.","Technology"),

("what is docker","Docker is a containerization platform used to package applications.","Technology"),

("what is kubernetes","Kubernetes is a container orchestration platform.","Technology"),

("what is jenkins","Jenkins is an automation server used for CI/CD pipelines.","Technology"),

("what is git","Git is a distributed version control system.","Technology"),

("what is github","GitHub is a platform for hosting and collaborating on Git repositories.","Technology"),

("what is aws","AWS is Amazon's cloud computing platform.","Technology"),

("what is azure","Microsoft Azure is a cloud computing platform.","Technology"),

("what is cloud computing","Cloud computing provides computing resources over the internet.","Technology"),

("what is ci cd","CI/CD automates software integration, testing and deployment.","Technology"),

("what is linux","Linux is an open-source operating system widely used on servers.","Technology"),

("what is api","An API enables communication between software applications.","Technology"),

("what is rest api","REST API follows REST architectural principles for communication.","Technology"),

("what is fastapi","FastAPI is a modern Python framework for building APIs.","Technology"),

("what is sql","SQL is used to manage relational databases.","Technology"),

("what is database","A database stores and organizes information efficiently.","Technology"),

("what is data science","Data Science extracts insights from data using analysis and machine learning.","Technology"),

("what is machine learning","Machine Learning enables systems to learn from data.","Technology"),

("what is artificial intelligence","AI enables machines to perform tasks requiring human intelligence.","Technology"),

("what is cybersecurity","Cybersecurity protects systems and data from attacks.","Technology"),

("what is networking","Networking enables communication between computers and devices.","Technology"),

("what is terraform","Terraform is an Infrastructure as Code tool.","Technology"),

("what is ansible","Ansible automates configuration management and deployment.","Technology")
]

course_faqs = [

("best python course","Choose courses covering Python fundamentals, projects and APIs.","Course"),

("best devops course","Learn Linux, Docker, Jenkins, Kubernetes and AWS.","Course"),

("best cloud computing course","AWS, Azure and Google Cloud certifications are recommended.","Course"),

("best data science course","Choose courses covering Python, statistics and machine learning.","Course"),

("how to learn python","Start with basics, practice coding and build projects.","Course"),

("how to learn devops","Learn Linux, Git, Docker, Jenkins and cloud platforms.","Course"),

("how to learn aws","Begin with AWS Cloud Practitioner certification.","Course"),

("how to learn data science","Learn Python, statistics and machine learning step by step.","Course"),

("how long does python take to learn","Basic Python can be learned in one to three months.","Course"),

("how long does devops take to learn","DevOps fundamentals typically take three to six months.","Course"),

("what is certification","Certification validates your skills through exams.","Course"),

("is aws certification worth it","AWS certifications are highly valued in the industry.","Course"),

("which certification is best for freshers","AWS Cloud Practitioner, Azure Fundamentals and Google Cloud Digital Leader are good options.","Course"),

("what is online course","An online course is delivered through the internet.","Course"),

("what is bootcamp","A bootcamp is an intensive short-term training program.","Course"),

("what is self learning","Self-learning is acquiring knowledge independently.","Course"),

("how to create learning roadmap","Identify goals, skills and projects required for success.","Course"),

("which programming language should i learn first","Python is often recommended for beginners.","Course"),

("best resources for python","Official documentation, YouTube and project-based learning are useful.","Course"),

("best resources for devops","Docker, Kubernetes and AWS documentation are excellent resources.","Course"),

("how to build projects while learning","Apply concepts through practical projects.","Course"),

("what is project based learning","Learning by building real-world projects.","Course"),

("how to stay motivated while learning","Set goals, track progress and celebrate achievements.","Course"),

("how many hours should i study daily","One to three focused hours daily is effective.","Course"),

("how to prepare for certification exam","Study objectives, practice labs and take mock tests.","Course")
]


java_faqs = [

("what is java","Java is an object-oriented programming language widely used for enterprise, web and Android applications.","Technology"),

("why learn java","Java is widely used in industry, offers excellent career opportunities and has strong community support.","Technology"),

("is java good for career","Yes, Java remains one of the most demanded programming languages in software development.","Technology"),

("what is jdk","JDK stands for Java Development Kit and contains tools required to develop Java applications.","Technology"),

("what is jre","JRE stands for Java Runtime Environment and is used to run Java applications.","Technology"),

("what is jvm","JVM stands for Java Virtual Machine and executes Java bytecode.","Technology"),

("what is object oriented programming","Object-Oriented Programming organizes code using objects and classes.","Technology"),

("what are the pillars of oops","The four pillars are Encapsulation, Inheritance, Polymorphism and Abstraction.","Technology"),

("what is class in java","A class is a blueprint used to create objects.","Technology"),

("what is object in java","An object is an instance of a class.","Technology"),

("what is inheritance in java","Inheritance allows one class to acquire properties and methods from another class.","Technology"),

("what is polymorphism in java","Polymorphism allows one interface to have multiple implementations.","Technology"),

("what is abstraction in java","Abstraction hides implementation details and shows only essential functionality.","Technology"),

("what is encapsulation in java","Encapsulation binds data and methods together while restricting direct access.","Technology"),

("what is constructor in java","A constructor initializes objects when they are created.","Technology"),

("what is method overloading","Method overloading allows multiple methods with the same name but different parameters.","Technology"),

("what is method overriding","Method overriding allows a subclass to provide its own implementation of a parent method.","Technology"),

("what is exception handling in java","Exception handling manages runtime errors using try, catch and finally blocks.","Technology"),

("what is collection framework","The Collection Framework provides data structures such as List, Set and Map.","Technology"),

("what is arraylist","ArrayList is a dynamic array implementation in Java.","Technology"),

("what is hashmap","HashMap stores key-value pairs and provides fast retrieval.","Technology"),

("what is multithreading","Multithreading allows multiple threads to execute concurrently.","Technology"),

("what is spring boot","Spring Boot is a Java framework used for building REST APIs and enterprise applications.","Technology"),

("what is hibernate","Hibernate is an ORM framework that simplifies database operations in Java.","Technology"),

("how to become java developer","Learn Core Java, OOP, Collections, JDBC, Spring Boot, Hibernate, SQL and build projects.","Technology")

]

faq_data = (
    career_faqs +
    internship_faqs +
    technology_faqs +
    course_faqs +
    java_faqs
)

for question, answer, category in faq_data:

    exists = db.query(FAQ).filter(
        FAQ.question == question
    ).first()

    if not exists:

        db.add(
            FAQ(
                question=question,
                answer=answer,
                category=category
            )
        )

db.commit()
db.close()

print("FAQs Inserted Successfully")