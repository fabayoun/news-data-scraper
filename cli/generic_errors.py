import contextlib
import logging

logger = logging.getLogger(__name__)


@contextlib.contextmanager
def common_error_handling() -> None:
    try:
        yield
    except KeyboardInterrupt:
        logger.info("Caught KeyboardInterrupt", exc_info=True)
    except Exception:
        logger.fatal("Caught fatal error", exc_info=True)
        raise
