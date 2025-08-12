# Flask + Nginx + Docker + Terraform + Ansible Project

This project demonstrates deploying a Flask application with Nginx using Docker, provisioning infrastructure via Terraform, and automating environment setup (Docker & Git installation) using Ansible.

---

## 📖 Project Description
I ran into a classic “It works on my machine” issue — my Flask app worked perfectly inside the instance but wasn’t accessible via Public IP.  
The culprit? Flask’s default host binding (`127.0.0.1`).  
I broke down the fix, corporate network quirks, and Nginx pitfalls in detail here:  
🔗 [**[Read the full Medium story](https://medium.com/)**
](https://medium.com/@kartikeya_1901/why-your-flask-app-works-locally-on-your-instance-but-fails-on-the-public-ip-and-how-to-fix-it-e8ba86ebab15)
---

## 🛠 Tech Stack
- **Flask** – Backend application framework  
- **Nginx** – Reverse proxy server  
- **Docker & Docker Compose** – Containerization and orchestration  
- **Terraform** – Infrastructure as Code (EC2 instance creation)  
- **Ansible** – Automated Docker & Git installation  

<img width="975" height="499" alt="image" src="https://github.com/user-attachments/assets/51cf8469-d535-48ef-bbb8-1ba1d2400c11" />


