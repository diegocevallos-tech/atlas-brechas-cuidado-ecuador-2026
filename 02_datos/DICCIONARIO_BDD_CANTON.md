# DICCIONARIO_BDD_CANTON

> Conversión automática desde `DICCIONARIO_BDD_CANTON.xlsx` a Markdown para lectura por otra IA.

## Portada

- Instituto Nacional de Estadística y Censos
- VIII Censo de Población y VII de Vivienda
- Diccionario de Variables
- Base de Datos a Nivel de Cantón
- (Incluye variables de Identidad de Género y Orientación Sexual)

## Índice

| Tabla.N° | Contenido |
| --- | --- |
| 1 | Diccionario de variables de la tabla de vivienda |
| 2 | Diccionario de variables de la tabla de hogar |
| 3 | Diccionario de variables de la tabla de mortalidad |
| 4 | Diccionario de variables de la tabla de emigración |
| 5 | Diccionario de variables de la tabla de población |

## 1. Vivienda

**Cuadro N.°:** 1  
**Nombre del cuadro:** Diccionario de variables de la tabla Vivienda

### Descripción

- Diccionario de Variables de Base a Nivel de Cantón
- El Cuadro N°1  describe los elementos alfanuméricos que integran la tabla de datos de Vivienda de la base a nivel cantonal. Esta tabla contienen 6.611.555 registros y 32 variables, y se la puede descargar en tres formatos (.csv / .spss / redatam) en los sitios web oficiales de INEC (www.ecuadorencifras.gob.ec) y Censo 2022 (www.censoecuador.gob.ec).

### Diccionario de variables

| CÓDIGO DE VARIABLE | NOMBRE DE LA VARIABLE | PREGUNTA | CATEGORÍAS<br>(Código y etiqueta) | TIPO DE VARIABLE | FORMATO DEL DATO | LONGITUD DEL DATO |
| --- | --- | --- | --- | --- | --- | --- |
| I01 | Provincia | Provincia | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I02 | Identificador de Cantón | Cantón | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I10 | Número de vivienda | Número de la vivienda | 0000001-0499992 | Identificación | Texto | 7 |
| D01 | Tipo de vía | Tipo de vía | 1 Calle<br>2 Avenida<br>3 Carretera<br>4 Pasaje<br>5 Callejón<br>6 Sendero<br>7 Camino<br>8 Otro | Estadística Cualitativa | Categórico | 1 |
| V01 | Tipo de vivienda | Tipo de vivienda | 1 Casa/villa<br>2 Departamento en casa o edificio<br>3 Cuarto/s en casa de inquilinato.<br>4 Mediagua<br>5 Rancho<br>6 Covacha<br>7 Choza<br>8 Otra vivienda particular<br>9 Hotel, pensión, residencial u hostal<br>10 Cuartel militar, policía o bomberos<br>11 Centro de privación de libertad/cárcel<br>12 Hospital, clínica, etc.<br>13 Convento o institución religiosa<br>14 Centro de acogida y protección para niñas/os y adolescentes<br>15 Residencia de adultos mayores/Asilo de ancianos<br>16 Internado de estudiantes<br>17 Campamento de trabajo<br>18 Otra vivienda colectiva<br>19 Sin vivienda | Estadística Cualitativa | Categórico | 2 |
| V0201 | Condición de ocupación de vivienda particular | Condición de ocupación de la<br>vivienda particular | 1 Ocupada con personas presentes<br>2 Ocupada con personas ausentes<br>3 De temporada o vacacional<br>4 Desocupada<br>5 En construcción | Estadística Cualitativa | Categórico | 1 |
| V0202 | Condición de ocupación de vivienda colectiva | Condición de ocupación de la vivienda colectiva | 1 Con residentes habituales <br>2 Sin residentes habituales | Estadística Cualitativa | Categórico | 1 |
| V03 | Material predominante del techo o cubierta | ¿El material predominante del techo o cubierta de la vivienda es de: | 1 Hormigón (losa, cemento)<br>2 Fibrocemento, asbesto (eternit, eurolit)<br>3 Zinc, aluminio (lámina o plancha metálica)<br>4 Teja<br>5 Palma, paja u hoja<br>6 Otro material | Estadística Cualitativa | Categórico | 1 |
| V04 | Estado del techo o cubierta<br> | ¿El estado del techo o cubierta de la vivienda es:<br> | 1 Bueno<br>2 Regular<br>3 Malo | Estadística Cualitativa | Categórico | 1 |
| V05 | Material predominante de las paredes exteriores | ¿El material predominante de las paredes exteriores de la vivienda es de: | 1 Hormigón<br>2 Ladrillo o bloque<br>3 Panel prefabricado (yeso, fibrocemento, etc.)<br>4 Adobe o tapia<br>5 Madera<br>6 Caña revestida o bahareque<br>7 Caña no revestida<br>8 Otro material | Estadística Cualitativa | Categórico | 1 |
| V06 | Estado de las paredes exteriores | ¿El estado de las paredes exteriores de la vivienda es: | 1 Bueno<br>2 Regular<br>3 Malo | Estadística Cualitativa | Categórico | 1 |
| V07 | Material predominante del piso | ¿El material predominante del piso de la vivienda es de: | 1 Duela, parquet, tablón o piso flotante<br>2 Cerámica, baldosa, vinil o porcelanato<br>3 Mármol o marmetón<br>4 Ladrillo o cemento<br>5 Tabla sin tratar<br>6 Caña sin tratar<br>7 Tierra<br>8 Otro material | Estadística Cualitativa | Categórico | 1 |
| V08 | Estado del piso | ¿El estado del piso de la vivienda es: | 1 Bueno<br>2 Regular<br>3 Malo | Estadística Cualitativa | Categórico | 1 |
| V09 | El agua que recibe la vivienda es | ¿El agua que recibe la vivienda es: | 1 Por tubería, dentro de la vivienda<br>2 Por tubería, fuera de la vivienda pero dentro del edificio, lote o terreno<br>3 Por tubería, fuera del edificio, lote o terreno<br>4 No recibe agua por tubería, sino por otros medios | Estadística Cualitativa | Categórico | 1 |
| V10 | El agua que recibe la vivienda proviene o es suministrada por | Principalmente, ¿el agua que recibe la vivienda proviene o es suministrada por: | 1 Empresa Pública/Municipio<br>2 Juntas de Agua/Organizaciones comunitarias/GAD parroquial<br>3 Pozo<br>4 Carro o tanquero repartidor<br>5 Otras fuentes (río, vertiente, acequia, canal, grieta o agua lluvia) | Estadística Cualitativa | Categórico | 1 |
| V11 | El servicio higiénico de la vivienda es | ¿El servicio higiénico de la vivienda es: | 1 Inodoro o escusado, conectado a red pública de alcantarillado<br>2 Inodoro o escusado, conectado a pozo séptico<br>3 Inodoro o escusado, conectado a biodigestor<br>4 Inodoro o escusado, conectado a pozo ciego<br>5 Inodoro o escusado, con descarga directa al mar, río, lago o quebrada<br>6 Letrina<br>7 No tiene | Estadística Cualitativa | Categórico | 1 |
| V12 | Disponibilidad de energía eléctrica por red pública | ¿Dispone la vivienda de luz (energía eléctrica) proveniente de la red pública? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| V13 | Disponibilidad de otra fuente de energía eléctrica | ¿Dispone la vivienda de otra fuente de energía eléctrica distinta a la red pública, cómo: | 1 Planta eléctrica (generador de luz)<br>2 Energía solar (panel fotovoltaico)<br>3 Energía eólica (a partir del viento)<br>4 Otra fuente (desechos vegetales y animales)<br>5 No dispone | Estadística Cualitativa | Categórico | 1 |
| V14 | Eliminación de la basura | Principalmente, ¿cómo eliminan la basura de la vivienda: | 1 Por carro recolector<br>2 Por contenedor municipal<br>3 La arroja en terreno baldío<br>4 La quema<br>5 La entierra<br>6 La arroja al río, acequia, canal o quebrada<br>7 De otra forma | Estadística Cualitativa | Categórico | 1 |
| V15 | Número de cuartos | Sin contar la cocina, baño(s) y cuartos de negocio, ¿cuántos cuartos tiene la vivienda, incluyendo sala y comedor? | 1-20 | Estadística Cuantitativa | Numérico | 2 |
| V16 | Todas las personas comparten un mismo gasto para la alimentación | Todas las personas que viven habitualmente en esta vivienda, ¿comparten un mismo gasto para la alimentación? (olla común) | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| V17 | Número de hogares | Incluyendo su hogar, ¿cuántos grupos de personas  (hogares) mantienen gastos separados para la alimentación? (cocinan los alimentos por separado) | 1-9 | Estadística Cuantitativa | Numérico | 2 |
| AUR | Área urbana o rural | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | 1 Área urbana<br>2 Área rural | Estadística Cualitativa | Categórico | 1 |
| CANTON | Cantón | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 4 |
| ID_VIV | Identificador de la vivienda | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | Secuencial | Identificación | Texto | 21 |
| TOTFALL | Total de fallecidos de la vivienda | Variable derivada - <br>Sección IV. Hogar.<br>Módulo B. Mortalidad | 1-11 | Estadística Cuantitativa | Numérico | 2 |
| TOTEMI | Total de emigrantes de la vivienda | Variable derivada - <br>Sección IV. Hogar.<br>Módulo C. Emigración | 1-15 | Estadística Cuantitativa | Numérico | 2 |
| TOTPER | Total de personas de la vivienda | Variable derivada - <br>Sección V. Población | 1-7196 | Estadística Cuantitativa | Numérico | 4 |
| V0201R | Condición de ocupación de vivienda particular (recodificada) | Condición de ocupación de la<br>vivienda particular (recodificada) | 1 Ocupada<br>2 De temporada o vacacional<br>3 Desocupada<br>4 En construcción | Estadística Cualitativa | Categórico | 1 |
| V15R | Número de cuartos (recodificada) | Sin contar la cocina, baño(s) y cuartos de negocio, ¿cuántos cuartos tiene la vivienda, incluyendo sala y comedor? (recodificada) | 1 Un cuarto<br>2 Dos cuartos<br>3 Tres cuartos<br>4 Cuatro cuartos<br>5 Cinco cuartos<br>6 Seis o más cuartos | Estadística Cualitativa | Categórico | 1 |
| DEF_HAB | Déficit habitacional | Variable derivada - <br>Se calcula a partir de 6 preguntas del cuestionario, 3 sobre el material predominante y 3 sobre la percepción del estado del material:<br>- ¿El material predominante del (techo/paredes/piso) de la vivienda es:<br>- ¿El estado del (techo/paredes/piso) de la vivienda es:<br>A partir del cruce entre el material y el estado del mismo, se categorizan los materiales como: a) aceptable b) recuperable y c) irrecuperable. Esta categorización permite a su vez clasificar a las viviendas en a) dignas o aceptables, b) con déficit cualitativo y c) con déficit cuantitativo. Para mayor información sobre este cálculo, consultar la ficha metodológica del déficit habitacional en nuestro sitio web. | 1 Dignas o aceptables<br>2 Déficit cualitativo (Recuperables)<br>3 Déficit cuantitativo (Irrecuperables) | Estadística Cualitativa | Categórico | 1 |
| IMP_VOPA | Registro imputado en vivienda ocupada con personas ausentes | Variable técnica - <br>Sección III. Vivienda.<br>Condición de ocupación de la vivienda particular<br>2. Ocupada con personas ausentes | 1 Sí<br>2 No | Técnica | Categórico | 1 |

### Nota

- Elaboración: Instituto Nacional de Estadística y Censos (INEC)

## 2. Hogar

**Cuadro N.°:** 2  
**Nombre del cuadro:** Diccionario de variables de la tabla Hogar

### Descripción

- Diccionario de Variables de Base a Nivel de Cantón
- El Cuadro N°2 describe los elementos alfanuméricos que integran la tabla de datos de Hogar de la base a nivel cantonal. Esta tabla contienen 5.193.548 registros y 47 variables, y se puede descargar en tres formatos (.csv / .spss / redatam) en los sitios web oficiales de INEC (www.ecuadorencifras.gob.ec) y Censo 2022 (www.censoecuador.gob.ec).

### Diccionario de variables

| CÓDIGO DE VARIABLE | NOMBRE DE LA VARIABLE | PREGUNTA | CATEGORÍAS<br>(Código y etiqueta) | TIPO DE VARIABLE | FORMATO DEL DATO | LONGITUD DEL DATO |
| --- | --- | --- | --- | --- | --- | --- |
| I01 | Provincia | Provincia | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I02 | Identificador de Cantón | Cantón | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I10 | Número de vivienda | Número de la vivienda | 0000001-0499992 | Identificación | Texto | 7 |
| INH | Número de hogar | Número de hogar | 00-09 | Identificación | Texto | 2 |
| H01 | Número de dormitorios | Del total de cuartos de este hogar, ¿cuántos son exclusivos para dormir? | 0-20 | Estadística Cuantitativa | Numérico | 2 |
| H02 | Cuarto o espacio exclusivo para cocinar | ¿Este hogar tiene cuarto o espacio exclusivo para cocinar? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H03 | Disponibilidad de servicio higiénico, inodoro o escusado | ¿El servicio higiénico, inodoro o escusado que dispone el hogar es: | 1 De uso exclusivo del hogar<br>2 Compartido con varios hogares<br>3 No tiene | Estadística Cualitativa | Categórico | 1 |
| H04 | Disponibilidad de espacio con instalaciones y/o ducha para bañarse | ¿Dispone este hogar de espacio con instalaciones y/o ducha para bañarse: | 1 De uso exclusivo del hogar<br>2 Compartido con varios hogares<br>3 No tiene | Estadística Cualitativa | Categórico | 1 |
| H05 | Principal combustible o energía para cocinar | ¿Cuál es el principal combustible o energía que utiliza este hogar para cocinar: | 1 Gas de tanque o cilindro<br>2 Gas centralizado (por tubería)<br>3 Electricidad<br>4 Leña o carbón<br>5 Biogás (residuos vegetales y/o animales, etc.)<br>6 Otro (Ej: gasolina, kerex, diésel, etc.)<br>7 Ninguno (No cocina) | Estadística Cualitativa | Categórico | 1 |
| H06 | Principalmente, el agua que beben los miembros del hogar | ¿Principalmente, ¿el agua que beben los miembros del hogar: | 1 La beben, tal como llega al hogar?<br>2 La compran (agua envasada en bidón, botella o funda)?<br>3 La hierven?<br>4 Le ponen cloro?<br>5 La filtran (colocan filtros en el grifo o usan purificadores)?<br>6 Realizan otro tratamiento? | Estadística Cualitativa | Categórico | 1 |
| H0701 | Acostumbra separar la basura en orgánica e inorgánica<br> | ¿Este hogar acostumbra:<br>1. Separar la basura en orgánica (restos de comida, vegetales, etc.) e inorgánica (papel, cartón, plástico, vidrio, etc.)?<br> | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H0702 | Acostumbra separar desperdicios para dar a los animales o plantas | ¿Este hogar acostumbra:<br>2. Separar desperdicios para dar a los animales o para las plantas? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H0703 | Acostumbra separar papel, cartón, plástico o vidrio para vender, regalar o reutilizar | ¿Este hogar acostumbra:<br>3. Separar papel, cartón, plástico o vidrio para vender, regalar o reutilizar? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H0801 | Tiene este hogar perros | ¿Tiene este hogar:<br>1. Perros? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H0801N | Número de perros | ¿Tiene este hogar:<br>1. Perros? cuántos? | 1-29 | Estadística Cuantitativa | Numérico | 2 |
| H0802 | Tiene este hogar gatos | ¿Tiene este hogar:<br>2. gatos? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H0802N | Número de gatos | ¿Tiene este hogar:<br>2. Gatos? cuántos? | 1-24 | Estadística Cuantitativa | Numérico | 2 |
| H09 | Tenencia de la vivienda | ¿La vivienda que ocupa este hogar es: | 1 Propia y totalmente pagada<br>2 Propia y la está pagando<br>3 Propia (regalada, donada, heredada o por posesión)<br>4 Arrendada/anticresis<br>5 Prestada o cedida (no paga)<br>6 Por servicios | Estadística Cualitativa | Categórico | 1 |
| H1001 | Dispone de servicio de teléfono convencional | ¿Este hogar dispone de:                                            <br>1. Servicio de teléfono convencional? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1002 | Dispone de servicio de teléfono celular | ¿Este hogar dispone de:                                       <br>2. Servicio de teléfono celular? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1003 | Dispone de servicio de televisión pagada | ¿Este hogar dispone de:                                       <br>3. Servicio de televisión pagada (cable/satelital, otra)? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1004 | Dispone de servicio de internet fijo | ¿Este hogar dispone de:                                       <br>4. Servicio de internet fijo? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1005 | Dispone de computadora | ¿Este hogar dispone de:                                       <br>5. Computadora (de escritorio o laptop)? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1006 | Dispone de refrigeradora | ¿Este hogar dispone de:                                       <br>6. Refrigeradora? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1007 | Dispone de máquina lavadora de ropa | ¿Este hogar dispone de:                                     <br>7. Máquina lavadora de ropa? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1008 | Dispone de máquina secadora de ropa | ¿Este hogar dispone de:                                       <br>8. Máquina secadora de ropa? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1009 | Dispone de horno microondas | ¿Este hogar dispone de:                                       <br>9. Horno microondas? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1010 | Dispone de máquina extractora de olores | ¿Este hogar dispone de:                                <br>10. Máquina extractora de olores? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1011 | Dispone de automóvil o camioneta para uso exclusivo | ¿Este hogar dispone de:                                       <br>11. Automóvil o camioneta, para uso exclusivo del hogar? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H1012 | Dispone de motocicleta para uso exclusivo | ¿Este hogar dispone de:                                       <br>12. Motocicleta, para uso exclusivo del hogar? | 1 Sí<br>2 No | Estadística Cualitativa | Categórico | 1 |
| H11 | Alguna persona falleció en los últimos tres años (a partir de enero 2020) | Incluyendo a recién nacidos y adultos mayores, ¿Alguna persona que vivía en este hogar falleció en los últimos tres años? (a partir de enero de 2020) | 1 Sí<br>2 No<br>9 Se ignora | Estadística Cualitativa | Categórico | 1 |
| H1101 | Número de personas fallecidas | Incluyendo a recién nacidos y adultos mayores, ¿alguna persona que vivía en este hogar falleció en los últimos tres años? (a partir de enero de 2020)<br>¿Cuántas? | 1-11<br> | Estadística Cuantitativa | Numérico | 2 |
| H12 | Alguna persona viajó a otro país y todavía no regresa (a partir de nov. 2010) | A partir del último censo de población y vivienda (noviembre 2010), ¿una o más personas que vivían en este hogar viajaron a otro país y todavía no regresan para quedarse definitivamente? | 1 Sí<br>2 No<br>9 Se ignora | Estadística Cualitativa | Categórico | 1 |
| H1201 | Número de personas emigrantes | A partir del último censo de población y vivienda (noviembre 2010), ¿una o más personas que vivían en este hogar viajaron a otro país y todavía no regresan para quedarse definitivamente?                                                  ¿Cuántas? | 1-15<br> | Estadística Cuantitativa | Numérico | 2 |
| H1301 | Total de hombres en el hogar | ¿Cuántas personas viven habitualmente en este hogar, estén o no presentes al momento de la entrevista? Hombres | 0-6524 | Estadística Cuantitativa | Numérico | 4 |
| H1302 | Total de mujeres en el hogar | ¿Cuántas personas viven habitualmente en este hogar, estén o no presentes al momento de la entrevista? Mujeres | 0-672 | Estadística Cuantitativa | Numérico | 4 |
| H1303 | Total de personas en el hogar | ¿Cuántas personas viven habitualmente en este hogar, estén o no presentes al momento de la entrevista? Total | 1-7196 | Estadística Cuantitativa | Numérico | 4 |
| H15 | Existe alguna persona que no haya sido mencionada en el hogar | ¿Hay alguna persona que no haya sido mencionada porque se encuentra en este momento de: vacaciones, trabajo, enfermedad u otro motivo y que viva habitualmente en este hogar? | 1 Sí<br>2 No<br>9 Se ignora | Estadística Cualitativa | Categórico | 1 |
| AUR | Área urbana o rural | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | 1 Área urbana<br>2 Área rural | Estadística Cualitativa | Categórico | 1 |
| CANTON | Cantón | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 4 |
| ID_VIV | Identificador de la vivienda | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | Secuencial | Identificación | Texto | 21 |
| ID_HOG | Identificador del hogar | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda.<br>Sección IV. Hogar | Secuencial | Identificación | Texto | 23 |
| H01R | Número de dormitorios (recodificada) | Variable derivada - <br>Del total de cuartos de este hogar, ¿cuántos son exclusivos para dormir? | 0 Ninguno<br>1 Un dormitorio<br>2 Dos dormitorios<br>3 Tres dormitorios<br>4 Cuatro dormitorios<br>5 Cinco dormitorios<br>6 Seis o más dormitorios | Estadística Cualitativa | Categórico | 1 |
| HAC | Hacinamiento | Variable derivada - <br>Del total de cuartos de este hogar, ¿cuántos son exclusivos para dormir? | 1 Con hacinamiento<br>2 Sin hacinamiento | Estadística Cualitativa | Categórico | 1 |
| NBI | Pobreza por necesidades básicas insatisfechas | Variable derivada | 1 Pobres<br>2 No pobres | Estadística Cualitativa | Categórico | 1 |
| TIPO_HOGAR | Tipo de hogar | Variable derivada | 1 Hogar unipersonal<br>2 Hogar nuclear<br>3 Hogar extenso<br>4 Hogar compuesto<br>5 Hogar sin núcleo conyugal | Estadística Cualitativa | Categórico | 1 |
| IMP_VOPA | Registro imputado en vivienda ocupada con personas ausentes | Variable técnica - <br>Sección III. Vivienda.<br>Condición de ocupación de la vivienda particular<br>2. Ocupada con personas ausentes | 1 Sí<br>2 No | Técnica | Categórico | 1 |

### Nota

- Elaboración: Instituto Nacional de Estadística y Censos (INEC)

## 3. Mortalidad

**Cuadro N.°:** 3  
**Nombre del cuadro:** Diccionario de variables de la tabla Mortalidad

### Descripción

- Diccionario de Variables de Base a Nivel de Cantón
- El Cuadro N°3 describe los elementos alfanuméricos que integran la tabla de datos de Mortalidad de la base a nivel cantonal. Esta tabla contienen 250.746 registros y 16 variables, y se la puede descargar en tres formatos (.csv / .spss / redatam) en los sitios web oficiales de INEC (www.ecuadorencifras.gob.ec) y Censo 2022 (www.censoecuador.gob.ec).

### Diccionario de variables

| CÓDIGO DE VARIABLE | NOMBRE DE LA VARIABLE | PREGUNTA | CATEGORÍAS<br>(Código y etiqueta) | TIPO DE VARIABLE | FORMATO DEL DATO | LONGITUD DEL DATO |
| --- | --- | --- | --- | --- | --- | --- |
| I01 | Provincia | Provincia | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I02 | Identificador de Cantón | Cantón | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I10 | Número de vivienda | Número de la vivienda | 0000001-0499992 | Identificación | Texto | 7 |
| INH | Número de hogar | Número de hogar | 00-06 | Identificación | Texto | 2 |
| M00 | Número de la persona fallecida | Número persona | 01-11 | Identificación | Texto | 2 |
| M0201 | Mes de fallecimiento | ¿En qué mes y año murió?                                    <br>mes | 1 Enero<br>2 Febrero <br>3 Marzo <br>4 Abril<br>5 Mayo <br>6 Junio <br>7 Julio <br>8 Agosto <br>9 Septiembre <br>10 Octubre <br>11 Noviembre <br>12 Diciembre<br>99 Se ignora | Estadística Cuantitativa | Categórico | 2 |
| M0202 | Año de fallecimiento | ¿En qué mes y año murió?                                 <br>año | 2020-2023<br>9999 Se ignora | Estadística Cuantitativa | Numérico | 4 |
| M03 | Edad al fallecer | ¿Qué edad tenía? | 0-120<br>0 Menores de 1 año<br>999 Se ignora | Estadística Cuantitativa | Numérico | 3 |
| M04 | Sexo del fallecido | ¿Cuál era su sexo? | 1 Hombre<br>2 Mujer | Estadística Cualitativa | Categórico | 1 |
| M05 | Murió estando embarazada, en el parto o dentro de los 42 días posteriores al parto | ¿Murió estando embarazada, en el parto o dentro de los 42 días posteriores al parto? | 1 Si<br>2 No<br>9 Se ignora | Estadística Cualitativa | Categórico | 1 |
| M06 | Causa de fallecimiento | ¿Murió a causa de: | 1 Accidente, suicidio o asesinato<br>2 COVID-19<br>3 Otros? (Ej: enfermedad, causa natural)<br>9 Se ignora | Estadística Cualitativa | Categórico | 1 |
| AUR | Área urbana o rural | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | 1 Área urbana<br>2 Área rural | Estadística Cualitativa | Categórico | 1 |
| CANTON | Cantón | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 4 |
| ID_VIV | Identificador de la vivienda | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | Secuencial | Identificación | Texto | 21 |
| ID_HOG | Identificador del hogar | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda.<br>Sección IV. Hogar | Secuencial | Identificación | Texto | 23 |
| ID_FALL | Identificador de persona fallecida | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda.<br>Sección IV. Hogar<br>Módulo B. Mortalidad. | Secuencial | Identificación | Texto | 25 |

### Nota

- Elaboración: Instituto Nacional de Estadística y Censos (INEC)

## 4. Emigración

**Cuadro N.°:** 4  
**Nombre del cuadro:** Diccionario de variables de la tabla Emigración

### Descripción

- Diccionario de Variables de Base a Nivel de Cantón
- El Cuadro N°4  describe los elementos alfanuméricos que integran la tabla de datos de Emigración de la base a nivel cantonal. Esta tabla contienen 124.992 registros y 14 variables, y se la puede descargar en tres formatos (.csv / .spss / redatam) en los sitios web oficiales de INEC (www.ecuadorencifras.gob.ec) y Censo 2022 (www.censoecuador.gob.ec).

### Diccionario de variables

| CÓDIGO DE VARIABLE | NOMBRE DE LA VARIABLE | PREGUNTA | CATEGORÍAS<br>(Código y etiqueta) | TIPO DE VARIABLE | FORMATO DEL DATO | LONGITUD DEL DATO |
| --- | --- | --- | --- | --- | --- | --- |
| I01 | Provincia | Provincia | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I02 | Identificador de Cantón | Cantón | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 2 |
| I10 | Número de vivienda | Número de la vivienda | 0000001-0499992 | Identificación | Texto | 7 |
| INH | Número de hogar | Número de hogar | 00-05 | Identificación | Texto | 2 |
| E00 | Número de la persona emigrante | Número persona | 01-15 | Identificación | Texto | 2 |
| E01 | Año de salida | ¿En qué año salió del país? | 2010-2023<br>9999. Se ignora | Estadística Cuantitativa | Numérico | 4 |
| E02 | Sexo del emigrante | ¿Cuál es el sexo? | 1 Hombre<br>2 Mujer | Estadística Cualitativa | Categórico | 1 |
| E03 | Edad al salir | ¿Qué edad tenía al salir del país? | 0-98<br>0 Menores de 1 año<br>999 Se ignora | Estadística Cuantitativa | Numérico | 3 |
| E04 | País actual de residencia | ¿Cuál es el país actual de residencia? | De acuerdo al Código Uniforme de Países para uso Estadístico<br>999999 Se ignora | Estadística Cualitativa | Categórico | 6 |
| AUR | Área urbana o rural | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | 1 Área urbana<br>2 Área rural | Estadística Cualitativa | Categórico | 1 |
| CANTON | Cantón | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | De acuerdo a Clasificador Geográfico Estadístico | Identificación | Texto | 4 |
| ID_VIV | Identificador de la vivienda | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda | Secuencial | Identificación | Texto | 21 |
| ID_HOG | Identificador del hogar | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda.<br>Sección IV. Hogar | Secuencial | Identificación | Texto | 23 |
| ID_EMI | Identificador de persona emigrante | Variable derivada - <br>Sección I. Ubicación geográfica de la vivienda.<br>Sección IV. Hogar<br>Módulo C. Emigración | Secuencial | Identificación | Texto | 25 |

### Nota

- Elaboración: Instituto Nacional de Estadística y Censos (INEC)

## 5. Población

| Instituto Nacional de Estadística y Censos |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| VIII Censo de Población y VII de Vivienda |  |  |  |  |  |
| Diccionario de Variables de Base a Nivel de Cantón |  |  |  |  |  |
| (Incluye variables de Identidad de Género y Orientación Sexual) |  |  |  |  |  |
