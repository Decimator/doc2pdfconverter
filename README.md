# RapidFort Assignment

### Project Overview
This project is an offline assignment to create a web application that processes Word documents (.docx) and converts them to PDF. The user can upload a .docx file, view its metadata, and download the converted PDF.

### Features
- Upload `.docx` files for conversion to PDF.
- Display metadata of the uploaded file.
- Download the converted PDF.
- **Bonus**:
  - Hosted endpoint to test the service.
  - Password protection support for PDF files.
  - Microservice architecture.

---

## Hosted Links

- **Web Application**: [http://20.40.55.144:8000](http://20.40.55.144:8000)
- **API Endpoint**: [http://20.40.55.144:8000/api/api/convert](http://20.40.55.144:8000/api/api/convert)

---

## Rubric

1. **Repository and Documentation**
   - The program should be stored in a GitHub or Bitbucket repository.
   - Comprehensive documentation for easy understanding and usage.

2. **Exception Handling**
   - Handle exceptions to ensure smooth user experience and graceful error handling.

3. **User Interface**
   - A simple, intuitive UI for uploading, converting, and downloading files.

4. **Dockerization**
   - Dockerize the application to enable easy deployment and containerization.

5. **CI/CD Pipeline**
   - Add a GitHub Actions pipeline (or equivalent) to build the Docker image.

6. **Bash Script**
   - Include a bash script with instructions to run the container.

7. **Kubernetes Deployment**
   - Kubernetes manifest files to host the web application on a Kubernetes cluster.

---

## Tech Stack
- **Framework**: Django REST Framework & Django
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

---

## Installation and Setup

### Prerequisites
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repo-url>
   cd <repo-name>
