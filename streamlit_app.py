import streamlit as st
import random

st.title("🍿 Snack Suggestion Bot")
st.caption("Feeling snacky? Let the universe (aka Python) decide for you.")

# Step 1: Mood selection
mood = st.selectbox(
    "How are you feeling today?",
    ["✨ Magical", "😩 Burnt out", "😐 Meh", "🧠 Hyperfocused", "😢 Sad", "😎 Unbothered", "🤡 Delulu", "😵‍💫 Spiral Mode",  "🥱 Just Here",  "🤔 Existential Crunch", "😴 Mentally Logged Out", "🧃 Soft Mode"]
)

# Step 2: Sweet or savory?
flavor = st.radio("Sweet or savory?", ["Sweet", "Savory"])

sweet_snack_dict = {
    "Salted Egg Churros": "Crispy, creamy, a little weird—but in a good way. Like you on a Wednesday.",
    "Pisang Nugget": "Deep-fried banana with toppings. Sweet chaos, just like your social calendar.",
    "Dessert Box": "Layers of emotions, sugar, and probably repressed feelings. Eat it layer by layer.",
    "Martabak Manis Red Velvet": "It’s classic martabak but dressed for Instagram. Aesthetic cravings approved.",
    "Korean Garlic Bread (Sweet)": "Garlic? Sweet? Yes. Your brain might glitch, but your taste buds won’t.",
    "Soft Baked Cookies": "Crispy outside, soft inside. Just like your carefully curated online persona.",
    "Puding Regal": "Childhood nostalgia with adult responsibilities. Creamy, crunchy, emotionally complex.",
    "Brown Sugar Boba Milk Cake": "You wanted boba, you got boba. But make it thicc and sliceable.",
    "Matcha cookies": "A little green energy, but make it aesthetic.",
    "Donut": "You need a soft, frosted hug. No notes.",
    "Mochi ice cream": "Because cold, chewy joy exists... and it's this.",
    "Churros": "Your brain just yelled 'cinnamon sugar'. You're welcome.",
    "Es teler": "Fruit. Jelly. Avocado. Coconut. Ice. Sugar. Therapy, but edible.",
    "Kue cubit": "Half-baked like your energy levels.",
    "Roti bakar coklat keju": "When toast wants to party.",
    "Pisang goreng": "Banana. Fried. Period.",
    "Klepon": "Tiny bursts of joy—like hope, but chewy.",
    "Putri salju": "It melts away your stress. Almost.",
    "Sago gula melaka": "Gentle, sweet, and quiet. Like a warm nap."
    "Roti Bakar Kekinian": "This is toast that went to art school and got sponsored by Ovomaltine.",
}

savory_snack_dict = {
    "Sate Taichan": "Grilled, spicy, and commitment-free—just how you like your situationships.",
    "Seblak Jeletot": "Spicy noodle soup that fights back. If you cry, it’s working.",
    "Cilok Mozarella": "Chewy outside, cheesy core. Like a plot twist in snack form.",
    "Tahu Walik": "Tofu turned inside-out, deep-fried and thriving. We love a redemption arc.",
    "Ayam Geprek Keju": "Crispy, spicy, then smothered in cheese. It’s a hot mess you’ll keep coming back to.",
    "Cireng Bumbu Rujak": "Chewy tapioca with sweet-spicy sauce. Basically, emotional damage in snack form.",
    "Bakso Aci Kuah Pedas": "Chewy meatballs swimming in spicy broth. Basically, your comfort zone with drama.",
    "Mie Level": "Noodles that dare you to destroy your mouth. Spicy regrets guaranteed.",
    "Potato chips": "Because sometimes life is a little salty, and that’s okay.",
    "Lumpia goreng": "Crispy on the outside, productive on the inside.",
    "Popcorn": "Brain fuel. Movie not required.",
    "Chicken nuggets": "Adulting? Nah. You need crispy comfort in sauce form.",
    "Pempek": "Chewy, crispy, fried, and comes with spicy vinegar sauce. Don’t ask, just dip.",
    "Roti john": "An egg-meat-onion sandwich that tastes like late-night decisions. And we respect that.",
    "Tahu isi": "Tofu stuffed with vegetables and deep-fried. It’s protein with vibes.",
    "Nasi lemak bungkus": "Yes, it's technically a meal. But who’s checking?",
    "Telur gulung": "Rolled egg on a stick. With suspicious sauce that tastes like heaven. Roll with it.",
    "Martabak telur": "Heavy snack for a heavy brain.",
    "Tempe mendoan": "Softly fried, softly flavorful."
}
# Mood-to-snack mapping (feel free to add more for each)
mood_snack_map = {
    "✨ Magical": {
        "Sweet": ["Mochi ice cream", "Es teler","Dessert box","Mochi ice cream"],
        "Savory": ["Lumpia goreng", "Sate Taichan", "Tahu Walik"]
    },
    "😩 Burnt out": {
        "Sweet": ["Kue cubit", "Pisang goreng", "Donut", "Pisang Nugget", "Soft Baked Cookies"],
        "Savory": ["Pempek", "Martabak telur", "Tempe mendoan", "Ayam Geprek Keju", "Seblak Jeletot"]
    },
    "😐 Meh": {
        "Sweet": ["Matcha cookies", "Putri salju", "Puding Regal", "Roti bakar coklat keju"],
        "Savory": ["Potato chips", "Tahu isi", "Cireng Bumbu Rujak"]
    },
    "🧠 Hyperfocused": {
        "Sweet": ["Brown Sugar Boba Milk Cake", "Roti bakar coklat keju"],
        "Savory": ["Popcorn", "Cilok Mozarella"]
    },
    "😢 Sad": {
        "Sweet": ["Donut", "Korean Garlic Bread (Sweet)", "Klepon", "Roti Bakar Kekinian"],
        "Savory": ["Nasi lemak bungkus", "Tahu isi", "Bakso Aci Kuah Pedas"]
    },
    "😎 Unbothered": {
        "Sweet": ["Es teler", "Churros", "Martabak Manis Red Velvet"],
        "Savory": ["Roti john", "Chicken nuggets"]
    },
    "🤡 Delulu": {
        "Sweet": ["Klepon", "Mochi ice cream", "Dessert Box"],
        "Savory": ["Telur gulung", "Pempek", "Sate Taichan"]
    },
    "😵‍💫 Spiral Mode": {
        "Sweet": ["Putri salju", "Donut"],
        "Savory": ["Potato chips", "Martabak telur"]
    },
    "🥱 Just Here": {
        "Sweet": ["Pisang goreng", "Sago gula melaka", "Churros"],
        "Savory": ["Cilok Mozarella", "Tempe mendoan", "Telur gulung"]
    },
    "🤔 Existential Crunch": {
        "Sweet": ["Es teler", "Matcha cookies", "Puding Regal"],
        "Savory": ["Tahu isi", "Potato chips"]
    },
    "😴 Mentally Logged Out": {
        "Sweet": ["Putri salju", "Kue cubit", "Churros"],
        "Savory": ["Martabak telur", "Popcorn","Tahu Walik", "Bakso Aci Kuah Pedas"]
    },
    "🧃 Soft Mode": {
        "Sweet": ["Sago gula melaka", "Salted Egg Churros", "Putri salju"],
        "Savory": ["Tempe mendoan", "Sate Taichan", "Tahu Walik"]
    },
}

# Step 3: Suggest snack based on mood + flavor
if st.button("Gimme a snack suggestion 🍭"):
    # Try mood-specific suggestion
    snack_names = mood_snack_map.get(mood, {}).get(flavor)
    
    if snack_names:
        snack = random.choice(snack_names)
    else:
        # Fallback to general snack pool
        snack = random.choice(list(sweet_snack_dict.keys()) if flavor == "Sweet" else list(savory_snack_dict.keys()))
    
    # Get the reason from either dictionary
    reason = sweet_snack_dict.get(snack) or savory_snack_dict.get(snack)

    st.subheader(f"🥳 Your Snack Soulmate: **{snack}**")
    st.write(reason)
