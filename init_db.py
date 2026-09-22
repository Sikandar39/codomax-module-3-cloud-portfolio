from app import get_db_connection


projects = [

    (
        "Student Database Management App",
        "Developed a student database application for Government Primary School Totano Bandai to organize student records and academic data.",
        "Python / Database",
        "Database"
    ),

    (
        "Banking System",
        "Designed and configured a simulated banking network using Cisco Packet Tracer with a focus on connectivity and device configuration.",
        "Cisco Packet Tracer",
        "Networking"
    ),

    (
        "Smart Attendance System",
        "Developed a structured digital attendance solution designed to reduce manual record keeping.",
        "Software Development",
        "Application"
    ),

    (
        "Hospital Management System",
        "Developed a SQL-based database system for managing patients, doctors, appointments and hospital records.",
        "SQL",
        "Database"
    ),

    (
        "Patient Record System",
        "Built a patient record application using Python Object-Oriented Programming.",
        "Python OOP",
        "Application"
    ),

    (
        "Zero Trust Pro",
        "Founded and manage a cybersecurity learning community focused on practical cybersecurity, cloud fundamentals, networking and hands-on learning.",
        "Cybersecurity / Cloud",
        "Community"
    )
]


connection = get_db_connection()

cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id SERIAL PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        description TEXT NOT NULL,
        technology VARCHAR(200),
        category VARCHAR(100)
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact_messages (
        id SERIAL PRIMARY KEY,
        name VARCHAR(150) NOT NULL,
        email VARCHAR(200) NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")


cursor.execute(
    "SELECT COUNT(*) FROM projects;"
)

count = cursor.fetchone()[0]


if count == 0:

    cursor.executemany(
        """
        INSERT INTO projects
        (title, description, technology, category)
        VALUES (%s, %s, %s, %s)
        """,
        projects
    )


connection.commit()

cursor.close()

connection.close()


print(
    "Database initialized successfully."
)
