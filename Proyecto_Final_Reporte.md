# 📄 REPORTE DE PROYECTO FINAL INTEGRADOR - PYTHON QUEST
**Estudiante:** Ernesto  
**Proyecto:** Simulador de Liga Deportiva en Python  
**Estado:** ✅ FINALIZADO  
**Fecha de finalización:** 2026  

---

## 📌 Resumen del Proyecto
El sistema consiste en un simulador completo de liga deportiva orientado a objetos, capaz de registrar equipos y jugadores, gestionar partidos por turnos o ingreso directo, calcular puntos/goles, mostrar una tabla de posiciones ordenada y almacenar los resultados en un archivo `.txt`.

---

## 🧠 Arquitectura y Módulos Desarrollados
1. **Clase `Jugador`**: Registro de atributos individuales (`nombre`, `posicion`, `goles`) y métodos de anotación.
2. **Clase `Equipo`**: Gestión de listas de jugadores (`lista_jugadores`), acumulación de `puntos` y `goles_favor`.
3. **Clase `Partido`**: Evaluación de marcadores, cálculo de puntos (3 victoria, 1 empate) y actualización automática de los equipos.
4. **Clase `Liga`**: Administración general, ordenamiento dinámico mediante `lambda` y persistencia con `with open("liga_datos.txt", "w")`.
5. **Menú de Interacción Continuo**: Control de menú con `while True`, `if/elif/else` y captura de excepciones con `try/except (ValueError)`.

---

## 📊 Estado Final del Curso
* **Progreso Total:** 100%
* **Mundos Completados:** 10 / 10
* **Rango:** 🐍 Python Master