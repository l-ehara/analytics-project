import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon=":wave:",
    layout="centered",
    initial_sidebar_state="auto",
)
left_col, center_col, right_col = st.columns([0.01 , 10, 0.01])

st.title("""Hello! :wave:""")

st.write("""Hello! I'm currently a 6th semester software engineering student and have always had a deep passion for software development. 
The journey of coding, creating, and watching a simple concept grow into a complex program truly captivates me. 
I have an insatiable curiosity for learning, constantly seeking to expand my skills and knowledge in various programming languages, 
software systems, and innovative technologies.

My academic experience has equipped me with a solid foundation in computer science and software engineering principles. 
Yet, it's not just the technical aspect of software development that draws me in; 
I am also fascinated by the role it plays in solving real-world problems and enhancing users' lives.

Looking forward, my ambition is to continually evolve in this ever-changing field of software development and data engineering, 
staying on top of current trends and advancements. My goal is to apply my passion and knowledge to a forward-thinking company, 
contributing to impactful projects that push boundaries and facilitate societal advancement.""")

st.write("""### Check out my [Linkedin Profile](https://www.linkedin.com/in/lucasehara/) and my [GitHub Profile](https://github.com/l-ehara/)""")
st.image("https://media.licdn.com/dms/image/D4D03AQEtawooWdSApw/profile-displayphoto-shrink_800_800/0/1707934962015?e=1715817600&v=beta&t=J9CqfBCJ3wvUMal7greS_4DwksOoTNn8telRKEXlarU", width= 250)


