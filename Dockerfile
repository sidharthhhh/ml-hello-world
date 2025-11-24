# 1. Base Image
# We use 'slim' to avoid the 1GB+ bloat of the full python image.
# It strips out GUI tools/compilers we don't need for runtime.
FROM python:3.11-slim

# 2. Set Working Directory
WORKDIR /app

# 3. Install Dependencies
# We copy requirements FIRST to leverage Docker Layer Caching.
# If you change code (main.py) but not requirements, this step is skipped.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Application & Artifacts
# We copy the API code (main.py) AND the trained model (iris_model.pkl).
# In a real pipeline, the .pkl might be downloaded from S3/Azure Blob here.
COPY main.py .
COPY iris_model.pkl .

# 5. Expose Port
EXPOSE 8000

# 6. Start Command
# --host 0.0.0.0 is CRITICAL. 
# If you leave it default (127.0.0.1), Docker won't expose it outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]