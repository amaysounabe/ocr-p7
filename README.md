<h1 style="text-align: center; font-size: 35px;">Implémentation d'un modèle de scoring</h1>

<div style = "text-align: center;">
    <img src = "https://user.oc-static.com/upload/2023/03/22/16794938722698_Data%20Scientist-P7-01-banner.png", alt="Bannière" style="width: 70%">
</div>

## Description
La société **Prêt à dépenser** propose des crédits à la consommation pour des 
personnes ayant peu ou pas d'historiques de prêt. <br>
Les données utilisées au cours de ce projet sont disponibles [**ici**](https://www.kaggle.com/c/home-credit-default-risk/data) ou peuvent être téléchargées via les commandes suivantes
    
```bash
pip install kaggle
kaggle competitions download -c home-credit-default-risk
```
<br>

(Vous aurez besoin d'un compte sur le site Kaggle et d'une clé d'API)

Afin d'installer les données correctement, une fois le répertoire cloné, assurez-vous que l'archive des données est dans le répertoire `../ocr-p7/`. <br>
Ensuite, effectuez les commandes suivantes :
```bash
cd ocr-p7
unzip home-credit-default-risk.zip -d data/csv_files
rm home-credit-default-risk.zip
```

### Objectifs
- Mise en oeuvre d'un outil de **scoring crédit** qui calcule la probabilité qu'un client rembourse son crédit
- Mise en production du modèle de classification à l'aide d'une **API**
- Détection de dérives de données

### Fichiers
- **notebook_modelisation.ipynb** &rarr; Nootebook comportant : EDA, feature engineering, modélisation & optimisation du modèle final
- **fonctions.py** &rarr; Fichier python comportant les fonctions utilisées dans le notebook
- **data_drift_report** &rarr; Rapport de dérive de données au format HTML
- **slides_presentation.pdf** &rarr; Support de présentation utilisé lors de la soutenance du projet
- **`data/`** &rarr; Dossier contenant les données ainsi que les dataframes et autres (modèles, seuil) enregistrés au cours du projet <br>
├── `csv_files/` &rarr; Données de base <br>
├── `dataframes/` &rarr; Dataframes enregistrés à l'issue de l'analyse et modélisation (Feature Engineering) <br>
├── df_test.csv &rarr; Jeu de test (Cible non renseignée) <br>
├── optimal_threshold.npy &rarr; Seuil de décision optimal au format numpy <br>
└── xgbclassifier.pkl &rarr; Modèle retenu (XGBoost) au format pickle <br>
- **`graphics/`** &rarr; Dossier contenant les graphiques enregistrés au cours du projet
- **`dashboard/`** &rarr; Dossier comportant les fichiers python pour l'API et le dashboard Streamlit <br>
├── api_flask.py &rarr; Code source de l'API <br>
├── dashboard_interface.py &rarr; Code source du dashboard Streamlit <br>
├── dashboard_fonctions.py &rarr; Fonctions python utilisées dans l'interface du dashboard <br>
├── dashboard_fonctions_test.py &rarr; Fonctions testées lors du push sur GitHub <br>
├── pytest_requirements.txt &rarr; Liste des librairies nécessaires pour les tests unitaires <br>
└── `styles/` &rarr; Dossier contenant le fichier **css** utilisé dans le dashboard Streamlit
- **`mlruns/`** &rarr; Dossier contenant les runs des modélisations (visibles dans l'interface de MlFlow)
- **requirements.txt** &rarr; Fichier texte contenant les librairies python nécessaires

### Détails
- Version de Python utilisée &rarr; **Python 3.12**
- Liste des librairies utilisées
    - **numpy**
    - **pandas**
    - **matplotlib**
    - **seaborn**
    - **scikit-learn**
    - **xgboost**
    - **mlflow**
    - **shap**
    - **joblib**
    - **evidently**
    - **pytest**
    - **streamlit**

## Procédure
- Analyse exploratoire des données à l'aide d'un  moteur **KAGGLE** 
    (disponible [**ici**](https://www.kaggle.com/code/willkoehrsen/start-here-a-gentle-introduction/notebook))
- Feature engineering
- Entraînement des modèles de classification et tracking via **Mlflow**
- Optimisation du meilleur modèle via un **score** adapté au contexte métier
- &Eacute;tude de l'importance des features via **shap**
- Réalisation du dashboard **Streamlit**
- Déploiement du dashboard sur le cloud
- &Eacute;tude de la dérive de données

## API & Dashboard interactif
Initialement, l'API et le dashboard étaient disponibles en ligne via des solutions gratuites (Render pour l'API, Streamlit pour le dashboard). <br>
Ces solutions n'étant pas durables, le code du projet a été modifié pour être utilisé en local.

## Installation
```bash
git clone https://github.com/amaysounabe/ocr-p7.git
cd ocr-p7
pip install -r requirements.txt
```

### MlFlow
***
Pour lancer MlFlow, assurez-vous d'être dans le dossier `ocr-p7/` puis lancer la commande suivante :
```bash
mlflow ui
```
Par défaut, **MlFlow** écoute sur le port **5000**. Vous pouvez personnaliser cette option comme suit :

```bash
mlflow ui --port=xxxx
```

### API & Dashboard
***

- *L'API est configurée pour écouter sur le port **7000**. Il est donc important que ce port soit disponible et non occupé par une autre application.*
  ```bash
  cd dashboard/
  python api_flask.py
  ```
    Pour tester l'API, vous pouvez essayer de lancer la commande suivante dans votre terminal
  ```bash
  curl http://127.0.0.1:7000/predict/100001
  ```
- Pour lancer le dashboard Streamlit, assurez-vous que l'API soit déployée en local et de vous situer dans le dossier `dashboard/`
  ```bash
  streamlit run dashboard_interface.py
  ```
  Vous devriez voir un message apparaître de type :
  ```bash
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://xxx.xxx.x.xxx:8501
  ```

  Si l'application ne se lance pas automatiquement dans votre navigateur, allez à la première URL indiquée plus haut.