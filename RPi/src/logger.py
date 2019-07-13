import logging

logger = logging.getLogger(__name__)
fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)


def Info(message: str) -> None:
    """Output an infomation message to log

    Arguments:
        message {str} -- info message
    """
    logger.info(message)


def Warn(message: str) -> None:
    """Output a warning message to log

    Arguments:
        message {str} -- warn message
    """
    logger.warn(message)


def Error(message: str) -> None:
    """Output an error message to log
    Arguments:
        message {str} -- error message
    """
    logger.error(message)


def Debug(message: str) -> None:
    """Output an debug message to log
    
    Arguments:
        message {str} -- debug message
    """
    logger.debug(message)


if __name__ == "__main__":
    Error("A sample error message")
    Warn("A sample warning message")
    Info("A sample Info message")
    Debug("A sample debug message")