import os
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

# Load environment variables from .env file
load_dotenv()

# Load the variables from the .env file
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_port = os.getenv('POSTGRES_PROD_PORT')

clickhouse_user = os.getenv('CLICKHOUSE_USER')
clickhouse_password = os.getenv('CLICKHOUSE_PASSWORD')
clickhouse_port = os.getenv('CLICKHOUSE_PORT_1')

# Define the template directory and file
template_dir = os.path.dirname(os.path.abspath(__file__))
template_file = 'credentials_render.yaml'

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Load the template file
template = env.get_template(template_file)

# Render the template with the variables
rendered_yaml = template.render(POSTGRES_USER=postgres_user, 
				POSTGRES_PASSWORD=postgres_password,
				POSTGRES_PROD_PORT=postgres_port,
				CLICKHOUSE_USER=clickhouse_user,
				CLICKHOUSE_PASSWORD=clickhouse_password,
				CLICKHOUSE_PORT_1=clickhouse_port)

# Save the rendered YAML to a new file
with open('credentials.yaml', 'w') as output_file:
    output_file.write(rendered_yaml)

print("YAML file generated successfully!")
