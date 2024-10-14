class: center, middle, inverse

# Putting the workshop knowledge into practice

---

# Un tío/amigo/conocido te comenta una idea

Che, ¿no estaría bueno poder seguir cuánto está el dólar todos los días y guardar un registro?

Onda, cada día vemos a cuánto está el dólar y lo anotamos en algún lado, y después de un tiempo podemos ver cómo fue cambiando. Capaz podríamos hacer un gráfico o algo con eso.

Escuché que hay una página donde podés ver el valor del dólar, así que ni siquiera tendríamos que hacerlo a mano. 

Y bueno, como vos sabés de estas cosas de la compu, capaz podríamos armar algo que guarde los datos automáticamente y los suba a algún lado, así los podemos ver desde cualquier parte. ¿Te copa la idea? ¿Me ayudarías a hacerlo?

---

# Qué vimos en el taller?

- Con bash uno puede hacer scripts para automatizar tareas de todos los días, y existen muchos comandos que facilitan varias tareas.
- Usando git uno puede versionar archivos y carpetas, e incluso hacer un backup de ellas a un repositorio en la nube para acceder a esos archivos desde internet.
- Jupyter es una herramienta usada para reporting y presentación de datos

---

# Obteniendo los datos

- curl: `curl -s https://dolarapi.com/v1/dolares`
- jq:
  - `response=$(curl -s https://dolarapi.com/v1/dolares)` 
  - `# Process the JSON with jq to extract values (e.g., the 'dolar_blue' value)`
  - `dolar_value=$(echo "$response" | jq -r '.dolares.blue.value')`
- date:
  - `timestamp=$(date +"%Y-%m-%d %H:%M:%S")`

---

# Mostrando los datos

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('dolar_values.csv', names=['Timestamp', 'Dollar_Value'])

# Convert the Timestamp column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Dollar_Value'], marker='o')
plt.title('Daily Dollar Value Over Time')
plt.xlabel('Date')
plt.ylabel('Dollar Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

# Subiendo todo a internet

- git:

```bash
# Run the Jupyter notebook to update graphs/tables
jupyter nbconvert --execute --to notebook --inplace notebook.ipynb

# Git: Add, commit, and push the updated CSV and notebook to GitHub
git add dolar_values.csv notebook.ipynb
git commit -m "Update dolar values and notebook on $timestamp"
git push origin main  # Change 'main' to your branch name if necessary
```

---

# Corriendo el script todos los días

- cronjob

```bash
crontab -e
0 8 * * * /path/to/your/script/fetch_dolar.sh
```

---

# Cronjob

Un cron job es una tarea o script programado para ejecutarse automáticamente a intervalos específicos en sistemas operativos tipo Unix (como Linux o macOS). Es un programador de tareas basado en tiempo que automatiza tareas repetitivas, como:

- Realizar copias de seguridad
- Enviar notificaciones
- Obtener datos de APIs
- Ejecutar scripts a intervalos regulares

El cron job utiliza el demonio cron, un servicio en segundo plano que revisa la tabla de cron (crontab) para ejecutar las tareas.

---

# Sintaxis

```bash
*    *    *    *    *   comando-a-ejecutar
-    -    -    -    -
|    |    |    |    |
|    |    |    |    ----- Día de la semana (0-7) (Domingo = 0 o 7)
|    |    |    ------- Mes (1-12)
|    |    -------- Día del mes (1-31)
|    ---------- Hora (0-23)
------------ Minuto (0-59)
```

```bash
# Este cron job ejecuta un script todos los días a las 2:30 AM.
30 2 * * * /ruta/al/script.sh
```

--- 

# Ejemplos comúnes de cronjob

```bash
0 7 * * * /home/usuario/tarea-diaria.sh # Este cron job se ejecuta todos los días a las 7:00 AM.

15 10 * * 1 /home/usuario/tarea-semanal.sh # Este cron job se ejecuta todos los lunes a las 10:15 AM.

*/5 * * * * /home/usuario/tarea-frecuente.sh # Este cron job se ejecuta cada 5 minutos.
```

---

# Configurar un cronjob

```bash
# abrir el crontab
crontab -e
```

- **Agregar un Cron Job:** Simplemente agrega la hora y el comando que quieres programar, siguiendo la estructura mencionada anteriormente.
- **Guardar y Salir:** Guarda el archivo y el cron job se registrará y comenzará a ejecutarse según lo programado.
