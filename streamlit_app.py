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
    "Chocolate-covered almonds": "You deserve something fancy *and* efficient.",
    "Matcha cookies": "A little green energy, but make it aesthetic.",
    "Donut": "You need a soft, frosted hug. No notes.",
    "Mochi ice cream": "Because cold, chewy joy exists... and it's this.",
    "Churros": "Your brain just yelled 'cinnamon sugar'. You're welcome.",
    "Es teler": "Fruit. Jelly. Avocado. Coconut. Ice. Sugar. Therapy, but edible.",
    "Kue cubit": "Half-baked like your energy levels.",
    "Roti bakar coklat keju": "When toast wants to party.",
    "Pisang goreng": "Banana. Fried. Period.",
    "Klepon": "Tiny bursts of joy—like hope, but chewy.",
    "Kuih seri muka": "Layered like your problems. Still tasty.",
    "Kuih talam": "Do we exist? At least this does.",
    "Putri salju": "It melts away your stress. Almost.",
    "Sago gula melaka": "Gentle, sweet, and quiet. Like a warm nap."
}

savory_snack_dict = {
    "Potato chips": "Because sometimes life is a little salty, and that’s okay.",
    "Mini spring rolls": "Crispy on the outside, productive on the inside.",
    "Cheese cubes": "You’re too tired to cook, but not too tired for cheese.",
    "Popcorn": "Brain fuel. Movie not required.",
    "Chicken nuggets": "Adulting? Nah. You need crispy comfort in sauce form.",
    "Pempek": "Chewy, crispy, fried, and comes with spicy vinegar sauce. Don’t ask, just dip.",
    "Roti john": "An egg-meat-onion sandwich that tastes like late-night decisions. And we respect that.",
    "Tahu isi": "Tofu stuffed with vegetables and deep-fried. It’s protein with vibes.",
    "Karipap": "A curry puff that’s flaky, spicy, and judgment-free.",
    "Nasi lemak bungkus": "Yes, it's technically a meal. But who’s checking?",
    "Telur gulung": "Rolled egg on a stick. With suspicious sauce that tastes like heaven. Roll with it.",
    "Martabak telur": "Heavy snack for a heavy brain.",
    "Tempe mendoan": "Softly fried, softly flavorful."
}
# Mood-to-snack mapping (feel free to add more for each)
mood_snack_map = {
    "✨ Magical": {
        "Sweet": ["Mochi ice cream", "Es teler", "Chocolate-covered almonds"],
        "Savory": ["Mini spring rolls", "Karipap"]
    },
    "😩 Burnt out": {
        "Sweet": ["Kue cubit", "Pisang goreng", "Donut"],
        "Savory": ["Pempek", "Martabak telur", "Tempe mendoan"]
    },
    "😐 Meh": {
        "Sweet": ["Matcha cookies", "Putri salju"],
        "Savory": ["Potato chips", "Tahu isi"]
    },
    "🧠 Hyperfocused": {
        "Sweet": ["Chocolate-covered almonds", "Roti bakar coklat keju"],
        "Savory": ["Popcorn", "Cheese cubes"]
    },
    "😢 Sad": {
        "Sweet": ["Donut", "Kuih talam", "Klepon"],
        "Savory": ["Nasi lemak bungkus", "Tahu isi"]
    },
    "😎 Unbothered": {
        "Sweet": ["Es teler", "Churros"],
        "Savory": ["Roti john", "Chicken nuggets"]
    },
    "🤡 Delulu": {
        "Sweet": ["Klepon", "Mochi ice cream", "Kuih seri muka"],
        "Savory": ["Telur gulung", "Pempek"]
    },
    "😵‍💫 Spiral Mode": {
        "Sweet": ["Kuih seri muka", "Donut"],
        "Savory": ["Karipap", "Martabak telur"]
    },
    "🥱 Just Here": {
        "Sweet": ["Pisang goreng", "Sago gula melaka"],
        "Savory": ["Cheese cubes", "Tempe mendoan"]
    },
    "🤔 Existential Crunch": {
        "Sweet": ["Kuih talam", "Matcha cookies"],
        "Savory": ["Tahu isi", "Potato chips"]
    },
    "😴 Mentally Logged Out": {
        "Sweet": ["Putri salju", "Kue cubit", "Churros"],
        "Savory": ["Martabak telur", "Popcorn"]
    },
    "🧃 Soft Mode": {
        "Sweet": ["Sago gula melaka", "Kuih seri muka", "Putri salju"],
        "Savory": ["Tempe mendoan", "Cheese cubes"]
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
