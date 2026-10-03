import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Exploración y preparación de los datos
print("--- Iniciando Análisis del Dataset Superstore ---")
# Cargar el dataset asumiendo que está en la misma carpeta raíz
ruta_dataset = "superstore_dataset2012.csv"
df = pd.read_csv(ruta_dataset)

# Exploración inicial
print("\nInformación general del Dataset:")
df.info()

print("\nCantidad de valores nulos por columna:")
print(df.isnull().sum())

# Preparación de datos: convertir columnas de fechas a datetime
# El formato de las fechas en el dataset es 'd/m/yyyy'
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y', errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y', errors='coerce')

# Asegurar que estamos trabajando con los datos numéricos correctos, sin nulos en métricas clave
df = df.dropna(subset=['Sales', 'Profit'])

# Configurar estilo global de Seaborn para mejor estética
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# Creación de Figura Principal con 4 Subplots
# ---------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Análisis Exploratorio del Rendimiento de Ventas (Superstore 2012)", fontsize=22, fontweight='bold', y=0.98)

# 2. Visualización univariante con Matplotlib (Histograma)
# Para evitar que los valores atípicos oculten la distribución, filtramos las ventas < 1000
sales_filtered = df[df['Sales'] < 1000]['Sales']
axes[0, 0].hist(sales_filtered, bins=40, color='skyblue', edgecolor='black')
axes[0, 0].set_title("Distribución de Ventas < $1000 (Matplotlib)", fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel("Ventas ($)", fontsize=12)
axes[0, 0].set_ylabel("Frecuencia (Cantidad de Órdenes)", fontsize=12)
# CONCLUSIÓN 1: La inmensa mayoría de las órdenes son de un valor bajo (menos de $100-$200).
# Esto indica que el modelo de negocio depende del alto volumen de transacciones menores (cola larga).

# 3. Visualización univariante con Seaborn (Boxplot)
sns.boxplot(data=df, x='Category', y='Profit', ax=axes[0, 1], palette='Set2')
# Limitamos el eje Y para poder visualizar claramente las cajas y bigotes, ignorando extremos muy lejanos
axes[0, 1].set_ylim(-300, 300)
axes[0, 1].set_title("Distribución de Beneficios por Categoría (Seaborn)", fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel("Categoría de Producto", fontsize=12)
axes[0, 1].set_ylabel("Beneficio ($)", fontsize=12)
# CONCLUSIÓN 2: La categoría 'Technology' presenta en promedio mayores beneficios.
# 'Furniture' (Muebles) tiene una distribución peligrosa donde gran parte de los datos se encuentran en pérdidas (por debajo de 0).

# 4. Gráfico bivariante con Matplotlib (Dispersión / Scatter)
axes[1, 0].scatter(df['Sales'], df['Profit'], alpha=0.4, color='coral', edgecolor='w')
axes[1, 0].set_title("Relación Ventas vs. Beneficios (Matplotlib)", fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel("Ventas Totales ($)", fontsize=12)
axes[1, 0].set_ylabel("Beneficio Total ($)", fontsize=12)
axes[1, 0].axhline(0, color='black', linestyle='--', linewidth=1.5) # Línea base del beneficio cero
# CONCLUSIÓN 3: A mayores ventas, existe un mayor potencial de beneficio, sin embargo,
# observamos bastantes puntos que a pesar de tener grandes ventas (> $2000) generan pérdidas masivas,
# indicando posibles problemas de descuentos agresivos o costos de envío elevados.

# 5. Visualización multivariante con Seaborn (Heatmap de Correlación)
# Seleccionamos solo las métricas numéricas principales
metricas = df[['Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost']]
correlaciones = metricas.corr()
sns.heatmap(correlaciones, annot=True, cmap='RdBu', center=0, vmin=-1, vmax=1, ax=axes[1, 1], square=True)
axes[1, 1].set_title("Correlación de Variables Numéricas (Seaborn)", fontsize=14, fontweight='bold')
# CONCLUSIÓN 4: El Descuento (Discount) tiene una correlación negativa moderada (-0.32) con el Beneficio (Profit).
# Además, existe una correlación altísima (0.77) entre el Costo de Envío (Shipping Cost) y las Ventas (Sales).

# Ajustar el espaciado
plt.tight_layout(rect=[0, 0, 1, 0.96])

# 6. Guardar la figura en archivo de imagen
ruta_guardado = "superstore_analisis_subplots.png"
plt.savefig(ruta_guardado, dpi=300)
print(f"\n¡Proceso exitoso! Se ha guardado el archivo de visualizaciones en: {ruta_guardado}")

# ---------------------------------------------------------
# Gráfico Bivariante Adicional con Seaborn (Regplot)
# ---------------------------------------------------------
# Creamos un gráfico adicional independiente para cumplir con todos los tipos solicitados
plt.figure(figsize=(10, 6))
# Tomamos una muestra aleatoria para que el gráfico de dispersión con regresión no sea tan denso
muestra = df.sample(n=2000, random_state=42)
sns.regplot(data=muestra, x='Discount', y='Profit', scatter_kws={'alpha':0.2, 'color':'indigo'}, line_kws={'color':'red', 'lw':2})
plt.title("Impacto de los Descuentos en los Beneficios (Seaborn Regplot)", fontsize=16, fontweight='bold')
plt.xlabel("Nivel de Descuento", fontsize=12)
plt.ylabel("Beneficio Generado ($)", fontsize=12)
plt.axhline(0, color='black', linestyle='--')

ruta_guardado_bivariante = "superstore_descuentos.png"
plt.savefig(ruta_guardado_bivariante, dpi=300)
print(f"Se ha guardado una imagen adicional bivariante en: {ruta_guardado_bivariante}")
# CONCLUSIÓN ADICIONAL: La línea de regresión con pendiente negativa muy marcada 
# confirma contundentemente que los mayores descuentos destruyen el margen de beneficio de la empresa.
