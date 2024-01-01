import os
from jinja2 import Environment, FileSystemLoader

def render_template(template_content, context):
    # Create a Jinja2 environment and specify the loader
    env = Environment(loader=FileSystemLoader(searchpath="./"))

    # Create a template from the provided content
    template = env.from_string(template_content)

    # Render the template with the given context
    rendered_content = template.render(context)

    return rendered_content

def render_and_save_html_files(directory, context):
    # Get a list of HTML files in the specified directory
    html_files = ["index.html", "getting-started/index.html", "getting-started/introduction/index.html", "getting-started/introduction/accessing-variables.html", "getting-started/introduction/accounts.html", "getting-started/introduction/setting-variables.html"]

    # Determine the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Loop through each HTML file
    for filename in html_files:
        # Construct the full path to the template file
        template_path = os.path.join(script_directory, directory, filename)

        # Read the content of the original file
        with open(template_path, 'r') as file:
            original_content = file.read()

        # Render the template
        rendered_content = render_template(original_content, context)

        # Save the rendered content back to the original file
        with open(template_path, 'w') as file:
            file.write(rendered_content)

if __name__ == "__main__":
    # Set your context data
    context_data = {
    "components": {
        "navbar": """
    <!-- Navigation -->
    <nav data-bs-theme="dark" class="navbar navbar-expand-lg bg-body-tertiary">
        <a style="margin-right: 5px;" class="navbar-brand" href="/">
            <img id="navbar-img" src="/LOGO.jpg" height="50px" width="50px">
            EnvHub
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/getting-started">Getting Started</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/dashboard">Dashboard</a>
                </li>
            </ul>
        </div>
        <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
    </nav>
        """,

        "sidebar": """
    <!-- Sidebar -->
    <div id="sidebar">
        <h2>Pages</h2>
        <ul>
            <li><a href="/getting-started">Overview</a></li>
            <li>
                <a href="/getting-started/introduction">Introduction</a>
                <ul>
                    <li><a href="/getting-started/introduction/accounts">Accounts</a></li>
                    <li><a href="/getting-started/introduction/setting-variables">Setting Variables</a></li>
                    <li><a href="/getting-started/introduction/accessing-variables">Accessing Variables</a></li>
                </ul>
            </li>
        </ul>
    </div>
        """
    }
}
    # Specify pages the directory containing your HTML files
    pages_directory = "pages"

    # Render and save HTML files
    render_and_save_html_files(pages_directory, context_data)

    
    
