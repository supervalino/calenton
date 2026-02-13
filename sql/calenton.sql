------------------------------------------------------------------------------
--  CALENTON
--
--  (C) Trustserver SL, 2009
--  (C) LITEC, 2009
--
--  Este paquete ha sido desarrollado por Trustserver S. L. para el 
--  Laboratorio de Investigación en Tecnologías de la Combustión (LITEC)
--
--  $Id: calenton.sql 346 2010-10-29 06:43:46Z bruno $
--  $URL: https://www.litec.csic.es/svn/emisiones/trunk/sql/calenton.sql $
------------------------------------------------------------------------------

SET CLIENT_ENCODING = 'UTF8';

------------------------------------------------------------------------------
-- 
-- Cada uno de los escenarios o campañas previstos.  Cada campaña tendrá unos
-- puntos de toma de datos, además de variaciones en el marco regulatorio
-- 
------------------------------------------------------------------------------

CREATE TABLE escenario (
	id		NUMERIC(10)	CONSTRAINT c_escenario_id PRIMARY KEY,
	nombre		VARCHAR(100)	CONSTRAINT c_escenario_nombre UNIQUE
					NOT NULL
	);
	
CREATE SEQUENCE seq_escenario;

------------------------------------------------------------------------------
--
-- Parámetros que luego se pueden utilizar en la definición de los parámetros
-- de emisión
--
------------------------------------------------------------------------------

CREATE TABLE parametro (
	id		NUMERIC(10)	CONSTRAINT c_parametro_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_parametro_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL,
	valor		NUMERIC		NOT NULL,
	descripcion	VARCHAR(1000),

	CONSTRAINT c_parametro_nombre UNIQUE(idescenario, nombre)
	);

CREATE SEQUENCE seq_parametro;

------------------------------------------------------------------------------
--
-- El origen por sector (Agricultura, Industrial) de los distintos datos
--
------------------------------------------------------------------------------

CREATE TABLE origen (
	id		NUMERIC(10)	CONSTRAINT c_origen_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_escenario_id 
						REFERENCES escenario(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL,
	
	CONSTRAINT c_origen_nombre UNIQUE(idescenario, nombre)
	);
	
CREATE SEQUENCE seq_origen;

------------------------------------------------------------------------------
--
-- Los distintos niveles administrativos (municipio, comarca,
-- provincia que tendremos en cuenta).
--
------------------------------------------------------------------------------

CREATE TABLE nivelzona (
	id		NUMERIC(10)	CONSTRAINT c_nivelzona_id PRIMARY KEY,
	nombre		VARCHAR(100)	CONSTRAINT c_nivelzona_nombre UNIQUE
					NOT NULL
	);
	
CREATE SEQUENCE seq_nivelzona;

------------------------------------------------------------------------------
--
-- Los datos que se guardan para cada unidad administrativa (Superficie, 
-- población, cabezas de ganado...)
--
------------------------------------------------------------------------------

CREATE TABLE tipodatozona (
	id		NUMERIC(10)	CONSTRAINT c_tipodatozona_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_tipodatozona_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL,
	unidades	VARCHAR(100)	NOT NULL,
	valor_defecto	NUMERIC		NOT NULL,
	variable	VARCHAR(100)	NOT NULL,

	CONSTRAINT c_tipodatozona_idescenario_nombre UNIQUE(idescenario, nombre)
	);

CREATE SEQUENCE seq_tipodatozona;

------------------------------------------------------------------------------
--
-- Las unidades administrativas.  Cada unidad administrativa debe indicar
-- el nivel de agregación que corresponde.
--
------------------------------------------------------------------------------

CREATE TABLE zona (
	id		NUMERIC(10)	CONSTRAINT c_zona_id PRIMARY KEY,
	idnivelzona	NUMERIC(10)	CONSTRAINT c_zona_idnivelzona 
						REFERENCES nivelzona(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL
	);

CREATE SEQUENCE seq_zona;

------------------------------------------------------------------------------
-- 
-- Relación de unidades administrativas.  Sólo se indicarán para las más 
-- básicas (ie. municipios).  Cada municipio tendrá una entrada por cada
-- unidad administrativa a la que pertenece (ie: comarca, provincia, 
-- comunidad autónoma).
--
------------------------------------------------------------------------------

CREATE TABLE relzona (
	id		NUMERIC(10)	CONSTRAINT c_relzona_id PRIMARY KEY,
	idzona		NUMERIC(10)	CONSTRAINT c_relzona_idzona
						REFERENCES zona(id)
					NOT NULL,
	idzonapadre	NUMERIC(10)	CONSTRAINT c_relzona_idzonapadre
						REFERENCES zona(id)
					NOT NULL,
					
	CONSTRAINT c_relzona_idzona_idzonapadre UNIQUE(idzona, idzonapadre)
	);
	
CREATE SEQUENCE seq_relzona;

------------------------------------------------------------------------------
--
-- Los datos para cada unidad administrativa
--
------------------------------------------------------------------------------

CREATE TABLE datozona (
	id		NUMERIC(10)	CONSTRAINT c_datozona_id PRIMARY KEY,
	idzona		NUMERIC(10)	CONSTRAINT c_datozona_idzona
						REFERENCES zona(id)
					NOT NULL,
	idtipodatozona	NUMERIC(10)	CONSTRAINT c_datozona_idtipodatozona
						REFERENCES tipodatozona(id)
					NOT NULL,
	dato		NUMERIC,

	CONSTRAINT c_datozona_idzona_idtipodatozona 
			UNIQUE(idzona, idtipodatozona)
	);

CREATE SEQUENCE seq_datozona;

-----------------------------------------------------------------------------
--
-- Sobrecarga de valores de parámetros por zona
--
-----------------------------------------------------------------------------

CREATE TABLE parametrozona (
	id		NUMERIC(10)	CONSTRAINT c_parametrozona_id PRIMARY KEY,
	idzona		NUMERIC(10)	CONSTRAINT c_parametrozona_idzona
						REFERENCES zona(id)
					NOT NULL,
	idparametro	NUMERIC(10)	CONSTRAINT c_parametrozona_idparametro
						REFERENCES parametro(id)
					NOT NULL,
	valor		NUMERIC,

	CONSTRAINT c_parametrozona_idzona_idparametro 
			UNIQUE(idzona, idparametro)
	);

CREATE SEQUENCE seq_parametrozona;

------------------------------------------------------------------------------
--
-- Las distintas clasificaciones de los tipos de emisiones (IPCC, SNAP...)
--
------------------------------------------------------------------------------

CREATE TABLE tipoclas (
	id		NUMERIC(10)	CONSTRAINT c_tipoclas_id PRIMARY KEY,
	nombre		VARCHAR(100)	CONSTRAINT c_tipoclas_nombre UNIQUE
					NOT NULL,
	descripcion	VARCHAR(1000)
	);

CREATE SEQUENCE seq_tipoclas;

------------------------------------------------------------------------------
--
-- Las clasificaciones en sí.  Cada clasificación es de un tipo y es 
-- jerárquica.  La relación padre-hijo viene dada por el campo idpadre.
-- 
------------------------------------------------------------------------------

CREATE TABLE clasificacion (
	id		NUMERIC(10)	CONSTRAINT c_clasificacion_id PRIMARY KEY,
	idtipoclas	NUMERIC(10)	CONSTRAINT c_clasificacion_idtipoclas
						REFERENCES tipoclas(id)
					NOT NULL,
	idpadre		NUMERIC(10)	CONSTRAINT c_clasificacion_idpadre
						REFERENCES clasificacion(id),
	codigo		VARCHAR(100)	NOT NULL,
	descripcion	VARCHAR(300),

	CONSTRAINT c_clasificacion_idtipoclas_codigo UNIQUE(idtipoclas, codigo)
	);

CREATE SEQUENCE seq_clasificacion;

-----------------------------------------------------------------------------
-- 
-- Tabla para mapear los datos de la clasificación en que se hacen los 
-- cálculos a otra distinta.
-- 
-----------------------------------------------------------------------------

CREATE TABLE equivclasificacion (
	id		NUMERIC(10)	CONSTRAINT c_equivclasificacion_id PRIMARY KEY,
	idclasorig	NUMERIC(10)	CONSTRAINT c_equivclasificacion_idclasorig
						REFERENCES clasificacion(id)
					NOT NULL,
	idclasmap	NUMERIC(10)	CONSTRAINT c_equivcontaminante_idclasmap
						REFERENCES clasificacion(id)
					NOT NULL
	);

CREATE SEQUENCE seq_equivclasificacion;
------------------------------------------------------------------------------
-- 
-- Los distintos motores de cálculo para contaminantes.  Hace referencia a una
-- clase en python responsable de llevar a cabo el cálculo.  La versión 
-- "estándar" es que los contaminantes son una combinación lineal de los datos
-- de entrada.
-- 
------------------------------------------------------------------------------

CREATE TABLE motorcalculo (
	id		NUMERIC(10)	CONSTRAINT c_motorcalculo_id PRIMARY KEY,
	codigo		VARCHAR(20)	CONSTRAINT c_motorcalculo_codigo UNIQUE
					NOT NULL,
	nombre		VARCHAR(100)	CONSTRAINT c_motorcalculo_nombre UNIQUE
					NOT NULL,
	descripcion	VARCHAR(1000),
	clase		VARCHAR(100)
	);

CREATE SEQUENCE seq_motorcalculo;

------------------------------------------------------------------------------
--
-- Los distintos datos que se recogen en cada punto de toma de datos, 
-- normalmente emisión de contaminantes o referentes al tamaño de la 
-- instalación.
--
-- Cada dato está relacionado con un item de la clasificación de datos.
--
-- Se supone que el universo de datos posibles es estable en el marco
-- regulatorio.
--
------------------------------------------------------------------------------
CREATE TABLE dato (
	id		NUMERIC(10)	CONSTRAINT c_dato_id PRIMARY KEY,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_dato_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL,
	descripcion	VARCHAR(1000),
	unidades	VARCHAR(100)	NOT NULL,
	
	CONSTRAINT c_emision_nombre UNIQUE(idclasificacion, nombre)
	);
	
CREATE SEQUENCE seq_dato;

------------------------------------------------------------------------------
--
-- Los diversos contaminantes cuyas emisiones se calcularán a partir de los
-- datos de entrada en cada punto de toma de datos.
--
------------------------------------------------------------------------------

CREATE TABLE contaminante (
	id		NUMERIC(10)	CONSTRAINT c_contaminante_id PRIMARY KEY,
	nombre		VARCHAR(100)	CONSTRAINT c_contaminante_nombre UNIQUE
					NOT NULL,
	descripcion	VARCHAR(1000),
	unidades	VARCHAR(100)	NOT NULL
	);
	
CREATE SEQUENCE seq_contaminante;

------------------------------------------------------------------------------
--
-- Los combustibles para los que es necesario sacar datos desagregados en 
-- el informe
--
------------------------------------------------------------------------------

CREATE TABLE combustible (
	id		NUMERIC(10)	CONSTRAINT c_combustible_id PRIMARY KEY,
	nombre		VARCHAR(100)	NOT NULL
	);

CREATE SEQUENCE seq_combustible;

------------------------------------------------------------------------------
--
-- Las combinaciones clasificación-combustible que requieren tratamiento
-- especial
--
------------------------------------------------------------------------------

CREATE TABLE clascombustible (
	id		NUMERIC(10)	CONSTRAINT c_clascombustible_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_clascombustible_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_clascombustible_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	idcombustible	NUMERIC(10)	CONSTRAINT c_clascombustible_idcombustible
						REFERENCES combustible(id)
					NOT NULL,
	idcontaminante	NUMERIC(10)	CONSTRAINT c_clascombustible_idcontaminante
						REFERENCES contaminante(id)
					NOT NULL,
	reparto		NUMERIC		NOT NULL,
	emisionbase	NUMERIC		NOT NULL,
	va		NUMERIC		NOT NULL,
	fe		NUMERIC		NOT NULL
	);

CREATE SEQUENCE seq_clascombustible;

------------------------------------------------------------------------------
--
-- El parámetro para convertir cada contaminante en emisiones equivalentes
-- de CO2.  Como varía de año en año debido al marco regulatorio, se hace
-- depender del escenario.
--
------------------------------------------------------------------------------

CREATE TABLE equivcontaminante (
	id		NUMERIC(10)	CONSTRAINT c_equivcontaminante_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_equivcontaminante_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	idcontaminante	NUMERIC(10)	CONSTRAINT c_equivcontaminante_idcontaminante
						REFERENCES contaminante(id)
					NOT NULL,
	p		NUMERIC		NOT NULL
	);

CREATE SEQUENCE seq_equivcontaminante;

CREATE TABLE formula (
	id		NUMERIC(10)	CONSTRAINT c_formula_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_formula_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	expresion	VARCHAR(500)	NOT NULL,
	valor		NUMERIC
	);

CREATE SEQUENCE seq_formula;

------------------------------------------------------------------------------
--
-- Tabla de parámetros lineales que utiliza el motor de cálculo estandar para
-- convertir los datos de entrada en contaminantes.  Esta tabla contiene los 
-- parámetros de aplicación general, si bien en algunos puntos de toma de 
-- datos se pueden requerir parámetros especiales que están contenidos en
-- la tabla mapdatocontaminanteaforo
--
------------------------------------------------------------------------------

CREATE TABLE mapdatocontaminante (
	id		NUMERIC(10)	CONSTRAINT c_mapdatocontaminante_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_mapdatocontaminante_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	iddato		NUMERIC(10)	CONSTRAINT c_mapdatocontaminante_iddato
						REFERENCES dato(id),
	idclasificacion	NUMERIC(10)	CONSTRAINT c_mapdatocontaminante_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	idcontaminante	NUMERIC(10)	CONSTRAINT c_mapdatocontaminante_idcontaminante
						REFERENCES contaminante(id),
	idformula	NUMERIC(10)	CONSTRAINT c_mapdatocontaminante_idformula
						REFERENCES formula(id)
					NOT NULL,
	
	CONSTRAINT c_mapdatocontaminante_idescenario_iddato_idclasificacion_idcontaminante 
			UNIQUE(idescenario, iddato, idclasificacion, idcontaminante)
	);
	
CREATE SEQUENCE seq_mapemisioncontaminante;

------------------------------------------------------------------------------
--
-- Las distintas fuentes de datos ("ficheros") que están disponibles.  
-- Varían de año en año, así que depende del escenario.  Cada fuente de datos
-- utiliza un motor de cálculo distinto.
--
------------------------------------------------------------------------------

CREATE TABLE fuente (
	id		NUMERIC(10)	CONSTRAINT c_fuente_id PRIMARY KEY,
	idescenario	NUMERIC(10)	CONSTRAINT c_fuente_idescenario
						REFERENCES escenario(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL,
	descripcion	VARCHAR(1000),
	idorigen	NUMERIC(10)	CONSTRAINT c_fuente_idorigen
						REFERENCES origen(id)
					NOT NULL,
	idmotorcalculo	NUMERIC(10)	CONSTRAINT c_fuente_idmotorcalculo
						REFERENCES motorcalculo(id)
					NOT NULL,
	idnivelzona	NUMERIC(10)	CONSTRAINT c_fuente_idnivelzona
						REFERENCES nivelzona(id),
	idtipodatozona	NUMERIC(10)	CONSTRAINT c_fuente_idtipodatozona
						REFERENCES tipodatozona(id)

	CONSTRAINT c_fuente_nombre UNIQUE(idescenario, nombre)
	);
	
CREATE SEQUENCE seq_fuente;

------------------------------------------------------------------------------
--
-- Items de la clasificación SNAP o IPCC a la que se adscriben los puntos
-- de toma de datos de cada fuente.  Estos items definen el conjunto de datos
-- que se tomarán en cada punto.
--
------------------------------------------------------------------------------

CREATE TABLE fuenteclasificacion (
	id		NUMERIC(10)	CONSTRAINT c_fuenteclasificacion_id PRIMARY KEY,
	idfuente	NUMERIC(10)	CONSTRAINT c_fuenteclasificacion_idfuente
						REFERENCES fuente(id)
					NOT NULL,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_fuenteclasificacion_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL
	);

CREATE SEQUENCE seq_fuenteclasificacion;

------------------------------------------------------------------------------
--
-- Conjunto de puntos de toma de datos.
--
------------------------------------------------------------------------------
	
CREATE TABLE aforo (
	id		NUMERIC(10)	CONSTRAINT c_aforo_id PRIMARY KEY,
	idfuente	NUMERIC(10)	CONSTRAINT c_aforo_idfuente 
						REFERENCES fuente(id)
					NOT NULL,
	nombre		VARCHAR(100)	NOT NULL,
	descripcion	VARCHAR(1000),
	escala		NUMERIC		NOT NULL,
	idzona		NUMERIC(10)	CONSTRAINT c_aforo_idzona 
						REFERENCES zona(id),
	idtipodatozona	NUMERIC(10)	CONSTRAINT c_aforo_idtipodatozona
						REFERENCES tipodatozona(id),
	
	CONSTRAINT c_aforo_nombre UNIQUE(idfuente, nombre)
	);
	
CREATE SEQUENCE seq_aforo;
CREATE INDEX i_aforo_idfuente ON aforo(idfuente);

-----------------------------------------------------------------------------
--
-- Valor específico de parámetros por aforo
--
-----------------------------------------------------------------------------

CREATE TABLE parametroaforo (
	id		NUMERIC(10)	CONSTRAINT c_parametroaforo_id PRIMARY KEY,
	idaforo		NUMERIC(10)	CONSTRAINT c_parametroaforo_idaforo
						REFERENCES aforo(id)
					NOT NULL,
	idparametro	NUMERIC(10)	CONSTRAINT c_parametroaforo_idparametro
						REFERENCES parametro(id)
					NOT NULL,
	valor		NUMERIC,

	CONSTRAINT c_parametroaforo_idaforo_idparametro 
				UNIQUE(idaforo, idparametro)
	);

CREATE SEQUENCE seq_parametroaforo;

-----------------------------------------------------------------------------
--
-- Valores de emisión validados para un contaminante y que no se deben
-- calcular.
--
-----------------------------------------------------------------------------

CREATE TABLE contaminantevalidadoaforo (
	id		NUMERIC(10)	CONSTRAINT c_contaminantevalidadoaforo_id PRIMARY KEY,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_contaminantevalidadoaforo_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	idaforo		NUMERIC(10)	CONSTRAINT c_contaminantevalidadoaforo_idaforo
						REFERENCES aforo(id)
					NOT NULL,
	idcontaminante	NUMERIC(10)	CONSTRAINT c_contaminantevalidadoaforo_idcontaminante
						REFERENCES contaminante(id)
					NOT NULL,
	valor		NUMERIC		NOT NULL,

	CONSTRAINT c_contaminantevalidadoaforo_idclasificacion_idaforo_idcontaminante
			UNIQUE(idclasificacion, idaforo, idcontaminante)
	);

CREATE SEQUENCE seq_contaminantevalidadoaforo;

------------------------------------------------------------------------------
--
-- Valores tomados en cada aforo.  Deben corresponder a los distintos valores 
-- definidos para los item de clasificación asociados a su fuente.
--
------------------------------------------------------------------------------

CREATE TABLE valordato (
	id		NUMERIC(10)	CONSTRAINT c_valordato_id PRIMARY KEY,
	idaforo		NUMERIC(10)	CONSTRAINT c_valordato_idaforo
						REFERENCES aforo(id)
					NOT NULL,
	iddato		NUMERIC(10)	CONSTRAINT c_valordato_iddato
						REFERENCES dato(id)
					NOT NULL,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_valordato_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	valor		NUMERIC		NOT NULL,
	
	CONSTRAINT c_valordato_idaforo_iddato UNIQUE(idaforo, iddato)
	);
	
CREATE SEQUENCE seq_valordato;
CREATE INDEX i_valordato_idaforo ON valordato(idaforo);

------------------------------------------------------------------------------
--
-- Contaminantes emitidos en cada punto de toma de datos, calculados a partir
-- de los datos de la tabla valordato por aplicación del motor de cálculo
-- correspondiente.  Las emisiones se detallan por contaminante, punto de 
-- toma de datos y clasificación del dato que lo origina.
--
------------------------------------------------------------------------------

CREATE TABLE contaminanteaforo (
	id		NUMERIC(10)	CONSTRAINT c_contaminanteaforo_id PRIMARY KEY,
	idcontaminante	NUMERIC(10)	CONSTRAINT c_contaminanteaforo_idcontaminante
						REFERENCES contaminante(id)
					NOT NULL,
	idaforo		NUMERIC(10)	CONSTRAINT c_contaminanteaforo_idaforo
						REFERENCES aforo(id)
					NOT NULL,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_contaminanteaforo_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	valor		NUMERIC		NOT NULL,
	
	CONSTRAINT c_contaminanteaforo_idaforo_idclasificacion_idcontaminante 
			UNIQUE(idaforo, idclasificacion, idcontaminante)
	);
	
CREATE SEQUENCE seq_contaminanteaforo;

------------------------------------------------------------------------------
--
-- Matriz para calcular la contribución de contaminantes de cada punto de toma 
-- de datos a cada zona.  Por ejemplo, la contribución de una carretera a los
-- municipios por los que pasa.  Sólo se considerarán las zonas de menor
-- nivel (municipìos), el resto se calculará por agregación.
--
------------------------------------------------------------------------------

CREATE TABLE mapaforozona (
	id		NUMERIC(10)	CONSTRAINT c_mapaforozona PRIMARY KEY,
	idaforo		NUMERIC(10)	CONSTRAINT c_mapaforozona_idaforo
						REFERENCES aforo(id)
					NOT NULL,
	iddato		NUMERIC(10)	CONSTRAINT c_mapaforozona_iddato
						REFERENCES dato(id),
	idzona		NUMERIC(10)	CONSTRAINT c_mapaforozona_idzona
						REFERENCES zona(id)
					NOT NULL,
	p		NUMERIC		NOT NULL
	);
	
CREATE UNIQUE INDEX i_mapaforozona_idaforo_idzona ON mapaforozona (idaforo, idzona, iddato);
CREATE SEQUENCE seq_mapaforozona;

------------------------------------------------------------------------------
--
-- Emisiones de contaminantes por zona, clasificadas por fuente ("ficheros"), 
-- clasificación (SNAP, IPCC) y contaminante.
--
------------------------------------------------------------------------------

CREATE TABLE contaminantezona (
	id		NUMERIC(10)	CONSTRAINT c_contaminantezona_id PRIMARY KEY,
	idcontaminante	NUMERIC(10)	CONSTRAINT c_contaminantezona_idcontaminante
						REFERENCES contaminante(id)
					NOT NULL,
	idfuente	NUMERIC(10)	CONSTRAINT c_contaminantezona_idfuente
						REFERENCES fuente(id)
					NOT NULL,
	idzona		NUMERIC(10)	CONSTRAINT c_contaminantezona_idzona
						REFERENCES zona(id)
					NOT NULL,
	idclasificacion	NUMERIC(10)	CONSTRAINT c_contaminantezona_idclasificacion
						REFERENCES clasificacion(id)
					NOT NULL,
	valor		NUMERIC		NOT NULL,
	
	CONSTRAINT c_contaminantezona_idfuente_idzona_idclasificacion_idcontaminante 
			UNIQUE(idfuente, idzona, idclasificacion, idcontaminante)
	);
	
CREATE SEQUENCE seq_contaminantezona;
CREATE INDEX i_contaminantezona_idcontaminante ON contaminantezona(idcontaminante);

