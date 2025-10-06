# Boxyz Hub

Application de domotique moderne développée avec Electron pour contrôler et gérer votre maison intelligente.

## 📋 Description

Boxyz Hub est une interface utilisateur élégante qui vous permet de :
- Visualiser l'heure et la météo en temps réel
- Contrôler vos lumières connectées
- Gérer différentes pièces de votre maison
- Personnaliser les paramètres de votre système domotique

## 🚀 Installation

### Prérequis

- [Node.js](https://nodejs.org/) (version 12 ou supérieure)
- npm (inclus avec Node.js)

### Étapes d'installation

1. Cloner le repository :
```bash
git clone https://github.com/Ekyoz/Boxyz_Hub.git
cd Boxyz_Hub
```

2. Installer les dépendances :
```bash
npm install
```

3. Configurer votre clé API OpenWeatherMap :
```bash
cp config.example.js config.js
```
Puis éditer `config.js` et ajouter votre clé API OpenWeatherMap.

## 🎯 Lancement de l'application

Pour démarrer l'application Electron :

```bash
npm start
```

L'application s'ouvrira automatiquement dans une fenêtre native.

## 📁 Structure du projet

```
Boxyz_Hub/
├── main.js              # Point d'entrée principal de l'application Electron
├── preload.js           # Script de préchargement pour le contexte Electron
├── package.json         # Configuration npm et dépendances
├── resources/           # Ressources de l'application
│   ├── html/           # Pages HTML
│   │   ├── home.html   # Page d'accueil
│   │   ├── light.html  # Contrôle des lumières
│   │   ├── weather.html # Météo détaillée
│   │   └── piece/      # Pages par pièce
│   ├── css/            # Feuilles de style
│   ├── js/             # Scripts JavaScript
│   ├── image/          # Images et icônes
│   └── video/          # Vidéos de fond
```

## 🔧 Fonctionnalités

### Page d'accueil
- Affichage de l'heure en temps réel
- Affichage de la date
- Météo actuelle avec icône
- Navigation vers les différentes sections

### Gestion des lumières
- Allumer/éteindre les lumières par pièce
- Interface intuitive avec boutons on/off

### Gestion des pièces
Les pièces disponibles :
- Chambre Alex
- Chambre Antoine
- Bureau Eric
- Salon
- Salle à manger

### Météo
- Intégration avec l'API OpenWeatherMap
- Affichage de la température
- Icônes météo dynamiques

## ⚙️ Configuration

### API Météo
L'application utilise l'API OpenWeatherMap. Pour configurer votre propre clé API :

1. Créer un fichier `config.js` à la racine du projet en copiant `config.example.js` :
```bash
cp config.example.js config.js
```

2. Ouvrir `config.js` et remplacer `YOUR_API_KEY_HERE` par votre clé API OpenWeatherMap :
```javascript
module.exports = {
    openWeatherMapApiKey: 'VOTRE_CLE_API',
    weatherCity: 'Villeurbanne'  // Ou votre ville
};
```

**Note importante**: Le fichier `config.js` contient votre clé API et ne doit **jamais** être committé dans Git. Il est déjà inclus dans `.gitignore`.

### Contrôle des lumières
L'application communique avec un serveur assistant. Modifier l'URL dans `resources/js/light.js` :
```javascript
url: 'http://VOTRE_IP:PORT/assistant',
```

## 🎨 Personnalisation

### Thème visuel
- Les styles sont définis dans `resources/css/style.css`
- Les vidéos de fond sont dans `resources/video/`
- Les icônes et images sont dans `resources/image/`

## 📝 Technologies utilisées

- **Electron** - Framework pour applications desktop
- **Bootstrap** - Framework CSS
- **jQuery** - Bibliothèque JavaScript
- **OpenWeatherMap API** - Service météo

## 🐛 Dépannage

### L'application ne démarre pas
- Vérifier que Node.js est installé : `node --version`
- Réinstaller les dépendances : `npm install`

### La météo ne s'affiche pas
- Vérifier votre connexion internet
- Vérifier que la clé API OpenWeatherMap est valide

### Les lumières ne répondent pas
- Vérifier que le serveur assistant est en cours d'exécution
- Vérifier l'adresse IP et le port dans `light.js`

## 📄 Licence

CC0-1.0 License

## 👥 Auteur

Ekyoz

---

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.
