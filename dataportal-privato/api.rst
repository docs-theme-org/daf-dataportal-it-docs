*********************************
Modalità di impiego dell'API REST
*********************************

A ogni dataset caricato sul DAF è associato un API endpoint che permette l'interazione con lo stesso in via programmatica. L'endpoint è mostrato nella pagina di dettaglio del dataset, e assume la forma:

``https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/<dataset_name>``

È possibile richiamarlo previa autenticazione (basic) utilizzando l'indirizzo email associato al proprio account.


====================
Download del dataset
====================

È possibile effettuare lo scarico del dataset (in formato JSON) effettuando una richiesta HTTP GET alla URL associata.

Ad esempio: https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/daf%3A%2F%2Fdataset%2Fdefault_org%2FGOVE__amministrazione%2Fistat_elenco_comuni_italiani


===========================
Recupero del dataset schema
===========================

Richiamare (HTTP GET) l'endpoint aggiungendo il suffisso ``/schema``. 

Ad esempio: https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/daf%3A%2F%2Fdataset%2Fdefault_org%2FGOVE__amministrazione%2Fistat_elenco_comuni_italiani/schema


==========================
Interrogazione del dataset 
==========================

Richiamare l'endpoint in HTTP POST aggiungendo alla url il suffisso ``/search``. 

Ad esempio: https://api.daf.teamdigitale.it/dataset-manager/v1/dataset/daf%3A%2F%2Fdataset%2Fdefault_org%2FGOVE__amministrazione%2Fistat_elenco_comuni_italiani/search

Nel corpo della richiesta fornire un oggetto json per specificare le proprietà di interesse, e le condizioni di filtro e raggruppamento:

.. code-block:: json

   {
   	"select": ["denominazione_corrente", "denominazione_regione", "denominazione_citta_metropolitana", "sigla_automobilistica", "codice_comune_formato_alfanumerico", "codice_catastale_del_comune", "popolazione_legale_2011"],
   	"where": ["denominazione_regione = 'Piemonte'"],
   	"groupby": [""]
   }
