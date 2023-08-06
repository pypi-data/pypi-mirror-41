This is an extension module for `imaplib`. The functions of 'copy', 'search', 'fetch', 'store', and possibly others, in the standard `imaplib` module do not return unique-identifier message numbers in their number sets, which makes interaction with messages via 'store' a little bit more difficult, and can result in the wrong messages being adjusted. This extension module is designed to override the 'copy', 'search', 'fetch', and 'store' functions and provide UID-based commands, by using the `uid` command and passing UID-format commands for the functions that are overridden.


