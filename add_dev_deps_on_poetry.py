import subprocess

# Path to the .dev file
dev_file = "requirements.txt.dev"

# Read the .dev file
with open(dev_file, "r") as file:
    dependencies = [line.strip() for line in file if line.strip()]

# Add each dependency to the dev group in Poetry
for dependency in dependencies:
    try:
        print(f"Adding {dependency} to the dev group...")
        command=f"poetry add --group dev {dependency}"
        subprocess.run(["poetry", "add", "--group", "dev", dependency], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to add {dependency}: {e}")
