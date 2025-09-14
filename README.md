# Library Management System

A modular, object-oriented Library Management System developed collaboratively using Python and GitHub. This project demonstrates collaborative software development practices with multiple teams working on different modules that integrate into a single working application.

## 🚀 Features

- **Book Management**: Add, remove, and track library books with ISBN, title, author, and copies
- **Member Management**: Register and manage library members with borrowing history
- **Issue & Return System**: Handle book borrowing and returning with availability tracking
- **Search Functionality**: Search books by title, author, or ISBN
- **Authentication System**: Basic login system for librarians and members
- **User Interface**: Interactive menu-driven application
- **Unit Testing**: Comprehensive test coverage for all modules

## 📁 Project Structure

```
library-management-system/
├── book.py                        # Book class implementation
├── member.py                      # Member class implementation  
├── library.py                     # Library class implementation
├── issue_return.py                # Book issue and return functionality
├── search.py                      # Search functionality
├── auth_system.py                 # Authentication system
├── library_management_system.py   # Main application interface
├── test_library.py                # Unit tests
├── README.md                      # Project documentation
└── .github/
    └── PULL_REQUEST_TEMPLATE.md   # PR template
```

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Requirements**
   - Python 3.6 or higher
   - No external dependencies required

3. **Run the application**
   ```bash
   python main.py
   ```

## 🎮 Usage

### Running the Main Application
```bash
python main.py
```

### Running Tests
```bash
python -m pytest unittest discover -s tests -p "test_*.py"
```

## 🏗️ Architecture

The system follows object-oriented design principles:

- **Separation of Concerns**: Each module has a specific responsibility
- **Modularity**: Components can be developed and tested independently  
- **Integration**: All modules work together through well-defined interfaces
- **Testability**: Each module includes comprehensive test coverage

## 📋 Final Deliverables

- ✅ Individual module files (`book.py`, `member.py`, etc.)
- ✅ Integrated application (`library_management_system.py`)
- ✅ Comprehensive testing suite (`test_library.py`)
- ✅ Complete documentation (`README.md`, PR template)
- ✅ GitHub workflow setup with branch protection

## 📄 License

This project is developed as part of a collaborative learning exercise.

## 📞 Support

For questions about specific modules or integration issues, please:
1. Check existing GitHub issues
2. Create a new issue with appropriate labels

---

**Happy coding! 📚✨**
