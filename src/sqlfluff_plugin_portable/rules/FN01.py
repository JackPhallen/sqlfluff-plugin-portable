"""Implementation of rule FN01 - Portable functions"""

from sqlfluff.core.rules import (
    BaseRule,
    LintResult,
    RuleContext,
)
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_Portable_FN01(BaseRule):
    """Function is not on allowed list of portable functions"""

    groups = ("all", "portable")
    config_keywords = ["function_allowlist"]
    crawl_behaviour = SegmentSeekerCrawler({"function_name_identifier"})

    def __init__(self, *args, **kwargs):
        """Overwrite __init__ to set config."""
        super().__init__(*args, **kwargs)
        if self.function_allowlist:
            self.function_allowlist = set(
                col.strip().upper() for col in self.function_allowlist.split(",")
            )
        else:
            self.function_allowlist = set()
        # If function_allowlist is empty, we don't want this rule to evaluate
        self.is_configured = bool(self.function_allowlist)

    def _eval(self, context: RuleContext):
        """Functions must be in function_allowlist."""
        # We do not throw linter errors if function_allowlist is not configured in .sqlfluff
        if not self.is_configured:
            return
        fn_name = context.segment.raw.upper()
        if fn_name not in self.function_allowlist:
            return LintResult(
                anchor = context.segment,
                description = f"Function `{fn_name}` is not portable"
            )
