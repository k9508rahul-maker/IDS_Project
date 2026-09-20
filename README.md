# 🛡️ IDS Security Dashboard

A **Machine Learning Based Intrusion Detection System (IDS)** built with Python and Flask.
The system analyzes network traffic parameters and predicts whether the traffic is **Normal** or an **Attack**.

## 📌 Project Overview

An Intrusion Detection System monitors network traffic and helps identify potentially malicious activity.

This project uses a Machine Learning model to classify network traffic based on:

* Packet Size
* Connection Count
* Failed Connections
* Duration

The prediction results are displayed through a web-based security dashboard.

## ✨ Features

* 🛡️ Machine Learning based traffic classification
* 🔍 Network traffic analysis
* 🚨 Attack detection
* ✅ Normal traffic detection
* 📊 Security dashboard
* 🧠 Trained ML model
* 🌐 Flask web application
* 💾 CSV dataset
* 📈 Prediction results

## 🏗️ Project Structure

```text
IDS_Project/
│
├── dataset/
│   └── network_traffic.csv
│
├── model/
│   ├── ids_model.pkl
│   └── label_encoder.pkl
│
├── static/
│
├── templates/
│   └── dashboard.html
│
├── app.py
├── train_model.py
├── .gitignore
└── README.md
```

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **HTML**
* **CSS**
* **Machine Learning**
* **Git & GitHub**

## 🤖 Machine Learning

The project uses a supervised Machine Learning classification model.

### Input Features

| Feature            | Description                  |
| ------------------ | ---------------------------- |
| Packet Size        | Size of network packets      |
| Connection Count   | Number of connections        |
| Failed Connections | Number of failed connections |
| Duration           | Connection duration          |

### Output

The model classifies traffic into:

* **Normal**
* **Attack**

## 📊 Model Training

The model can be trained using:

```bash
python train_model.py
```

The training script creates/trains the model and saves the trained files inside the `model/` directory.

Generated model files:

```text
model/
├── ids_model.pkl
└── label_encoder.pkl
```

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/k9508rahul-maker/IDS_Project.git
```

### 2. Open the Project

```bash
cd IDS_Project
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```cmd
venv\Scripts\activate
```

### 5. Install Dependencies

Install the required packages:

```bash
pip install flask pandas scikit-learn
```

### 6. Train the Model

```bash
python train_model.py
```

### 7. Start Flask Application

```bash
python app.py
```

The application should start on a local address similar to:

```text
http://127.0.0.1:5000/
```

Open the address in your browser.

## 🔍 Using the Dashboard

1. Open the IDS Security Dashboard.
2. Enter the network traffic information.
3. Provide:

   * Packet Size
   * Connection Count
   * Failed Connections
   * Duration
4. Click **Analyze Traffic**.
5. The Machine Learning model will classify the traffic.
6. The result will be displayed on the dashboard.

## 📈 Example

Example of normal traffic:

```text
Packet Size: 150
Connection Count: 3
Failed Connections: 0
Duration: 15
```

Example of suspicious traffic:

```text
Packet Size: 900
Connection Count: 80
Failed Connections: 20
Duration: 2
```

These examples are for demonstrating the application and do not represent a production-grade IDS threshold.

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

The included dataset is small and simplified. The model's reported training/test performance should not be interpreted as evidence of real-world intrusion-detection accuracy.

For production use, an IDS would require a substantially larger and representative dataset, appropriate validation, monitoring, security controls, and testing against realistic network traffic.

## 🔮 Future Improvements

Possible future enhancements include:

* Real-time packet capture
* Larger cybersecurity datasets
* More Machine Learning algorithms
* Deep Learning based detection
* Real-time alerts
* IP address monitoring
* Attack type classification
* Interactive charts
* Database integration
* User authentication
* Deployment to a cloud platform
* Model performance monitoring

## 👨‍💻 Author

**Rahul**

GitHub:
https://github.com/k9508rahul-maker

## 📄 License

This project is available for educational and personal use. A specific open-source license can be added if the project is intended for redistribution.
