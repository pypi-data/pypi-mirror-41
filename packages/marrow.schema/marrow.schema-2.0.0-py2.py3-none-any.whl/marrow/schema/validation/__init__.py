from warnings import warn

# Replicate the original imports available here.

from ..validate import Validator, Callback, In, Contains, Length, Range, Pattern, Instance, Subclass, Equal
from ..validate import Always, always, Never, never, Unique, unique
from ..validate import AlwaysTruthy, truthy, Truthy, AlwaysFalsy, falsy, Falsy
from ..validate import AlwaysRequired, required, Required, AlwaysMissing, missing, Missing
from ..validate import Validated


warn("This package has been re-named, import your modules from marrow.schema.validate instead.", DeprecationWarning)
