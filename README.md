# Book Collection and Task Manager  

A web application that combines two main functionalities:  
1. A REST API for managing a collection of books.  
2. A task management app with multi-user registration and role-based access control.  

## Features  

### Book Collection API  
- Add, update, delete, and view books.  

### Task Manager  
- **User Registration**: Supports multiple user accounts.  
- **Roles**: Users can have roles such as `Manager` and `Worker`.  
- **Task Creation**: Only `Manager` role users can create tasks.  

### Notes  
- Roles (`Manager` and `Worker`) need to be created manually via the admin panel -> Roles admin view.  

## Setup  

### Using Docker (Recommended)  
1. Install **Docker** and **Docker Compose** on your machine.  
2. Open the project in a code editor and select **"Reopen in Container"**.  
3. Run the command:  
   ```bash
   Launch Test App
   ```  

### Manual Setup  
1. Create a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the application:  
   ```bash
   python manage.py runserver
   ```  

## Usage  
- Access the application at `http://127.0.0.1:8000/`.  
- Use the admin panel to create roles (`Manager` and `Worker`).  
- Register users and assign roles via the admin panel.  

## Technologies Used  
- **Backend**: Django  
- **Database**: SQLite (default, can be configured)  
- **Containerization**: Docker  

## Contributing  
Contributions are welcome! Fork the repository and submit a pull request for review.  

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  
