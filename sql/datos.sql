
SET CLIENT_ENCODING='UTF8';

insert into motorcalculo (id, codigo, nombre, clase)
values (nextval('seq_motorcalculo'), 'LINEAL', 'Parámetros lineales', 'ParamLineal');
insert into tipoclas (id, nombre, descripcion)
values (nextval('seq_tipoclas'), 'SNAP', 'Código SNAP');

