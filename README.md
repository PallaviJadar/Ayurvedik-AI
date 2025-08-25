# Ayurvedik AI - Medicinal Plant Identification System

An intelligent web application that identifies medicinal plants using AI and provides detailed Ayurvedic information about them.

## 🌿 Features

- **Plant Identification**: Upload images of medicinal plants for AI-powered identification
- **Ayurvedic Information**: Get comprehensive details about medicinal properties, uses, and benefits
- **User Authentication**: Secure login/registration system
- **Chat Interface**: Interactive chat with AI expert for plant-related queries
- **Responsive Design**: Clean and user-friendly web interface

## 🚀 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Jinja2 Templates
- **AI/ML**: Transformers (Hugging Face), Google Gemini AI
- **Database**: SQLite
- **Image Processing**: Pillow, OpenCV
- **Authentication**: Session-based with password hashing

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PallaviJadar/Ayurvedik-AI.git
   cd Ayurvedik-AI
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open your browser and go to `http://localhost:5000`

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `SECRET_KEY`: Flask secret key for session management

### API Keys

1. **Google Gemini API**: 
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Create an API key
   - Add it to your `.env` file

## 📁 Project Structure

```
Ayurvedik-AI/
├── app.py                 # Main Flask application
├── model.py              # ML model definitions
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables (not in repo)
├── README.md           # This file
├── static/
│   └── uploads/         # User uploaded images
├── templates/           # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── predict.html
│   ├── plant_info.html
│   └── about.html
├── model/              # Trained model files
├── Samples/            # Sample plant images
├── Data/              # Data files
└── Docs/              # Documentation
```

## 🎯 Usage

1. **Register/Login**: Create an account or login to access plant identification features
2. **Upload Image**: Navigate to the prediction page and upload a plant image
3. **Get Results**: The AI will identify the plant and provide confidence score
4. **Learn More**: Click on the plant name to get detailed Ayurvedic information
5. **Chat**: Use the chat interface to ask questions about medicinal plants

## 🌟 Supported Plants

The system can identify various medicinal plants including:
- Aloe Vera
- Amla (Indian Gooseberry)
- Mint
- Tulsi (Holy Basil)
- Neem
- Turmeric
- And many more...

## 🔒 Security Features

- Password hashing using SHA256
- Session-based authentication
- File upload validation
- SQL injection prevention
- Environment variable protection

## 🛠️ Development

### Adding New Plant Support

1. Train the model with new plant images
2. Update the model files
3. Test the identification accuracy

### Customizing Templates

Modify HTML files in the `templates/` directory to change the UI.

### Database Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

## 📊 Performance

- Image processing: < 2 seconds
- Plant identification: < 3 seconds
- AI response generation: < 5 seconds

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for natural language processing
- Hugging Face for the plant identification model
- Flask community for the web framework
- Ayurvedic experts for medicinal plant knowledge

## 📞 Support

For support and questions, please open an issue on GitHub or contact the development team.

---

**Note**: This project is for educational and research purposes. Always consult healthcare professionals before using medicinal plants for treatment.
