import os
import subprocess
import sys

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jinja2'])

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
    html_files = ["index", "getting-started/index", "getting-started/introduction/index", "getting-started/introduction/accessing-variables", "getting-started/introduction/accounts", "getting-started/introduction/setting-variables"]

    # Determine the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Loop through each HTML file
    for filename in html_files:
        # Construct the full path to the template file
        template_path = os.path.join(script_directory, directory, filename + ".jinja")
        html_template_path = os.path.join(script_directory, directory, filename + ".html")

        # Read the content of the original file
        with open(template_path, 'r') as file:
            original_content = file.read()

        # Render the template
        rendered_content = render_template(original_content, context)

        # Save the rendered content back to the original file
        with open(html_template_path, 'w') as file:
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
    <div data-bs-theme="dark" id="sidebar">

        <ul class="list-group">
            <li class="list-group-item"><a href="/getting-started">
                    <svg height=16px width=16px xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                        <path fill="#ffa500"
                            d="M288 80c-65.2 0-118.8 29.6-159.9 67.7C89.6 183.5 63 226 49.4 256c13.6 30 40.2 72.5 78.6 108.3C169.2 402.4 222.8 432 288 432s118.8-29.6 159.9-67.7C486.4 328.5 513 286 526.6 256c-13.6-30-40.2-72.5-78.6-108.3C406.8 109.6 353.2 80 288 80zM95.4 112.6C142.5 68.8 207.2 32 288 32s145.5 36.8 192.6 80.6c46.8 43.5 78.1 95.4 93 131.1c3.3 7.9 3.3 16.7 0 24.6c-14.9 35.7-46.2 87.7-93 131.1C433.5 443.2 368.8 480 288 480s-145.5-36.8-192.6-80.6C48.6 356 17.3 304 2.5 268.3c-3.3-7.9-3.3-16.7 0-24.6C17.3 208 48.6 156 95.4 112.6zM288 336c44.2 0 80-35.8 80-80s-35.8-80-80-80c-.7 0-1.3 0-2 0c1.3 5.1 2 10.5 2 16c0 35.3-28.7 64-64 64c-5.5 0-10.9-.7-16-2c0 .7 0 1.3 0 2c0 44.2 35.8 80 80 80zm0-208a128 128 0 1 1 0 256 128 128 0 1 1 0-256z" />
                    </svg>
                    Overview
                </a></li>
            <li class="list-group-item">
                <a href="/getting-started/introduction">
                    <svg height=20px width=20px class="svg-icon"
                        style="width: 1em; height: 1em;vertical-align: middle;fill: #87CEEB;overflow: hidden;"
                        viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M512 938.666667c-25.6 0-42.666667-17.066667-42.666667-42.666667 0-46.933333-38.4-85.333333-85.333333-85.333333H85.333333c-25.6 0-42.666667-17.066667-42.666666-42.666667V128c0-25.6 17.066667-42.666667 42.666666-42.666667h256c119.466667 0 213.333333 93.866667 213.333334 213.333334v597.333333c0 25.6-17.066667 42.666667-42.666667 42.666667z m-384-213.333334h256c29.866667 0 59.733333 8.533333 85.333333 21.333334V298.666667c0-72.533333-55.466667-128-128-128H128v554.666666z" />
                        <path
                            d="M512 938.666667c-25.6 0-42.666667-17.066667-42.666667-42.666667V298.666667c0-119.466667 93.866667-213.333333 213.333334-213.333334h256c25.6 0 42.666667 17.066667 42.666666 42.666667v640c0 25.6-17.066667 42.666667-42.666666 42.666667h-298.666667c-46.933333 0-85.333333 38.4-85.333333 85.333333 0 25.6-17.066667 42.666667-42.666667 42.666667z m170.666667-768c-72.533333 0-128 55.466667-128 128v448c25.6-12.8 55.466667-21.333333 85.333333-21.333334h256V170.666667h-213.333333z" />
                    </svg>
                    Introduction
                </a>
                <ul class="list-group">
                    <li class="list-group-item"><a href="/getting-started/introduction/accounts">
                            <svg height=16px width=16px xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 448 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                <path fill="#11ba16"
                                    d="M304 128a80 80 0 1 0 -160 0 80 80 0 1 0 160 0zM96 128a128 128 0 1 1 256 0A128 128 0 1 1 96 128zM49.3 464H398.7c-8.9-63.3-63.3-112-129-112H178.3c-65.7 0-120.1 48.7-129 112zM0 482.3C0 383.8 79.8 304 178.3 304h91.4C368.2 304 448 383.8 448 482.3c0 16.4-13.3 29.7-29.7 29.7H29.7C13.3 512 0 498.7 0 482.3z" />
                            </svg>
                            Accounts
                        </a></li>
                    <li class="list-group-item"><a href="/getting-started/introduction/setting-variables">
                            <svg height=16px width=16px class="svg-icon"
                                style="vertical-align: middle;fill: #808080;overflow: hidden;" viewBox="0 0 1024 1024"
                                version="1.1" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M725.333333 597.333333c-42.666667 0-85.333333-8.533333-128-29.866667-21.333333-8.533333-29.866667-34.133333-21.333333-55.466667 8.533333-21.333333 34.133333-29.866667 55.466667-21.333333 81.066667 38.4 179.2 21.333333 243.2-42.666667 34.133333-34.133333 55.466667-76.8 59.733333-119.466667L904.533333 298.666667l-119.466667 119.466667c-8.533333 8.533333-17.066667 12.8-29.866667 12.8-8.533333 0-81.066667 0-119.466667-42.666667-42.666667-42.666667-42.666667-110.933333-42.666667-119.466667 0-12.8 4.266667-21.333333 12.8-29.866667L725.333333 119.466667l-29.866667-29.866667c-46.933333 4.266667-89.6 25.6-119.466667 59.733333-64 64-81.066667 162.133333-42.666667 243.2 8.533333 21.333333 0 46.933333-21.333333 55.466667-21.333333 8.533333-46.933333 0-55.466667-21.333333-55.466667-115.2-29.866667-251.733333 59.733333-341.333333 51.2-51.2 119.466667-81.066667 196.266667-85.333333 12.8 0 25.6 4.266667 34.133333 12.8l72.533333 72.533333c17.066667 17.066667 17.066667 42.666667 0 59.733333l-136.533333 136.533333c4.266667 17.066667 8.533333 34.133333 17.066667 42.666667 8.533333 8.533333 29.866667 12.8 42.666667 17.066667l136.533333-136.533333c17.066667-17.066667 42.666667-17.066667 59.733333 0l72.533333 72.533333C1019.733333 290.133333 1024 302.933333 1024 315.733333c-4.266667 72.533333-34.133333 140.8-85.333333 196.266667C878.933333 567.466667 802.133333 597.333333 725.333333 597.333333z" />
                                <path
                                    d="M785.066667 162.133333c-12.8 0-21.333333-4.266667-29.866667-12.8L695.466667 85.333333c-17.066667-17.066667-17.066667-42.666667 0-59.733333 17.066667-17.066667 42.666667-17.066667 59.733333 0l59.733333 59.733333c17.066667 17.066667 17.066667 42.666667 0 59.733333C806.4 157.866667 797.866667 162.133333 785.066667 162.133333z" />
                                <path
                                    d="M968.533333 341.333333c-12.8 0-21.333333-4.266667-29.866667-12.8l-59.733333-59.733333c-17.066667-17.066667-17.066667-42.666667 0-59.733333s42.666667-17.066667 59.733333 0l59.733333 59.733333c17.066667 17.066667 17.066667 42.666667 0 59.733333C989.866667 337.066667 977.066667 341.333333 968.533333 341.333333z" />
                                <path
                                    d="M128 1024c-34.133333 0-64-12.8-89.6-38.4-51.2-51.2-51.2-132.266667 0-179.2l426.666667-426.666667c17.066667-17.066667 42.666667-17.066667 59.733333 0 17.066667 17.066667 17.066667 42.666667 0 59.733333l-426.666667 426.666667c-17.066667 17.066667-17.066667 42.666667 0 59.733333 17.066667 17.066667 42.666667 17.066667 59.733333 0l426.666667-426.666667c17.066667-17.066667 42.666667-17.066667 59.733333 0s17.066667 42.666667 0 59.733333l-426.666667 426.666667C192 1011.2 162.133333 1024 128 1024z" />
                            </svg>
                            Setting Variables
                        </a></li>
                    <li class="list-group-item"><a href="/getting-started/introduction/accessing-variables">
                            <svg height=20px width=20px class="svg-icon"
                                style="vertical-align: middle;fill: #FFD700;overflow: hidden;" viewBox="0 0 1024 1024"
                                version="1.1" xmlns="http://www.w3.org/2000/svg">
                                <path d="M893.456828 709.055005" />
                                <path d="M491.889987 337.939709" />
                                <path d="M568.154951 338.993714" />
                                <path
                                    d="M953.576067 767.43974 587.612095 396.544455c35.753295-95.363951 15.47239-200.659089-55.477522-271.613094C483.524458 76.321246 419.484933 49.5403 350.739223 49.5403c-68.750827 0-133.084041 26.779923-181.694155 75.391061C120.428813 173.542498 93.803409 238.174518 93.803409 306.931484c0 68.74571 26.849508 133.378753 75.465762 181.988868 49.374524 49.384757 116.001991 75.93546 183.428659 75.924203 24.37106 0 48.836265-3.697205 72.655763-10.80816l110.324688 110.550839c3.227508 3.233648 7.235798 5.191232 11.417027 5.929036 1.566682 0.551562 3.195785 0.981351 4.92108 1.156336l52.467979 5.368264 5.406127 54.031591c0.988514 9.858532 8.613168 17.759479 18.434861 19.098987l55.110155 7.503904 4.117784 49.835012c0.408299 4.939499 2.517333 9.586332 5.969968 13.144368l109.777219 113.25953c1.425466 1.826602 3.082198 3.461845 5.019317 4.746094 3.852748 3.00852 8.458649 2.309602 13.113669 2.309602 2.12643 0 4.231371-3.330862 6.284123-3.330862l114.27465 0c17.638729 0 18.584264-6.043646 18.584264-23.844058L960.576505 800.865014C960.576505 794.387485 964.219475 778.167059 953.576067 767.43974zM917.597645 894.660236l-88.098477 0L729.638809 793.982256l-4.90266-58.161654c-0.826831-10.015098-8.507768-17.527189-18.46556-18.876929l-55.407937-7.251148-5.462408-54.480822c-1.01512-10.130731-9.021467-18.083867-19.151176-19.10922l-64.974827-6.600325L446.571848 514.572592c-6.060019-6.075369-14.842033-7.682983-22.413476-4.962012l-0.019443-0.048095c-77.515445 27.92091-165.615968 7.91425-224.487797-50.952462-40.515762-40.510646-62.833047-94.383624-62.833047-151.680585 0-57.307194 22.317285-111.170962 62.833047-151.691841s94.385671-62.832024 151.686724-62.832024c57.296961 0 111.165846 22.312168 151.686724 62.833047 58.774615 58.779731 76.608795 146.175197 47.124274 225.605248-1.157359 0.769526-2.26253 1.653663-3.285836 2.670829-8.398274 8.340969-8.445346 21.914102-0.104377 30.30726L921.909857 796.439214c0.25071 0.952698-4.312212 2.605338-4.312212 4.426823L917.597645 894.660236 917.597645 894.660236z" />
                                <path
                                    d="M301.221436 174.36933c-41.36306 0-75.014484 33.655518-75.014484 75.014484s33.650401 75.014484 75.014484 75.014484 75.014484-33.655518 75.014484-75.014484S342.584496 174.36933 301.221436 174.36933zM301.221436 281.532001c-17.727757 0-32.149211-14.421454-32.149211-32.149211s14.421454-32.149211 32.149211-32.149211 32.149211 14.421454 32.149211 32.149211C333.370647 267.110547 318.949192 281.532001 301.221436 281.532001z" />
                            </svg>
                            Accessing Variables
                        </a></li>
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

    
    
