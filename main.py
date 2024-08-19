from fasthtml.common import (
    fast_app,
    serve,
    Container,
    Div,
    H2,
    H3,
    Article,
    H1,
    Ul,
    Li,
    A,
    P,
    Main,
    Nav,
    Form,
    Fieldset,
    Label,
    Input,
    Textarea,
    Card,
)

app, rt = fast_app(live=True)

paragraph_1 = """
Hello! I'm rhodlib, a technology enthusiast with over 3 years of experience in web and mobile development. My journey in the programming world began with a passion for JavaScript and Python, and over the years, I've had the privilege of working on innovative projects that have honed my ability to create efficient and elegant solutions.
"""
paragraph_2 = """
I currently work at a company, where we're developing B2B software that's transforming the way businesses manage their operations. In this exciting environment, I work with a robust tech stack that includes React for frontend development and Django along with Django REST framework for backend development. These frameworks enable me to build fast, secure, and highly scalable web applications.
"""

paragraph_3 = """
In addition, I use Docker to streamline and manage our development and deployment processes, ensuring consistent environments and efficient workflows. I also have experience with TanStack for effective state management in React applications and we use Tailwind CSS to create modern and visually appealing user interfaces. My interests also extend to mobile development, where I've used React Native to build mobile applications that deliver a smooth and native user experience across different platforms.
"""

paragraph_4 = """
My approach to technology is driven by curiosity and a constant desire to learn and improve. I'm passionate about solving complex problems and exploring new tools that can elevate projects to the next level. If you're interested in learning more about my work or collaborating on a project, feel free to reach out.
"""


def HomeView():
    return Div(
        H2("Welcome to my website"),
        Article(P(paragraph_1), P(paragraph_2), P(paragraph_3), P(paragraph_4)),
    )


def ProjectView():
    return Div(
        H2("Projects"),
        Div(
            Card(
                H3("MMO Project"),
                P(
                    "This project is under construction; it is an MMO that will be played through the browser. More updates coming soon."
                ),
            ),
            Card(
                H3("The Weirdos"),
                P(
                    "The Weirdos is a blog where we talk about technology, anime, series, movies, video games, and life topics. A podcast will be added soon."
                ),
                A("Link to the Weirdos", href="https://theweirdos.substack.com/"),
            ),
        ),
    )


def ContactMeView():
    return Div(
        H2("Contact Me"),
        Form(
            Fieldset(
                Label("Fullname", Input()),
                Label("Email", Input()),
                Label("Subject", Input()),
                Label("Mensaje", Textarea()),
            ),
            Input(type="submit"),
        ),
    )


def NavComponent():
    return Nav(
        H1("Rodo Talibs"),
        Ul(
            Li(A("Home", hx_get=("/"), hx_target="main")),
            Li(A("Projects", hx_get="/projects", hx_target="main")),
            Li(A("Contact Me", hx_get="/contact", hx_target="main")),
        ),
    )


@rt("/")
def get():
    return Container(NavComponent(), Main(HomeView(), id="main"))


@rt("/projects")
def get():
    return Container(
        NavComponent(),
        ProjectView(),
    )


@rt("/contact")
def get():
    return Container(NavComponent(), ContactMeView())


serve()
