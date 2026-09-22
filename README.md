# Codomax Module 3 — Cloud Portfolio Application

A cloud-based personal portfolio web application developed as part of the **Codomax Digital Solutions Module 3: Cloud Services & Web Application Deployment** internship project.

The project demonstrates the practical integration of AWS compute, networking, storage, managed database, IAM, secrets management, monitoring, and a Python Flask web application.

---

## 👨‍💻 Project Information

**Student:** Sikandar Shah  
**Program:** BS Cyber Security  
**University:** Abasyn University Peshawar  
**Organization:** Codomax Digital Solutions  
**Module:** Module 3 — Cloud Services & Web Application Deployment  
**AWS Region:** Asia Pacific (Mumbai) — `ap-south-1`

---

## 🎯 Project Objective

The objective of this project is to design, deploy, and secure a cloud-based web application using AWS services.

The project covers:

- Cloud compute services
- Object storage
- Managed databases
- Virtual networking
- IAM roles and permissions
- Secrets management
- Environment variables
- Application logging
- Cloud monitoring
- Resource quotas
- Web application deployment

---

## 🏗️ Architecture

The application follows this general architecture:

```
                    Internet
                       │
                       ▼
                ┌──────────────┐
                │     EC2      │
                │    Ubuntu    │
                │              │
                │    Nginx     │
                │      ↓       │
                │   Gunicorn   │
                │      ↓       │
                │    Flask     │
                └──────┬───────┘
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      ┌──────────────┐    ┌──────────────┐
      │ RDS          │    │ S3           │
      │ PostgreSQL   │    │ Object       │
      │ Database     │    │ Storage      │
      └──────────────┘    └──────────────┘
             ▲                   ▲
             │                   │
             └───────┬───────────┘
                     │
             ┌───────┴────────┐
             │ Secrets        │
             │ Manager        │
             └────────────────┘

        IAM → Access Control
        CloudWatch → Monitoring & Logs
        VPC → Network Isolation

---
Main AWS Services
Service	Purpose
Amazon EC2	Hosts the web application
Amazon VPC	Provides network isolation
Security Groups	Controls network traffic
Amazon RDS PostgreSQL	Managed relational database
Amazon S3	Object storage
AWS IAM	Access control and permissions
AWS Secrets Manager	Secure database credentials
Amazon CloudWatch	Monitoring and logging
Nginx	Reverse proxy
Gunicorn	Python WSGI application server
---
---
💻 Technology Stack
Application
- Python
- Flask
- HTML5
- CSS3
- PostgreSQL
- Boto3
Cloud & Infrastructure
- Amazon EC2
- Amazon VPC
- Amazon S3
- Amazon RDS
- AWS IAM
- AWS Secrets Manager
- Amazon CloudWatch
Server
- Ubuntu Linux
- Nginx
- Gunicorn
Development & Version Control
- Git
- GitHub
- VS Code


🌐 Portfolio Application
The web application contains the following sections:
- Home
- About
- Skills
- Certifications
- Projects
- Experience
- Contact
The portfolio presents my background as a Cyber Security student and aspiring Cloud Security Professional, with a focus on AWS, cloud security, networking, Linux, Python and cybersecurity.



🗄️ Database
The application uses Amazon RDS PostgreSQL as its managed database.
The database contains tables for:
Projects
Stores portfolio project information.
Contact Messages
Stores messages submitted through the portfolio contact form.
Database credentials are not stored directly inside the application source code.



☁️ Amazon S3 Integration
Amazon S3 is used as secure object storage for the application.
The application accesses S3 using Boto3 and the EC2 IAM role.
Example application functionality:
Portfolio Application
        │
        ▼
     Boto3
        │
        ▼
   IAM Role
        │
        ▼
      S3 Bucket
Public access to the S3 bucket is blocked.



🔐 Security Implementation
Security was considered throughout the deployment.
Implemented Security Controls
- RDS configured without public access
- PostgreSQL access restricted through Security Groups
- SSH restricted to the administrator's IP
- IAM role used for AWS service access
- Secrets Manager used for database credentials
- S3 Block Public Access enabled
- Sensitive configuration stored outside source code
- .env excluded from Git
- .pem private keys excluded from Git
- AWS credentials are not stored in the repository



🔑 Environment Variables
The application uses environment variables for configuration.
Example:
AWS_REGION=ap-south-1
S3_BUCKET=YOUR_BUCKET_NAME
SECRET_NAME=module3/database
FLASK_SECRET_KEY=CHANGE_THIS_IN_PRODUCTION
The actual .env file is intentionally excluded from the repository.



📦 Installation
Clone the repository:
git clone https://github.com/Sikandar39/codomax-module-3-cloud-portfolio.git
Move into the project:
cd codomax-module-3-cloud-portfolio/portfolio
Create a virtual environment:
python3 -m venv venv
Activate it:
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt



▶️ Run the Application
Configure the required environment variables in .env.
Then initialize the database:
python3 init_db.py
Start the Flask application:
python3 app.py
The application will run locally on:
http://127.0.0.1:5000



❤️ Health Check
The application includes a health endpoint:
/health
Example successful response:
{
  "application": "online",
  "database": "online",
  "s3": "online"
}
This verifies the connection between the application and its major AWS dependencies.



🚀 Production Deployment
The application is designed for deployment using:
Internet
    ↓
Nginx
    ↓
Gunicorn
    ↓
Flask
    ↓
RDS PostgreSQL / S3
Gunicorn is used as the production WSGI server, while Nginx acts as the reverse proxy.



📊 Monitoring
Amazon CloudWatch is used for monitoring and operational visibility.
Monitoring includes:
- EC2 CPU utilization
- Application logs
- System/application activity
- CloudWatch Logs



📸 Project Evidence
Detailed implementation evidence is included in the final project report.
The report contains screenshots for:
- VPC configuration
- Security Groups
- EC2
- SSH
- Software installation
- S3
- RDS
- IAM
- Secrets Manager
- Database initialization
- Application health
- S3 application integration
- Gunicorn/systemd
- Nginx
- Live website
- Contact database
- Application logs
- CloudWatch
- Service Quotas
- Final architecture verification



📄 Documentation
The repository includes:
Module-3-Report.pdf
Final project report containing implementation details and screenshot evidence.
Module-3-Professional-Report.docx
Editable professional version of the project report.
architecture-diagram.png
Visual representation of the AWS application architecture.



🔗 Project Links
GitHub Repository
https://github.com/Sikandar39/codomax-module-3-cloud-portfolio
Live Website
ADD_LIVE_WEBSITE_URL
LinkedIn Post
ADD_LINKEDIN_POST_URL




👤 About the Developer
Sikandar Shah
Cyber Security Student | Aspiring Cloud Security Professional
Areas of interest:
- Cloud Security
- AWS
- Cybersecurity
- Networking
- Linux
- Python
- Cloud Infrastructure
- Secure Application Deployment
Contact
Email: zerotrustpro1@gmail.com
GitHub: https://github.com/Sikandar39
LinkedIn: https://www.linkedin.com/in/sikandar-shah-28739a404/


🎓 Learning Outcomes
Through this project, I gained practical experience in:
- AWS cloud infrastructure
- EC2 deployment
- VPC networking
- Security Groups
- PostgreSQL on RDS
- S3 object storage
- IAM roles
- Secrets Manager
- Linux server administration
- Flask application development
- Gunicorn
- Nginx
- CloudWatch monitoring
- Application logging
- Secure cloud configuration


🔒 Security Notice
Do not upload or commit the following files or information:
.env
*.pem
AWS Access Keys
AWS Secret Keys
Database Passwords
Private Credentials
Before publishing the repository, verify that no sensitive information is present in the Git history or project files.


📌 Project Status
Module: 3 — Cloud Services & Web Application Deployment
Organization: Codomax Digital Solutions
Project: Cloud-Based Personal Portfolio Application
Status: In Development / Deployment
Learn • Build • Secure

**For your GitHub repo, use this README after you have completed the remaining deployment tests.** Replace only the `ADD_LIVE_WEBSITE_URL` and `ADD_LINKEDIN_POST_URL` placeholders when those links are ready.

Would you like me to turn this into a shorter GitHub-ready README with your exact repository name and links
