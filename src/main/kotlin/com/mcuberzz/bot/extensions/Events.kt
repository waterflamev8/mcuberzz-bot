package com.mcuberzz.bot.extensions

import com.kotlindiscord.kord.extensions.extensions.Extension
import com.mcuberzz.bot.botSuccessColour
import com.mcuberzz.bot.eventChannel
import dev.kord.common.annotation.KordUnsafe
import dev.kord.core.behavior.channel.createEmbed
import dev.kord.core.event.gateway.ConnectEvent
import dev.kord.core.event.gateway.ReadyEvent
import kotlinx.datetime.Clock

class Events : Extension() {
    override val name = "Events"

    @OptIn(KordUnsafe::class, dev.kord.common.annotation.KordExperimental::class)
    override suspend fun setup() {
        event<ReadyEvent> {
            kord.unsafe.messageChannel(eventChannel).createEmbed {
                title = "Bot Ready"
                color = botSuccessColour
                timestamp = Clock.System.now()
            }
        }

        event<ConnectEvent> {
            val event = this

            kord.unsafe.messageChannel(eventChannel).createEmbed {
                title = "Shard ${event.}"
                color = botSuccessColour
                timestamp = Clock.System.now()
            }
        }
    }
}
