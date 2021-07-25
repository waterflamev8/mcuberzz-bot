import ch.qos.logback.core.joran.spi.ConsoleTarget

def defaultLevel = INFO

logger("io.ktor.util.random", ERROR)

appender("CONSOLE", ConsoleAppender) {
    encoder(PatternLayoutEncoder) {
        pattern = "%d{yyyy-MM-dd HH:mm:ss:SSS Z} | %5level | %40.40logger{40} | %msg%n"
    }

    target = ConsoleTarget.SystemErr
}

root(defaultLevel, ["CONSOLE"])
