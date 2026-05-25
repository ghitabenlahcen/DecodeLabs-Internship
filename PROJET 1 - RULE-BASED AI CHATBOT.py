# PROJET 1 - RULE-BASED AI CHATBOT
# DecodeLabs - Industrial Training Kit 2026

def nettoyer_entrée(texte):
    """Nettoie l'entrée utilisateur : minuscules + suppression espaces"""
    return texte.lower().strip()

def chatbot():
    """Fonction principale du chatbot"""
    
    # Base de connaissances (dictionnaire intention → réponse)
    responses = {
        # Salutations
        "bonjour": "👋 Bonjour ! Comment puis-je t'aider ?",
        "salut": "Salut ! Content de te voir !",
        "coucou": "Coucou ! 😊",
        "hello": "Hello ! Comment ça va ?",
        
        # Questions sur l'identité
        "qui es-tu": "Je suis un chatbot",
        "ton nom": "Je m'appelle GHBot",
        "que fais-tu": "Je réponds à des commandes prédéfinies. C'est mon rôle !",
        
        # Capacités
        "tu peux faire quoi": "Je peux te saluer, répondre à quelques questions et te dire au revoir !",
        "aide": "🔧 Commandes disponibles : bonjour, comment ça va, météo, au revoir, quit",
        
        # État / humeur
        "comment ça va": "Ça va très bien, et toi ? 🤖",
        "ça va": "Tant mieux ! Je suis là pour t'aider.",
        
        # Météo (exemple simple)
        "météo": "Je ne suis pas connecté à Internet, mais je parie qu'il fait beau ☀️",
        "il fait quel temps": "Désolé, je ne peux pas vérifier la météo pour l'instant.",
        
        # Au revoir / sortie
        "au revoir": "👋 Au revoir ! À bientôt !",
        "bye": "Bye ! Merci d'avoir discuté avec moi.",
        "quit": "Fermeture du chatbot. À la prochaine !",
        "exit": "Fermeture en cours..."
    }
    
    
    print("🤖 GHBot - Chatbot à base de règles")
    print("💬 Tape 'aide' pour voir les commandes disponibles")
    print("❌ Tape 'quit' ou 'exit' pour quitter")
    
    # Boucle infinie → le cœur du squelette
    while True:
        # 1. INPUT : récupérer la saisie utilisateur
        user_input = input("\n🧑 Vous : ")
        
        # 2. SANITIZATION : nettoyer l'entrée
        clean_input = nettoyer_entrée(user_input)
        
        # 3. Vérifier la commande de sortie
        if clean_input in ["quit", "exit", "fermer", "quitter"]:
            print("🤖 GHBot : Au revoir ! 👋")
            break
        
        # 4. LOGIC ENGINE : chercher la réponse (avec fallback)
        #    La méthode .get() = lookup + valeur par défaut en 1 opération
        reponse = responses.get(clean_input, "😕 Je ne comprends pas cette commande. Tape 'aide' pour voir ce que je sais faire.")
        
        # 5. OUTPUT : afficher la réponse
        print(f"🤖 GHBot : {reponse}")

# Point d'entrée du programme
if __name__ == "__main__":
    chatbot()