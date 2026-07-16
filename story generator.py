import streamlit as st

st.set_page_config(
    page_title="Story Generator",
    page_icon="✍️",
    layout="centered",
)

def generate_story(topic, genre, length):
    topic = topic.strip() or "a mysterious kingdom"
    genre = genre.lower()

    base_story = (
        f"Once upon a time, {topic} became the center of a {genre} tale. "
        "Every shadow seemed to whisper, and every path promised a new surprise. "
        "The heroes followed clues through forgotten ruins and moonlit forests, "
        "learning that courage was often quieter than thunder. "
        "At dawn, the truth was revealed, and the world felt a little brighter "
        "for everyone who had taken the journey."
    )

    words = base_story.split()
    while len(words) < length:
        base_story = f"{base_story} {base_story}"
        words = base_story.split()

    return base_story

def main():
    st.title("AI makes mid stories")
    st.write("Generate creative stories with a lightweight local story builder.")

    topic = st.text_input(
        "Story topic",
        placeholder="Once upon a time there wasn't a princess",
    )

    genre = st.selectbox(
        "Genre",
        ["Adventure", "Fantasy", "Science fiction", "Mystery", "Comedy", "Horror"],
    )

    length = st.slider(
        "Story length (words)",
        min_value=100,
        max_value=1000,
        value=300,
        step=50,
    )

    if st.button("Generate mid story"):
        if not topic.strip():
            st.warning("Enter a topic")
            st.stop()

        with st.spinner("Writing your story..."):
            story = generate_story(topic, genre, length)

        st.subheader("Your mid story")
        st.write(story)

if __name__ == "__main__":
    main()
