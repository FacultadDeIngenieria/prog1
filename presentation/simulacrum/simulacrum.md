---
title: Simulacrum
layout: practice
permalink: /simulacrum
---

# **Programación I - Simuacro de Primer Parcial**

**Instrucciones:**
*   Todos los ejercicios deben resolverse en **Python**.
*   Para los ejercicios de listas y strings, **no se permite el uso de estructuras iterativas (loops)** como `for` o `while`.

### **1. Seguimiento de Código (2 puntos)**
¿Qué valor imprime en pantalla al ejecutar el siguiente código? Justifique brevemente su respuesta siguiendo el flujo de las variables.

```python
def exam_mystery(text):
    word = "pythonic"
    if len(text) > 5:
        if "a" in text:
            word = text[:3].upper() + word[-2:]
        elif "e" in text:
            word = text[1:4] + "123"
        
        if len(word) > 5:
            result = word[::-1]
        else:
            result = word + "!!!"
    else:
        result = text[::2] + "&" + word[:2]
    
    print("Valor final:", result)

exam_mystery("parcial")
```

### **2. Manipulación de Listas y Slicing (2 puntos)**
Escribir una función llamada **`shuffle_list`** que reciba una lista de **exactamente 6 elementos**. La función debe devolver una nueva lista siguiendo estas reglas (sin usar loops):
*   El primer elemento de la nueva lista debe ser el último de la original.
*   Los elementos en la posición central (índices 2 y 3) deben estar invertidos.
*   El resto de los elementos deben ser los mismos que en la lista original.
*   Si la lista no tiene 6 elementos, debe devolver una lista vacía y mostrar el mensaje: "Lista no válida".

**Ejemplo:** `shuffle_list([10, 20, 30, 40, 50, 60])` devuelve `[60, 20, 40, 30, 50, 10]`

### **3. Validación de Strings (2 puntos)**
Escribir una función llamada **`validate_token`** que reciba un string y devuelva **True** si cumple con todas las siguientes condiciones, o **False** en caso contrario:
1.  El string debe empezar y terminar con la misma letra (ignorando mayúsculas/minúsculas).
2.  Debe tener una longitud de al menos 8 caracteres.
3.  Debe contener al menos un dígito numérico (0-9).
4.  No debe contener espacios en blanco al principio ni al final.

**Ejemplos:**
*   `validate_token("  a123456a")` -> `False` (tiene espacios)
*   `validate_token("A_token_9A")` -> `True`
*   `validate_token("abc123de")` -> `False` (no empieza y termina igual)

### **4. Resolución de Problemas: Sistema de Gimnasio (4 puntos)**
Implementar una función llamada **`gym_membership`** que calcule el costo mensual de la cuota de un socio basándose en su edad y el tipo de plan.

**Reglas de cálculo:**
*   **Plan "Básico":** $2000 por mes.
*   **Plan "Premium":** $3500 por mes.
*   **Descuentos por edad:**
    *   Si el socio es menor de 18 años, obtiene un **15% de descuento** sobre el valor del plan.
    *   Si el socio tiene 60 años o más, obtiene un **25% de descuento** sobre el valor del plan.
*   **Recargo por fin de semana:** Si el socio desea acceso los fines de semana, se suma un costo fijo de **$500** al total final (después de aplicar descuentos).

**La función debe:**
1.  Pedir al usuario la edad (convertir a `int`) con el mensaje: `"Ingrese la edad del socio: "`.
2.  Pedir el tipo de plan con el mensaje: `"Ingrese el plan (basico/premium): "`.
3.  Pedir si desea acceso fines de semana con el mensaje: `¿Acceso fin de semana? (si/no): "`.
4.  **Imprimir:** `"El costo final de la membresía es: $X"`, siendo X el valor calculado.
5.  Si la edad es negativa o el plan no es válido, imprimir: `"Datos de entrada no válidos"`.

**Ejemplo del cálculo:**
*   Edad: 70, Plan: "premium", Fin de semana: "no" -> $3500 - 25% = **$2625.0**
*   Edad: 25, Plan: "basico", Fin de semana: "si" -> $2000 + $500 = **$2500.0**