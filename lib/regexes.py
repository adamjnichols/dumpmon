import re

regexes = {
    'email': re.compile(r'[A-Z0-9._%+-]+@(?:domain1|domain2|domain3)\.[A-Z]{2,4}', re.I),
    #'ssn' : re.compile(r'\d{3}-?\d{2}-?\d{4}'),
    #'lulz': re.compile(r'(lulzsec|antisec)', re.I),
    'blacklist': [  # I was hoping to not have to make a blacklist, but it looks like I don't really have a choice
    re.compile(
    r'(select\s+.*?from|join|declare\s+.*?\s+as\s+|update.*?set|insert.*?into)', re.I),  # SQL
        re.compile(
            r'(define\(.*?\)|require_once\(.*?\))', re.I),  # PHP
        re.compile(
            r'(function.*?\(.*?\))', re.I),
        re.compile(
            r'(Configuration(\.Factory|\s*file))', re.I),
        re.compile(
            r'((border|background)-color)', re.I),  # Basic CSS (Will need to be improved)
        re.compile(
            r'(Traceback \(most recent call last\))', re.I),
        re.compile(
            r'(java\.(util|lang|io))', re.I),
        re.compile(r'(sqlserver\.jdbc)', re.I)
    ],
    # The banlist is the list of regexes that are found in crash reports
    'banlist': [
        re.compile(r'faf\.fa\.proxies', re.I),
        re.compile(r'Technic Launcher is starting', re.I),
        re.compile(r'TDSS rootkit removing tool', re.I),
        re.compile(r'INFO: Processing cookbook_file', re.I),
        re.compile(r'loading\.target\.rdio', re.I),
        re.compile(r'<key>SysInfoCrashReporterKey</key>', re.I)
    ]
}
