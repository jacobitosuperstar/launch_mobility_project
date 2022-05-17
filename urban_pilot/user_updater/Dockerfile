FROM python:3.9 AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

FROM base AS python-deps

# instalando las dependencias
RUN pip install pipenv

# instalar las dependencias en /.venv
COPY Pipfile .
# COPY ./Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --skip-lock

FROM base AS runtime

COPY --from=python-deps .venv /.venv
ENV PATH="/.venv/bin:$PATH"

# crear y cambiarnos a un nuevo usuario
# RUN useradd --create-home appuser
# WORKDIR /home/appuser
# USER appuser
RUN mkdir appuser
WORKDIR /appuser

# copiar la apliación al contenedor
COPY . .

# Crear archivos logs
RUN touch /appuser/app.log

# Puerto que vamos a exponer
EXPOSE 5000
