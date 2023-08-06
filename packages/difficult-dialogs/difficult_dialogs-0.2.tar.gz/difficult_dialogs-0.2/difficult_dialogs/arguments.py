from os.path import join, isdir
from os import listdir

from difficult_dialogs.premises import Premise
from difficult_dialogs.statements import Statement
from difficult_dialogs.exceptions import MissingStatementException, \
    MissingAssertionException, BadAssertionJson, UnrecognizedStatementFormat, \
    UnrecognizedSourceFormat, UnrecognizedArgumentFormat, BadArgumentJson, \
    UnrecognizedConclusionFormat, UnrecognizedIntroFormat, \
    UnrecognizedDescriptionFormat


class Argument(object):
    def __init__(self, description="", premises=None, intro="",
                 conclusion="", path=None):
        self._premises = premises or {}
        self.description = description
        self.conclusion_statement = conclusion
        self.intro_statement = intro
        self.path = path
        if path:
            self.load()

    def _validate_premise(self, premise):
        try:
            premise = self.add_premise(premise)
            return premise.description
        except Exception as e:
            print(e)
            return ""

    def add_premise(self, premise):
        """ add an premise to this argument

        premise should be an Premise object

        if premise is a string, an premise will be created from it

        if premise is a dictionary, an premise will be created from data

        if premise is a list, an premise will be created with list as statements

        """
        if isinstance(premise, dict):
            premise = Premise("dummy").from_json(premise)
            if premise.description == "dummy":
                raise BadAssertionJson("no premise text given")
        elif isinstance(premise, str):
            premise = Premise(premise)
        elif isinstance(premise, list):
            if len(premise):
                for s in premise:
                    if not isinstance(s, str) and not isinstance(s, Statement):
                        raise UnrecognizedStatementFormat("Tried to create "
                                                          "an premise from invalid statements list")
                text = premise[0]
                statements = premise[1:]
                premise = Premise(text, statements)
            else:
                raise MissingStatementException("Empty Statements list "
                                                "provided")
        if not isinstance(premise, Premise):
            raise MissingAssertionException("Tried to add a non Premise "
                                            "object")

        if premise.description not in self._premises:
            self._premises[premise.description] = premise
        else:
            self._premises[premise.description].update(premise)
        return self._premises[premise.description]

    def add_support(self, support_statement, premise):
        """
        adds a support statement to an premise of this argument

        premise will be created or modified

        support_statememt may be a string, Statement, list of strings or
        list of Statements
        """
        txt = self._validate_premise(premise)
        if not txt:
            raise MissingAssertionException("tried to add support statement "
                                            "to non existing Premise")

        if not isinstance(support_statement, list):
            support_statement = [support_statement]
        for s in support_statement:
            if not isinstance(s, Statement) and not isinstance(s, str):
                raise UnrecognizedStatementFormat("Tried to create a "
                                                  "statement from bad input "
                                                  "type: " + str(type(s)))
            self._premises[txt].add_support_statement(s)

    def add_statement(self, statement, premise):
        """
        adds a statement to an premise of this argument

        premise will be created or modified

        statement may be a string, Statement, list of strings or list of Statements
        """

        txt = self._validate_premise(premise)
        if not txt:
            raise MissingAssertionException("tried to add statement to non "
                                            "existing Premise")

        if not isinstance(statement, list):
            statement = [statement]
        for s in statement:
            if not isinstance(s, Statement) and not isinstance(s, str):
                raise UnrecognizedStatementFormat("Tried to create a "
                                                  "statement from bad input "
                                                  "type: " + str(type(s)))
            self._premises[txt].add_statement(s)

    def add_source(self, source, premise):
        """
        adds a source to an premise of this argument

        premise will be created or modified

        source may be a string or list of strings
        """

        txt = self._validate_premise(premise)
        if not txt:
            raise MissingAssertionException("tried to add source to non "
                                            "existing Premise")

        if not isinstance(source, list):
            source = [source]
        for s in source:
            if not isinstance(s, str):
                raise UnrecognizedSourceFormat
            self._premises[txt].add_source(s)

    def agree(self):
        """ flag all premises as True """

        for a in self._premises:
            self._premises[a].agree()

    def set_description(self, text):
        """ set argument description from string"""
        if not isinstance(text, str):
            raise UnrecognizedDescriptionFormat("description of an Argument "
                                                "must be a string")
        self.description = text

    def set_intro(self, text):
        """ set argument introduction from string or Statement """
        if isinstance(text, str):
            text = Statement(text)
        if not isinstance(text, Statement):
            raise UnrecognizedIntroFormat("introductions must be Statements")
        self.intro_statement = text

    def set_conclusion(self, text):
        """ set argument conclusion from string or Statement """
        if isinstance(text, str):
            text = Statement(text)
        if not isinstance(text, Statement):
            raise UnrecognizedConclusionFormat("conclusions must be "
                                               "Statements")
        self.conclusion_statement = text

    def load(self, path=None):
        """ load argument from directory """
        if not path:
            path = self.path

        if not path:
            return
        elif not isdir(path):
            return

        self.path = path
        self.description = self.description or path.split("/")[-1]
        files = listdir(path)
        for f in files:
            a = f.split(".")[0]

            with open(join(path, f), "r") as fi:
                if ".premise" in f:
                    self.add_premise(
                        Premise(description=a, statements=fi.readlines()))
                elif ".support" in f:
                    self.add_support(fi.readlines(), a)
                elif ".source" in f:
                    self.add_source(fi.readlines(), a)
                elif ".conclusion" in f:
                    with open(join(path, f), "r") as fi:
                        self.set_conclusion(" ".join(fi.readlines()))
                elif ".intro" in f:
                    with open(join(path, f), "r") as fi:
                        self.set_intro(" ".join(fi.readlines()))

    @property
    def intro(self):
        """ objective of this argument """
        return self.intro_statement

    @property
    def conclusion(self):
        """ conclusion of this argument """
        return self.conclusion_statement

    @property
    def is_true(self):
        """ Arguments are true if all their premises are true """
        for s in self.assertions:
            if not s.is_true:
                return False
        return True

    @property
    def as_json(self):
        return {"intro": self.intro_statement.text,
                "conclusion": self.conclusion_statement.text,
                "premises": [s.as_json for s in self.assertions],
                "is_true": self.is_true}

    def update(self, argument):
        """
        argument can be an Argument object or a dictionary with a "premises" field

        if argument is a list, each item will be added recursively

        premises will be updated or created

        """
        if isinstance(argument, Argument):
            for a in argument.assertions:
                self.add_premise(a)
        elif isinstance(argument, dict):
            assertions = argument.get("premises", [])
            if not len(assertions):
                raise BadArgumentJson("no premises provided")

            for a in assertions:
                self.add_premise(a)

        elif isinstance(argument, list):
            for a in argument:
                self.update(a)

        else:
            raise UnrecognizedArgumentFormat(
                "could not merge invalid argument type: " +
                str(type(argument)))

    @property
    def assertions(self):
        """ list of Premise objects in this Argument """
        bucket = []
        for a in self._premises:
            bucket.append(self._premises[a])
        return bucket

    @property
    def statements(self):
        """ list of Statement objects from all premises in this Argument """
        bucket = []
        for a in self._premises:
            bucket += self._premises[a].statements
        return bucket

    @property
    def support_statements(self):
        """ list of Statement objects from all premises in this Argument """
        bucket = []
        for a in self._premises:
            bucket += self._premises[a].support_statements
        return bucket

    @property
    def sources(self):
        """ list of sources from all premises in this Argument """
        bucket = []
        for a in self._premises:
            bucket += self._premises[a].sources
        return bucket

    @property
    def stats(self):
        """ return dictionary with stats about argument """
        return {"num_statements": len(self.statements),
                "num_support": len(self.support_statements),
                "num_sources": len(self.sources),
                "num_premises": len(self.assertions),
                "is_true": self.is_true}

    def __str__(self):
        return self.description

    def __bool__(self):
        return self.is_true
