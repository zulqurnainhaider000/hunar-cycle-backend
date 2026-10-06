"""
Complete Object-Oriented Programming (OOP) 55-Day Curriculum Blueprint
Assembles all 55 days of topic-per-day lessons, deep ELI5 analogies,
progressive multi-language OOP snippets, daily coding challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.oop_curriculum_days_1_15 import DAYS_1_TO_15
from seeder.courses.oop_curriculum_days_16_30 import DAYS_16_TO_30
from seeder.courses.oop_curriculum_days_31_42 import DAYS_31_TO_42
from seeder.courses.oop_curriculum_days_43_55 import DAYS_43_TO_55

# Consolidate all 55 days in strict sequential order
ALL_55_DAYS = DAYS_1_TO_15 + DAYS_16_TO_30 + DAYS_31_TO_42 + DAYS_43_TO_55

OOP_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Object-Oriented Programming (OOP)",
    category="TECH",
    description=(
        "The definitive 55-Day Object-Oriented Programming (OOP) Roadmap. "
        "Enforced universal topic-per-day architecture: "
        "OOP Foundations (Procedural vs OOP, Classes & Objects, State & Behavior, self/this, Constructors, Destructors & Garbage Collection, Student Management System), "
        "Encapsulation & Data Hiding (Data Binding, Public/Private/Protected Modifiers, Getters & Setters, Data Hiding & Slots, Secure Bank Account System), "
        "Inheritance & Code Reusability (IS-A, Single & Multilevel, Hierarchical & Hybrid, Multiple Inheritance & Diamond MRO, super/base, Constructor Chaining, Corporate Hierarchy System), "
        "Polymorphism (Many Forms, Method Overloading, Operator Overloading, Method Overriding, Upcasting & Downcasting, Geometric Shapes CAD System), "
        "Abstraction (Hiding Complexity, Abstract Classes & Methods, Pure Interfaces & Protocols, Abstract Class vs Interface, Payment Gateway Gateway System), "
        "Object Relationships & Associations (Association, Aggregation weak HAS-A, Composition strong PART-OF, Dependency uses-a, Complete Library Management System), "
        "Advanced OOP Concepts (Static Members & Class Methods, Final & Const Immutability, Custom Exception Hierarchies, Enumerations, Inner & Nested Classes, Deep vs Shallow Copying), "
        "OOAD (UML Class Diagrams, Object Diagrams, Use Case Diagrams, Sequence Diagrams), "
        "SOLID Principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion, Legacy Refactoring Project), and "
        "Design Patterns & Architecture (Singleton & Factory Method, Builder & Prototype & Abstract Factory, Adapter & Decorator & Facade, Observer & Strategy & State, Grand E-Commerce Architecture Capstone). "
        "Features 55 hands-on OOP challenges and 275 verified knowledge verification quizzes."
    ),
    color="#4F46E5",
    days=ALL_55_DAYS
)
