# ProteinDB

A small demo of how to use sqlite in python and BioPy to ready fasta files and put them in databases.  

Provides a ProteinDB class that can be populated with fasta files and queried by uniprot id and sequence.

## Installation


## Usage

```python
from proteindb import ProteinDB
>> db = ProteinDB()

>> db.populate('uniprot1.fasta')

>> db.query(uniprot_id='DFAFDA1')
>> db.result
'SDFYUONNAJDMAMDFHAABWQ'

>> db.query(sequence='SDFYUONNAJDMAMDFHAABWQ')
>> db.result
'DFAFDA1'

```  