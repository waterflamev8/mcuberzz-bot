package com.mcuberzz.bot

import com.kotlindiscord.kord.extensions.ExtensibleBot
import com.mcuberzz.bot.extensions.Admin
import dev.kord.common.entity.PresenceStatus
import dev.kord.gateway.Intents

lateinit var bot: ExtensibleBot

suspend fun main() {
    bot = ExtensibleBot(botToken) {
        messageCommands {
            defaultPrefix = "]"
            invokeOnMention = true
        }

        extensions {
            help {
                pingInReply = false
                colour {
                    botPrimaryColour
                }
            }

            sentry {
                enable = false
            }

            add(::Admin)
        }

        intents {
            +Intents.nonPrivileged
        }

        members {
            all()
        }

        presence {
            status = PresenceStatus.Online
            playing(botActivity)
        }
    }

    bot.start()
}

