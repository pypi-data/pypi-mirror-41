Pyrlamento
==========

Government information wrapper
******************************

This library is an interface between your program and the various legal systems.
It is still very very bare (only works with the portuguese Diário da República),
yet its aim is to work seamlessly with other systems as needed.

Ideally you'd specify the country and what you want, and you'd have it.

This should eventually be able to retrieve
------------------------------------------
- Laws
- Public legal documents
- Profiles of politicians
- Other information within the public interest.

Supported countries
-------------------
- Portugal (Laws and document URLs only)

Usage
-----
::

    from pyrlamento import Pyrlamento
    from datetime import date
    pyrlamento = Pyrlamento('countries.portugal')
    publications = pyrlamento.publicationsdDate(2019, 1, 1), date(2019, 2, 1))
    diploma = pyrlamento.diploma(1234567890)