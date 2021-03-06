from protowhat.sct_context import create_sct_context, get_checks_dict
from shellwhat import checks

SCT_DICT = get_checks_dict(checks)
SCT_CTX = create_sct_context(SCT_DICT)

# put on module for easy * importing
globals().update(SCT_CTX)
__all__ = list(SCT_CTX.keys())
