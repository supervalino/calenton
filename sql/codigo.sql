------------------------------------------------------------------------------
--  CALENTON
--
--  (C) Trustserver SL, 2009-2010
--  (C) LITEC, 2009-2010
--
--  Este paquete ha sido desarrollado por Trustserver S. L. para el 
--  Laboratorio de Investigación en Tecnologías de la Combustión (LITEC)
--
--  $Id: codigo.sql 230 2010-04-29 10:46:41Z bruno $
--  $URL: https://www.litec.csic.es/svn/emisiones/trunk/sql/codigo.sql $
------------------------------------------------------------------------------

SET CLIENT_ENCODING = 'UTF8';

------------------------------------------------------------------------------
--
-- Devuelve una fila para cada clasificación a la que pertenece el nodo 
-- cuyo id es idorigen.
--
-- Las filas devueltas tienen un sólo elemento que es el id.
-- 
-- La primera fila es el propio idorigen.
--
------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION jerarquia_clasificacion (
	idorigen	clasificacion.id%TYPE
	) 
	RETURNS SETOF clasificacion.id%TYPE AS
$BODY$
DECLARE 
	ide	clasificacion.id%TYPE;
BEGIN
	ide := idorigen;
	LOOP
		RETURN NEXT ide;
		SELECT idpadre INTO ide 
			FROM clasificacion 
			WHERE id = ide;
		EXIT WHEN NOT FOUND;
	END LOOP;
	RETURN;
END;
$BODY$
LANGUAGE plpgsql;

------------------------------------------------------------------------------
-- 
-- Trigger para garantizar que las tuplas (idaforo, idzona, iddato) son únicas
-- en la tabla mapaforozona.  Incluye el caso en que iddato es NULL.
--
------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION before_mapaforozona() 
	RETURNS trigger AS
$BODY$
DECLARE
	idm	BOOLEAN;
BEGIN
	idm := EXISTS (SELECT 1
			FROM mapaforozona m
			WHERE (NEW.id IS NULL OR NEW.id <> m.id) AND
				NEW.idzona = m.idzona AND
				NEW.idaforo = m.idaforo AND
				(NEW.iddato = m.iddato OR
					(NEW.iddato IS NULL AND 
					m.iddato IS NULL)));
	IF idm THEN
		RAISE EXCEPTION 'No se pueden introducir dos mapeos para el mismo caso en mapaforozona';
	END IF;
	RETURN NEW;
END;
$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER before_mapaforozona 
	BEFORE INSERT OR UPDATE ON mapaforozona
	FOR EACH ROW EXECUTE PROCEDURE before_mapaforozona();

CREATE OR REPLACE FUNCTION get_contaminante (
	idcontaminante	contaminante.id%TYPE
	) RETURNS contaminante.nombre%TYPE AS
$BODY$
DECLARE
	res	contaminante.nombre%TYPE;
BEGIN
	SELECT nombre INTO res
		FROM contaminante
		WHERE id = idcontaminante;
	RETURN res;
END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_clasificacion (
	idclasificacion	clasificacion.id%TYPE
	) RETURNS clasificacion.codigo%TYPE AS
$BODY$
DECLARE
	res	clasificacion.codigo%TYPE;
BEGIN
	SELECT codigo INTO res
		FROM clasificacion
		WHERE id = idclasificacion;
	RETURN res;
END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_dato (
	iddato	dato.id%TYPE
	) RETURNS dato.nombre%TYPE AS
$BODY$
DECLARE
	res	dato.nombre%TYPE;
BEGIN
	SELECT nombre INTO res
		FROM dato
		WHERE id = iddato;
	RETURN res;
END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_escenario (
	idescenario	escenario.id%TYPE
	) RETURNS escenario.nombre%TYPE AS
$BODY$
DECLARE
	res	escenario.nombre%TYPE;
BEGIN
	SELECT nombre INTO res
		FROM escenario
		WHERE id = idescenario;
	RETURN res;
END;
$BODY$
LANGUAGE plpgsql;

------------------------------------------------------------------------------
-- 
-- Trigger para garantizar que las tuplas (idescenario, idclasificacion, 
-- iddato, idcontaminante) son únicas en la tabla mapdatocontaminante.  
-- Incluye el caso en que iddato es NULL.
--
------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION before_mapdatocontaminante() 
	RETURNS trigger AS
$BODY$
DECLARE
	idm	BOOLEAN;
	msg	TEXT;
BEGIN
	idm := EXISTS (SELECT 1
			FROM mapdatocontaminante m
			WHERE (NEW.id IS NULL OR NEW.id <> m.id) AND
				NEW.idescenario = m.idescenario AND
				NEW.idcontaminante = m.idcontaminante AND
				NEW.idclasificacion = m.idclasificacion AND
				(NEW.iddato = m.iddato OR
					(NEW.iddato IS NULL AND 
					m.iddato IS NULL)));
	IF idm THEN
		RAISE EXCEPTION 'No se puede introducir mapeo para mapdatocontaminante con idescenario = % (%), idclasificacion = % (%), idcontaminante = % (%), iddato = % (%)',
			NEW.idescenario, get_escenario(NEW.idescenario), NEW.idclasificacion, get_clasificacion(NEW.idclasificacion), 
			NEW.idcontaminante, get_contaminante(NEW.idcontaminante), NEW.iddato, get_dato(NEW.iddato);
	END IF;
	RETURN NEW;
END;
$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER before_mapdatocontaminante 
	BEFORE INSERT OR UPDATE ON mapdatocontaminante
	FOR EACH ROW EXECUTE PROCEDURE before_mapdatocontaminante();

