import matplotlib.pyplot as plt

# Antworten vom Fragebogen und Modell
answers = {
    "Picture 1": {
        "correct": "Alfa Romeo",
        "responses": {
            "Alfa Romeo": 1,
            "Audi": 0,
            "Hyundai": 0,
            "Lancia": 0,
            "Mahindra": 0,
            "Rolls Royce": 0,
            "Suzuki": 0,
            "Tata": 0,
            "Toyota": 0,
        },
        "model": {
            "Alfa Romeo": 0.3507400453090668 ,
            "Audi": 0.03013278730213642,
            "Hyundai": 0.005508130416274071,
            "Lancia": 0.6040554642677307,
            "Mahindra": 0.0,
            "Rolls Royce": 0.0,
            "Suzuki": 0.005786998197436333,
            "Tata": 0.0,
            "Toyota": 0.0,
        }
    },
    "Picture 2": {
        "correct": "Audi",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 1,
            "Hyundai": 0,
            "Lancia": 0,
            "Mahindra": 0,
            "Rolls Royce": 0,
            "Suzuki": 0,
            "Tata": 0,
            "Toyota": 0,
        },
        "model": {
            "Alfa Romeo": 0.0,
            "Audi": 0.9790475964546204,
            "Hyundai": 0.0031706257723271847,
            "Lancia": 0.005931041669100523,
            "Mahindra": 0.00,
            "Rolls Royce": 0.0038955521304160357,
            "Suzuki": 0.00,
            "Tata": 0.006769973784685135,
            "Toyota": 0.00,
        }
    },
    "Picture 3": {
        "correct": "Toyota",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0.,
            "Hyundai": 0.2553,
            "Lancia": 0,
            "Mahindra": 0.0588,
            "Rolls Royce": 0,
            "Suzuki": 0.0588,
            "Tata": 0.0588,
            "Toyota": 0.5882,
        },
        "model": {
            "Alfa Romeo": 0.04852062836289406 ,
            "Audi": 0.48643016815185547,
            "Hyundai": 0.01,
            "Lancia": 0.03397078067064285 ,
            "Mahindra": 0.01,
            "Rolls Royce": 0.01,
            "Suzuki": 0.20137836039066315,
            "Tata": 0.01,
            "Toyota": 0.21510370075702667,
        }
    },
    "Picture 4": {
        "correct": "Suzuki",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0,
            "Hyundai": 0,
            "Lancia": 0,
            "Mahindra": 0,
            "Rolls Royce": 0,
            "Suzuki": 0.9412,
            "Tata": 0,
            "Toyota": 0.0588,
        },
        "model": {
            "Alfa Romeo": 0.06436432152986526 ,
            "Audi": 0.026714054867625237 ,
            "Hyundai": 0.0352608896791935 ,
            "Lancia": 0.0729294866323471 ,
            "Mahindra": 0.0,
            "Rolls Royce": 0.0,
            "Suzuki": 0.7994698286056519 ,
            "Tata": 0.0,
            "Toyota": 0.0,
        }
    },
    "Picture 5": {
        "correct": "Tata",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0,
            "Hyundai": 0.2353,
            "Lancia": 0.1176,
            "Mahindra": 0.0588,
            "Rolls Royce": 0.0588,
            "Suzuki": 0,
            "Tata": 0.3529,
            "Toyota": 0.1765,
        },
        "model": {
            "Alfa Romeo": 0.00,
            "Audi": 0.00,
            "Hyundai": 0.00,
            "Lancia": 0.00,
            "Mahindra": 0.00,
            "Rolls Royce": 0.00,
            "Suzuki": 0.00,
            "Tata": 0.9990381002426147 ,
            "Toyota": 0.00,
        }
    },
    "Picture 6": {
        "correct": "Hyundai",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0,
            "Hyundai": 0.7059,
            "Lancia": 0.0588,
            "Mahindra": 0.1176,
            "Rolls Royce": 0.0588,
            "Suzuki": 0,
            "Tata": 0.0588,
            "Toyota": 0,
        },
        "model": {
            "Alfa Romeo": 0.00,
            "Audi": 0.00,
            "Hyundai": 0.9957627654075623 ,
            "Lancia": 0.00,
            "Mahindra": 0.00,
            "Rolls Royce": 0.00,
            "Suzuki": 0.00,
            "Tata": 0.00,
            "Toyota": 0.0027619306929409504 ,
        }
    },
    "Picture 7": {
        "correct": "Rolls Royce",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0,
            "Hyundai": 0,
            "Lancia": 0,
            "Mahindra": 0,
            "Rolls Royce": 1,
            "Suzuki": 0,
            "Tata": 0,
            "Toyota": 0,
        },
        "model": {
            "Alfa Romeo": 0.09079265594482422 ,
            "Audi": 0.20279589295387268 ,
            "Hyundai": 0.00,
            "Lancia": 0.09386775642633438 ,
            "Mahindra": 0.006110547110438347 ,
            "Rolls Royce": 0.6028501391410828,
            "Suzuki": 0.00,
            "Tata": 0.00,
            "Toyota": 0.0,
        }
    },
    "Picture 8": {
        "correct": "Lancia",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0,
            "Hyundai": 0,
            "Lancia": 0.7647,
            "Mahindra": 0.0588,
            "Rolls Royce": 0,
            "Suzuki": 0,
            "Tata": 0.1176,
            "Toyota": 0.0588,
        },
        "model": {
            "Alfa Romeo": 0.0,
            "Audi": 0.2482433021068573 ,
            "Hyundai": 0.14523030817508698 ,
            "Lancia": 0.15755595266819 ,
            "Mahindra": 0.21694867312908173 ,
            "Rolls Royce": 0.00,
            "Suzuki": 0.00,
            "Tata": 0.18094444274902344 ,
            "Toyota": 0.0,
        }
    },
    "Picture 9": {
        "correct": "Alfa Romeo",
        "responses": {
            "Alfa Romeo": 0.8235,
            "Audi": 0,
            "Hyundai": 0,
            "Lancia": 0,
            "Mahindra": 0.0588,
            "Rolls Royce": 0,
            "Suzuki": 0,
            "Tata": 0.1176,
            "Toyota": 0,
        },
        "model": {
            "Alfa Romeo": 0.682945191860199 ,
            "Audi": 0.11495053768157959 ,
            "Hyundai": 0.00,
            "Lancia": 0.15758858621120453 ,
            "Mahindra": 0.00,
            "Rolls Royce": 0.02797536738216877 ,
            "Suzuki": 0.00,
            "Tata": 0.008212029933929443 ,
            "Toyota": 0.0,
        }
    },
    "Picture 10": {
        "correct": "Mahindra",
        "responses": {
            "Alfa Romeo": 0,
            "Audi": 0.0588,
            "Hyundai": 0.1176,
            "Lancia": 0.0588,
            "Mahindra": 0.2353,
            "Rolls Royce": 0,
            "Suzuki": 0.1765,
            "Tata": 0.3529,
            "Toyota": 0,
        },
        "model": {
            "Alfa Romeo": 0.043620526790618896 ,
            "Audi": 0.46873411536216736 ,
            "Hyundai": 0.06705201417207718 ,
            "Lancia": 0.1773829460144043 ,
            "Mahindra": 0.21717634797096252 ,
            "Rolls Royce": 0.00,
            "Suzuki": 0.00,
            "Tata": 0.00,
            "Toyota": 0.0,
        }
    },
}


# Berechnung der Genauigkeit / Wenn diese Wahrscheinlichkeit höher als 0.5 ist, wird dies als korrekt gezählt.
def calculate_accuracy(answers):
    correct_user_count = 0
    correct_model_count = 0
    total_pictures = len(answers)

    for picture, data in answers.items():
        correct_brand = data["correct"]
        
        # Benutzerantworten
        user_votes = data["responses"].get(correct_brand, 0)
        user_accuracy = user_votes  # hier sind die Antworten schon Wahrscheinlichkeiten
        if user_accuracy > 0.5:
            correct_user_count += 1
        
        # Modellantworten
        model_accuracy = data["model"].get(correct_brand, 0)
        if model_accuracy > 0.5:
            correct_model_count += 1

    user_overall_accuracy = (correct_user_count / total_pictures) * 100
    model_overall_accuracy = (correct_model_count / total_pictures) * 100

    return user_overall_accuracy, model_overall_accuracy

# Diagramm erstellen
def plot_accuracy(user_accuracy, model_accuracy):
    labels = ['User', 'Model']
    accuracy = [user_accuracy, model_accuracy]

    fig, ax = plt.subplots()
    ax.bar(labels, accuracy, color=['blue', 'green'])
    ax.set_ylim(0, 100)
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Overall Accuracy Comparison')

    for i, v in enumerate(accuracy):
        ax.text(i, v + 1, f"{v:.2f}%", ha='center', va='bottom')

    plt.show()

# Genauigkeit berechnen
user_accuracy, model_accuracy = calculate_accuracy(answers)

# Diagramm anzeigen
plot_accuracy(user_accuracy, model_accuracy)