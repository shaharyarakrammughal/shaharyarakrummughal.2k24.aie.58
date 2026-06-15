Assignment 1: AI System Specification
Chosen System: Fraud Detection System for Digital Payments and Banking Transactions
Task 1: PEAS Specification
P – Performance Measures

Success of the fraud detection system is measured by:

Fraud Detection Accuracy – Percentage of fraudulent transactions correctly identified.
False Positive Rate – Percentage of legitimate transactions incorrectly flagged as fraud.
Transaction Processing Speed – Time required to analyze and classify a transaction.
Financial Loss Prevention – Amount of fraud-related losses prevented.
Customer Satisfaction – Reduction in inconvenience caused to legitimate customers.
Recall Rate – Percentage of total fraud cases successfully detected.
E – Environment

The system operates within:

Online banking platforms
Mobile banking applications
E-commerce payment gateways
Credit/debit card transaction networks
ATM networks
Financial institutions and digital wallets
Key External Factors
Evolving fraud techniques
User transaction behavior
Network traffic volume
Regulatory requirements
Geographical transaction locations
Device and IP address information
A – Actuators

The system can affect its environment through:

Transaction approval mechanism
Transaction blocking system
Customer alert notifications (SMS/Email/App)
Risk scoring engine
Account suspension module
Reporting and audit systems
S – Sensors

The system gathers information using:

Transaction records
Customer account history
Device fingerprinting data
IP address monitoring
Geolocation data
Login activity logs
Card usage patterns
Behavioral analytics data
Task 2: Environment Classification
Dimension	Classification	Justification
Observability	Partially Observable	The system cannot directly observe the true intention of users and fraudsters; it only sees transaction-related data.
Agents	Multi-Agent	The environment contains legitimate customers, fraudsters, banks, merchants, and the AI system interacting together.
Determinism	Stochastic	Similar transaction patterns may lead to different outcomes, making the environment uncertain and probabilistic.
Episodic vs Sequential	Sequential	Current decisions influence future account behavior, risk scores, and security actions.
Static vs Dynamic	Dynamic	New transactions and fraud patterns continuously appear in real time.
Discrete vs Continuous	Continuous	Transaction amounts, time intervals, and behavioral variables can take continuous values.
Task 3: Critical Analysis
1. Greatest Technical Challenge

The stochastic nature of the environment presents the greatest challenge. Fraudsters constantly develop new attack methods, and legitimate customer behavior changes over time. Because the same transaction pattern may be fraudulent in one situation and legitimate in another, the AI system must continuously learn from new data while minimizing both missed fraud cases and false alarms. This uncertainty makes accurate decision-making difficult.

2. Utility Function

A utility function balancing fraud detection and customer convenience:

U=0.7(Fraud Detection Accuracy)−0.3(False Positive Rate)

Where:

Higher fraud detection accuracy increases utility.
Higher false positive rates decrease utility.
Effect of Doubling the Accuracy Weight

If the weight of fraud detection accuracy is doubled:

U=1.4(Fraud Detection Accuracy)−0.3(False Positive Rate)

The agent becomes more aggressive in identifying fraud. It will flag more suspicious transactions to maximize fraud detection, but this may also increase false positives and occasionally inconvenience legitimate customers.

Task 4: Structured Representation (JSON)
{
  "system_name": "Fraud Detection System for Digital Payments and Banking Transactions",
  "peas": {
    "performance_measures": [
      "fraud_detection_accuracy",
      "false_positive_rate",
      "transaction_processing_speed",
      "financial_loss_prevention",
      "customer_satisfaction",
      "recall_rate"
    ],
    "environment": "Online banking platforms, mobile banking applications, e-commerce payment gateways, ATM networks, digital wallets, and financial institutions where transactions occur in real time.",
    "actuators": [
      "transaction_approval_mechanism",
      "transaction_blocking_system",
      "customer_alert_notifications",
      "risk_scoring_engine",
      "account_suspension_module",
      "reporting_and_audit_system"
    ],
    "sensors": [
      "transaction_records",
      "customer_account_history",
      "device_fingerprinting_data",
      "ip_address_monitoring",
      "geolocation_data",
      "login_activity_logs",
      "card_usage_patterns",
      "behavioral_analytics_data"
    ]
  },
  "environment_classification": {
    "observability": {
      "choice": "Partially Observable",
      "justification": "The system cannot directly observe the true intentions of users and fraudsters."
    },
    "agents": {
      "choice": "Multi-Agent",
      "justification": "Customers, fraudsters, merchants, banks, and the AI system interact in the environment."
    },
    "determinism": {
      "choice": "Stochastic",
      "justification": "Transaction outcomes and fraud patterns involve uncertainty and probability."
    },
    "episodic_vs_sequential": {
      "choice": "Sequential",
      "justification": "Current decisions influence future risk assessments and account behavior."
    },
    "static_vs_dynamic": {
      "choice": "Dynamic",
      "justification": "Transactions and fraud tactics change continuously in real time."
    },
    "discrete_vs_continuous": {
      "choice": "Continuous",
      "justification": "Variables such as transaction amount, time, and risk scores have continuous values."
    }
  },
  "utility_function": "U = 0.7 * Fraud_Detection_Accuracy - 0.3 * False_Positive_Rate"
}
