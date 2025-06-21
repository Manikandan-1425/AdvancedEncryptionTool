# AdvancedEncryptionTool

OMPANY:CODTECH IT SOLUTIONS
NAME:MANIKANDAN L
INTERN ID:CT04DG1797
DOMAIN:CYBER SECCURITY & ETHICAL HACKING
DURATION:4 WEEKS
MENTOR:NEELA SANTHOSH
DESCRIPTION:
🔐 Task 4 – Advanced Encryption Tool
📄 Internship Project Report
As part of the Cyber Security Internship under CodTech, Task 4 focused on designing and implementing a secure and user-friendly Advanced Encryption Tool using Python. The objective of this task was to build a software utility that can encrypt and decrypt files using strong encryption techniques, thereby ensuring data confidentiality and file protection against unauthorized access.

🧩 Project Objective
The main goal of this project was to create a robust encryption application capable of protecting sensitive information by transforming readable files into an unreadable encrypted format. The project demanded the use of advanced encryption standards such as AES-256. By completing this task, I aimed to gain hands-on experience with encryption libraries and enhance my understanding of secure data handling practices.

🛠️ Technologies and Tools Used
Programming Language: Python 3.12

Encryption Library: cryptography (Fernet module)

Development Environment: Visual Studio Code

Platform: Windows 10

The Python cryptography library was chosen for its simplicity, reliability, and support for modern encryption standards. The Fernet module, which is part of this library, provides symmetric encryption using AES in CBC mode with a 128-bit key and HMAC for authentication. While not exactly AES-256, it follows best practices for secure encryption in real-world applications.

🔧 How It Works
The tool operates through a command-line interface (CLI) and supports two main operations:

Encryption: Users provide a file path, and the tool reads the content, encrypts it using a Fernet key, and stores the result as a new file with a .enc extension.

Decryption: Users select an encrypted file, and the tool reverses the process, restoring the original file content and saving it with a _decrypted suffix.

The encryption key is either generated once and saved in a file called encryption.key, or reused if it already exists. This ensures consistency in encryption/decryption sessions and keeps the process secure and repeatable.

🔍 Features and Benefits
Simple CLI Interface: Users can quickly choose to encrypt or decrypt with easy prompts.

Persistent Key Management: Ensures the same key is used unless regenerated, allowing consistent decryption.

Fast and Secure: Uses AES-CBC mode encryption with HMAC authentication.

Cross-Platform Compatibility: Works on any system with Python installed.

File Agnostic: Works with text files, documents, media, and more.

✅ Testing and Validation
To validate the tool, I created a sample file (myfile.txt), encrypted it using the tool, and then decrypted the resulting .enc file. The decrypted file (myfile.txt_decrypted) matched the original content exactly, proving the tool’s accuracy and reliability.

📂 Outcome
This task strengthened my understanding of file handling, symmetric encryption, key management, and secure programming practices. It also introduced me to cryptographic standards and the importance of data privacy in cybersecurity. The tool created is simple yet powerful and can be expanded into a more advanced application with features like password-based encryption, GUI interface, batch processing, and cloud integration.
📝 Conclusion
Task 4 provided an essential foundation in encryption techniques and secure file handling. I successfully implemented a Python-based Advanced Encryption Tool that fulfills the internship’s objective and demonstrates my capability to apply theoretical knowledge in practical cybersecurity scenarios. This project not only helped me learn about real-world encryption mechanisms but also improved my coding, debugging, and project documentation skills — all of which are valuable for my growth as a cybersecurity professional.

#OUTPUT:
![Image](https://github.com/user-attachments/assets/0820b942-b86d-402f-a723-596a46162ec2)
