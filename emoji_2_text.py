import emoji

# -------------------------------
# 1. Basic Emoji Conversion
# -------------------------------
text_with_emoji = "Hello 😊! How are you? 👍"

converted_text = emoji.demojize(text_with_emoji)


# -------------------------------
# 2. Multilingual (Spanish) Conversion
# -------------------------------
# emoji.demojize() does not directly translate emoji names
# into Spanish, so we use a simple replacement dictionary.
spanish_emoji = {
    "😊": "sonriendo",
    "👍": "pulgar arriba",
    "❤️": "corazón",
    "😂": "cara riendo con lágrimas",
    "😢": "cara llorando",
    "🔥": "fuego",
    "🎉": "fiesta",
    "🚀": "cohete"
}

spanish_converted_text = text_with_emoji

for emj, spanish_name in spanish_emoji.items():
    spanish_converted_text = spanish_converted_text.replace(
        emj, f"[{spanish_name}]"
    )


# -------------------------------
# 3. Extended Emoji Conversion
# -------------------------------
many_emojis = "😀 😃 😄 😁 😆 😅 😂 🤣 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 ❤️ 👍 👎 🔥 🎉 🚀"

converted_many_emojis = emoji.demojize(many_emojis)


# -------------------------------
# 4. Interactive Input
# -------------------------------
user_emoji_input = input("Enter some text with emojis: ")

user_converted_text = emoji.demojize(user_emoji_input)

print(f"\nYour original input: {user_emoji_input}")
print(f"Converted text: {user_converted_text}")


# -------------------------------
# 5. Save Results to File
# -------------------------------
output_filename = "emoji_conversion_results.txt"

with open(output_filename, "w", encoding="utf-8") as f:

    f.write("--- Emoji to Text Conversion Results ---\n\n")

    f.write("1. Basic Conversion:\n")
    f.write(f"Original: {text_with_emoji}\n")
    f.write(f"Converted: {converted_text}\n\n")

    f.write("2. Multilingual (Spanish) Conversion:\n")
    f.write(f"Original: {text_with_emoji}\n")
    f.write(f"Converted (Spanish): {spanish_converted_text}\n\n")

    f.write("3. Extended Emoji Conversion:\n")
    f.write(f"Original (partial): {many_emojis[:100]}...\n")
    f.write(f"Converted: {converted_many_emojis}\n\n")

    f.write("4. Interactive Input Conversion:\n")
    f.write(f"Original: {user_emoji_input}\n")
    f.write(f"Converted: {user_converted_text}\n\n")


print(f"\nAll converted results have been exported to '{output_filename}'")