

# Part-of-Speech Tagging para el quechua

Este repositorio proporciona el modelo POS-Tagging para la lengua quechua sureño. El modelo es una mejora del modelo POS-Tagging presentado por [Llamacha](https://aclanthology.org/2022.deeplo-1.1/). 

# Instalación


Se debe crear un entorno virtual e instalar las librerías de requerimiento
```
python -m venv venv
source venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

# Forma de usar

```
usage: POS-Tagging quechua sureño

required arguments:
  -t root_train, --train root_train
                        Dataset de entrenamiento en formato csv.
  -e root_eval, --evaluation root_eval
                        Dataset de evaluación en formato csv.
  -o root_output, --output root_output
                        Dirección de la salida del proceso.

optional arguments:
  -h, --help            show help message and exit

  -u root_text, --usage root_text
                        Archivo quechua a procesar.
  -i, --interactive     Interactuar con el modelo NER desde consola
```

## Modo interactivo

En este modo se puede interactuar mediante linea de comandos para reconocer el Part-of-Speech del texto.

```
python src/main.py -i
```

## Procesar un archivo csv


```
python src/main.py -u pos_quechua/resources/data.csv -o pos_quechua/results/
```

## Entrenar nuevo modelo POS-Tagging

```
python src/main.py -t pos_quechua/resources/train_qu_pos.csv -e pos_quechua/resources/test_qu_pos.csv -o pos_quechua/results/
```
