Dataportal: area privata
========================

L'area privata del Dataportal è disponibile all'indirizzo `dataportal-private.daf.teamdigitale.it <https://dataportal-private.daf.teamdigitale.it/>`__. 

Gli utenti hanno la possibilità di registrarsi per avere accesso all'area privata del Dataportal e, conseguentemente, agli strumenti di analisi messi a disposizione dalla piattaforma.

.. figure:: _img/dataportal-private.png
   :scale: 50 %

   Area privata del Dataportal.


L'idea è quella di fornire alle Pubbliche Amministrazioni e alla community di utilizzatori un insieme di strumenti per l'analisi e l'accesso ai dati contenuti nel DAF, chiaramente preservando i diritti di accesso associati alle varie utenze.

Dopo aver effettuato la `registrazione e il login <accesso.html>`__, nell'area privata è possibile [1]_:

* Accedere al cruscotto utile alla `registrazione di nuovi dataset <dataset.html>`_. La procedura guidata facilita una completa metadatazione in conformità al profilo DCAT-AP_IT; i metadati sono arricchiti con informazioni sulla struttura del dato e relativa semantica [2]_.

* Creare e pubblicare :ref:`Dashboard <dashboard>`, ovvero un insieme di grafici creati con gli strumenti messi a disposizione dal DAF.

* Creare e pubblicare :ref:`Storie <storie>` (*data stories*), ovvero dei blog post in cui è possibile inserire nativamente risultati di analisi svolte con gli strumenti messi a disposizione dal DAF.

* Utilizzare `Jupyter Notebook <../datascience/jupyter/index.html>`_ integrato con il cluster big data del DAF, con cui effettuare analisi esplorative iniziali fino a complessi modelli di machine learning.

* Accedere allo `strumento di business intelligence (Superset) <../datascience/superset/index.html>`_ e strumenti più orientati alla `data visualization (Metabase) <../datascience/metabase.html>`_. I risultati delle analisi svolte con questi strumenti possono essere integrati nativamente nelle Data Story e nelle Dashboard.

Le pubbliche amministrazioni registrate potranno inoltre usufruire di strumenti avanzati di `gestione degli utenti <organization.html>`_.

.. rubric:: Operazioni e strumenti dell'area privata del Dataportal

.. toctree::
   :maxdepth: 1
   
   Registrazione e accesso all'area privata <accesso>
   Gestione dei dataset <dataset>
   Dashboard e storie <dashboard>
   Gestione degli utenti <organization>
   Modalità di impiego dell'API REST <api>

.. [1] Elenco non esaustivo e in evoluzione.
.. [2] Al momento questa funzionalità è offerta solo alle Pubbliche Amministrazioni
