from fpdf import FPDF
import os

# Function to generate a sample resume
def create_resume(filename, name, skills, experience, education):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, f"Resume - {name}", ln=True, align="C")
    pdf.ln(10)

    # Add Sections
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, "Skills:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, skills)
    pdf.ln(5)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, "Experience:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, experience)
    pdf.ln(5)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, "Education:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, education)
    pdf.ln(5)

    # Save the PDF
    pdf_folder = "resumes"
    os.makedirs(pdf_folder, exist_ok=True)
    pdf.output(os.path.join(pdf_folder, filename))

# Create sample resumes
create_resume("resume_1.pdf", "Alice Johnson",
              "Python, Machine Learning, Data Science, NLP",
              "Data Scientist at XYZ Corp (2018-2023)\nWorked on AI-powered chatbots and predictive analytics.",
              "MSc in Data Science - Stanford University")

create_resume("resume_2.pdf", "Bob Williams",
              "Java, Web Development, SQL, Flask",
              "Software Engineer at ABC Tech (2019-2024)\nDeveloped scalable backend systems for web applications.",
              "B.Tech in Computer Science - MIT")

create_resume("resume_3.pdf", "Charlie Brown",
              "Cybersecurity, Ethical Hacking, Linux",
              "Cybersecurity Analyst at DEF Security (2020-2024)\nConducted penetration testing and security audits.",
              "BSc in Information Security - Harvard University")

print("Sample resumes created in the 'resumes/' folder!")
