*********************************
Modalità di impiego dell'API REST
*********************************

A ogni dataset caricato sul DAF è associato un API endpoint che permette l'interazione con lo stesso in via programmatica. L'endpoint è mostrato nella pagina di dettaglio del dataset, e assume la forma:

``https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/<dataset_logical_url>``

È possibile richiamarlo previa autenticazione (basic) utilizzando l'indirizzo email associato al proprio account.


====================
Download del dataset
====================

È possibile effettuare lo scarico del dataset (bulk download) con una richiesta ``HTTP GET`` alla URL ad esso associata.

	Ad esempio: https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/daf%3A%2F%2Fdataset%2Fdefault_org%2FGOVE__amministrazione%2Fistat_elenco_comuni_italiani

Di default la chiamata restituisce i primi 1.000 record del dataset in formato JSON. E' comunque possibile specificare i seguenti parametri in *query string*:

- ``limit`` per limitare il numero di record restituiti, indicare un valore numerico non superiore al massimo consentito (1.000)
- ``format`` per specificare il formato dei dati restituiti, valori possibili: ``json`` (default) e ``csv``
- ``method`` per specificare il metodo di download, valori possibili ``quick`` (default) e ``batch``. La prima è soggetta alla limitazione sul numero di record restituiti, la seconda invece nel caso di dataset molto grandi restituisce una redirect per lo scarico dell'intero file

===========================
Recupero del dataset schema
===========================

Richiamando (in ``HTTP GET``) l'endpoint col suffisso ``/schema``, si possono ottenere informazioni sullo schema del dataset.

Ad esempio: https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/daf%3A%2F%2Fdataset%2Fdefault_org%2FGOVE__amministrazione%2Fistat_elenco_comuni_italiani/schema


==========================
Interrogazione del dataset 
==========================

Richiamare l'endpoint in ``HTTP POST`` aggiungendo alla url il suffisso ``/search``. 

Ad esempio: https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/daf%3A%2F%2Fdataset%2Fdefault_org%2FGOVE__amministrazione%2Fistat_elenco_comuni_italiani/search

L'API è ottimizzata per dataset con una struttura colonnare (csv), il supporto ai json è al momento consente l'interazione solo con gli elementi di primo livello.

Una query può essere composta di un insieme di clausole, scelte tra le seguenti supportate:

1. select
2. where
3. groupBy
4. having
5. limit

Le clausole rappresentano le proprietà complesse dell'oggetto json che deve essere inserito nel corpo della richiesta, che quindi assume la forma mostrata di seguito:

.. code-block:: json

	{
		"select": ...,
		"where": ...,
		"groupBy": ...,
		"having": ...,
		"limit": ...
	}

Di seguito vengono dettagliate le singole proprietà.

SELECT
------

Permette di indicare i campi (colonne) di interesse del dataset ed eventualmente l'alias. La proprietà ``select`` accetta come valore una lista di oggetti del tipo: ``{ "name": "col2", "alias": "alias_col2" }``. Come valore di ``name`` è ammesso l'uso del carattere ``*``. La lista può essere vuota, in tal caso si assume l'estrazione di tutte le colonne (come con l'uso del ``*``)

Esempio: selezione della colonna ``col1`` e della colonna ``col2`` con alias ``alias_col2`` 

.. code-block:: json

	{
		"select": [
			{ "name": "col1" }, 
			{ "name": "col2", "alias": "alias_col2" }
		]
	}

è equivalente a 

.. code-block:: sql

	SELECT col1, col2 AS alias_col2
	FROM table


E' anche possibile rappresentare una colonna contenente un valore costante utilizzando un oggetto del tipo ``{ "value": 1, "alias": "one_alias" }``, con alias sempre opzionale.

Esempio: 

.. code-block:: json

	{
		"select": [
			{ "value": "string" }, 
			{ "value": 1, "alias": "one_alias" }
		]
	}

è equivalente a 

.. code-block:: sql

	SELECT 'string', 1 AS one_alias
	FROM table


WHERE
-----

Permette di indicare condizioni di filtro mediante l'uso di operatori logici e di confronto. La proprietà ``where`` accetta come valore un oggetto composto da uno o più operatori, a seconda della complessità del filtro, scelti tra quelli:

- logici
	- unario di negazione ``not``: accetta come valore un oggetto
	- ``and`` e ``or``: accettano come valore una lista di oggetti
- binari di confronto: accettano come valore un oggetto composto dalle proprietà ``left`` e ``right`` relativi ai due elementi di confronto
	- ``gt`` (maggiore strettamente di)
	- ``gte`` (maggiore o uguale di)
	- ``lt`` (minore strettamente di)
	- ``lte`` (minore o uguale di)
	- ``eq`` (uguale a)
	- ``neq`` (non uguale a)

Gli operatori logici possono essere innestati tra di loro per creare filtri complessi.
E' possibile confrontare tra loro due colonne o una colonna con una costante.

Esempio:

.. code-block:: json

	{
		"where": {
			"not": {
				"and": [
					{
						"or": [
							{"gt": { "left": "col1", "right": "col2" }}, 
							{"eq": { "left": "col3", "right": false }}
						]
					}, 
					{
						"neq": { "left": "col4", "right": "'string'" }
					}
				]
			}
		}
	}

è equivalente a 

.. code-block:: sql

	SELECT *
	FROM table
	WHERE NOT (
			col1 > col2 
		 OR col3 == false
		AND col4 <> 'string'
	)

Nota: effettuare l'escaping delle costanti testuali con ``\"`` o usare il delimitatore ``'``


GROUP BY
--------

Permette di indicare condizioni di raggruppamento per il calcolo di valori aggregati. La proprietà ``groupBy`` accetta come valore una lista non vuota di oggetti del tipo: ``{"name": "col2"}``. Gli operatori di aggregazione attualmente supportati sono ``min``, ``max``, ``count``, ``sum`` e ``avg``.

Esempio:

.. code-block:: json

	{
		"select": [
			{ "name": "col1" },
			{ "name": "col2" },
			{
				"max": { "name": "col3"}, "alias": "max_col3" }
			}, 
			{
				"count": { "name": "*" }
			}
		],
		"groupBy": [
			{ "name": "col1" }, 
			{ "name": "col2" }
		]
	}

è equivalente a 

.. code-block:: sql

	SELECT col1, col2, MAX(col3) AS max_col3, COUNT(*)
	FROM table
	GROUP BY col1, col2

HAVING
------

Permette di specificare clausole having se presente un raggruppamento. La proprietà ``having`` accetta come valore una lista non vuota di oggetti del tipo impiegato per esplicitare condizioni di filtro.

Esempio:

.. code-block:: json

	{
		"select": [
			{ "name": "col1" },
			{ "name": "col2" },
			{
				"max": { "name": "col3", "alias": "max_col3" }
			}, 
			{
				"count": { "name": "*" }
			}
		],
		"groupBy": [
			{ "name": "col1" }, 
			{ "name": "col2" }
		],
		"having": [
			{ 
				"gt": { "left": "max_col3", "right": 50 } 
			}
		]
	}

è equivalente a 

.. code-block:: sql

	SELECT col1, col2, MAX(col3) AS max_col3, COUNT(*)
	FROM table
	GROUP BY col1, col2
	HAVING max_col3 > 50


LIMIT
-----

Permette di specificare il numero massimo di elementi restituiti. La proprietà ``limit`` accetta un valore numerico.

Esempio:

.. code-block:: json

	{
		"limit": 5
	}

è equivalente a 

.. code-block:: sql

	SELECT *
	FROM table
	LIMIT 5
