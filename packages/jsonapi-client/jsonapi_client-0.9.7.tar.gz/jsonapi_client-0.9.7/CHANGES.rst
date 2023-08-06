CHANGELOG
=========

0.9.7 (2019-02-01)
------------------

- Support __getitem__ in Meta
- Handle empty relationship data list
- Allow returning link to relationship as an iterator
- Fix handling null one-to-one-relationship
- Don't explicitly quote filter values
- Include support

0.9.6 (2017-06-26)
------------------

 - When creating new resources, use default value specified in
   jsonschema, when available.


0.9.5 (2017-06-16)
------------------

 - Change Session.create_and_commit signature similarly as Session.create

0.9.4 (2017-06-16)
------------------

 - Remove ? from filenames (illegal in Windows)
 - Pass event loop aiohttp's ClientSession
 - Return resource from .commit if return status is 202
 - Support underscores in field names in Session.create() through fields keyword argument.
 - Add support for extra arguments such as authentication object
 - AsyncIO support for context manager usage of Session


0.9.3 (2017-04-03)
------------------

 - Added aiohttp to install requirements


0.9.2 (2017-04-03)
------------------

 - Github release.


0.9.1 (2017-03-23)
------------------

 - Fix async content_type checking
 - Use Python 3's new typing.NamedTuple instead of collections.NamedTuple
 - Make included resources available from Document
 - ResourceObject.json property
