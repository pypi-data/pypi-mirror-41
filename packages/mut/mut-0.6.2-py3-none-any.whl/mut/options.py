import logging
import os
import os.path

from typing import *
import rstcloth.rstcloth

import mut
import mut.config
import mut.state
import mut.util

__all__ = ['PREFIXES', 'run']

PREFIXES = ['options']

logger = logging.getLogger(__name__)


class OptionsConfig:
    def __init__(self, root_config: mut.config.RootConfig) -> None:
        self.root_config = root_config
        self.options = {}  # type: Dict[str, Option]
        self.final_options = []  # type: List[str]

    def register(self, option: 'Option') -> None:
        option_id = self.option_global_id(option.path, option.ref)
        if option_id in self.options:
            raise ValueError('Option ID {} is already used'.format(option.human_ref))

        self.options[option_id] = option

        if not option.state.program.startswith('_'):
            self.final_options.append(option_id)

    def get_option(self, path: str, ref: str) -> 'Option':
        return self.options[self.option_global_id(path, ref)]

    def output(self) -> None:
        try:
            os.makedirs(self.output_path)
        except FileExistsError:
            pass

        for option_id in self.final_options:
            self.options[option_id].output()

    @property
    def output_path(self) -> str:
        return os.path.join(self.root_config.output_path, 'source', 'includes', 'option')

    @staticmethod
    def option_global_id(path: str, ref: str) -> str:
        return '{}#{}'.format(path, ref)


class OptionInputError(mut.MutInputError):
    @property
    def plugin_name(self):
        return 'option'


class OptionState(mut.state.State):
    DIRECTIVES = ('option', 'commandoption', 'data', 'setting',
                  'method', 'function', 'class')

    def __init__(self, program: str, name: str) -> None:
        self._replacements = {}  # type: Dict[str, str]

        self._program = program
        self._name = name
        self._filename = None  # type: str
        self._command = None  # type: str
        self._aliases = None  # type: str
        self._args = None  # type: str
        self._default = None  # type: str
        self._description = None  # type: str
        self._directive = None  # type: str
        self._optional = None  # type: bool
        self._type = None  # type: str

        self._pre = None  # type: str
        self._post = None  # type: str

    @property
    def program(self) -> str: return self._program or ''

    @property
    def name(self) -> str: return self._name or ''

    @property
    def filename(self) -> str: return self._filename or ''

    @filename.setter
    def filename(self, filename: str) -> None: self._filename = filename

    @property
    def command(self) -> str: return self._command or ''

    @command.setter
    def command(self, command: str) -> None: self._command = command

    @property
    def aliases(self) -> str: return self._aliases or ''

    @aliases.setter
    def aliases(self, aliases: str) -> None: self._aliases = aliases

    @property
    def args(self) -> str: return self._args or ''

    @args.setter
    def args(self, args: str) -> None: self._args = args

    @property
    def default(self) -> str: return self._default or ''

    @default.setter
    def default(self, default: str) -> None: self._default = default

    @property
    def description(self) -> str: return self._description or ''

    @description.setter
    def description(self, description: str) -> None: self._description = description

    @property
    def directive(self) -> str: return self._directive or 'option'

    @directive.setter
    def directive(self, directive: str) -> None:
        if directive not in self.DIRECTIVES and directive is not None:
            raise ValueError(directive)

        self._directive = directive

    @property
    def optional(self) -> bool: return self._optional or False

    @optional.setter
    def optional(self, optional: bool) -> None: self._optional = optional

    @property
    def type(self) -> str: return self._type or ''

    @type.setter
    def type(self, entry_type: str) -> None: self._type = entry_type

    @property
    def pre(self) -> str: return self._pre or ''

    @pre.setter
    def pre(self, pre: str) -> None: self._pre = pre

    @property
    def post(self) -> str: return self._post or ''

    @post.setter
    def post(self, post: str) -> None: self._post = post

    @property
    def replacements(self) -> Dict[str, str]:
        return self._replacements

    @property
    def ref(self) -> str:
        return '{}-{}'.format(self.program, self.name)

    @property
    def ref_filename(self) -> str:
        """Returns a variant of the ref that makes use of the "filename" option,
           and substitutes spaces in the *program* for compatibility with giza."""
        return '{}-{}'.format(self.program.replace(' ', '-'), self.filename or self.name)

    @property
    def keys(self):
        return ['_program', '_name', '_filename', '_command', '_directive', '_type',
                '_default', '_args', '_description', '_aliases', '_optional',
                '_pre', '_post']


class Option:
    def __init__(self,
                 program: str,
                 name: str,
                 path: str,
                 config: OptionsConfig) -> None:
        self.path = os.path.basename(path)
        self._inherit = None  # type: Tuple[str, str]

        self.state = OptionState(program, name)

        self.config = config
        self.config.register(self)

    @property
    def ref(self) -> str:
        return self.state.ref

    @property
    def human_ref(self) -> str:
        return '{} in program {}'.format(self.state.name, self.state.program)

    @property
    def parent(self) -> 'Option':
        if self._inherit is None:
            return None

        parent_path, parent_ref = self._inherit
        try:
            return self.config.get_option(parent_path, parent_ref)
        except KeyError:
            msg = 'Could not find Option "{}" to inherit from in "{}"'.format(parent_ref, parent_path)
            raise OptionInputError(self.path, self.ref, msg)

    def inherit(self) -> None:
        parent = self.parent
        if parent is None:
            return

        parent.inherit()
        self.state.inherit(parent.state)
        self._inherit = None

    def output(self) -> None:
        self.inherit()

        cloth = rstcloth.rstcloth.RstCloth()

        if 'program' not in self.state.replacements:
            self.state.replacements['program'] = rstcloth.rstcloth.RstCloth.role('program', self.state.program)

        if self.state.command:
            self.state.replacements['command'] = rstcloth.rstcloth.RstCloth.role('toolcommand', self.state.command)

        if self.state.directive == 'option':
            if len(self.state.name) > 1 and self.state.name[0] in ('<', '-'):
                prefix = ''
            else:
                prefix = '--'

            directive_str = '{prefix}{name}'

            if self.state.args:
                directive_str += ' {args}'

            if self.state.aliases:
                directive_str += ', {0}'.format(self.state.aliases)

                if self.state.args:
                    directive_str += ' {args}'

            if self.state.args:
                directive_str = directive_str.format(prefix=prefix,
                                                     name=self.state.name,
                                                     args=self.state.args)
            else:
                directive_str = directive_str.format(prefix=prefix,
                                                     name=self.state.name)
        else:
            prefix = ''
            directive_str = self.state.name

        if 'role' not in self.state.replacements:
            self.state.replacements['role'] = ':{0}:`{1}{2}`'.format(self.state.directive, prefix, self.state.name)

        cloth.directive(self.state.directive, directive_str)
        cloth.newline()

        indent = 3
        if self.state.type:
            cloth.content('*Type*: {0}'.format(self.state.type), indent=indent)
            cloth.newline()

        if self.state.default:
            cloth.content('*Default*: {0}'.format(self.state.default), indent=indent)
            cloth.newline()

        for field in ('pre', 'description', 'post'):
            value = getattr(self.state, field)

            if not value:
                continue

            cloth.content(value.split('\n'), indent=indent, wrap=False)
            cloth.newline()

        try:
            content = mut.util.substitute_rstcloth(cloth, self.state.replacements)
        except KeyError as error:
            raise OptionInputError(self.path,
                                   self.ref,
                                   'Failed to substitute {}'.format(str(error))) from error

        mut.util.save_if_changed(content, self.output_path)

    @property
    def output_path(self) -> str:
        self.inherit()
        # Use an explicit filename if we were given one, or construct a name
        # where our *option name* can have spaces, but not our *program*.
        # Why? Compatibility with giza.
        filename = self.state.directive + '-' + self.state.ref_filename
        return os.path.join(self.config.output_path, filename) + '.rst'

    def _populate(self, value: Any) -> None:
        self.state.aliases = mut.util.withdraw(value, 'aliases', str)
        self.state.args = mut.util.withdraw(value, 'args', str)
        self.state.default = mut.util.withdraw(value, 'default', str)
        self.state.description = mut.util.withdraw(value, 'description', str)

        directive = mut.util.withdraw(value, 'directive', str)
        try:
            self.state.directive = directive
        except ValueError:
            msg = 'Illegal key "{}". Must be in set {}'.format(directive,
                                                               OptionState.DIRECTIVES)
            raise ValueError(msg)

        self.state.optional = mut.util.withdraw(value, 'optional', bool)
        self.state.type = mut.util.withdraw(value, 'type', str)

        self.state.pre = mut.util.withdraw(value, 'pre', str)
        self.state.post = mut.util.withdraw(value, 'post', str)
        self.state.filename = mut.util.withdraw(value, 'filename', str)
        self.state.command = mut.util.withdraw(value, 'command', str)

        replacements = mut.util.withdraw(value, 'replacement', mut.util.str_dict)
        if replacements:
            for src, dest in replacements.items():
                self.state.replacements[src] = dest

        raw_inherit = mut.util.withdraw(value, 'inherit', mut.util.str_dict, default={})  # type: Dict[str, str]
        if raw_inherit:
            self._inherit = (raw_inherit['file'],
                             '{}-{}'.format(raw_inherit['program'], raw_inherit['name']))

        if value:
            msg = 'Unknown fields "{}"'.format(', '.join(value.keys()))
            raise ValueError(msg)

    @classmethod
    def load(cls, value: Any, path: str, config: OptionsConfig) -> 'Option':
        program = mut.util.withdraw(value, 'program', str)
        if not program:
            raise OptionInputError(path, '<unknown>', 'Missing field "name"')

        name = mut.util.withdraw(value, 'name', str)
        if not name:
            raise OptionInputError(path, program, 'Missing field "name"')

        try:
            option = cls(program, name, path, config)  # type: Option
        except ValueError as err:
            raise OptionInputError(path, program, str(err)) from err

        try:
            option._populate(value)
        except ValueError as err:
            raise OptionInputError(path, option.state.ref, str(err)) from err

        return option

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.ref))


def run(root_config: mut.config.RootConfig, paths: List[str]):
    logger.info('Options')
    config = OptionsConfig(root_config)
    for path in paths:
        raw_options = mut.util.load_yaml(path)
        [Option.load(o, path, config) for o in raw_options if o]

    config.output()
