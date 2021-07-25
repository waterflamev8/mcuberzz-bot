package com.mcuberzz.bot.extensions

import com.kotlindiscord.kord.extensions.commands.converters.impl.coalescedString
import com.kotlindiscord.kord.extensions.commands.converters.impl.optionalChannel
import com.kotlindiscord.kord.extensions.commands.parser.Arguments
import com.kotlindiscord.kord.extensions.extensions.Extension
import com.mcuberzz.bot.botPrimaryColour
import com.mcuberzz.bot.utils.isAdmin
import dev.kord.core.behavior.channel.createEmbed
import dev.kord.core.behavior.channel.createMessage
import dev.kord.core.entity.channel.TextChannel

class Admin : Extension() {
    override val name = "Admin"

    override suspend fun setup() {
        command(::EchoArguments) {
            name = "echo"
            description = "Make me say something"
            hidden = true

            check(isAdmin())

            action {
                val channel = arguments.channel as TextChannel? ?: message.channel

                message.delete()
                channel.createMessage {
                    content = arguments.content
                    allowedMentions {}
                }
            }
        }

        command(::EmbedArguments) {
            name = "embed"
            description = "Make me say something via an embed"
            hidden = true

            check(isAdmin())

            action {
                val channel = arguments.channel as TextChannel? ?: message.channel

                message.delete()
                channel.createEmbed {
                    description = arguments.content
                    color = botPrimaryColour
                }
            }
        }

        command(::TypeArguments) {
            name = "type"
            description = "Make me type"
            hidden = true

            action {
                val channel = arguments.channel as TextChannel? ?: message.channel

                message.delete()
                channel.type()
            }
        }
    }

    inner class EchoArguments : Arguments() {
        val channel by optionalChannel("channel", "Channel to send message to")
        val content by coalescedString("content", "Message to send")
    }

    inner class EmbedArguments : Arguments() {
        val channel by optionalChannel("channel", "Channel to send embed to")
        val content by coalescedString("content", "Content of embed to send")
    }

    inner class TypeArguments : Arguments() {
        val channel by optionalChannel("channel", "Channel to type in")
    }
}
