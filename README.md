# BIG_clientdeliverable_Spring-25

Welcome aboard with our **Pilot Buddy** an AI-powered assistant built for pilots to simplify contract navigation, fatigue tracking, and schedule clarity.
Think of it as your smart first officer, always on duty, never off course.

## 📚 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Map](#-project-map)
- [Relational Schema and EER diagram](#-er-diagram)
- [How Captain Navigates](#-how-captain-navigates)
- [Our MVP's Techstack](#-techstack)
- [Setup Instructions](#-setup-instructions)
- [Our MVP project UI Demo](#-ui)
- [Product Strengths & Current Limitations](#-strengths&limitations)
- [Suggested Technologies](#-suggested-technologies)
- [Crew & Credits](#-credits)

---
## 🙌🏻 Overview
Pilots shouldn’t need to dig through 300-page CBAs mid-duty.
Our solution helps flight crew query union rules, monitor flight hours, and flag compliance risks, all in plain English.

- Built with love (and LangChain), this system includes:
- A responsive web interface (via Streamlit)
- An AI chatbot assistant for CBA guidance

---

## ⛅ Features

✅ Natural Language CBA Queries
✅ Login/Signup Flow with OAuth
✅ Fatigue Risk Prediction

✅ Flight vs. Rest Analytics
✅ Multi-language Support (EN/ES)
✅ Secure, Airline-themed UI

---

## ✈️ Project Map 

```
/
|-- AI_chatbot_design.ipynb         # AI chatbot backend code file (Streamlit app)
|-- app.py                          # Chatbot Interface GUI
|-- Figma_protoype.pdf              # What you can see (User Interface)
|-- README.md                       # You be readin’ it now, mate
```

## 🌏 Relational Schema and EER diagram
![relational_diagram](https://github.com/user-attachments/assets/d70eace4-7791-42aa-913b-84fc7e74a666)
![er diag](https://github.com/user-attachments/assets/06013461-c637-4206-a2b3-a79eb272980b)

## 🗺️ How Captain navigates
![image](https://github.com/user-attachments/assets/9cd91036-69da-4aea-a900-2bdac3bde98b)
![image](https://github.com/user-attachments/assets/af528a2c-92b3-479a-8c66-a7ce5a6735e5)

## ⚙️ Our MVP's Techstack

| Layer              | Technology         | Purpose                                                                 |
|--------------------|--------------------|-------------------------------------------------------------------------|
| Frontend UI        | **Streamlit**       | Rapid app development for interactive pilot interface                  |
| UI/UX Design       | **Figma**           | Wireframing and high-fidelity mockups                                  |
| Backend Logic      | **Python**          | Core app logic, integration, and orchestration                         |
| NLP + LLM          | **OpenAI GPT-4**    | Understands and responds to pilot queries                              |
| Chatbot Framework  | **LangChain**       | Orchestrates prompt, retrieval, and response logic                     |
| Vector Search      | **FAISS**           | Semantic search of CBA documents                                       |
| Document Parsing   | **AWS Textract**    | Extracts structured text from scanned PDF CBAs                         |
| Database           | **MySQL**           | Stores flight logs and structured pilot data                           |
| ETL / Data Sync    | **Airbyte**         | Connects and ingests external data sources                             |

---

## 🏢 Set up instructions 

**Step 1: Upload Project Files**
Begin by uploading the required backend source code files to your local system or server. The raw text data file used to train the chatbot and app.py file, which contains the Streamlit-based GUI code for the chatbot interface.

**Step 2: Run the Chatbot Code**
Open your code editor and run the chatbot code.

**Step 3: Host the Chatbot on Streamlit**
Once executed, Streamlit will host the chatbot locally or on your cloud environment.

**Step 4: Integrate with Figma Website Prototype**
Copy the generated Streamlit link and open the Figma website prototype. Then use the Figma embed feature or link placeholder component to integrate the chatbot link within the prototype. Ensure the chatbot is embedded within the desired section or wherever required in the pilot-facing interface.

**Step 5: Test the Final Functional Prototype**
Run or preview the Figma prototype. You should now be able to, Interact with the static website UI. Access the working chatbot directly from the prototype, enabling end-to-end demonstration and functionality testing.

## 📺 Our MVP Project UI Demo

Here is the [Figma UI Demo](https://www.figma.com/proto/wVMpGCL0WFhtL41Fe2VtGa/BIG_UIDemo_Team2?node-id=0-1&t=B9hqEcNErn9PZ8hc-1) 

![image](https://github.com/user-attachments/assets/a1147587-2baa-48cc-ab35-208366567c21)

## ✅ Product Strengths & ⚠️ Current Limitations

| Category             | Points                                                                 |
|----------------------|------------------------------------------------------------------------|
| ✅ Strength           | Smart CBA Query Handling                                               |
| ✅ Strength           | Support for Flight Assignment Decisions                                |
| ✅ Strength           | Clause-Level Information Access                                        |
| ✅ Strength           | Independent Functionality                                              |
| ⚠️ Limitation         | Static Sample Data                                                     |
| ⚠️ Limitation         | Manual Updates for New CBAs                                            |
| ⚠️ Limitation         | Fatigue Dashboard Based on Assumptions                                 |
| ⚠️ Limitation         | Limited Training Sources and AI Dependence                             |

## 🔧 Recommended Tech Stack (Long-Term)

| Category          | Recommended Technology                    | Why We Recommend It                                                                 |
|------------------|-------------------------------------------|-------------------------------------------------------------------------------------|
| ETL              | Informatica                                | Scalable and robust for enterprise-level data extraction, transformation, and loading |
| Database         | PostgreSQL                                 | Reliable open-source relational DB with strong support for complex queries and analytics |
| UI & Stack       | MERN Stack (Mongo, Express, React, Node)   | Enables a responsive, modern, full-stack web application with modular scalability   |
| Chatbot          | RAG (Retrieval-Augmented Generation)       | Supports contextual and accurate answers using grounding documents like CBAs        |
| Document Reading | Amazon Textract                            | Extracts structured data from unstructured documents, ideal for reading CBA clauses  |

## ✨ Crew & Credits

- Flight captained by **Aditi Dahare (Project Manager)**  
- Navigated by technical crew: **Aditi Patil**, **Dhyey Kasundra**, **Viral Sheth**, and **Sylvia Zhou** ✈️  
- Powered by: **OpenAI (GPT-4)**, **AWS Textract**, **LangChain**, and **Streamlit**  
- Inspired by the dream: *Making CBAs as easy to query as plotting a course — clear, fast, and pilot-friendly.*


**Ready to embark on our own CBA documents and scheduling database voyage?**  
**Let’s touch the sky and beyond!✈️**

---
