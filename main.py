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
    Button,
    Title,
    Meta,
    Favicon,
    Img,
)

description = (
    "Rodolfo Talibs Website, Web developer with experience in JavaScript & Python."
)

hdrs = [
    Meta(charset="UTF-8"),
    Meta(
        name="viewport",
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
    ),
    Meta(name="description", content=description),
    *Favicon("/favicon.ico", "/favicon.ico"),
]

app, rt = fast_app(live=True, hdrs=hdrs)

_blank = dict(target="_blank", rel="noopener noreferrer")

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
    return (
        H2("Welcome to my website", style=dict({"text-align": "center"})),
        Article(
            P(paragraph_1),
            P(paragraph_2),
            P(paragraph_3),
            P(paragraph_4),
        ),
    )


def ProjectView():
    return Div(
        H2("Projects", style=dict({"text-align": "center"})),
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
                A(
                    "The Weirdos Blog",
                    hx_replace_url="https://theweirdos.substack.com/",
                    **_blank,
                ),
            ),
        ),
    )


def ContactMeView():
    return Div(
        H2("Contact Me", style=dict({"text-align": "center"})),
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
        H1("Rodo Talibs", style=dict({"margin": "0px"})),
        Ul(
            Li(A("Home", hx_get=("/"), hx_target="main")),
            Li(A("Projects", hx_get="/projects", hx_target="main")),
            Li(Button("Contact Me", hx_get="/contact", hx_target="main")),
        ),
        style=dict(
            {
                "display": "flex",
                "align-items": "center",
            }
        ),
    )


@rt("/")
def get():
    return (
        Title("Rodo Talibs - Web developer"),
        Container(
            NavComponent(),
            Main(HomeView(), id="main", style=dict({"padding-top": "30px"})),
        ),
    )


@rt("/projects")
def get():
    return Container(
        NavComponent(), Main(ProjectView(), style=dict({"padding-top": "30px"}))
    )


@rt("/contact")
def get():
    return Container(
        NavComponent(), Main(ContactMeView(), style=dict({"padding-top": "30px"}))
    )


serve()
