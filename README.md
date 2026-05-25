# DecodeLabs-Internship
# Projet 1 - Rule-Based AI Chatbot

**Batch:** 2026  
**Powered by:** DecodeLabs  

---

## À propos du projet

Ce projet constitue la première étape du parcours d'ingénieur IA chez DecodeLabs.

Avant de construire des systèmes qui apprennent par eux-mêmes (deep learning, LLM), nous maîtrisons d'abord la logique déterministe à travers un chatbot basé sur des règles.

> "Un LLM sans règles est un moteur à hallucinations. Aujourd'hui, nous construisons le squelette qui contiendra l'intelligence de demain."

---

##  Objectifs pédagogiques

| Compétence | Description |
|------------|-------------|
| ✅ Contrôle de flux | Boucle infinie `while True` |
| ✅ Prise de décision | Structure conditionnelle (`if`, dictionnaire) |
| ✅ Nettoyage d'entrée | Normalisation des données utilisateur |
| ✅ Gestion d'état | Commande de sortie propre |
| ✅ Architecture IPO | Input → Process → Output |


##  Fonctionnalités

- Répond aux salutations (`bonjour`, `salut`, `coucou`, `hello`)
- Répond aux questions simples (`qui es-tu`, `ton nom`, `que fais-tu`)
- Fournit une commande `aide` pour l'utilisateur
- Gère la météo (réponse statique)
- Commande de sortie (`quit`, `exit`, `au revoir`)
- Réponse par défaut pour les entrées inconnues
- Nettoyage automatique (minuscules + suppression espaces)

---

##  Installation et exécution

### Prérequis
- Python 3.6

### Étapes

```bash
# 1. Cloner ou télécharger le projet
git clone https://github.com/ton-compte/projet1-chatbot.git
cd projet1-chatbot

# 2. Exécuter le chatbot
python chatbot.py
