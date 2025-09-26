# Use Miniconda as the base image
FROM continuumio/miniconda3:latest

# Set working directory inside the container
WORKDIR /app

# Copy the conda environment file into the container
COPY environment.yml .

# Create the conda environment
RUN conda env create -f environment.yml

# Make commands use the new environment
SHELL ["conda", "run", "-n", "riveterEnv", "/bin/bash", "-c"]

# Copy your notebooks and code
COPY . .

# Expose Jupyter Notebook port
EXPOSE 8888

# Default command: run Jupyter Notebook
CMD ["conda", "run", "-n", "riveterEnv", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
