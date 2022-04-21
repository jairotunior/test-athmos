# Test

Esta es la solucion para la prueba propuesta.

## Configuarion

Las siguientes instrucciones permitiran tener el proyecto configurado.

### Instalación

1. Crear un entorno virtual.
2. Copiar el repositorio https://github.com/jairotunior/test-athmos.git
3. Instalar las dependencias.

```
pip install -r requerimientos.txt
```

Esto es todo!!!

### Exercise 1

Como primer paso se necesita iniciar InfluxDB (Base de Datos de Serie de tiempo) que se encargara de guardas los datos provenientes del webservice.

```
bash run_influxdb.sh
```

Con la finalidad de cumplir el proposito del problema de la mejor manera posible se divide el problema en 2 partes. La primera parte es la captura de datos (exercise1_ws.py) y la segunda parte (exercise1_process.py) es el procesamiento de datos.

```
bash run_exercise1_ws.sh
```

En otra terminal se ejecuta el proceso de procesamiento de datos.

```
bash run_exercise1_process.sh
```

### Exercise 2

Para usar la CLI con las caracteristicas solicitadas ejecutar el comando.

```
python exercise2.py -h
```

Si se desea ejecutar una prueba unitaria para la CLI se debe correr el siguiente comando.

```
bash run_test.py -h
```


## Built With

* [Pandas](https://pandas.pydata.org) - Is the fundamental package for scientific computing with Python.
* [Python](https://www.python.org/) - Programming Language.
* [Docker](https://www.docker.com) - Container system.
* [InfluxDB](https://www.influxdata.com) - Time Series Database.

